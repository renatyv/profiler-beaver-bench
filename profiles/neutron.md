---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:04:27.752405Z
dialect: mysql
database: neutron
schema: neutron
skipped_technical_tables:
  - `alembic_version`
---

## Relationships

- `agents`.`id` ← `bgp_speaker_dragent_bindings`.`agent_id`, `cisco_hosting_devices`.`cfg_agent_id`, `ha_router_agent_port_bindings`.`l3_agent_id`, `lbaas_loadbalanceragentbindings`.`agent_id`, `networkdhcpagentbindings`.`dhcp_agent_id`, `poolloadbalanceragentbindings`.`agent_id`, `routerl3agentbindings`.`l3_agent_id`
- `bgp_peers`.`id` ← `bgp_speaker_peer_bindings`.`bgp_peer_id`
- `bgp_speakers`.`id` ← `bgp_speaker_dragent_bindings`.`bgp_speaker_id`, `bgp_speaker_network_bindings`.`bgp_speaker_id`, `bgp_speaker_peer_bindings`.`bgp_speaker_id`
- `brocadenetworks`.`id` ← `brocadeports`.`network_id`
- `cisco_hosting_devices`.`id` ← `cisco_router_mappings`.`hosting_device_id`
- `cisco_ml2_n1kv_network_profiles`.`id` ← `cisco_ml2_n1kv_network_bindings`.`profile_id`, `cisco_ml2_n1kv_vlan_allocations`.`network_profile_id`, `cisco_ml2_n1kv_vxlan_allocations`.`network_profile_id`
- `firewall_policies`.`id` ← `firewall_rules`.`firewall_policy_id`, `firewalls`.`firewall_policy_id`
- `firewalls`.`id` ← `cisco_firewall_associations`.`fw_id`, `firewall_router_associations`.`fw_id`
- `flavors`.`id` ← `flavorserviceprofilebindings`.`flavor_id`, `lbaas_loadbalancers`.`flavor_id`
- `floatingips`.`id` ← `floatingipdnses`.`floatingip_id`
- `healthmonitors`.`id` ← `nsxv_edge_monitor_mappings`.`monitor_id`, `poolmonitorassociations`.`monitor_id`
- `ikepolicies`.`id` ← `ipsec_site_connections`.`ikepolicy_id`
- `ipallocationpools`.`id` ← `ipavailabilityranges`.`allocation_pool_id`
- `ipamallocationpools`.`id` ← `ipamavailabilityranges`.`allocation_pool_id`
- `ipamsubnets`.`id` ← `ipamallocationpools`.`ipam_subnet_id`, `ipamallocations`.`ipam_subnet_id`
- `ipsec_site_connections`.`id` ← `cisco_csr_identifier_map`.`ipsec_site_conn_id`, `ipsecpeercidrs`.`ipsec_site_connection_id`
- `ipsecpolicies`.`id` ← `ipsec_site_connections`.`ipsecpolicy_id`
- `lbaas_healthmonitors`.`id` ← `lbaas_pools`.`healthmonitor_id`
- `lbaas_l7policies`.`id` ← `lbaas_l7rules`.`l7policy_id`
- `lbaas_listeners`.`id` ← `lbaas_l7policies`.`listener_id`, `lbaas_sni`.`listener_id`
- `lbaas_loadbalancers`.`id` ← `lbaas_listeners`.`loadbalancer_id`, `lbaas_loadbalancer_statistics`.`loadbalancer_id`, `lbaas_loadbalanceragentbindings`.`loadbalancer_id`, `lbaas_pools`.`loadbalancer_id`
- `lbaas_pools`.`id` ← `lbaas_l7policies`.`redirect_pool_id`, `lbaas_listeners`.`default_pool_id`, `lbaas_members`.`pool_id`, `lbaas_sessionpersistences`.`pool_id`
- `lsn`.`lsn_id` ← `lsn_port`.`lsn_id`
- `meteringlabels`.`id` ← `meteringlabelrules`.`metering_label_id`
- `ml2_brocadenetworks`.`id` ← `ml2_brocadeports`.`network_id`
- `ml2_network_segments`.`id` ← `ml2_port_binding_levels`.`segment_id`
- `ml2_nexus_vxlan_allocations`.`vxlan_vni` ← `ml2_nexus_vxlan_mcast_groups`.`associated_vni`
- `networkgateways`.`id` ← `networkconnections`.`network_gateway_id`, `networkgatewaydevicereferences`.`network_gateway_id`
- `networks`.`id` ← `auto_allocated_topologies`.`network_id`, `bgp_speaker_network_bindings`.`network_id`, `cisco_ml2_n1kv_network_bindings`.`network_id`, `externalnetworks`.`network_id`, `ha_router_networks`.`network_id`, `ha_router_vrid_allocations`.`network_id`, `ipallocations`.`network_id`, `ml2_network_segments`.`network_id`, `multi_provider_networks`.`network_id`, `networkconnections`.`network_id`, `networkdhcpagentbindings`.`network_id`, `networkdnsdomains`.`network_id`, `networkqueuemappings`.`network_id`, `networkrbacs`.`object_id`, `networksecuritybindings`.`network_id`, `neutron_nsx_network_mappings`.`neutron_id`, `nsxv_internal_networks`.`network_id`, `nsxv_spoofguard_policy_network_mappings`.`network_id`, `nsxv_tz_network_bindings`.`network_id`, `nuage_provider_net_bindings`.`network_id`, `ports`.`network_id`, `qos_network_policy_bindings`.`network_id`, `subnets`.`network_id`, `tz_network_bindings`.`network_id`
- `nuage_net_partitions`.`id` ← `nuage_net_partition_router_mapping`.`net_partition_id`, `nuage_subnet_l2dom_mapping`.`net_partition_id`
- `pools`.`id` ← `members`.`pool_id`, `nsxv_edge_pool_mappings`.`pool_id`, `nsxv_edge_vip_mappings`.`pool_id`, `poolloadbalanceragentbindings`.`pool_id`, `poolmonitorassociations`.`pool_id`, `poolstatisticss`.`pool_id`
- `ports`.`id` ← `allowedaddresspairs`.`port_id`, `cisco_firewall_associations`.`port_id`, `cisco_hosting_devices`.`management_port_id`, `cisco_ml2_n1kv_port_bindings`.`port_id`, `cisco_port_mappings`.`hosting_port_id`, `cisco_port_mappings`.`logical_port_id`, `extradhcpopts`.`port_id`, `floatingips`.`fixed_port_id`, `floatingips`.`floating_port_id`, `ha_router_agent_port_bindings`.`port_id`, `ipallocations`.`port_id`, `lbaas_loadbalancers`.`vip_port_id`, `maclearningstates`.`port_id`, `ml2_dvr_port_bindings`.`port_id`, `ml2_port_binding_levels`.`port_id`, `ml2_port_bindings`.`port_id`, `networkconnections`.`port_id`, `neutron_nsx_port_mappings`.`neutron_id`, `nsxv_port_index_mappings`.`port_id`, `nsxv_port_vnic_mappings`.`neutron_id`, `portbindingports`.`port_id`, `portdnses`.`port_id`, `portqueuemappings`.`port_id`, `portsecuritybindings`.`port_id`, `qos_port_policy_bindings`.`port_id`, `routerports`.`port_id`, `routers`.`gw_port_id`, `securitygroupportbindings`.`port_id`, `vips`.`port_id`
- `qos_policies`.`id` ← `qos_bandwidth_limit_rules`.`qos_policy_id`, `qos_network_policy_bindings`.`policy_id`, `qos_port_policy_bindings`.`policy_id`, `qospolicyrbacs`.`object_id`
- `qosqueues`.`id` ← `networkqueuemappings`.`queue_id`, `portqueuemappings`.`queue_id`
- `reservations`.`id` ← `resourcedeltas`.`reservation_id`
- `routerrules`.`id` ← `nexthops`.`rule_id`
- `routers`.`id` ← `auto_allocated_topologies`.`router_id`, `cisco_ml2_apic_contracts`.`router_id`, `cisco_router_mappings`.`router_id`, `firewall_router_associations`.`router_id`, `floatingips`.`router_id`, `ha_router_agent_port_bindings`.`router_id`, `neutron_nsx_router_mappings`.`neutron_id`, `nsxv_router_ext_attributes`.`router_id`, `nuage_net_partition_router_mapping`.`router_id`, `router_extra_attributes`.`router_id`, `routerl3agentbindings`.`router_id`, `routerports`.`router_id`, `routerroutes`.`router_id`, `routerrules`.`router_id`, `vpnservices`.`router_id`
- `securitygrouprules`.`id` ← `nsxv_rule_mappings`.`neutron_id`
- `securitygroups`.`id` ← `default_security_group`.`security_group_id`, `neutron_nsx_security_group_mappings`.`neutron_id`, `nsxv_security_group_section_mappings`.`neutron_id`, `securitygroupportbindings`.`security_group_id`, `securitygrouprules`.`remote_group_id`, `securitygrouprules`.`security_group_id`
- `serviceprofiles`.`id` ← `flavorserviceprofilebindings`.`service_profile_id`
- `standardattributes`.`id` ← `floatingips`.`standard_attr_id`, `networks`.`standard_attr_id`, `ports`.`standard_attr_id`, `routers`.`standard_attr_id`, `securitygrouprules`.`standard_attr_id`, `securitygroups`.`standard_attr_id`, `subnetpools`.`standard_attr_id`, `subnets`.`standard_attr_id`, `tags`.`standard_attr_id`
- `subnetpools`.`id` ← `subnetpoolprefixes`.`subnetpool_id`
- `subnets`.`id` ← `dnsnameservers`.`subnet_id`, `ipallocationpools`.`subnet_id`, `ipallocations`.`subnet_id`, `nuage_subnet_l2dom_mapping`.`subnet_id`, `subnetroutes`.`subnet_id`, `vpnservices`.`subnet_id`
- `vips`.`id` ← `pools`.`vip_id`, `sessionpersistences`.`vip_id`
- `vpnservices`.`id` ← `ipsec_site_connections`.`vpnservice_id`

# `agents`  (rows=129)

columns:
`id` varchar36 PK: uuid, unique identifier
`agent_type` varchar255 NOTNULL: "Open vSwitch agent"=125, "DHCP agent"=1, "L3 agent"=1, "Loadbalancerv2 agent"=1, "Metadata agent"=1
`binary` varchar255 NOTNULL: "neutron-openvswitch-agent"=125, "neutron-dhcp-agent"=1, "neutron-l3-agent"=1, "neutron-lbaasv2-agent"=1, "neutron-metadata-agent"=1
`topic` varchar255 NOTNULL: ""=126, "dhcp_agent"=1, "l3_agent"=1, "n-lbaasv2_agent"=1
`host` varchar255 NOTNULL: 125 distinct, "gamut-16"=5, "align-73"=1, "align-79"=1, "align-86"=1, "alpha-80"=1, "arrow-57"=1, "astro-92"=1, "astro1-40"=1, "axis-11"=1, "beam8-22"=1
`admin_state_up` int NOTNULL: 1=129
`created_at` datetime NOTNULL: 80 distinct
`started_at` datetime NOTNULL: 115 distinct
`heartbeat_timestamp` datetime NOTNULL: 86 distinct
`description` varchar255: all NULL
`configurations` varchar4095 NOTNULL: all distinct
`load` int NOTNULL: 0=128, 42=1
`availability_zone` varchar255: "nova"=2, nulls=127
`resource_versions` varchar8191: "{"QosPolicy": "1.0"}"=123, "{"Subnet": "1.0", "Network": "1.0", "SubPort": "1.0", "SecurityGroup": "1.0", "SecurityGroupRule": "1.0", "Trunk": "1.1", "QosPolicy": "1.7", "Port": "1.1", "Log": "1.0"}"=1, nulls=5

indexes: UNIQUE (`agent_type`,`host`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | ff9b1722-0846-4fdf-9c33-97d8cefcdf35 | ef8f86b7-dc70-41ed-9c9b-80b0945d501a | 50218173-3ea7-4499-b4c9-3d545810f488 |
| agent_type | Open vSwitch agent | Open vSwitch agent | Open vSwitch agent |
| binary | neutron-openvswitch-agent | neutron-openvswitch-agent | neutron-openvswitch-agent |
| topic |  |  |  |
| host | spark5-69 | flash4-74 | xenon5-10 |
| admin_state_up | 1 | 1 | 1 |
| created_at | 2017-12-11T17:13:05 | 2014-12-04T15:46:31 | 2018-02-05T21:08:19 |
| started_at | 2022-03-09T13:07:46 | 2017-11-30T11:46:08 | 2022-07-16T13:01:53 |
| heartbeat_timestamp | 2024-07-08T06:59:43 | 2017-12-11T15:42:49 | 2022-08-05T15:27:40 |
| description | null | null | null |
| configurations | {"ovs_hybrid_plug": true, "in_distributed_mode": false, "datapath_type": "system", "arp_responder_enabled": false, "tunneling_ip": "10.60.50.88/8", "vhostuser_socket_dir": "/var/run/openvswitch", "de… | {"ovs_hybrid_plug": true, "in_distributed_mode": false, "datapath_type": "system", "arp_responder_enabled": false, "tunneling_ip": "10.43.41.123/8", "vhostuser_socket_dir": "/var/run/openvswitch", "d… | {"ovs_hybrid_plug": true, "in_distributed_mode": false, "datapath_type": "system", "arp_responder_enabled": false, "tunneling_ip": "10.47.215.156/8", "vhostuser_socket_dir": "/var/run/openvswitch", "… |
| load | 0 | 0 | 0 |
| availability_zone | null | null | null |
| resource_versions | {"QosPolicy": "1.0"} | {"QosPolicy": "1.0"} | {"QosPolicy": "1.0"} |

# `alembic_version_fwaas`  (rows=2)

columns:
`version_num` varchar32 NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| version_num | 458aa42b14b | 4b47ea298795 |

# `alembic_version_lbaas`  (rows=2)

columns:
`version_num` varchar32 NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| version_num | 130ebfdef43 | 62deca5010cd |

# `allowedaddresspairs`  (rows=1)

columns:
`port_id` varchar36 PK FK
`mac_address` varchar32 PK
`ip_address` varchar64 PK

indexes: none

all rows:
| column | row 1 |
|---|---|
| port_id | 25d421c1-c76d-4c26-9550-9f871a1d5034 |
| mac_address | fa:16:3e:33:7f:de |
| ip_address | 10.232.210.41/8 |

# `default_security_group`  (rows=804)

columns:
`tenant_id` varchar255 PK: unique identifier
`security_group_id` varchar36 NOTNULL FK: uuid, unique identifier

indexes: `security_group_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | ffa0e5fc492e4b4290bb9e2757850411 | 22198a26210d4204978593a6c1a4cfdb | 7f8fbdfe72704ac4b6c99a29f31bed87 |
| security_group_id | 28c85503-4127-43be-b2d4-842965390d71 | aa6083c9-17f0-4670-9375-87c69eb8a96f | 89ae18ac-cf2d-46ae-a678-a93ee5ad9f56 |

# `dnsnameservers`  (rows=65)

columns:
`address` varchar128 PK: "10.229.203.154/8"=20, "10.67.40.40/8"=19, "10.49.228.132/8"=17, "10.107.23.242/8"=6, "10.159.230.188/8"=2, "10.61.127.33/8"=1
`subnet_id` varchar36 PK FK: uuid, 22 distinct
`order` int NOTNULL: 0=35, 1=14, 2=14, 3=2, 0..3

indexes: `subnet_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| address | 10.67.40.40/8 | 10.67.40.40/8 | 10.67.40.40/8 |
| subnet_id | faee7948-a17f-4e58-a557-7ea1219c3b5f | 25a309b3-7334-44b7-99b5-85a874d28475 | 862e31fa-ce44-4f58-95b7-9bf1193cb5c9 |
| order | 0 | 0 | 0 |

# `externalnetworks`  (rows=1)

columns:
`network_id` varchar36 PK FK
`is_default` int NOTNULL

indexes: none

all rows:
| column | row 1 |
|---|---|
| network_id | 8ad137b5-cc2b-44c7-9db0-e4f81d978d0c |
| is_default | 0 |

# `floatingips`  (rows=23)

columns:
`tenant_id` varchar255: "bfd50153a2e9476f93e33e30e922cd06"=9, "e3fb2659584e436a832461dac02835f0"=8, "98333a1a28e746fa8c629c83a818ad57"=6
`id` varchar36 PK: uuid, unique identifier
`floating_ip_address` varchar64 NOTNULL: all distinct
`floating_network_id` varchar36 NOTNULL: "8ad137b5-cc2b-44c7-9db0-e4f81d978d0c"=23
`floating_port_id` varchar36 NOTNULL FK: uuid, unique identifier
`fixed_port_id` varchar36 FK: "0f528984-32f5-42cc-8300-7891a95de4b2"=1, "1ad79ec8-e474-4e47-b6ac-8172c0bc864d"=1, "30473f2c-8bc6-4f7d-9e56-ce98c3c3b18c"=1, "39f05ecd-f829-4643-8c9b-e82eebc255ba"=1, "4de74bdc-9b15-425b-a7b2-5241e0cb77c5"=1, "6c01c261-75db-4ba0-9426-b6aae8b24050"=1, "6ce29c77-5c0c-4565-a344-fb0a20069624"=1, "6e3ad94d-2fc1-4725-b2a7-c56649d13817"=1, "719c6ad3-5352-44ab-8414-c0e790ab52ce"=1, "b85cba43-623e-4983-abfc-3b1ef8d52f03"=1, nulls=13
`fixed_ip_address` varchar64: "10.131.164.126/8"=1, "10.163.134.148/8"=1, "10.198.158.49/8"=1, "10.20.127.222/8"=1, "10.209.133.213/8"=1, "10.220.221.69/8"=1, "10.66.46.213/8"=1, "10.67.41.78/8"=1, "10.71.60.243/8"=1, "10.92.93.246/8"=1, nulls=13
`router_id` varchar36 FK: "9ff894ce-d884-46fd-9c47-c5fb7d6fb933"=3, "fa95b6df-6eef-49a9-a7df-753eeb99c527"=3, "a154bb98-4a0d-4a6c-bcfa-e1afb65ce71e"=2, "71e9342c-dd51-4f9d-843d-892285bff645"=1, "8f10910e-4827-4528-9d63-501ef1e25ffa"=1, nulls=13
`last_known_router_id` varchar36: "71e9342c-dd51-4f9d-843d-892285bff645"=1, nulls=22
`status` varchar16: "DOWN"=13, "ACTIVE"=10
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 5825..49574

indexes: `fixed_port_id`, `floating_port_id`, `tenant_id`, `router_id`, UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | e3fb2659584e436a832461dac02835f0 | e3fb2659584e436a832461dac02835f0 | bfd50153a2e9476f93e33e30e922cd06 |
| id | e34474f1-b958-4969-b073-b66c9a449ea4 | 84b503c0-9cf2-4155-98e5-5868703ac6f2 | d189e6ab-4e60-4876-99f3-d9b2f5d75803 |
| floating_ip_address | 10.144.191.176/8 | 10.37.254.28/8 | 10.136.216.22/8 |
| floating_network_id | 8ad137b5-cc2b-44c7-9db0-e4f81d978d0c | 8ad137b5-cc2b-44c7-9db0-e4f81d978d0c | 8ad137b5-cc2b-44c7-9db0-e4f81d978d0c |
| floating_port_id | bf817042-61e4-4a1f-9a18-7313f52cc604 | e4961a83-21c2-446b-8964-84460741fbb8 | a9ccabcf-c298-4997-9dd1-2851b26c8b68 |
| fixed_port_id | null | null | 39f05ecd-f829-4643-8c9b-e82eebc255ba |
| fixed_ip_address | null | null | 10.209.133.213/8 |
| router_id | null | null | fa95b6df-6eef-49a9-a7df-753eeb99c527 |
| last_known_router_id | null | null | null |
| status | DOWN | DOWN | ACTIVE |
| standard_attr_id | 49570 | 49574 | 21352 |

# `healthmonitors`  (rows=3)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`type` enum NOTNULL
`delay` int NOTNULL
`timeout` int NOTNULL
`max_retries` int NOTNULL
`http_method` varchar16
`url_path` varchar255
`expected_codes` varchar64
`admin_state_up` int NOTNULL

indexes: `tenant_id`

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| tenant_id | 98333a1a28e746fa8c629c83a818ad57 | 0fe46c69adaf4d2fb01401e0dd952815 | 98333a1a28e746fa8c629c83a818ad57 |
| id | 12373804-bd7c-4ea0-86c1-a74985093e9d | a9ec94c3-756f-40ad-ac48-1570196fd8fc | b96f96fe-beb1-4225-a73c-0b42ed6a792a |
| type | HTTP | PING | HTTP |
| delay | 3 | 300 | 5 |
| timeout | 3 | 3 | 2 |
| max_retries | 3 | 3 | 3 |
| http_method | GET | GET | GET |
| url_path | / | / | / |
| expected_codes | 200 | 200 | 302 |
| admin_state_up | 1 | 1 | 1 |

# `ipallocationpools`  (rows=49)

columns:
`id` varchar36 PK: uuid, unique identifier
`subnet_id` varchar36 FK: uuid, unique identifier
`first_ip` varchar64 NOTNULL: 45 distinct
`last_ip` varchar64 NOTNULL: 46 distinct

indexes: `subnet_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | f2c784e3-2b56-4fca-b9d2-f5432b4fbce3 | 32206cb1-51e5-43e3-85b5-b4a9498f4ba0 | c16562ef-a48d-4189-a672-7ae1129203e7 |
| subnet_id | c8dbe01f-3465-46f8-a3b0-20436272a81a | 26a23140-1cb7-4ccd-b2d7-50611eb82663 | 9a5dbe03-34ac-4c93-89b8-cd16bb198697 |
| first_ip | 10.148.172.254/8 | 10.89.22.204/8 | 10.30.33.48/8 |
| last_ip | 10.179.7.202/8 | 10.91.230.4/8 | 10.20.2.132/8 |

# `ipallocations`  (rows=3779)

columns:
`port_id` varchar36 FK: uuid, 3773 distinct, nulls=1, "8b2ca872-1f42-42ef-b9d3-1dbff697a0c4"=3, "37d52145-4026-4917-8382-0275704b5d34"=2, "8c4b66f2-3a91-40aa-b72c-2a18452f277c"=2, "de76bee3-ddcd-4140-9efc-16b384d7c82d"=2, "000a1fab-1d06-449d-a126-fd838e023596"=1, "0012b1a9-8387-4c17-8578-755f5984aec4"=1, "00167498-2a08-49f1-932e-6d329fb8d469"=1, "002abd1b-ea0c-4d24-8813-de12b56314c3"=1, "0036e9ca-2908-40a9-8c5b-49ae337fd939"=1, "003b4cf8-a0fe-4143-908c-9098683cd970"=1
`ip_address` varchar64 PK: 3771 distinct, "10.150.64.113/8"=3, "10.10.33.226/8"=2, "10.103.209.35/8"=2, "10.210.236.141/8"=2, "10.241.214.72/8"=2, "10.35.234.88/8"=2, "10.89.22.204/8"=2, "10.0.145.204/8"=1, "10.0.147.27/8"=1, "10.0.147.41/8"=1
`subnet_id` varchar36 PK FK: uuid, 48 distinct, "76123b94-2ae9-40c4-a4c6-03ee98d081d9"=3622, "36ad083d-c3cc-443f-8821-c85601c10084"=39, "e8da8ec5-364b-4a31-afaf-f68a206b7846"=19, "9ce2600b-6566-4c81-9370-9b758d5f7ccc"=7, "0807c5b3-aa6c-4108-8884-7b4948a19178"=5, "16eaae8c-1920-4b8b-8765-f149dde8a1a6"=5, "2019039a-089f-408c-b080-201a0c5cbe6f"=5, "34321473-f650-4886-808c-9b2431aafc8c"=4, "388ee748-7b3d-4049-99b4-7e582937bbd4"=4, "97c5b573-621a-4d16-8c90-12f7d411d7e9"=4
`network_id` varchar36 PK FK: uuid, 45 distinct, "0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d"=3622, "8ad137b5-cc2b-44c7-9db0-e4f81d978d0c"=39, "b3d6c27a-a9bb-4521-b5de-4d65eb7490dc"=20, "4207d69c-903d-48d3-be48-debcb46b3241"=7, "18b03960-577f-49a4-be38-aafb4e05f3f3"=5, "259e350d-9ea5-4dc5-8a1c-4ab7deef9eec"=5, "82caefaf-7420-4122-80c4-92e46e9fd658"=5, "c9e8f307-e1d5-4c06-b464-ef5370ca1d6d"=5, "38bfcc47-5f4d-46c8-9596-fb3a69f64e1e"=4, "5ec0b65f-6115-4525-8093-a8ce01707624"=4

indexes: `network_id`, `port_id`, `subnet_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| port_id | 44283b5e-1502-436a-be73-caf0d33ab36d | 2daa6cd5-7e85-46f2-9f87-d525aeb0a1a3 | 339efd58-eee9-4e80-8b17-8a6fe87ca2f9 |
| ip_address | track | 10.216.253.165/8 | 10.20.223.125/8 |
| subnet_id | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 |
| network_id | 0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d | 0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d | 0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d |

# `ipavailabilityranges`  (rows=184)

columns:
`allocation_pool_id` varchar36 PK FK: uuid, 47 distinct, "455ff839-68cc-497c-80cb-aec8ddd623a8"=138, "06e7704e-6327-445d-849c-1c9ca111c2e6"=1, "07a675f9-e85b-4204-82d2-15e7c8182a73"=1, "0948c06d-3279-46ff-93d5-1b9e23efc4f8"=1, "0e8845e0-2994-4c9e-a1e1-8c4f9e89aad6"=1, "189eb400-ef8d-4016-9635-fa002c46b890"=1, "2a7c6458-7c04-4592-866f-60523ee5e0cc"=1, "2a9523ea-0206-45ec-aed6-6223ed8d39ee"=1, "32206cb1-51e5-43e3-85b5-b4a9498f4ba0"=1, "399c52ff-0415-429d-ab58-1debafe21b75"=1
`first_ip` varchar64 PK: all distinct
`last_ip` varchar64 PK: 181 distinct, "10.128.178.118/8"=3, "10.8.222.32/8"=2, "10.0.114.247/8"=1, "10.101.177.172/8"=1, "10.103.105.29/8"=1, "10.103.41.89/8"=1, "10.104.153.88/8"=1, "10.106.196.208/8"=1, "10.107.244.154/8"=1, "10.11.159.85/8"=1

indexes: UNIQUE (`first_ip`,`allocation_pool_id`), UNIQUE (`last_ip`,`allocation_pool_id`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| allocation_pool_id | f2c784e3-2b56-4fca-b9d2-f5432b4fbce3 | 455ff839-68cc-497c-80cb-aec8ddd623a8 | 455ff839-68cc-497c-80cb-aec8ddd623a8 |
| first_ip | 10.58.155.83/8 | 10.255.13.100/8 | 10.36.210.233/8 |
| last_ip | 10.179.7.202/8 | 10.23.232.17/8 | 10.38.9.67/8 |

# `lbaas_listeners`  (rows=5)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`name` varchar255
`description` varchar255
`protocol` enum NOTNULL
`protocol_port` int NOTNULL
`connection_limit` int
`loadbalancer_id` varchar36 FK
`default_pool_id` varchar36 FK
`admin_state_up` int NOTNULL
`provisioning_status` varchar16 NOTNULL
`operating_status` varchar16 NOTNULL
`default_tls_container_id` varchar128

indexes: `tenant_id`, `default_pool_id`, UNIQUE (`loadbalancer_id`,`protocol_port`)

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| tenant_id | 98333a1a28e746fa8c629c83a818ad57 | 98333a1a28e746fa8c629c83a818ad57 | bfd50153a2e9476f93e33e30e922cd06 | bfd50153a2e9476f93e33e30e922cd06 | bfd50153a2e9476f93e33e30e922cd06 |
| id | 2a85040d-56d9-4207-8488-c5d2687be58c | 2ddb1f70-890b-4853-bf9b-a04593d47a21 | 4e33b66f-969d-4295-a69b-115f5f8c260d | c3371dba-3863-4f7f-a53e-5d17c3fbc488 | e7c78090-2943-40a7-a0c1-090008edf3c6 |
| name | arrow_qiwshhdpzmujcbjyihwd_0 | grav_inimyemtwhpmxlsuowhe_0 | alpha_tivizxmrkokbssycgdut_0 | flare_agkeptezowlzkavlvbwe_0 | pulse_nmjefdcfpqavsgrbhwfg_0 |
| description | null | null | null | null | null |
| protocol | TCP | TCP | TCP | TCP | TCP |
| protocol_port | 80 | 80 | 70 | 443 | 80 |
| connection_limit | -1 | -1 | -1 | -1 | -1 |
| loadbalancer_id | a77dc8fd-7a03-4094-8f00-91d110e076a3 | 24afca2d-35b7-4188-99c7-56d9db33f2a6 | 0367b35b-023b-41d5-816b-359b3bcbdd8e | 512a3faf-0374-4ef6-b0a7-c31dd9dc01a7 | 6f6557de-545d-4242-a7a4-eb18b3eba88f |
| default_pool_id | 03c2ef39-04ca-4652-a26e-e790cb7db5ce | 465bd555-a001-461a-9aed-41405a2a8bdb | 84ed8864-e9d5-436a-b662-4b4e8d4b7893 | 4b1b8e0d-663b-445a-b130-b409c2f41bf0 | f256a064-1fe7-43b3-ab76-522886bc27d8 |
| admin_state_up | 1 | 1 | 1 | 1 | 1 |
| provisioning_status | ACTIVE | ACTIVE | ACTIVE | ACTIVE | ACTIVE |
| operating_status | ONLINE | ONLINE | ONLINE | ONLINE | ONLINE |
| default_tls_container_id | null | null | null | null | null |

# `lbaas_loadbalancer_statistics`  (rows=6)

columns:
`loadbalancer_id` varchar36 PK FK
`bytes_in` bigint NOTNULL
`bytes_out` bigint NOTNULL
`active_connections` bigint NOTNULL
`total_connections` bigint NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| loadbalancer_id | 0367b35b-023b-41d5-816b-359b3bcbdd8e | 24afca2d-35b7-4188-99c7-56d9db33f2a6 | 512a3faf-0374-4ef6-b0a7-c31dd9dc01a7 | 6f6557de-545d-4242-a7a4-eb18b3eba88f | a77dc8fd-7a03-4094-8f00-91d110e076a3 | ed1c2c08-165d-413b-805f-2bdacfef89a6 |
| bytes_in | 21472 | 3716370 | 3125949 | 2692581 | 2933704 | 0 |
| bytes_out | 0 | 0 | 0 | 0 | 0 | 0 |
| active_connections | 0 | 0 | 0 | 0 | 0 | 0 |
| total_connections | 386 | 20412 | 14698 | 14349 | 15628 | 0 |

# `lbaas_loadbalanceragentbindings`  (rows=6)

columns:
`loadbalancer_id` varchar36 PK FK
`agent_id` varchar36 NOTNULL FK

indexes: `agent_id`

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| loadbalancer_id | 0367b35b-023b-41d5-816b-359b3bcbdd8e | 24afca2d-35b7-4188-99c7-56d9db33f2a6 | 512a3faf-0374-4ef6-b0a7-c31dd9dc01a7 | 6f6557de-545d-4242-a7a4-eb18b3eba88f | a77dc8fd-7a03-4094-8f00-91d110e076a3 | ed1c2c08-165d-413b-805f-2bdacfef89a6 |
| agent_id | f5e7202b-3276-4f9c-8d95-68e3688836db | f5e7202b-3276-4f9c-8d95-68e3688836db | f5e7202b-3276-4f9c-8d95-68e3688836db | f5e7202b-3276-4f9c-8d95-68e3688836db | f5e7202b-3276-4f9c-8d95-68e3688836db | f5e7202b-3276-4f9c-8d95-68e3688836db |

# `lbaas_loadbalancers`  (rows=6)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`name` varchar255
`description` varchar255
`vip_port_id` varchar36 FK
`vip_subnet_id` varchar36 NOTNULL
`vip_address` varchar36
`admin_state_up` int NOTNULL
`provisioning_status` varchar16 NOTNULL
`operating_status` varchar16 NOTNULL
`flavor_id` varchar36 FK

indexes: `flavor_id`, `vip_port_id`, `tenant_id`

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| tenant_id | bfd50153a2e9476f93e33e30e922cd06 | 98333a1a28e746fa8c629c83a818ad57 | bfd50153a2e9476f93e33e30e922cd06 | bfd50153a2e9476f93e33e30e922cd06 | 98333a1a28e746fa8c629c83a818ad57 | bfd50153a2e9476f93e33e30e922cd06 |
| id | 0367b35b-023b-41d5-816b-359b3bcbdd8e | 24afca2d-35b7-4188-99c7-56d9db33f2a6 | 512a3faf-0374-4ef6-b0a7-c31dd9dc01a7 | 6f6557de-545d-4242-a7a4-eb18b3eba88f | a77dc8fd-7a03-4094-8f00-91d110e076a3 | ed1c2c08-165d-413b-805f-2bdacfef89a6 |
| name | aurum-credo | bjuakvpbywrsmksufdmw | gqgxlywtlazwffeogfps | ether-flare | nexus-forge | wsokhmicwhimbikzygpg |
| description | 7320f5fc7ad77ef345055eb8080a8c14 | b719b94a8f2ff66de11da5ad5a388d95 | df93b65c6b85b9a7f306c05f31fbee97 | 44c601f0ed3ff090e3962cc1bc48d6e2 | ae23036216f4e1b8f978fc1dc7534d4e |  |
| vip_port_id | 39f05ecd-f829-4643-8c9b-e82eebc255ba | 6e3ad94d-2fc1-4725-b2a7-c56649d13817 | 6c01c261-75db-4ba0-9426-b6aae8b24050 | 719c6ad3-5352-44ab-8414-c0e790ab52ce | 30473f2c-8bc6-4f7d-9e56-ce98c3c3b18c | c492317a-3424-4226-9ba3-1ba08749cb27 |
| vip_subnet_id | 2019039a-089f-408c-b080-201a0c5cbe6f | 0807c5b3-aa6c-4108-8884-7b4948a19178 | 2019039a-089f-408c-b080-201a0c5cbe6f | 2019039a-089f-408c-b080-201a0c5cbe6f | 0807c5b3-aa6c-4108-8884-7b4948a19178 | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 |
| vip_address | 10.209.133.213/8 | 10.71.60.243/8 | 10.67.41.78/8 | 10.198.158.49/8 | 10.20.127.222/8 | 10.122.60.167/8 |
| admin_state_up | 1 | 1 | 1 | 1 | 1 | 1 |
| provisioning_status | ACTIVE | ACTIVE | ACTIVE | ACTIVE | ACTIVE | ACTIVE |
| operating_status | ONLINE | ONLINE | ONLINE | ONLINE | ONLINE | ONLINE |
| flavor_id | null | null | null | null | null | null |

# `lbaas_members`  (rows=22)

columns:
`tenant_id` varchar255: "bfd50153a2e9476f93e33e30e922cd06"=12, "98333a1a28e746fa8c629c83a818ad57"=10
`id` varchar36 PK: uuid, unique identifier
`pool_id` varchar36 NOTNULL FK: "03c2ef39-04ca-4652-a26e-e790cb7db5ce"=5, "465bd555-a001-461a-9aed-41405a2a8bdb"=5, "4b1b8e0d-663b-445a-b130-b409c2f41bf0"=4, "84ed8864-e9d5-436a-b662-4b4e8d4b7893"=4, "f256a064-1fe7-43b3-ab76-522886bc27d8"=4
`subnet_id` varchar36: "2019039a-089f-408c-b080-201a0c5cbe6f"=12, "0807c5b3-aa6c-4108-8884-7b4948a19178"=10
`address` varchar64 NOTNULL: "10.111.186.226/8"=3, "10.154.119.80/8"=3, "10.171.206.66/8"=3, "10.174.5.53/8"=3, "10.123.57.224/8"=2, "10.16.112.58/8"=2, "10.222.179.47/8"=2, "10.6.159.91/8"=2, "10.60.169.197/8"=2
`protocol_port` int NOTNULL: 31042=5, 31154=5, 30062=4, 30637=4, 31582=4, 30062..31582
`weight` int: 1=22
`admin_state_up` int NOTNULL: 1=22
`provisioning_status` varchar16 NOTNULL: "ACTIVE"=22
`operating_status` varchar16 NOTNULL: "ONLINE"=22
`name` varchar255: all NULL

indexes: `tenant_id`, UNIQUE (`pool_id`,`address`,`protocol_port`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | bfd50153a2e9476f93e33e30e922cd06 | 98333a1a28e746fa8c629c83a818ad57 | 98333a1a28e746fa8c629c83a818ad57 |
| id | f2bab0c3-e5d8-4577-9a7b-7340420dda81 | 14d172d4-801b-4fbe-a394-3375acbd93ca | 231b2eed-a101-4337-80aa-00ec0164f2a0 |
| pool_id | 84ed8864-e9d5-436a-b662-4b4e8d4b7893 | 03c2ef39-04ca-4652-a26e-e790cb7db5ce | 465bd555-a001-461a-9aed-41405a2a8bdb |
| subnet_id | 2019039a-089f-408c-b080-201a0c5cbe6f | 0807c5b3-aa6c-4108-8884-7b4948a19178 | 0807c5b3-aa6c-4108-8884-7b4948a19178 |
| address | 10.154.119.80/8 | 10.16.112.58/8 | 10.6.159.91/8 |
| protocol_port | 30637 | 31042 | 31154 |
| weight | 1 | 1 | 1 |
| admin_state_up | 1 | 1 | 1 |
| provisioning_status | ACTIVE | ACTIVE | ACTIVE |
| operating_status | ONLINE | ONLINE | ONLINE |
| name | null | null | null |

# `lbaas_pools`  (rows=5)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`name` varchar255
`description` varchar255
`protocol` enum NOTNULL
`lb_algorithm` enum NOTNULL
`healthmonitor_id` varchar36 UNIQ FK
`admin_state_up` int NOTNULL
`provisioning_status` varchar16 NOTNULL
`operating_status` varchar16 NOTNULL
`loadbalancer_id` varchar36 FK

indexes: UNIQUE `healthmonitor_id`, `tenant_id`, `loadbalancer_id`

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| tenant_id | 98333a1a28e746fa8c629c83a818ad57 | 98333a1a28e746fa8c629c83a818ad57 | bfd50153a2e9476f93e33e30e922cd06 | bfd50153a2e9476f93e33e30e922cd06 | bfd50153a2e9476f93e33e30e922cd06 |
| id | 03c2ef39-04ca-4652-a26e-e790cb7db5ce | 465bd555-a001-461a-9aed-41405a2a8bdb | 4b1b8e0d-663b-445a-b130-b409c2f41bf0 | 84ed8864-e9d5-436a-b662-4b4e8d4b7893 | f256a064-1fe7-43b3-ab76-522886bc27d8 |
| name | shift_qzvqvsbpucjgwxzxzvya_0 | track_lborfddzhtpfumnepdvi_0 | streak_fwxpvgiyyudtixsfcjvu_0 | meter_tbauczjaeoubpkmfukok_0 | twist_kmfenscozwggrvxjtsxi_0 |
| description | null | null | null | null | null |
| protocol | TCP | TCP | TCP | TCP | TCP |
| lb_algorithm | ROUND_ROBIN | ROUND_ROBIN | ROUND_ROBIN | ROUND_ROBIN | ROUND_ROBIN |
| healthmonitor_id | null | null | null | null | null |
| admin_state_up | 1 | 1 | 1 | 1 | 1 |
| provisioning_status | ACTIVE | ACTIVE | ACTIVE | ACTIVE | ACTIVE |
| operating_status | ONLINE | ONLINE | ONLINE | ONLINE | ONLINE |
| loadbalancer_id | a77dc8fd-7a03-4094-8f00-91d110e076a3 | 24afca2d-35b7-4188-99c7-56d9db33f2a6 | 512a3faf-0374-4ef6-b0a7-c31dd9dc01a7 | 0367b35b-023b-41d5-816b-359b3bcbdd8e | 6f6557de-545d-4242-a7a4-eb18b3eba88f |

# `members`  (rows=4)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`pool_id` varchar36 NOTNULL FK
`address` varchar64 NOTNULL
`protocol_port` int NOTNULL
`weight` int NOTNULL
`status` varchar16 NOTNULL
`status_description` varchar255
`admin_state_up` int NOTNULL

indexes: `tenant_id`, `pool_id`, UNIQUE (`pool_id`,`address`,`protocol_port`)

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| tenant_id | daa18fdafdf04b5eac18e04aa19ee214 | 0fe46c69adaf4d2fb01401e0dd952815 | 0fe46c69adaf4d2fb01401e0dd952815 | 0fe46c69adaf4d2fb01401e0dd952815 |
| id | 45561760-9ecc-4e85-8725-9cafb9691b83 | b2fb6a43-9e03-4d1c-9beb-35fcb25cffbb | b55b2590-0e1b-4847-aeec-d8e1625087ca | f1897fa4-5e59-4e68-b23d-9df0defd310f |
| pool_id | 213fccb5-6482-4c4b-b66a-06a1eb283331 | c7d33358-67e9-407f-91b4-241f2584e242 | c7d33358-67e9-407f-91b4-241f2584e242 | c7d33358-67e9-407f-91b4-241f2584e242 |
| address | 10.241.232.133/8 | 10.198.253.45/8 | 10.132.208.137/8 | 10.124.243.155/8 |
| protocol_port | 8080 | 443 | 443 | 443 |
| weight | 1 | 1 | 1 | 1 |
| status | ACTIVE | ACTIVE | ACTIVE | ACTIVE |
| status_description | null | null | null | null |
| admin_state_up | 1 | 1 | 1 | 1 |

# `ml2_gre_allocations`  (rows=1000)

columns:
`gre_id` int PK: unique identifier, 1..1000
`allocated` int NOTNULL: 0=968, 1=32

indexes: `allocated`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| gre_id | 1000 | 942 | 943 |
| allocated | 0 | 0 | 0 |

# `ml2_gre_endpoints`  (rows=124)

columns:
`ip_address` varchar64 PK: unique identifier
`host` varchar255 UNIQ: unique identifier, nulls=5

indexes: UNIQUE `host`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ip_address | 10.96.19.200/8 | 10.91.128.139/8 | 10.0.125.196/8 |
| host | drift-69 | null | null |

# `ml2_network_segments`  (rows=49)

columns:
`id` varchar36 PK: uuid, unique identifier
`network_id` varchar36 NOTNULL FK: uuid, unique identifier
`network_type` varchar32 NOTNULL: "gre"=42, "vlan"=7
`physical_network` varchar64: "trunk"=7, nulls=42
`segmentation_id` int: 40 distinct, 1..3000
`is_dynamic` int NOTNULL: 0=49
`segment_index` int NOTNULL: 0=49

indexes: `network_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | fd961fc1-c324-49bc-8f53-629f0af064d8 | ea0f417c-0c81-461b-a705-81ad4d2e62b0 | c583d60a-93ab-4a42-9ed9-4e587b1a8551 |
| network_id | b4f80478-cac6-49b2-9485-8d011dc9cb53 | 04dc6fb8-2d9e-4739-9c71-1e3dc9ab6390 | 18b03960-577f-49a4-be38-aafb4e05f3f3 |
| network_type | gre | gre | gre |
| physical_network | null | null | null |
| segmentation_id | 7 | 40 | 104 |
| is_dynamic | 0 | 0 | 0 |
| segment_index | 0 | 0 | 0 |

# `ml2_port_binding_levels`  (rows=3692)

columns:
`port_id` varchar36 PK FK: uuid, unique identifier
`host` varchar255 PK: 120 distinct, "blaze8-12"=231, "forge-23"=162, "drive-59"=116, "flare4-57"=116, "align-86"=113, "blitz1-32"=108, "galax4-70"=107, "spark9-96"=101, "cosmo3-23"=98, "flux-60"=95
`level` int PK: 0=3692
`driver` varchar64: "openvswitch"=3692
`segment_id` varchar36 FK: uuid, 46 distinct, "40c56f51-8c44-4d82-8369-d065010ed91a"=3569, "4cee9f71-2664-48bc-99c6-904f2e5e2a4d"=18, "1626d3ed-6340-4b68-a46c-2982bab302c8"=16, "849f1332-db7a-4bae-a09e-be6f272baede"=7, "8ca8cdd2-63f2-4b18-a86b-7f9c7c8542c4"=5, "f7506aa6-0a24-4a1d-b6d8-2582ca1f8c23"=5, "69796581-1c58-403c-a21e-7579bb5b05b4"=4, "c583d60a-93ab-4a42-9ed9-4e587b1a8551"=4, "e1f1caed-fc73-438f-ad9b-ba52fed4d338"=4, "fad83f9c-fff2-4170-ba77-dcd63ecb1e88"=4

indexes: `segment_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| port_id | ffe46d1d-3e9c-44f6-89c4-ad61eb5902d4 | aae859c9-1e74-4ba5-b79f-8912a363ae5e | 89fbbbe1-3947-4097-aee6-fcc1b9e5571f |
| host | forge-23 | nexis-43 | nexus-51 |
| level | 0 | 0 | 0 |
| driver | openvswitch | openvswitch | openvswitch |
| segment_id | 40c56f51-8c44-4d82-8369-d065010ed91a | 40c56f51-8c44-4d82-8369-d065010ed91a | 40c56f51-8c44-4d82-8369-d065010ed91a |

# `ml2_port_bindings`  (rows=3730)

columns:
`port_id` varchar36 PK FK: uuid, unique identifier
`host` varchar255 NOTNULL: 121 distinct
`vif_type` varchar64 NOTNULL: "ovs"=3692, "unbound"=37, "binding_failed"=1
`vnic_type` varchar64 NOTNULL: "normal"=3730
`vif_details` varchar4095 NOTNULL: "{"port_filter": true, "ovs_hybrid_plug": true}"=3671, ""=59
`profile` varchar4095 NOTNULL: ""=3682, "{}"=48

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| port_id | ffe46d1d-3e9c-44f6-89c4-ad61eb5902d4 | 3d9d5c0c-c9de-460d-9975-f46bbbb3bf64 | b42baff3-dbb7-45e1-99f9-4db649c8f6e3 |
| host | forge-23 | forge-23 | gamut-16 |
| vif_type | ovs | ovs | ovs |
| vnic_type | normal | normal | normal |
| vif_details | {"port_filter": true, "ovs_hybrid_plug": true} | {"port_filter": true, "ovs_hybrid_plug": true} | {"port_filter": true, "ovs_hybrid_plug": true} |
| profile |  |  |  |

# `ml2_vlan_allocations`  (rows=9)

columns:
`physical_network` varchar64 PK
`vlan_id` int PK
`allocated` int NOTNULL

indexes: (`physical_network`,`allocated`)

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 |
|---|---|---|---|---|---|---|---|---|---|
| physical_network | trunk | trunk | trunk | trunk | trunk | trunk | trunk | trunk | trunk |
| vlan_id | 9 | 2001 | 2002 | 2052 | 2112 | 2113 | 2114 | 2123 | 3000 |
| allocated | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |

# `networkdhcpagentbindings`  (rows=45)

columns:
`network_id` varchar36 PK FK: uuid, unique identifier
`dhcp_agent_id` varchar36 PK FK: "d72830f5-a71c-418d-8d47-ff23ef398336"=45

indexes: `dhcp_agent_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| network_id | fe178706-9942-4600-9224-b2ae7c61db71 | b0c35168-dd4a-43db-9eaf-40f72529d8c8 | 4207d69c-903d-48d3-be48-debcb46b3241 |
| dhcp_agent_id | d72830f5-a71c-418d-8d47-ff23ef398336 | d72830f5-a71c-418d-8d47-ff23ef398336 | d72830f5-a71c-418d-8d47-ff23ef398336 |

# `networkrbacs`  (rows=14)

columns:
`id` varchar36 PK: uuid, unique identifier
`object_id` varchar36 NOTNULL FK: "4207d69c-903d-48d3-be48-debcb46b3241"=7, "8ad137b5-cc2b-44c7-9db0-e4f81d978d0c"=2, "c9e8f307-e1d5-4c06-b464-ef5370ca1d6d"=2, "0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d"=1, "b0c35168-dd4a-43db-9eaf-40f72529d8c8"=1, "b3d6c27a-a9bb-4521-b5de-4d65eb7490dc"=1
`tenant_id` varchar255: "6f9adccbd03e4d2186756896957a14bf"=8, "7691c9955ce1444ab366d041f5bdf33c"=4, "09ad05432f914e26bc417bf58f1cb4d2"=1, "98333a1a28e746fa8c629c83a818ad57"=1
`target_tenant` varchar255 NOTNULL: "*"=2, "08a5710919764215ad1b2c98dc7a8112"=1, "1ee6b5b4fe8c45cfa16c3ecdbb8ee02b"=1, "2160dff3f28c4a368d52fd373abdba78"=1, "41875d895b664602869cdab371081dc3"=1, "47c0857cf5b5452a86f640fd44be1d40"=1, "7f90e41e2e7a4f5f805e5c81f3994f6d"=1, "98333a1a28e746fa8c629c83a818ad57"=1, "a3ccd76b29264bbe94415833015c9379"=1, "bfd50153a2e9476f93e33e30e922cd06"=1, "c1cb7bcbcb6040c9837c35ff8501b13a"=1, "df4ca50218b54171a83464a67dd8ec78"=1, "e3fb2659584e436a832461dac02835f0"=1
`action` varchar255 NOTNULL: "access_as_shared"=13, "access_as_external"=1

indexes: `tenant_id`, `object_id`, UNIQUE (`action`,`object_id`,`target_tenant`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | f2980872-481b-497a-9281-784178e4e555 | 8d848179-cea2-4b3a-9790-78e23b276a4c | 57051f7f-91ae-4d62-b98e-08041ae25928 |
| object_id | c9e8f307-e1d5-4c06-b464-ef5370ca1d6d | 4207d69c-903d-48d3-be48-debcb46b3241 | 4207d69c-903d-48d3-be48-debcb46b3241 |
| tenant_id | 7691c9955ce1444ab366d041f5bdf33c | 6f9adccbd03e4d2186756896957a14bf | 6f9adccbd03e4d2186756896957a14bf |
| target_tenant | c1cb7bcbcb6040c9837c35ff8501b13a | bfd50153a2e9476f93e33e30e922cd06 | 41875d895b664602869cdab371081dc3 |
| action | access_as_shared | access_as_shared | access_as_shared |

# `networks`  (rows=49)

columns:
`tenant_id` varchar255: 25 distinct, "98333a1a28e746fa8c629c83a818ad57"=6, "09ad05432f914e26bc417bf58f1cb4d2"=5, "17ea94ad74b64b9d92f4888336a598c7"=3, "70b2507b8cc44fcb917ddfb85f5079d9"=3, "bfd50153a2e9476f93e33e30e922cd06"=3, "d5a33464413740e19dbe588144de18d0"=3, "db95ae8358bd4566ba2e38702a128b6b"=3, "fab98a79c65a47a99d23492c39315927"=3, "5f321cb6f5454443876cfbe22aa1d6d8"=2, "6f9adccbd03e4d2186756896957a14bf"=2
`id` varchar36 PK: uuid, unique identifier
`name` varchar255: 46 distinct
`status` varchar16: "ACTIVE"=49
`admin_state_up` int: 1=49
`mtu` int: 8958=15, 0=10, 1458=2, 1500=2, 9000=2, 9134=1, nulls=17, 0..9134
`vlan_transparent` int: all NULL
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 1280..64760
`availability_zone_hints` varchar255: "[]"=21, nulls=28

indexes: `tenant_id`, UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | 17ea94ad74b64b9d92f4888336a598c7 | 98333a1a28e746fa8c629c83a818ad57 | ef0ebc28b4e54d1b818821b2fd5e7511 |
| id | fe178706-9942-4600-9224-b2ae7c61db71 | 2fd4865f-ed87-4b56-a1a3-8a20f3275c0d | d1419216-65f6-4bba-bd77-f35850328822 |
| name | twist0-28 | gamma3_helix | plasm8-93 |
| status | ACTIVE | ACTIVE | ACTIVE |
| admin_state_up | 1 | 1 | 1 |
| mtu | null | 8958 | 0 |
| vlan_transparent | null | null | null |
| standard_attr_id | 1311 | 54183 | 1304 |
| availability_zone_hints | null | [] | null |

# `networksecuritybindings`  (rows=36)

columns:
`network_id` varchar36 PK FK: uuid, unique identifier
`port_security_enabled` int NOTNULL: 1=33, 0=3

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| network_id | fe178706-9942-4600-9224-b2ae7c61db71 | 5ec0b65f-6115-4525-8093-a8ce01707624 | c9e8f307-e1d5-4c06-b464-ef5370ca1d6d |
| port_security_enabled | 1 | 1 | 0 |

# `poolmonitorassociations`  (rows=1)

columns:
`pool_id` varchar36 PK FK
`monitor_id` varchar36 PK FK
`status` varchar16 NOTNULL
`status_description` varchar255

indexes: `monitor_id`

all rows:
| column | row 1 |
|---|---|
| pool_id | c7d33358-67e9-407f-91b4-241f2584e242 |
| monitor_id | a9ec94c3-756f-40ad-ac48-1570196fd8fc |
| status | ACTIVE |
| status_description | null |

# `pools`  (rows=2)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`vip_id` varchar36 FK
`name` varchar255
`description` varchar255
`subnet_id` varchar36 NOTNULL
`protocol` enum NOTNULL
`lb_method` enum NOTNULL
`status` varchar16 NOTNULL
`status_description` varchar255
`admin_state_up` int NOTNULL

indexes: `tenant_id`, `vip_id`

all rows:
| column | row 1 | row 2 |
|---|---|---|
| tenant_id | daa18fdafdf04b5eac18e04aa19ee214 | 0fe46c69adaf4d2fb01401e0dd952815 |
| id | 213fccb5-6482-4c4b-b66a-06a1eb283331 | c7d33358-67e9-407f-91b4-241f2584e242 |
| vip_id | null | fec601e1-596d-4bd6-9149-682470ece8c1 |
| name | starx | spind.layer |
| description |  | 761fc0b85fc55ec8c4a54ed0a5830623 |
| subnet_id | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 |
| protocol | HTTP | HTTPS |
| lb_method | ROUND_ROBIN | LEAST_CONNECTIONS |
| status | ACTIVE | ACTIVE |
| status_description | null | null |
| admin_state_up | 1 | 1 |

# `poolstatisticss`  (rows=2)

columns:
`pool_id` varchar36 PK FK
`bytes_in` bigint NOTNULL
`bytes_out` bigint NOTNULL
`active_connections` bigint NOTNULL
`total_connections` bigint NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| pool_id | 213fccb5-6482-4c4b-b66a-06a1eb283331 | c7d33358-67e9-407f-91b4-241f2584e242 |
| bytes_in | 0 | 0 |
| bytes_out | 0 | 0 |
| active_connections | 0 | 0 |
| total_connections | 0 | 0 |

# `ports`  (rows=3775)

columns:
`tenant_id` varchar255: 397 distinct, nulls=38, "17ea94ad74b64b9d92f4888336a598c7"=602, "9c982b4e161647ddb5f8637ac9eb551d"=560, "d3ac3958f14941cdb205e76ba43bbe49"=495, "98333a1a28e746fa8c629c83a818ad57"=274, "3008a142e9524f7295b06ea811908f93"=235, "70b2507b8cc44fcb917ddfb85f5079d9"=168, "e3fb2659584e436a832461dac02835f0"=64, "e7e8e8eca25741c8abc96fc07a103b94"=43, "c6d36b416dac49f193b4a209546ce370"=40, "fe451fd0d7224ccb85592a2bf8ebe366"=38
`id` varchar36 PK: uuid, unique identifier
`name` varchar255: "forge-netix7"=2, "astro-zeph4"=1, "blaze"=1, "blitz"=1, "celes-speed-grav"=1, "comet-drive9"=1, "flare"=1, "flare1-87"=1, "flick-quark-flash"=1, "glint"=1, "helio"=1, "layer"=1, "prime-helix-speed"=1, "qubit-spike8"=1, "shine-celes4"=1, "spind_sdjt-gwxw-iryg-laob-ihwd"=1, "twist-pico7"=1, "void-neon"=1, "vortx"=1, nulls=3755
`network_id` varchar36 NOTNULL FK: uuid, 46 distinct, "0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d"=3620, "8ad137b5-cc2b-44c7-9db0-e4f81d978d0c"=39, "b3d6c27a-a9bb-4521-b5de-4d65eb7490dc"=19, "4207d69c-903d-48d3-be48-debcb46b3241"=7, "18b03960-577f-49a4-be38-aafb4e05f3f3"=5, "259e350d-9ea5-4dc5-8a1c-4ab7deef9eec"=5, "c9e8f307-e1d5-4c06-b464-ef5370ca1d6d"=5, "38bfcc47-5f4d-46c8-9596-fb3a69f64e1e"=4, "5ec0b65f-6115-4525-8093-a8ce01707624"=4, "82caefaf-7420-4122-80c4-92e46e9fd658"=4
`mac_address` varchar32 NOTNULL: 3774 distinct
`admin_state_up` int NOTNULL: 1=3774, 0=1
`status` varchar16 NOTNULL: "DOWN"=2700, "ACTIVE"=1034, ""=23, "BUILD"=18
`device_id` varchar255 NOTNULL: 3483 distinct
`device_owner` varchar255 NOTNULL: "compute:nova"=2077, "compute:None"=1561, "network:dhcp"=58, "network:floatingip"=23, "network:router_interface"=22, "network:router_gateway"=15, ""=12, "neutron:LOADBALANCERV2"=6, "neutron:LOADBALANCER"=1
`dns_name` varchar255: all NULL
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 1..65876

indexes: (`network_id`,`device_owner`), (`network_id`,`mac_address`), `tenant_id`, `network_id`, UNIQUE (`network_id`,`mac_address`), UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | 17ea94ad74b64b9d92f4888336a598c7 | 190ad02e1faa494a8ab7153c6d2e56c1 | 17ea94ad74b64b9d92f4888336a598c7 |
| id | ffe46d1d-3e9c-44f6-89c4-ad61eb5902d4 | 97a87c72-9670-44f5-b273-b686009fdca4 | 740a66f7-985f-4abe-97ba-b2e140b7bc5f |
| name | null | null | null |
| network_id | 0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d | 0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d | 0a1d0a27-cffa-4de3-92c5-9d3fd3f2e74d |
| mac_address | fa:16:3e:87:d2:36 | fa:16:3e:d1:8d:59 | fa:16:3e:18:4f:0b |
| admin_state_up | 1 | 1 | 1 |
| status | DOWN | ACTIVE | ACTIVE |
| device_id | 429c0638-c9b8-465d-8516-6b5b26693f20 | cd2d1b2c-aca9-44a0-8b41-a737dad178c6 | daac82da-ed6b-432b-a062-201e7e9181bc |
| device_owner | compute:None | compute:nova | compute:None |
| dns_name | null | null | null |
| standard_attr_id | 52214 | 65408 | 56139 |

# `portsecuritybindings`  (rows=3194)

columns:
`port_id` varchar36 PK FK: uuid, unique identifier
`port_security_enabled` int NOTNULL: 1=3134, 0=60

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| port_id | ffe46d1d-3e9c-44f6-89c4-ad61eb5902d4 | a9584655-42e9-4be3-a9c7-70cbb15c3db5 | d5ca0d36-f2f1-459b-ae69-6779e3da5c63 |
| port_security_enabled | 1 | 1 | 1 |

# `providerresourceassociations`  (rows=38)

columns:
`provider_name` varchar255 PK: "haproxy"=38
`resource_id` varchar36 PK UNIQ: uuid, unique identifier

indexes: UNIQUE `resource_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| provider_name | haproxy | haproxy | haproxy |
| resource_id | f07300df-e29d-4f56-9315-d358fedcb2ff | 3995ac2a-8013-4bf3-8eb2-3fe47d824621 | 70c1dd6a-1752-42a8-b1a5-7d6db5e4c36d |

# `quotas`  (rows=1521)

columns:
`id` varchar36 PK: uuid, unique identifier
`tenant_id` varchar255: 218 distinct
`resource` varchar255: "network"=218, "subnet"=218, "router"=217, "floatingip"=216, "port"=216, "security_group"=216, "security_group_rule"=216, "pool"=2, "rbac_policy"=2
`limit` int: -1=711, 10=593, 0=213, 1=2, 3=1, 8=1, -1..10

indexes: `tenant_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | ffb411ff-27ba-4657-9604-f446f8a76619 | 9ad8fbee-c891-4ed6-b695-2f2cf0b4c57b | b9c382df-bb31-4a8d-8358-0a55830cc35a |
| tenant_id | 5ff7fc0747b44990a271062cbaba0581 | a632c7327bec4f86b7fa93b1c93f3dab | 66bb3791b211443c9bc39c0a392420bc |
| resource | security_group | security_group_rule | router |
| limit | -1 | -1 | 10 |

# `quotausages`  (rows=810)

columns:
`tenant_id` varchar255 PK: 438 distinct, "98333a1a28e746fa8c629c83a818ad57"=7, "bfd50153a2e9476f93e33e30e922cd06"=6, "09ad05432f914e26bc417bf58f1cb4d2"=5, "3a3dd8971d2e4f6abf826e5dd0362895"=5, "5b92ec1146d04f9091ab48b6cdba3eff"=5, "70b2507b8cc44fcb917ddfb85f5079d9"=5, "7ab3a43d5b86462996112bb62bab39cd"=5, "a51d86f76bc640c2b9c892c63bff688b"=5, "e3fb2659584e436a832461dac02835f0"=5, "e8fa7c20e65e4b38b51d43f97ea35f6d"=5
`resource` varchar255 PK: "port"=428, "security_group"=318, "network"=22, "subnet"=18, "router"=17, "floatingip"=4, "security_group_rule"=3
`dirty` int NOTNULL: 0=658, 1=152
`in_use` int NOTNULL: 45 distinct, 0..602, avg=6.8099, median=2
`reserved` int NOTNULL: 0=810

indexes: `resource`, `tenant_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | ffa0e5fc492e4b4290bb9e2757850411 | f0ae1d7c6f7b4417b2c9c4c82933ebd5 | cdb8fd3639134748aaa55cad3c4a1366 |
| resource | security_group | port | security_group |
| dirty | 0 | 0 | 0 |
| in_use | 2 | 2 | 6 |
| reserved | 0 | 0 | 0 |

# `reservations`  (rows=5)

columns:
`id` varchar36 PK
`tenant_id` varchar255
`expiration` datetime

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| id | 1c8ca579-e3d4-48a0-8f16-7e4f85533bd4 | 21366ef0-6ebc-42da-8f2b-32589ad30797 | 3b2052b2-fbc1-426c-8143-a0927c85ce96 | 60fa92eb-f589-4c93-b6b0-1a3384683bb8 | d8434831-9abb-4971-afd4-62c969aff654 |
| tenant_id | d3ac3958f14941cdb205e76ba43bbe49 | d3ac3958f14941cdb205e76ba43bbe49 | d3ac3958f14941cdb205e76ba43bbe49 | d3ac3958f14941cdb205e76ba43bbe49 | d3ac3958f14941cdb205e76ba43bbe49 |
| expiration | 2019-04-08T20:00:39 | 2019-04-08T20:00:13 | 2019-04-08T20:00:38 | 2019-04-03T15:16:01 | 2019-04-08T20:01:00 |

# `resourcedeltas`  (rows=5)

columns:
`resource` varchar255 PK
`reservation_id` varchar36 PK FK
`amount` int

indexes: `reservation_id`

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 |
|---|---|---|---|---|---|
| resource | port | port | port | port | port |
| reservation_id | 1c8ca579-e3d4-48a0-8f16-7e4f85533bd4 | 21366ef0-6ebc-42da-8f2b-32589ad30797 | 3b2052b2-fbc1-426c-8143-a0927c85ce96 | 60fa92eb-f589-4c93-b6b0-1a3384683bb8 | d8434831-9abb-4971-afd4-62c969aff654 |
| amount | 1 | 1 | 1 | 1 | 1 |

# `router_extra_attributes`  (rows=27)

columns:
`router_id` varchar36 PK FK: uuid, unique identifier
`distributed` int NOTNULL: 0=27
`service_router` int NOTNULL: 0=27
`ha` int NOTNULL: 0=27
`ha_vr_id` int: 0=22, nulls=5
`availability_zone_hints` varchar255: "[]"=16, nulls=11

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| router_id | fa95b6df-6eef-49a9-a7df-753eeb99c527 | 71e9342c-dd51-4f9d-843d-892285bff645 | 30029469-c5b0-49f3-9f7e-a74a592b7d82 |
| distributed | 0 | 0 | 0 |
| service_router | 0 | 0 | 0 |
| ha | 0 | 0 | 0 |
| ha_vr_id | 0 | 0 | 0 |
| availability_zone_hints | [] | [] | [] |

# `routerl3agentbindings`  (rows=27)

columns:
`router_id` varchar36 PK FK: uuid, unique identifier
`l3_agent_id` varchar36 PK FK: "f650dff7-3bb0-44a7-8626-069e2b346dcf"=27

indexes: `l3_agent_id`, `router_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| router_id | fa95b6df-6eef-49a9-a7df-753eeb99c527 | e0082509-7e89-4959-bf0c-b8c8b2acf639 | a154bb98-4a0d-4a6c-bcfa-e1afb65ce71e |
| l3_agent_id | f650dff7-3bb0-44a7-8626-069e2b346dcf | f650dff7-3bb0-44a7-8626-069e2b346dcf | f650dff7-3bb0-44a7-8626-069e2b346dcf |

# `routerports`  (rows=35)

columns:
`router_id` varchar36 PK FK: uuid, 22 distinct
`port_id` varchar36 PK FK: uuid, unique identifier
`port_type` varchar255: "network:router_interface"=20, "network:router_gateway"=15

indexes: `port_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| router_id | fa95b6df-6eef-49a9-a7df-753eeb99c527 | 76f35845-0279-4b3f-93a7-f9ef40922a1a | e10a8573-7b74-4a21-b9ce-eaf66bf58279 |
| port_id | 4eba9d6b-dea1-45ac-83b4-4857ff3dabf0 | 45ef9b25-dd08-47b3-a8ef-dd895e7527d4 | 65daa76d-d899-4518-8ed0-7d1bcd4c243c |
| port_type | network:router_interface | network:router_gateway | network:router_gateway |

# `routers`  (rows=27)

columns:
`tenant_id` varchar255: 21 distinct, "bfd50153a2e9476f93e33e30e922cd06"=3, "09ad05432f914e26bc417bf58f1cb4d2"=2, "98333a1a28e746fa8c629c83a818ad57"=2, "db95ae8358bd4566ba2e38702a128b6b"=2, "fab98a79c65a47a99d23492c39315927"=2, "17ea94ad74b64b9d92f4888336a598c7"=1, "3a3dd8971d2e4f6abf826e5dd0362895"=1, "5fea2ac1593844778bd57448717fe6fb"=1, "6707cc1c25b14cb6a625ea1d5c06946d"=1, "6790bdc54ef84195b4d1e7df6642d968"=1
`id` varchar36 PK: uuid, unique identifier
`name` varchar255: 25 distinct
`status` varchar16: "ACTIVE"=27
`admin_state_up` int: 1=27
`gw_port_id` varchar36 FK: "16c68923-8a8d-483e-96d0-dd441cab2747"=1, "2d54aa04-9d8d-4d3f-b3b4-4906aff79e96"=1, "45ef9b25-dd08-47b3-a8ef-dd895e7527d4"=1, "4872b855-26cd-4083-aa98-9b339b664970"=1, "49acce02-7758-4227-add2-6245101d65f0"=1, "5782bc41-a46e-4b17-a98f-a41d54935c6a"=1, "58432caa-fadd-4a5c-b340-e6a96b0038d6"=1, "59f08aea-2668-4294-b5b5-b032b220d003"=1, "5f7528dd-9436-4741-879a-5eb8ddf11a1e"=1, "65daa76d-d899-4518-8ed0-7d1bcd4c243c"=1, "7d292552-5b81-4545-99c9-650dcd4c0185"=1, "92dcf251-a673-422d-a30c-94bbbf833fd9"=1, "a5007dd1-9c54-46db-9a7c-a94449afed73"=1, "a5c5b832-e240-4a8c-9626-39ff38106018"=1, "d48341b3-5463-47fe-8145-18077a99c106"=1, nulls=12
`enable_snat` int NOTNULL: 1=27
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 2039..58641

indexes: `gw_port_id`, `tenant_id`, UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | bfd50153a2e9476f93e33e30e922cd06 | 98333a1a28e746fa8c629c83a818ad57 | 09ad05432f914e26bc417bf58f1cb4d2 |
| id | fa95b6df-6eef-49a9-a7df-753eeb99c527 | 9ff894ce-d884-46fd-9c47-c5fb7d6fb933 | 611b1438-7ede-437c-864d-e25bd30c03d4 |
| name | blitz | blitz | shine_flare |
| status | ACTIVE | ACTIVE | ACTIVE |
| admin_state_up | 1 | 1 | 1 |
| gw_port_id | 4872b855-26cd-4083-aa98-9b339b664970 | 7d292552-5b81-4545-99c9-650dcd4c0185 | 49acce02-7758-4227-add2-6245101d65f0 |
| enable_snat | 1 | 1 | 1 |
| standard_attr_id | 20998 | 21147 | 2041 |

# `securitygroupportbindings`  (rows=5921)

columns:
`port_id` varchar36 PK FK: uuid, 3654 distinct, "3d0d3872-f929-46ba-8adc-4fb128b557c6"=11, "25d421c1-c76d-4c26-9550-9f871a1d5034"=10, "d1c34ee8-d108-4e9e-940b-9d6530c9fec9"=10, "05480d0b-f6fe-4171-a418-58388d370045"=8, "44283b5e-1502-436a-be73-caf0d33ab36d"=8, "a6658428-5738-4d52-bf4b-3382697c0edd"=8, "c085d5ea-ad87-42d2-b7d3-689267243729"=8, "1264bcd0-981d-4c2e-882c-998ca2f61d68"=7, "13dd8945-535e-4b80-b1d5-89d19a8570a0"=7, "15b90be2-3cdc-47bf-9054-69a2d6024f35"=7
`security_group_id` varchar36 PK FK: uuid, 840 distinct, "afedef23-0032-445e-a773-e8d9ff32837f"=560, "d60ff86d-c3cf-485f-9149-0c5bec782af0"=495, "e89ea050-10bc-42e7-99a8-18b97cec2446"=356, "75770b75-1bff-4151-b97b-09754c85c63c"=345, "786ce6d8-44cb-40bc-98dd-96390b5de944"=345, "40ec5af9-3ba9-4d8c-a86c-27b90285b8e7"=230, "e5209cd6-b881-4633-b955-fdde1fefea58"=191, "ffd446f0-9e47-4200-be9f-9ebd690f67e6"=135, "3b1bc632-31c9-4331-b8e8-d9f7ea25e8f1"=120, "b78e6628-1f23-4a36-b9e6-ae0ddf2ac7dd"=113

indexes: `security_group_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| port_id | ffe46d1d-3e9c-44f6-89c4-ad61eb5902d4 | 13dd8945-535e-4b80-b1d5-89d19a8570a0 | 6e53dda9-1b3f-4014-9ae1-06a344e7181b |
| security_group_id | e89ea050-10bc-42e7-99a8-18b97cec2446 | e5209cd6-b881-4633-b955-fdde1fefea58 | d60ff86d-c3cf-485f-9149-0c5bec782af0 |

# `securitygrouprules`  (rows=9004)

columns:
`tenant_id` varchar255: 804 distinct, "98333a1a28e746fa8c629c83a818ad57"=405, "f0ae1d7c6f7b4417b2c9c4c82933ebd5"=360, "70b2507b8cc44fcb917ddfb85f5079d9"=200, "a3ccd76b29264bbe94415833015c9379"=187, "09ad05432f914e26bc417bf58f1cb4d2"=159, "47c0857cf5b5452a86f640fd44be1d40"=147, "e3fb2659584e436a832461dac02835f0"=145, "bfd50153a2e9476f93e33e30e922cd06"=112, "7705adbe5221408f845e3bb10b6de471"=107, "3008a142e9524f7295b06ea811908f93"=101
`id` varchar36 PK: uuid, unique identifier
`security_group_id` varchar36 NOTNULL FK: uuid, 1796 distinct, "0adc1d0c-c6ef-4695-be3b-82d04a227c59"=356, "3050a996-b1bf-4e86-bffd-795ca722575f"=122, "5b768ff6-6c4e-4c24-b5d2-1ec67832d5e4"=41, "1aeff992-dc10-4602-b24a-c1aeb0e889d4"=38, "2007a9a5-de89-4567-acf4-1fdc7879f120"=26, "e16f001d-ac14-49da-bea7-8126d9bc8484"=22, "123928be-24ec-473d-954d-e4c11712c37b"=21, "7c315ca1-f09a-4594-97a8-2d258f4dc4f8"=21, "8add0fa9-1335-414e-863f-9a5582af64aa"=21, "bfab842b-9377-44f4-9583-1250bc01e4be"=21
`remote_group_id` varchar36 FK: uuid, 853 distinct, nulls=7266, "c1e223f1-686e-4254-8f2d-700ae549c116"=7, "43088402-0954-4821-9db1-e7d29315a9f3"=6, "972612ec-9f7c-4590-ad77-8afda06c9d74"=6, "a725d978-f5d6-439d-963e-e23636cc88e1"=6, "c9a2e0de-0090-4229-8149-6b2a31c3ba8a"=6, "f588ab9e-cd4e-4c35-94dc-343001d8ecea"=6, "5b0c839c-7ed6-4648-abdb-876982205622"=5, "5b768ff6-6c4e-4c24-b5d2-1ec67832d5e4"=5, "d608fb65-0ade-406e-94db-41b73d832ec7"=5, "04f8626a-1d3c-4d93-8c25-fbd5c47ab4cf"=4
`direction` enum: "ingress"=5195, "egress"=3809
`ethertype` varchar40: "IPv4"=6349, "IPv6"=2655
`protocol` varchar40: "tcp"=3374, "udp"=330, "icmp"=283, "41"=1, "47"=1, nulls=5015
`port_range_min` int: 325 distinct, nulls=5290, 0..65535, avg=3642.9235, median=80
`port_range_max` int: 340 distinct, nulls=5290, 0..65535, avg=11844.6799, median=443
`remote_ip_prefix` varchar255: 739 distinct, nulls=5149
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 2051..65874

indexes: `tenant_id`, `remote_group_id`, `security_group_id`, UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | 1140b46602e84c47838f707b060d6fd2 | e6ef0f87a97247bda8cd853a782a60ff | 3cfac786b36a4bb18f523f6be739ae71 |
| id | ffff1ce1-7487-4ab7-8df4-720e79740710 | 0daa9546-cea5-44d5-bac6-e5f58b4ed017 | bf77a1d4-b46f-4c9a-8135-c52c0175ca56 |
| security_group_id | 450d2918-0e07-4111-a8af-948eedb8e1ce | 15eaf535-ce57-481f-bec6-7181ee0b00da | 7a1c9cc4-d27c-408a-8aa8-cac94978150b |
| remote_group_id | 450d2918-0e07-4111-a8af-948eedb8e1ce | null | 7a1c9cc4-d27c-408a-8aa8-cac94978150b |
| direction | ingress | egress | ingress |
| ethertype | IPv6 | IPv4 | IPv4 |
| protocol | null | null | null |
| port_range_min | null | null | null |
| port_range_max | null | null | null |
| remote_ip_prefix | null | null | null |
| standard_attr_id | 5383 | 2219 | 9361 |

# `securitygroups`  (rows=1798)

columns:
`tenant_id` varchar255: 804 distinct, "98333a1a28e746fa8c629c83a818ad57"=83, "70b2507b8cc44fcb917ddfb85f5079d9"=47, "09ad05432f914e26bc417bf58f1cb4d2"=35, "e3fb2659584e436a832461dac02835f0"=31, "3008a142e9524f7295b06ea811908f93"=29, "bfd50153a2e9476f93e33e30e922cd06"=27, "47c0857cf5b5452a86f640fd44be1d40"=24, "3a3dd8971d2e4f6abf826e5dd0362895"=16, "a3ccd76b29264bbe94415833015c9379"=16, "b7188a889c6a4800893445d969673bab"=15
`id` varchar36 PK: uuid, unique identifier
`name` varchar255: 640 distinct
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 1342..65867

indexes: `tenant_id`, UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | 734423d02a724aca891507bb4d858975 | 85b928765b6e4d07acf811833a763de4 | 9640284013ec4518812fd016846f8da9 |
| id | fff3003f-b772-4c44-ba63-8c55367dffa0 | 2dc0f7c6-9753-4df3-8242-aa6b4cdd32d5 | daaca2c2-4516-4aae-be1b-0e10ba995051 |
| name | aurum-xenon | qubit_shine_track | aurum-xenon |
| standard_attr_id | 2036 | 1468 | 1933 |

# `sessionpersistences`  (rows=1)

columns:
`vip_id` varchar36 PK FK
`type` enum NOTNULL
`cookie_name` varchar1024

indexes: none

all rows:
| column | row 1 |
|---|---|
| vip_id | fec601e1-596d-4bd6-9149-682470ece8c1 |
| type | HTTP_COOKIE |
| cookie_name | null |

# `standardattributes`  (rows=14725)

columns:
`id` bigint PK: unique identifier, 1..65876
`resource_type` varchar255 NOTNULL: "securitygrouprules"=9004, "ports"=3775, "securitygroups"=1798, "networks"=49, "subnets"=49, "routers"=27, "floatingips"=23
`created_at` datetime: 6788 distinct, nulls=4266
`updated_at` datetime: 6569 distinct, nulls=3971
`description` varchar255: 514 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 65876 | 10683 | 11001 |
| resource_type | ports | ports | ports |
| created_at | 2024-06-26T20:39:07 | 2017-02-04T18:51:46 | 2017-02-04T21:49:25 |
| updated_at | 2024-06-26T20:40:23 | 2024-02-02T20:55:19 | 2017-02-04T21:49:26 |
| description |  |  |  |

# `subnetroutes`  (rows=6)

columns:
`destination` varchar64 PK
`nexthop` varchar64 PK
`subnet_id` varchar36 PK FK

indexes: `subnet_id`

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| destination | 10.100.51.19/8 | 10.169.77.216/8 | 10.169.77.216/8 | 10.71.29.205/8 | 10.96.5.18/8 | 10.96.5.18/8 |
| nexthop | 10.30.19.197/8 | 10.232.49.230/8 | 10.75.231.144/8 | 10.30.19.197/8 | 10.33.34.94/8 | 10.72.174.11/8 |
| subnet_id | 012993ae-5d73-4aad-834b-e87a31e99d48 | 76123b94-2ae9-40c4-a4c6-03ee98d081d9 | 9ce2600b-6566-4c81-9370-9b758d5f7ccc | 012993ae-5d73-4aad-834b-e87a31e99d48 | e8da8ec5-364b-4a31-afaf-f68a206b7846 | faee7948-a17f-4e58-a557-7ea1219c3b5f |

# `subnets`  (rows=49)

columns:
`tenant_id` varchar255: 23 distinct, "98333a1a28e746fa8c629c83a818ad57"=7, "09ad05432f914e26bc417bf58f1cb4d2"=5, "fab98a79c65a47a99d23492c39315927"=4, "17ea94ad74b64b9d92f4888336a598c7"=3, "70b2507b8cc44fcb917ddfb85f5079d9"=3, "bfd50153a2e9476f93e33e30e922cd06"=3, "d5a33464413740e19dbe588144de18d0"=3, "5f321cb6f5454443876cfbe22aa1d6d8"=2, "6f9adccbd03e4d2186756896957a14bf"=2, "939a950b58f140b695f0da6c200e805c"=2
`id` varchar36 PK: uuid, unique identifier
`name` varchar255: 45 distinct
`network_id` varchar36 FK: uuid, 46 distinct
`ip_version` int NOTNULL: 4=47, 6=2
`cidr` varchar64 NOTNULL: 40 distinct
`gateway_ip` varchar64: 34 distinct, nulls=9
`enable_dhcp` int: 1=45, 0=4
`ipv6_ra_mode` enum: "dhcpv6-stateful"=2, nulls=47
`ipv6_address_mode` enum: "dhcpv6-stateful"=2, nulls=47
`subnetpool_id` varchar36: all NULL
`standard_attr_id` bigint UNIQ NOTNULL FK: unique identifier, 1312..59606

indexes: `subnetpool_id`, `tenant_id`, `network_id`, UNIQUE `standard_attr_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| tenant_id | daa18fdafdf04b5eac18e04aa19ee214 | d5a33464413740e19dbe588144de18d0 | 70b2507b8cc44fcb917ddfb85f5079d9 |
| id | faee7948-a17f-4e58-a557-7ea1219c3b5f | 890e8f54-c93f-4f2c-9e63-5a1b3d70d9d6 | 16eaae8c-1920-4b8b-8765-f149dde8a1a6 |
| name | axiom8 | galax-phase | dash_spark |
| network_id | 84ba89ec-68fd-4257-80eb-a1c3a65ee594 | 99d2d7a0-3a92-4f0d-8e2f-917201477f8b | c9e8f307-e1d5-4c06-b464-ef5370ca1d6d |
| ip_version | 4 | 4 | 4 |
| cidr | 10.44.3.58/8 | 10.82.4.115/8 | 10.49.195.222/8 |
| gateway_ip | 10.196.213.153/8 | 10.77.211.184/8 | 10.107.243.218/8 |
| enable_dhcp | 1 | 1 | 0 |
| ipv6_ra_mode | null | null | null |
| ipv6_address_mode | null | null | null |
| subnetpool_id | null | null | null |
| standard_attr_id | 1341 | 1329 | 16172 |

# `vips`  (rows=1)

columns:
`tenant_id` varchar255
`id` varchar36 PK
`name` varchar255
`description` varchar255
`port_id` varchar36 FK
`protocol_port` int NOTNULL
`protocol` enum NOTNULL
`pool_id` varchar36 UNIQ NOTNULL
`status` varchar16 NOTNULL
`status_description` varchar255
`admin_state_up` int NOTNULL
`connection_limit` int

indexes: `tenant_id`, UNIQUE `pool_id`, `port_id`

all rows:
| column | row 1 |
|---|---|
| tenant_id | 0fe46c69adaf4d2fb01401e0dd952815 |
| id | fec601e1-596d-4bd6-9149-682470ece8c1 |
| name | spind.layer |
| description | null |
| port_id | 81d292f6-881e-421f-93a3-e841a271e6e3 |
| protocol_port | 443 |
| protocol | HTTPS |
| pool_id | c7d33358-67e9-407f-91b4-241f2584e242 |
| status | ACTIVE |
| status_description | null |
| admin_state_up | 1 |
| connection_limit | -1 |

- Skipped 123 empty table(s): `address_scopes`, `arista_provisioned_nets`, `arista_provisioned_tenants`, `arista_provisioned_vms`, `auto_allocated_topologies`, `bgp_peers`, `bgp_speaker_dragent_bindings`, `bgp_speaker_network_bindings`, `bgp_speaker_peer_bindings`, `bgp_speakers`, `brocadenetworks`, `brocadeports`, `cisco_csr_identifier_map`, `cisco_firewall_associations`, `cisco_hosting_devices`, `cisco_ml2_apic_contracts`, `cisco_ml2_apic_host_links`, `cisco_ml2_apic_names`, `cisco_ml2_n1kv_network_bindings`, `cisco_ml2_n1kv_network_profiles`, `cisco_ml2_n1kv_policy_profiles`, `cisco_ml2_n1kv_port_bindings`, `cisco_ml2_n1kv_profile_bindings`, `cisco_ml2_n1kv_vlan_allocations`, `cisco_ml2_n1kv_vxlan_allocations`, `cisco_ml2_nexus_nve`, `cisco_ml2_nexusport_bindings`, `cisco_port_mappings`, `cisco_router_mappings`, `consistencyhashes`, `dvr_host_macs`, `extradhcpopts`, `firewall_policies`, `firewall_router_associations`, `firewall_rules`, `firewalls`, `flavors`, `flavorserviceprofilebindings`, `floatingipdnses`, `ha_router_agent_port_bindings`, `ha_router_networks`, `ha_router_vrid_allocations`, `ikepolicies`, `ipamallocationpools`, `ipamallocations`, `ipamavailabilityranges`, `ipamsubnets`, `ipsec_site_connections`, `ipsecpeercidrs`, `ipsecpolicies`, `lbaas_healthmonitors`, `lbaas_l7policies`, `lbaas_l7rules`, `lbaas_sessionpersistences`, `lbaas_sni`, `lsn`, `lsn_port`, `maclearningstates`, `meteringlabelrules`, `meteringlabels`, `ml2_brocadenetworks`, `ml2_brocadeports`, `ml2_dvr_port_bindings`, `ml2_flat_allocations`, `ml2_geneve_allocations`, `ml2_geneve_endpoints`, `ml2_nexus_vxlan_allocations`, `ml2_nexus_vxlan_mcast_groups`, `ml2_ucsm_port_profiles`, `ml2_vxlan_allocations`, `ml2_vxlan_endpoints`, `multi_provider_networks`, `networkconnections`, `networkdnsdomains`, `networkgatewaydevicereferences`, `networkgatewaydevices`, `networkgateways`, `networkqueuemappings`, `neutron_nsx_network_mappings`, `neutron_nsx_port_mappings`, `neutron_nsx_router_mappings`, `neutron_nsx_security_group_mappings`, `nexthops`, `nsxv_edge_dhcp_static_bindings`, `nsxv_edge_monitor_mappings`, `nsxv_edge_pool_mappings`, `nsxv_edge_vip_mappings`, `nsxv_edge_vnic_bindings`, `nsxv_firewall_rule_bindings`, `nsxv_internal_edges`, `nsxv_internal_networks`, `nsxv_port_index_mappings`, `nsxv_port_vnic_mappings`, `nsxv_router_bindings`, `nsxv_router_ext_attributes`, `nsxv_rule_mappings`, `nsxv_security_group_section_mappings`, `nsxv_spoofguard_policy_network_mappings`, `nsxv_tz_network_bindings`, `nsxv_vdr_dhcp_bindings`, `nuage_net_partition_router_mapping`, `nuage_net_partitions`, `nuage_provider_net_bindings`, `nuage_subnet_l2dom_mapping`, `poolloadbalanceragentbindings`, `portbindingports`, `portdnses`, `portqueuemappings`, `qos_bandwidth_limit_rules`, `qos_network_policy_bindings`, `qos_policies`, `qos_port_policy_bindings`, `qospolicyrbacs`, `qosqueues`, `routerroutes`, `routerrules`, `serviceprofiles`, `subnetpoolprefixes`, `subnetpools`, `tags`, `tz_network_bindings`, `vcns_router_bindings`, `vpnservices`
