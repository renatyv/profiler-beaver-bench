# Schema Links

- version: 0.0.5
- dialect: mysql
- database: neutron
- schema: neutron

## Declared PK/FK Links

allowedaddresspairs.port_id -> ports.id
auto_allocated_topologies.network_id -> networks.id
auto_allocated_topologies.router_id -> routers.id
bgp_speaker_dragent_bindings.agent_id -> agents.id
bgp_speaker_dragent_bindings.bgp_speaker_id -> bgp_speakers.id
bgp_speaker_network_bindings.bgp_speaker_id -> bgp_speakers.id
bgp_speaker_network_bindings.network_id -> networks.id
bgp_speaker_peer_bindings.bgp_peer_id -> bgp_peers.id
bgp_speaker_peer_bindings.bgp_speaker_id -> bgp_speakers.id
brocadeports.network_id -> brocadenetworks.id
cisco_csr_identifier_map.ipsec_site_conn_id -> ipsec_site_connections.id
cisco_firewall_associations.fw_id -> firewalls.id
cisco_firewall_associations.port_id -> ports.id
cisco_hosting_devices.cfg_agent_id -> agents.id
cisco_hosting_devices.management_port_id -> ports.id
cisco_ml2_apic_contracts.router_id -> routers.id
cisco_ml2_n1kv_network_bindings.network_id -> networks.id
cisco_ml2_n1kv_network_bindings.profile_id -> cisco_ml2_n1kv_network_profiles.id
cisco_ml2_n1kv_port_bindings.port_id -> ports.id
cisco_ml2_n1kv_vlan_allocations.network_profile_id -> cisco_ml2_n1kv_network_profiles.id
cisco_ml2_n1kv_vxlan_allocations.network_profile_id -> cisco_ml2_n1kv_network_profiles.id
cisco_port_mappings.hosting_port_id -> ports.id
cisco_port_mappings.logical_port_id -> ports.id
cisco_router_mappings.hosting_device_id -> cisco_hosting_devices.id
cisco_router_mappings.router_id -> routers.id
default_security_group.security_group_id -> securitygroups.id
dnsnameservers.subnet_id -> subnets.id
externalnetworks.network_id -> networks.id
extradhcpopts.port_id -> ports.id
firewall_router_associations.fw_id -> firewalls.id
firewall_router_associations.router_id -> routers.id
firewall_rules.firewall_policy_id -> firewall_policies.id
firewalls.firewall_policy_id -> firewall_policies.id
flavorserviceprofilebindings.flavor_id -> flavors.id
flavorserviceprofilebindings.service_profile_id -> serviceprofiles.id
floatingipdnses.floatingip_id -> floatingips.id
floatingips.fixed_port_id -> ports.id
floatingips.floating_port_id -> ports.id
floatingips.router_id -> routers.id
floatingips.standard_attr_id -> standardattributes.id
ha_router_agent_port_bindings.l3_agent_id -> agents.id
ha_router_agent_port_bindings.port_id -> ports.id
ha_router_agent_port_bindings.router_id -> routers.id
ha_router_networks.network_id -> networks.id
ha_router_vrid_allocations.network_id -> networks.id
ipallocationpools.subnet_id -> subnets.id
ipallocations.network_id -> networks.id
ipallocations.port_id -> ports.id
ipallocations.subnet_id -> subnets.id
ipamallocationpools.ipam_subnet_id -> ipamsubnets.id
ipamallocations.ipam_subnet_id -> ipamsubnets.id
ipamavailabilityranges.allocation_pool_id -> ipamallocationpools.id
ipavailabilityranges.allocation_pool_id -> ipallocationpools.id
ipsec_site_connections.ikepolicy_id -> ikepolicies.id
ipsec_site_connections.ipsecpolicy_id -> ipsecpolicies.id
ipsec_site_connections.vpnservice_id -> vpnservices.id
ipsecpeercidrs.ipsec_site_connection_id -> ipsec_site_connections.id
lbaas_l7policies.listener_id -> lbaas_listeners.id
lbaas_l7policies.redirect_pool_id -> lbaas_pools.id
lbaas_l7rules.l7policy_id -> lbaas_l7policies.id
lbaas_listeners.default_pool_id -> lbaas_pools.id
lbaas_listeners.loadbalancer_id -> lbaas_loadbalancers.id
lbaas_loadbalancer_statistics.loadbalancer_id -> lbaas_loadbalancers.id
lbaas_loadbalanceragentbindings.agent_id -> agents.id
lbaas_loadbalanceragentbindings.loadbalancer_id -> lbaas_loadbalancers.id
lbaas_loadbalancers.flavor_id -> flavors.id
lbaas_loadbalancers.vip_port_id -> ports.id
lbaas_members.pool_id -> lbaas_pools.id
lbaas_pools.healthmonitor_id -> lbaas_healthmonitors.id
lbaas_pools.loadbalancer_id -> lbaas_loadbalancers.id
lbaas_sessionpersistences.pool_id -> lbaas_pools.id
lbaas_sni.listener_id -> lbaas_listeners.id
lsn_port.lsn_id -> lsn.lsn_id
maclearningstates.port_id -> ports.id
members.pool_id -> pools.id
meteringlabelrules.metering_label_id -> meteringlabels.id
ml2_brocadeports.network_id -> ml2_brocadenetworks.id
ml2_dvr_port_bindings.port_id -> ports.id
ml2_network_segments.network_id -> networks.id
ml2_nexus_vxlan_mcast_groups.associated_vni -> ml2_nexus_vxlan_allocations.vxlan_vni
ml2_port_binding_levels.port_id -> ports.id
ml2_port_binding_levels.segment_id -> ml2_network_segments.id
ml2_port_bindings.port_id -> ports.id
multi_provider_networks.network_id -> networks.id
networkconnections.network_gateway_id -> networkgateways.id
networkconnections.network_id -> networks.id
networkconnections.port_id -> ports.id
networkdhcpagentbindings.dhcp_agent_id -> agents.id
networkdhcpagentbindings.network_id -> networks.id
networkdnsdomains.network_id -> networks.id
networkgatewaydevicereferences.network_gateway_id -> networkgateways.id
networkqueuemappings.network_id -> networks.id
networkqueuemappings.queue_id -> qosqueues.id
networkrbacs.object_id -> networks.id
networks.standard_attr_id -> standardattributes.id
networksecuritybindings.network_id -> networks.id
neutron_nsx_network_mappings.neutron_id -> networks.id
neutron_nsx_port_mappings.neutron_id -> ports.id
neutron_nsx_router_mappings.neutron_id -> routers.id
neutron_nsx_security_group_mappings.neutron_id -> securitygroups.id
nexthops.rule_id -> routerrules.id
nsxv_edge_monitor_mappings.monitor_id -> healthmonitors.id
nsxv_edge_pool_mappings.pool_id -> pools.id
nsxv_edge_vip_mappings.pool_id -> pools.id
nsxv_internal_networks.network_id -> networks.id
nsxv_port_index_mappings.port_id -> ports.id
nsxv_port_vnic_mappings.neutron_id -> ports.id
nsxv_router_ext_attributes.router_id -> routers.id
nsxv_rule_mappings.neutron_id -> securitygrouprules.id
nsxv_security_group_section_mappings.neutron_id -> securitygroups.id
nsxv_spoofguard_policy_network_mappings.network_id -> networks.id
nsxv_tz_network_bindings.network_id -> networks.id
nuage_net_partition_router_mapping.net_partition_id -> nuage_net_partitions.id
nuage_net_partition_router_mapping.router_id -> routers.id
nuage_provider_net_bindings.network_id -> networks.id
nuage_subnet_l2dom_mapping.net_partition_id -> nuage_net_partitions.id
nuage_subnet_l2dom_mapping.subnet_id -> subnets.id
poolloadbalanceragentbindings.agent_id -> agents.id
poolloadbalanceragentbindings.pool_id -> pools.id
poolmonitorassociations.monitor_id -> healthmonitors.id
poolmonitorassociations.pool_id -> pools.id
pools.vip_id -> vips.id
poolstatisticss.pool_id -> pools.id
portbindingports.port_id -> ports.id
portdnses.port_id -> ports.id
portqueuemappings.port_id -> ports.id
portqueuemappings.queue_id -> qosqueues.id
ports.network_id -> networks.id
ports.standard_attr_id -> standardattributes.id
portsecuritybindings.port_id -> ports.id
qos_bandwidth_limit_rules.qos_policy_id -> qos_policies.id
qos_network_policy_bindings.network_id -> networks.id
qos_network_policy_bindings.policy_id -> qos_policies.id
qos_port_policy_bindings.policy_id -> qos_policies.id
qos_port_policy_bindings.port_id -> ports.id
qospolicyrbacs.object_id -> qos_policies.id
resourcedeltas.reservation_id -> reservations.id
router_extra_attributes.router_id -> routers.id
routerl3agentbindings.l3_agent_id -> agents.id
routerl3agentbindings.router_id -> routers.id
routerports.port_id -> ports.id
routerports.router_id -> routers.id
routerroutes.router_id -> routers.id
routerrules.router_id -> routers.id
routers.gw_port_id -> ports.id
routers.standard_attr_id -> standardattributes.id
securitygroupportbindings.port_id -> ports.id
securitygroupportbindings.security_group_id -> securitygroups.id
securitygrouprules.remote_group_id -> securitygroups.id
securitygrouprules.security_group_id -> securitygroups.id
securitygrouprules.standard_attr_id -> standardattributes.id
securitygroups.standard_attr_id -> standardattributes.id
sessionpersistences.vip_id -> vips.id
subnetpoolprefixes.subnetpool_id -> subnetpools.id
subnetpools.standard_attr_id -> standardattributes.id
subnetroutes.subnet_id -> subnets.id
subnets.network_id -> networks.id
subnets.standard_attr_id -> standardattributes.id
tags.standard_attr_id -> standardattributes.id
tz_network_bindings.network_id -> networks.id
vips.port_id -> ports.id
vpnservices.router_id -> routers.id
vpnservices.subnet_id -> subnets.id

## Inferred Links

### tenant
- inferred: default_security_group.tenant_id, floatingips.tenant_id, healthmonitors.tenant_id, lbaas_listeners.tenant_id, lbaas_loadbalancers.tenant_id, lbaas_members.tenant_id, lbaas_pools.tenant_id, members.tenant_id, networkrbacs.target_tenant, networkrbacs.tenant_id, networks.tenant_id, pools.tenant_id, ports.tenant_id, quotas.tenant_id, quotausages.tenant_id, routers.tenant_id, securitygrouprules.tenant_id, securitygroups.tenant_id, subnets.tenant_id, vips.tenant_id

### port
- inferred: members.protocol_port, networksecuritybindings.port_security_enabled, portsecuritybindings.port_security_enabled, securitygrouprules.port_range_max, securitygrouprules.port_range_min

### status
- inferred: lbaas_listeners.provisioning_status, lbaas_loadbalancers.provisioning_status, lbaas_members.provisioning_status, lbaas_pools.provisioning_status, ports.status

### host
- inferred: agents.host, ml2_gre_endpoints.host, ml2_port_binding_levels.host, ml2_port_bindings.host

### subnets.id
- inferred: lbaas_loadbalancers.vip_subnet_id, lbaas_members.subnet_id, pools.subnet_id
- declared: dnsnameservers.subnet_id, ipallocationpools.subnet_id, ipallocations.subnet_id, nuage_subnet_l2dom_mapping.subnet_id, subnetroutes.subnet_id, vpnservices.subnet_id

### in
- inferred: poolstatisticss.bytes_in, quotausages.in_use

### ip
- inferred: ipallocationpools.first_ip, ipallocations.ip_address

### last
- inferred: ipallocationpools.last_ip, ipavailabilityranges.last_ip

### limit
- inferred: lbaas_listeners.connection_limit, quotas.limit

### physical
- inferred: ml2_network_segments.physical_network, ml2_vlan_allocations.physical_network

### networks.id
- inferred: floatingips.floating_network_id
- declared: auto_allocated_topologies.network_id, bgp_speaker_network_bindings.network_id, cisco_ml2_n1kv_network_bindings.network_id, externalnetworks.network_id, ha_router_networks.network_id, ha_router_vrid_allocations.network_id, ipallocations.network_id, ml2_network_segments.network_id, multi_provider_networks.network_id, networkconnections.network_id, networkdhcpagentbindings.network_id, networkdnsdomains.network_id, networkqueuemappings.network_id, networkrbacs.object_id, networksecuritybindings.network_id, neutron_nsx_network_mappings.neutron_id, nsxv_internal_networks.network_id, nsxv_spoofguard_policy_network_mappings.network_id, nsxv_tz_network_bindings.network_id, nuage_provider_net_bindings.network_id, ports.network_id, qos_network_policy_bindings.network_id, subnets.network_id, tz_network_bindings.network_id

### pools.id
- inferred: vips.pool_id
- declared: members.pool_id, nsxv_edge_pool_mappings.pool_id, nsxv_edge_vip_mappings.pool_id, poolloadbalanceragentbindings.pool_id, poolmonitorassociations.pool_id, poolstatisticss.pool_id

### routers.id
- inferred: floatingips.last_known_router_id
- declared: auto_allocated_topologies.router_id, cisco_ml2_apic_contracts.router_id, cisco_router_mappings.router_id, firewall_router_associations.router_id, floatingips.router_id, ha_router_agent_port_bindings.router_id, neutron_nsx_router_mappings.neutron_id, nsxv_router_ext_attributes.router_id, nuage_net_partition_router_mapping.router_id, router_extra_attributes.router_id, routerl3agentbindings.router_id, routerports.router_id, routerroutes.router_id, routerrules.router_id, vpnservices.router_id
