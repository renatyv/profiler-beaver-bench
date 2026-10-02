---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:04:32.359791Z
dialect: mysql
database: nova
schema: nova
profile_lines: 2323
profile_sha256: 5ffa341dfe221cec8bdf46ffefc52c6f5f9be14f28425e1577782ce8ea4dc131
enriched_model: openrouter/openai/gpt-6-luna
enriched_at_utc: 2026-09-29T14:47:08.076650+00:00
toc_sha256: b04196b72c2bcae97cf040c73cb2577aa8e200b137fe35c44d4ddf3298867f95

---

Relationships: lines 12-22
`aggregate_hosts` (rows=584): lines 24-46 — Maps compute hosts to host aggregates; unlike aggregate metadata, it records membership.
`aggregate_metadata` (rows=38): lines 48-72 — Key-value scheduling and allocation metadata attached to host aggregates, distinct from their host membership.
`aggregates` (rows=21): lines 74-96 — Defines host aggregates grouping compute hosts; metadata and memberships are stored separately.
`all_instances` (rows=717814): lines 98-159 — Union view of current `instances` and archived `shadow_instances`, unlike the current-only base table.
`block_device_mapping` (rows=16798): lines 161-209 — Connects instances to boot and attached local or Cinder volume devices; current mappings only.
`certificates` (rows=127): lines 211-235 — Tracks generated certificate file references by user and project, separate from SSH key pairs.
`compute_nodes` (rows=139): lines 237-311 — Current hypervisor capacity, utilization, and capabilities reported by compute hosts; PCI devices are separate.
`fixed_ips` (rows=63724): lines 313-347 — Pool of fixed network addresses and allocation state; unlike `floating_ips`, these belong to the private network.
`floating_ips` (rows=8190): lines 349-381 — Public floating-address pool entries for projects, separate from instance fixed-IP allocation.
`instance_actions` (rows=27472): lines 383-417 — Records user-facing operations requested on instances; execution steps and outcomes live in `instance_actions_events`.
`instance_actions_events` (rows=41690): lines 419-453 — Per-action event execution timings and results, complementing the parent instance action records.
`instance_extra` (rows=7253): lines 455-485 — Current instances' extended flavor, PCI request, NUMA, CPU model, and migration state.
`instance_faults` (rows=5624): lines 487-515 — Current-instance error reports with status code, message, details, and reporting host.
`instance_group_member` (rows=4085): lines 517-539 — Associates instance UUIDs with server groups; group policies are stored separately.
`instance_group_policy` (rows=228): lines 541-563 — Affinity or anti-affinity policy for a server group, distinct from its membership records.
`instance_groups` (rows=230): lines 565-591 — Server-group identity and ownership; membership and scheduling policy are separate tables.
`instance_id_mappings` (rows=277653): lines 593-613 — Maps instance UUIDs to legacy integer instance identifiers.
`instance_info_caches` (rows=7226): lines 615-637 — Current per-instance cached network information, distinct from extended compute metadata.
`instance_metadata` (rows=36): lines 639-663 — User-defined key-value metadata on instances, unlike system-maintained metadata.
`instance_system_metadata` (rows=76723): lines 665-689 — System-managed key-value attributes for current instances, distinct from user metadata.
`instance_type_extra_specs` (rows=135): lines 691-715 — Key-value scheduling and hardware specifications attached to instance types.
`instance_type_projects` (rows=232): lines 717-739 — Project access grants for instance types, not the type definitions themselves.
`instance_types` (rows=190): lines 741-781 — Compute flavor definitions specifying resource sizes and visibility; project grants and extra specs are separate.
`instances` (rows=7922): lines 783-897 — Current Nova server records, unlike the archived records in `shadow_instances` and combined `all_instances` view.
`key_pairs` (rows=3132): lines 899-927 — Current users' SSH public keys and fingerprints, distinct from generated certificates.
`migrate_version` (rows=1): lines 929-943 — Nova database migration repository version marker, not instance migration history.
`networks` (rows=1): lines 945-1019 — Legacy Nova network configuration and addressing settings; individual fixed addresses are in `fixed_ips`.
`pci_devices` (rows=16): lines 1021-1065 — Current PCI devices discovered on compute nodes, including availability and instance assignment.
`quota_classes` (rows=13): lines 1067-1091 — Resource quota limits assigned by quota class, rather than project-specific limits.
`quota_usages` (rows=3619): lines 1093-1123 — Current per-project and user resource usage counters; quota limits are in `quotas`.
`quotas` (rows=3579): lines 1125-1149 — Project-specific hard limits by resource; current usage and reservations are tracked separately.
`reservations` (rows=42003): lines 1151-1183 — Temporary quota deltas associated with usage records, distinct from persistent quota limits and counters.
`s3_images` (rows=2419): lines 1185-1205 — Maps S3 image UUIDs in Nova's legacy image integration.
`security_group_rules` (rows=152): lines 1207-1237 — Current ingress or egress protocol, port, and CIDR rules associated with security groups.
`security_groups` (rows=601): lines 1239-1265 — Current project-owned network security groups; their individual ingress rules are stored separately.
`services` (rows=149): lines 1267-1303 — Current Nova service heartbeats and operational status by host and service binary.
`shadow_aggregate_hosts` (rows=516): lines 1305-1327 — Archived host-aggregate membership records, unlike current `aggregate_hosts`.
`shadow_aggregate_metadata` (rows=4): lines 1329-1353 — Archived aggregate key-value metadata, unlike current `aggregate_metadata`.
`shadow_block_device_mapping` (rows=212755): lines 1355-1403 — Archived instance boot and volume device mappings retained after deletion, unlike current mappings.
`shadow_compute_nodes` (rows=3): lines 1405-1479 — Archived hypervisor capacity and capability records, unlike current `compute_nodes`.
`shadow_fixed_ips` (rows=15): lines 1481-1515 — Archived fixed-address allocation records, unlike the current private IP pool.
`shadow_instance_actions` (rows=523265): lines 1517-1551 — Archived instance operation requests, unlike current `instance_actions`.
`shadow_instance_actions_events` (rows=663442): lines 1553-1587 — Archived execution events and outcomes for instance actions, unlike current event records.
`shadow_instance_extra` (rows=179772): lines 1589-1619 — Archived extended instance flavor, PCI, NUMA, and migration data.
`shadow_instance_faults` (rows=201285): lines 1621-1649 — Archived instance error reports, unlike current fault records.
`shadow_instance_group_member` (rows=84): lines 1651-1673 — Archived server-group memberships, distinct from current group assignments.
`shadow_instance_group_policy` (rows=2): lines 1675-1697 — Archived affinity policies for server groups, unlike current policy records.
`shadow_instance_info_caches` (rows=263732): lines 1699-1721 — Archived per-instance cached network information, unlike current cache entries.
`shadow_instance_metadata` (rows=1554): lines 1723-1747 — Archived user-defined instance key-value metadata.
`shadow_instance_system_metadata` (rows=4879813): lines 1749-1773 — Archived system-managed instance attributes, distinct from current system metadata.
`shadow_instance_type_extra_specs` (rows=53): lines 1775-1799 — Archived key-value specifications for instance types, unlike current extra specs.
`shadow_instance_type_projects` (rows=104): lines 1801-1823 — Archived project grants for instance types, unlike current access grants.
`shadow_instances` (rows=709892): lines 1825-1939 — Archived deleted-instance records; current servers are in `instances`, and `all_instances` unions both.
`shadow_key_pairs` (rows=51): lines 1941-1969 — Archived SSH public keys and fingerprints, unlike current `key_pairs`.
`shadow_migrations` (rows=2112): lines 1971-2023 — Archived instance migration and resize attempts with source, destination, status, and progress.
`shadow_pci_devices` (rows=8): lines 2025-2069 — Archived PCI device inventory and assignment state from compute nodes.
`shadow_reservations` (rows=1297676): lines 2071-2103 — Archived quota reservation deltas, distinct from active reservation records.
`shadow_security_group_rules` (rows=40): lines 2105-2135 — Archived network security-group rules, unlike current `security_group_rules`.
`shadow_services` (rows=110): lines 2137-2173 — Archived Nova service status and heartbeat records; current service registrations are in `services`.
`shadow_snapshots` (rows=1): lines 2175-2211 — Archived Cinder volume snapshot metadata, unlike the current snapshot record.
`shadow_virtual_interfaces` (rows=742): lines 2213-2239 — Archived instance virtual-interface addresses, unlike the current network interface table.
`snapshot_id_mappings` (rows=1): lines 2241-2261 — Maps a legacy snapshot identifier to its UUID.
`snapshots` (rows=1): lines 2263-2299 — Current Cinder volume snapshot metadata, distinct from archived `shadow_snapshots`.
`volume_id_mappings` (rows=65): lines 2301-2321 — Maps legacy volume identifiers to UUIDs for Nova's volume references.
Summary: lines 2323-2323
