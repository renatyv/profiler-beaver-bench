---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:04:27.752405Z
dialect: mysql
database: neutron
schema: neutron
profile_lines: 1138
profile_sha256: ec20bb78011b480d845d130885586978d69435866a0f785f3367c9e44ebe67d1
enriched_model: openrouter/openai/gpt-6-luna
enriched_at_utc: 2026-09-29T14:46:44.309832+00:00
toc_sha256: 8de0c95ff5223168513adf903b692bb04975ce7b853c11d865569d4a252b0ee7

---

Relationships: lines 12-58
`agents` (rows=129): lines 60-96 — Registered Neutron agents with host, type, heartbeat, and configuration details.
`alembic_version_fwaas` (rows=2): lines 98-108 — FWaaS migration revision markers, separate from core and LBaaS migration state.
`alembic_version_lbaas` (rows=2): lines 110-120 — LBaaS migration revision markers, separate from FWaaS migration state.
`allowedaddresspairs` (rows=1): lines 122-136 — Extra permitted MAC and IP combinations attached to ports.
`default_security_group` (rows=804): lines 138-150 — Maps each tenant to its default security group.
`dnsnameservers` (rows=65): lines 152-166 — Ordered DNS resolver addresses configured per subnet.
`externalnetworks` (rows=1): lines 168-180 — Marks networks available for external routing and identifies defaults.
`floatingips` (rows=23): lines 182-212 — Public floating addresses and their optional associations with fixed ports and routers.
`healthmonitors` (rows=3): lines 214-242 — LB-v1 pool health-check configuration; distinct from LB-v2 monitor resources.
`ipallocationpools` (rows=49): lines 244-260 — Configured first-to-last address ranges available for subnet allocation.
`ipallocations` (rows=3779): lines 262-278 — Individual IP addresses assigned to network ports and subnets.
`ipavailabilityranges` (rows=184): lines 280-294 — Remaining allocatable address intervals within configured IP pools.
`lbaas_listeners` (rows=5): lines 296-330 — LB-v2 frontend protocol ports linked to load balancers and default pools.
`lbaas_loadbalancer_statistics` (rows=6): lines 332-350 — Traffic and connection counters for LB-v2 load balancers.
`lbaas_loadbalanceragentbindings` (rows=6): lines 352-364 — Assignment of each LB-v2 load balancer to its servicing agent.
`lbaas_loadbalancers` (rows=6): lines 366-396 — LB-v2 load balancer resources and their virtual IP ports.
`lbaas_members` (rows=22): lines 398-428 — LB-v2 backend pool members, with provisioning and operating status.
`lbaas_pools` (rows=5): lines 430-460 — LB-v2 backend pools, algorithms, and optional health monitor references.
`members` (rows=4): lines 462-488 — LB-v1 backend pool members; unlike LB-v2, uses status fields without provisioning status.
`ml2_gre_allocations` (rows=1000): lines 490-502 — Availability state of ML2 GRE tunnel identifiers.
`ml2_gre_endpoints` (rows=124): lines 504-516 — Host-to-IP endpoint registry for ML2 GRE tunnels.
`ml2_network_segments` (rows=49): lines 518-540 — Network segment encapsulation type and segmentation settings, including GRE or VLAN.
`ml2_port_binding_levels` (rows=3692): lines 542-560 — Per-port host binding level and selected network segment.
`ml2_port_bindings` (rows=3730): lines 562-582 — Per-port ML2 host binding result, VIF type, and driver details.
`ml2_vlan_allocations` (rows=9): lines 584-598 — VLAN identifiers and allocation state per physical network.
`networkdhcpagentbindings` (rows=45): lines 600-612 — DHCP agent serving each Neutron network.
`networkrbacs` (rows=14): lines 614-632 — Network sharing or external-access permissions granted to target tenants.
`networks` (rows=49): lines 634-660 — Neutron network resources and their tenant, state, and standard attributes.
`networksecuritybindings` (rows=36): lines 662-674 — Per-network setting controlling whether port security is enabled.
`poolmonitorassociations` (rows=1): lines 676-692 — LB-v1 pool-to-health-monitor association and status.
`pools` (rows=2): lines 694-724 — LB-v1 backend pools, distinct from LB-v2 pools prefixed `lbaas_`.
`poolstatisticss` (rows=2): lines 726-744 — LB-v1 pool traffic and connection counters, separate from load-balancer counters.
`ports` (rows=3775): lines 746-776 — Neutron network interfaces, including device ownership, MAC, and status.
`portsecuritybindings` (rows=3194): lines 778-790 — Per-port port-security setting, distinct from network-level security bindings.
`providerresourceassociations` (rows=38): lines 792-804 — Maps provider names to resources they manage, here for HAProxy.
`quotas` (rows=1521): lines 806-822 — Per-tenant configured limits for Neutron resource types.
`quotausages` (rows=810): lines 824-842 — Per-tenant in-use quota counts and dirty-state tracking by resource.
`reservations` (rows=5): lines 844-858 — Temporary tenant quota reservation identifiers and expiration times.
`resourcedeltas` (rows=5): lines 860-874 — Resource quantity reserved under each quota reservation.
`router_extra_attributes` (rows=27): lines 876-896 — Router HA, distribution, service-router, and availability-zone options.
`routerl3agentbindings` (rows=27): lines 898-910 — L3 agent assignment for each router.
`routerports` (rows=35): lines 912-926 — Associates router interfaces and gateway ports with their routers.
`routers` (rows=27): lines 928-952 — Neutron router resources, gateway references, and source NAT setting.
`securitygroupportbindings` (rows=5921): lines 954-966 — Many-to-many association of ports with applied security groups.
`securitygrouprules` (rows=9004): lines 968-998 — Security group ingress and egress filtering rules, including protocol and remote selectors.
`securitygroups` (rows=1798): lines 1000-1016 — Tenant-owned security group resources referenced by rules and port bindings.
`sessionpersistences` (rows=1): lines 1018-1032 — LB-v1 VIP persistence type and optional cookie name.
`standardattributes` (rows=14725): lines 1034-1052 — Shared timestamps and descriptions keyed by resource type for supported Neutron objects.
`subnetroutes` (rows=6): lines 1054-1068 — Custom destination and next-hop routes configured for subnets.
`subnets` (rows=49): lines 1070-1102 — Network address ranges, gateways, DHCP settings, and IP-version configuration.
`vips` (rows=1): lines 1104-1136 — LB-v1 virtual IP frontend settings linked to a pool and port.
Summary: lines 1138-1138
