// Tiny HTTPS forward proxy with a destination allow-list.
//
// Runs as a sidecar container on beaver-net. The agent container sets
// HTTPS_PROXY / HTTP_PROXY to point at it; only requests whose CONNECT
// host is on the allow-list are tunneled. Everything else is refused.
//
// This is deliberately minimal: no caching, no auth (the network is
// private), no HTTP/2. It exists solely to enforce "the agent may only
// talk to openrouter.ai" at the network layer.
//
// Allow-list is read from the space-separated EGRESS_ALLOW env var
// (exact hostnames, matched case-insensitively against the CONNECT host).
// Default: openrouter.ai.
const http = require("http");
const net = require("net");

const PORT = parseInt(process.env.PROXY_PORT || "8888", 10);
const ALLOW = (process.env.EGRESS_ALLOW || "openrouter.ai")
  .toLowerCase()
  .split(/\s+/)
  .filter(Boolean);

function allowed(hostPort) {
  // hostPort is "host:port"; strip the port for matching.
  const host = String(hostPort || "").split(":")[0].toLowerCase();
  if (!host) return false;
  return ALLOW.includes(host);
}

const server = http.createServer((req, res) => {
  // Plain HTTP (non-CONNECT) requests: also enforce the allow-list on the
  // request URL host. pi/OpenRouter uses HTTPS CONNECT, but we cover this
  // for completeness.
  const u = req.url || "";
  res.writeHead(403, { "Content-Type": "text/plain" });
  res.end("Forbidden by egress allow-list (plain HTTP not proxied).\n");
});

server.on("connect", (req, clientSocket, head) => {
  const target = req.url || "";
  if (!allowed(target)) {
    clientSocket.write(
      "HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n"
    );
    console.error(`[DENY] ${target}`);
    clientSocket.end();
    return;
  }
  console.log(`[ALLOW] ${target}`);
  const upstream = net.connect(
    { host: target.split(":")[0], port: parseInt(target.split(":")[1] || "443", 10) },
    () => {
      clientSocket.write("HTTP/1.1 200 Connection Established\r\n\r\n");
      upstream.write(head);
      upstream.pipe(clientSocket);
      clientSocket.pipe(upstream);
    }
  );
  upstream.on("error", (err) => {
    console.error(`[ERROR] ${target}: ${err.message}`);
    clientSocket.end();
  });
  clientSocket.on("error", () => upstream.destroy());
});

server.listen(PORT, "0.0.0.0", () => {
  console.log(`egress-proxy listening on :${PORT}, allow-list: ${ALLOW.join(", ")}`);
});
