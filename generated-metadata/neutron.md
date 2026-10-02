# Additional Metadata

## Clarified Semantics

- **Two independent load-balancer lineages, not one table family.** `pools`/`members`/`vips`/`healthmonitors`/`poolstatisticss`/`poolmonitorassociations` are the legacy LoadBalancer-v1 model: a `pools` row owns a `vips` VIP via `pools.vip_id`, and member hosts hang off `members.pool_id`. The `lbaas_*` tables are the LoadBalancer-v2 model (own `alembic_version_lbaas` versioning, `Loadbalancerv2 agent` bindings): `lbaas_loadbalancers` → `lbaas_listeners` → `lbaas_pools` → `lbaas_members`, with `lbaas_loadbalancer_statistics`/`lbaas_loadbalanceragentbindings`. Grain and scale differ: pools/members/vips are 2/4/1 rows vs lbaas_pools/lbaas_members/lbaas_loadbalancers 5/22/6. Do not treat them as one model or join across the two families.

- **IP provisioning vs. carve-out pools vs. assignments.** `ipallocationpools` (per-`subnet_id`, 49 rows) define logical allocatable pools; `ipavailabilityranges` (184 rows) carve those pools into `first_ip..last_ip` ranges (one pool, 455ff839…, contributes 138 ranges). `ipallocations` (3779 rows) are the actual assigned `ip_address` records keyed to a `port_id`+`subnet`. The `ipam*` (ipamallocationpools/ipamallocations/ipamavailabilityranges/ipamsubnets) family is a separate IPAM subsystem and is fully empty here.

- **Quota limits vs. accounting.** `quotas` stores per-tenant/resource configured `limit` (`-1` = unlimited; 1521 rows). `quotausages` stores current per-tenant/resource `in_use` counts (810 rows). The two share `tenant_id`+`resource` but differ in row grain (limits are per configured resource; usage rows exist per observed resource).

- **Security-enable flags vs. security-group membership.** `portsecuritybindings` (3194 rows) and `networksecuritybindings` (36 rows) both carry a boolean `port_security_enabled`, i.e. whether port-level security is turned on. `securitygroupportbindings` (5921 rows) instead records which SG is attached to a `port_id`. `securitygrouprules.remote_group_id` can point at another security group (7266 nulls otherwise), enabling cross-group (remote group) rule references distinct from the owning `security_group_id`.

## Potential Join Strategies

- **Assign an IP to a port:** `ports.id = ipallocations.port_id`, fan-in is up to 3 ipallocations per port; `ipallocations` also carries `subnet_id` and `network_id`, so it can be joined directly to `subnets.id`/`networks.id` without going through `ports`. One `ipallocations.port_id` is null (unbound row).

- **Constraint the sub-node hierarchy in place of fixed chains:** `subnets.network_id → networks.id`, then `subnets.id → ipallocationpools.subnet_id → ipavailabilityranges.allocation_pool_id` gives the carved address ranges underpinning assigned IPs; use `ipallocations.network_id` as the equally valid shortcut to attach a port/network to an address.

- **Floating (NAT) IP rewrite to its target:** `floatingips.floating_port_id`/`fixed_port_id` → `ports.id`, and `floatingips.floating_network_id` → `networks.id`. Caveat: all 23 rows point at the one external network (8ad137b5…), `router_id` is null on 13 of 23 (NAT state DOWN), and `last_known_router_id` is populated on only 1 row — prefer `router_id` and treat the last-known column as a sparse fallback.

- **ML2 host-layer binding chain:** `ml2_network_segments.id` → `ml2_port_binding_levels.segment_id` (level is always 0, driver always openvswitch), and `ml2_port_bindings.port_id`/`ml2_port_binding_levels.port_id` both give the host/port binding. Filter segments by `network_type` (`gre`=42, `vlan`=7); for vlan-type segments, `ml2_network_segments.physical_network` ('trunk') matches `ml2_vlan_allocations.physical_network`.

- **Gateway vs. edge ports on routers:** `routers.gw_port_id` names exactly one gateway port, while `routerports.router_id` lists all ports of a router with a `port_type` of `network:router_gateway` (15 rows) or `network:router_interface` (20 rows). Use `routerports` filtered to `port_type='network:router_gateway'` to recover the same set as `routers.gw_port_id` when enumerating router edges.

- **LB-v2 VIP/serving geometry:** `lbaas_loadbalancers.vip_port_id` → `ports.id`, `vip_subnet_id` → `subnets.id`. Then `lbaas_loadbalancers.id → lbaas_listeners.loadbalancer_id` (listeners carry their own `default_pool_id`), and `lbaas_pools.loadbalancer_id`/`lbaas_pools.healthmonitor_id`. Statistics: every one of the 6 load balancers has a `lbaas_loadbalancer_statistics` row, so that join is 1:1 and not sparse.

- **LB-v1 VIP geometry:** `pools.vip_id` → `vips.id`, `vips.pool_id` → back to pools, and `members.pool_id` → `pools.id`; `sessionpersistences.vip_id` exists for exactly 1 vip and only for `type=HTTP_COOKIE`.

- **Metadata unification:** `networks/ports/subnets/routers/floatingips/securitygroups/securitygrouprules` each carry a unique `standard_attr_id` → `standardattributes.id`, where `resource_type` distinguishes the owning table. Use `standardattributes.resource_type` as the discriminator when joining datetimes/updates uniformly across beans.