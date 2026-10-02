"""Docker network topology for the containerized agent run.

Three networks implement the experiment's isolation invariants:

  beaver-net      — user bridge with internet egress. Hosts ONLY the egress
                    proxy.
  beaver-sandbox  --internal bridge with NO internet route. Hosts the agent
                    containers + has beaver-mysql + the egress proxy attached.
                    This is the only network agents live on, so they cannot
                    bypass the proxy to reach the internet.
  bridge          — the Docker default; beaver-mysql's primary attachment and
                    the route the host scorer uses (127.0.0.1:3307).

The egress proxy is attached to BOTH beaver-net (for outbound to openrouter.ai)
and beaver-sandbox (so agents can reach it). It forwards only allow-listed
CONNECT hosts (see harness/egress/egress-proxy.js).

Topological picture (per the plan):

      internet ◄──────┐
                      │
            ┌─────────┴──────────┐   beaver-net (has internet)
            │  beaver-egress-proxy│ ◄── allow-list: openrouter.ai only
            └─────────┬──────────┘
                      │ (also attached to ↓)
            ┌─────────┴──────────┐   beaver-sandbox (--internal, no internet)
            │  agent containers   │
            │  beaver-mysql       │ ◄── agents reach MySQL by name here
            └────────────────────┘

All setup calls are idempotent. A failed network attachment or account setup
raises immediately rather than allowing an experiment to run outside its stated
isolation boundary.
"""
from __future__ import annotations

import os
import subprocess
import time

from . import config


def _docker(*args: str, check: bool = False) -> subprocess.CompletedProcess:
    """Run a docker CLI call, returning the CompletedProcess (never raising
    unless check=True). Errors go to stderr; we inspect returncode instead."""
    return subprocess.run(
        ["docker", *args],
        capture_output=True, text=True, timeout=120,
    )


def _network_exists(name: str) -> bool:
    r = _docker("network", "ls", "--filter", f"name=^{name}$", "--format", "{{.Name}}")
    return name in (r.stdout or "").split()


def _container_exists(name: str) -> bool:
    r = _docker("ps", "-a", "--filter", f"name=^{name}$", "--format", "{{.Names}}")
    return name in (r.stdout or "").split()


def _network_connect(net: str, container: str) -> None:
    """Attach a container to a network; idempotent (ignore 'already exists')."""
    r = _docker("network", "connect", net, container)
    # docker exits 1 with "already exists" in stderr if already connected — fine.
    if r.returncode != 0 and "already exists" not in (r.stderr or "").lower():
        raise RuntimeError(f"failed to connect {container} to {net}: {r.stderr.strip()}")


def ensure_networks() -> None:
    """Create beaver-net (egress) + beaver-sandbox (internal) if absent.

    Also attaches beaver-mysql to beaver-sandbox so agents can reach it by
    name. MySQL is deliberately not attached to the egress network.
    """
    # beaver-net: normal bridge (has internet). Only the proxy needs internet.
    if not _network_exists(config.AGENT_NET_EGRESS):
        r = _docker("network", "create", config.AGENT_NET_EGRESS)
        if r.returncode != 0:
            raise RuntimeError(f"failed to create {config.AGENT_NET_EGRESS}: {r.stderr.strip()}")
        else:
            print(f"  [network] created {config.AGENT_NET_EGRESS}")
    # beaver-sandbox: internal (NO internet route). Agents live here.
    if not _network_exists(config.AGENT_NET_SANDBOX):
        r = _docker("network", "create", "--internal", config.AGENT_NET_SANDBOX)
        if r.returncode != 0:
            raise RuntimeError(f"failed to create {config.AGENT_NET_SANDBOX}: {r.stderr.strip()}")
        else:
            print(f"  [network] created {config.AGENT_NET_SANDBOX} (internal)")
    # Attach mysql to the sandbox so agents resolve `beaver-mysql` by name.
    _network_connect(config.AGENT_NET_SANDBOX, config.MYSQL_CONTAINER)


def _sql_literal(value: str) -> str:
    """Quote the generated/configured account values for a MySQL statement."""
    return "'" + value.replace("\\", "\\\\").replace("'", "''") + "'"


def ensure_agent_db_user(databases: set[str] | None = None) -> None:
    """Reset the account injected into agents to SELECT-only benchmark access.

    The benchmark loader/scorer account is intentionally powerful, so it cannot
    be given to arbitrary bash in an agent container. A fresh random password is
    generated for this process unless BEAVER_AGENT_MYSQL_PWD is explicitly set.
    """
    account = f"{_sql_literal(config.AGENT_MYSQL_USER)}@'%'"
    statements = [
        f"CREATE USER IF NOT EXISTS {account} IDENTIFIED BY {_sql_literal(config.AGENT_MYSQL_PWD)}",
        f"ALTER USER {account} IDENTIFIED BY {_sql_literal(config.AGENT_MYSQL_PWD)}",
        f"REVOKE ALL PRIVILEGES, GRANT OPTION FROM {account}",
    ]
    for dataset in databases or config.all_mysql_dbs():
        statements.append(f"GRANT SELECT ON `{dataset.replace('`', '``')}`.* TO {account}")
    env = dict(os.environ, MYSQL_PWD=config.MYSQL_PWD)
    r = subprocess.run(
        ["mysql", "--skip-ssl", "--protocol=TCP", "-h", config.MYSQL_HOST,
         "-P", str(config.MYSQL_PORT), "-u", config.MYSQL_USER],
        input=";\n".join(statements) + ";\n",
        capture_output=True, text=True, timeout=30, env=env,
    )
    if r.returncode != 0:
        raise RuntimeError(f"failed to provision SELECT-only agent account: {r.stderr.strip()}")


def ensure_egress_proxy() -> str:
    """Start (or reuse) the egress-proxy sidecar. Returns the proxy container
    name (agents point HTTPS_PROXY at <name>:8888).

    The proxy is attached to both networks: beaver-net (outbound to
    openrouter.ai) and beaver-sandbox (so agents can reach it).
    """
    name = config.EGRESS_PROXY_CONTAINER
    if _container_exists(name):
        # Ensure it's on both networks (idempotent re-attach).
        _network_connect(config.AGENT_NET_SANDBOX, name)
        # Make sure it's running (it may have been stopped).
        r = _docker("start", name)
        if r.returncode != 0:
            raise RuntimeError(f"failed to start egress proxy: {r.stderr.strip()}")
        return name
    # Fresh start. Launch on the egress network first (it needs internet).
    r = _docker("run", "-d", "--name", name,
                "--network", config.AGENT_NET_EGRESS,
                "-e", f"EGRESS_ALLOW={config.EGRESS_ALLOW_HOSTS}",
                config.EGRESS_PROXY_IMAGE)
    if r.returncode != 0:
        raise RuntimeError(f"failed to start egress proxy: {r.stderr.strip()}")
    # Then attach to the sandbox so agents can reach it.
    _network_connect(config.AGENT_NET_SANDBOX, name)
    # Give it a moment to bind.
    time.sleep(0.5)
    print(f"  [network] egress proxy '{name}' started (allow: {config.EGRESS_ALLOW_HOSTS})")
    return name


def setup(databases: set[str] | None = None) -> str:
    """One-call bring-up: networks + proxy. Returns the proxy container name.
    Safe to call repeatedly (idempotent). Called once at experiment start."""
    ensure_networks()
    ensure_agent_db_user(databases)
    return ensure_egress_proxy()


def teardown_proxy() -> None:
    """Stop + remove the egress proxy (leave networks intact for reuse)."""
    if _container_exists(config.EGRESS_PROXY_CONTAINER):
        _docker("rm", "-f", config.EGRESS_PROXY_CONTAINER)
        print(f"  [network] removed egress proxy '{config.EGRESS_PROXY_CONTAINER}'")


def is_ready() -> bool:
    """Cheap readiness probe: proxy container running + sandbox network exists."""
    if not _network_exists(config.AGENT_NET_SANDBOX):
        return False
    r = _docker("ps", "--filter", f"name=^{config.EGRESS_PROXY_CONTAINER}$",
                "--format", "{{.Names}}")
    return config.EGRESS_PROXY_CONTAINER in (r.stdout or "").split()
