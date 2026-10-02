# Additional Metadata

## Clarified Semantics

- `deleted` int columns use the old nova soft-delete scheme: `0` = active/live row; non-zero = soft-deleted. For deleted rows the value is an internal marker (often the parent instance's id) shared across that instance's child tables (e.g. `instance_faults`, `instance_system_metadata`, `instance_extra`). Filter `deleted = 0` for current data; `deleted_at` is non-null only on soft-deleted rows.
- `instances.node` is the FQDN (host + `.yahoo.ca.com`), while `instances.host` is the short hostname. `compute_nodes.hypervisor_hostname` is likewise FQDN and `compute_nodes.host` is short; they describe the same machine under different name forms.
- `instances.host` / `instances.node` are empty (`''`, ~1416 rows) for instances never scheduled/built to a compute node.
- `all_instances` is a VIEW = `instances` UNION `shadow_instances`. It is ~717k rows vs ~7.9k in `instances`; the bulk comes from the shadow (historical/deleted) side. Use it for history across time, but filter carefully (e.g. by `deleted`, `vm_state`) to avoid the big decommissioned population.
- `block_device_mapping` stores one row per disk; `instance_uuid` may have many rows (root + data + swap). `boot_index = 0` marks the root disk; `source_type` ∈ {volume, image, blank, snapshot} and `destination_type` ∈ {volume, local} classify the device. `no_device`/`guest_format = 'swap'` are special flag rows.
- `fixed_ips.network_id = 1` for all rows and `networks` has exactly one row, so the network dimension is degenerate (1:1). In this dataset all `fixed_ips.instance_uuid` and `floating_ips.fixed_ip_id` are NULL/empty, so no live fixed<->floating association exists.
- `pci_devices` exposes per-NUMA-node physical devices (vendor `10de`, product `102d`, all `status='available'`). Its `instance_uuid` and `request_id` columns are present but always NULL here.
- `instance_groups` policy lives in `instance_group_policy` (affinity/anti-affinity), membership in `instance_group_member.instance_id` (a varchar uuid semantically pointing at `instances.uuid`, though no declared FK).
- `security_group_rules.group_id` = the security group that owns the rule; `security_group_rules.parent_group_id` = the source/parent group the rule refers to (both reference `security_groups.id`).
- `instance_type_projects` restricts flavor (instance_type) visibility per project, complementing `instance_types.is_public`.
- `pci_devices.dev_id` and `instance_extra.flavor`/`vcpu_model` store serialized nova objects (JSON), needing text parsing for joins.

## Potential Join Strategies

- **Instances to compute nodes**: `instances.node = compute_nodes.hypervisor_hostname` (FQDN) or `instances.host = compute_nodes.host` (short). Use `instances.host`→`compute_nodes.host` for simplicity; caveat: `compute_nodes.host` has ~8 `''` rows to exclude, and unscheduled instances have empty `host`.
- **Hosts to aggregates**: `aggregate_hosts.host` (short hostname) joins to `instances.host` and `compute_nodes.host`, letting you associate instances/nodes to `aggregates.id` without a declared FK. Restrict `aggregate_hosts.deleted = 0`.
- **Instance to group membership**: `instance_group_member.instance_id` (uuid) ↔ `instances.uuid`, with `group_id` ↔ `instance_groups.id` and `instance_group_policy.group_id` to classify groups as anti-affinity/affinity. Cardinality: one instance can belong to many groups; filter `deleted = 0` on member/policy rows.
- **Quota consumption**: `reservations.usage_id` → `quota_usages.id` (declared); both carry `project_id`/`user_id`, and `quota_usages` ↔ `quotas` by `project_id` to compare used vs hard limits. Prefer filtering by `quota_usages.deleted = 0`.
- **Flavor accessibility by project**: `instance_type_projects.instance_type_id` ↔ `instance_types.id` and `instance_type_projects.project_id` ↔ `instances.project_id`, useful to determine which flavors a project could use (in addition to `is_public`).
- **Failure/action forensics**: `instance_actions.id` ↔ `instance_actions_events.action_id` (declared), joining to `instances.uuid`; events carry `result` (Success/Error) and actions carry `message='Error'`. Similarly `instance_faults.instance_uuid` ↔ `instances.uuid` gives `code` 400/404/500.
- **Disk topology per instance**: drive via `block_device_mapping.instance_uuid` ↔ `instances.uuid`, filter `boot_index = 0` for root disks or `volume_id IS NOT NULL` for volume-backed; note many rows per instance (1:N).
- **Network mapping**: `fixed_ips.network_id` ↔ `networks.id` (degenerate 1:1, single network), and `instance_info_caches.network_info` holds serialized port/network JSON that can be text-parsed instead.
- **Numeric↔UUID instance identity**: `instance_id_mappings.uuid` ↔ `instances.uuid` and `instance_id_mappings.id` ↔ `instances.id` (numeric) to translate between the two identifiers used across tables.
- **GPU per instance**: `pci_devices.compute_node_id` ↔ `compute_nodes.id`, and `pci_devices.instance_uuid` ↔ `instances.uuid` for allocation tracking (currently all-NULL, so only node-level association is populated).