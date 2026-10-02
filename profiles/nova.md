---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:04:32.359791Z
dialect: mysql
database: nova
schema: nova
skipped_technical_tables:
  - `migrations`
---

## Relationships

- `aggregates`.`id` ← `aggregate_hosts`.`aggregate_id`, `aggregate_metadata`.`aggregate_id`
- `compute_nodes`.`id` ← `pci_devices`.`compute_node_id`
- `console_pools`.`id` ← `consoles`.`pool_id`
- `instance_actions`.`id` ← `instance_actions_events`.`action_id`
- `instance_groups`.`id` ← `instance_group_member`.`group_id`, `instance_group_policy`.`group_id`
- `instance_types`.`id` ← `instance_type_extra_specs`.`instance_type_id`, `instance_type_projects`.`instance_type_id`
- `instances`.`uuid` ← `block_device_mapping`.`instance_uuid`, `consoles`.`instance_uuid`, `fixed_ips`.`instance_uuid`, `instance_actions`.`instance_uuid`, `instance_extra`.`instance_uuid`, `instance_faults`.`instance_uuid`, `instance_info_caches`.`instance_uuid`, `instance_metadata`.`instance_uuid`, `instance_system_metadata`.`instance_uuid`, `security_group_instance_association`.`instance_uuid`, `virtual_interfaces`.`instance_uuid`
- `quota_usages`.`id` ← `reservations`.`usage_id`
- `security_groups`.`id` ← `security_group_instance_association`.`security_group_id`, `security_group_rules`.`group_id`, `security_group_rules`.`parent_group_id`

# `aggregate_hosts`  (rows=584)

columns:
`created_at` datetime: all distinct, nulls=57
`updated_at` datetime: 2017-08-04 16:36:52=96, nulls=488
`deleted_at` datetime: 351 distinct, nulls=138
`id` int PK: unique identifier, 1..1251
`host` varchar255: 127 distinct, "spark9-96"=23, "forge-23"=22, "align-86"=16, "streak-26"=16, "ether-50"=15, "blitz1-32"=13, "ether-18"=13, "shine-94"=13, "nexis-43"=12, "space2-35"=12
`aggregate_id` int NOTNULL FK: 2=183, 18=86, 17=62, 1=57, 13=40, 4=32, 21=20, 5=19, 15=19, 6=17, 19=15, 20=12, 14=10, 11=8, 9=2, 10=2, 1..21
`deleted` int: 352 distinct, 0..1247, avg=571.7055, median=759.5, 0=138, 1=96, 245=1, 516=1, 518=1, 519=1, 520=1, 521=1, 522=1, 523=1

indexes: `aggregate_id`, UNIQUE (`host`,`aggregate_id`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-05-06T16:14:41 | null | null |
| updated_at | null | 2017-08-04T16:36:52 | 2017-08-04T16:36:52 |
| deleted_at | null | 2017-08-04T16:36:52 | 2017-08-04T16:36:52 |
| id | 1251 | 59 | 60 |
| host | forge-23 | radar1-79 | forge3-2 |
| aggregate_id | 2 | 1 | 1 |
| deleted | 0 | 1 | 1 |

# `aggregate_metadata`  (rows=38)

columns:
`created_at` datetime: 27 distinct
`updated_at` datetime: 2017-07-21 16:42:43=2, 2013-08-06 01:43:56=1, 2014-12-16 14:51:10=1, 2016-05-10 20:04:24=1, 2016-05-10 20:04:34=1, 2017-12-14 03:48:48=1, 2022-11-21 20:22:19=1, 2022-11-21 20:22:34=1, nulls=29
`deleted_at` datetime: 2018-09-25 22:29:45=1, nulls=37
`id` int PK: unique identifier, 1..42
`aggregate_id` int NOTNULL FK: 2=5, 3=4, 4=4, 5=3, 6=3, 17=3, 19=3, 20=3, 21=3, 1=1, 9=1, 10=1, 11=1, 13=1, 14=1, 15=1, 1..21
`key` varchar255 NOTNULL: "cpu_allocation_ratio"=9, "ram_allocation_ratio"=9, "switch"=6, "availability_zone"=3, "generation"=3, "overcommit"=2, "cpu_ratio"=1, "hi_mem_use"=1, "test"=1, "testing"=1, "tig"=1, "ups"=1
`value` varchar255 NOTNULL: 25 distinct
`deleted` int: 0=37, 22=1

indexes: `aggregate_id`, `key`, UNIQUE (`aggregate_id`,`key`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-12-23T20:23:43 | 2019-12-23T19:48:50 | 2019-12-23T20:23:33 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 42 | 36 | 37 |
| aggregate_id | 20 | 20 | 21 |
| key | cpu_allocation_ratio | generation | ram_allocation_ratio |
| value | 8.0 | 3 | 3.5 |
| deleted | 0 | 0 | 0 |

# `aggregates`  (rows=21)

columns:
`created_at` datetime: all distinct, nulls=1
`updated_at` datetime: 2016-10-13 15:03:15=10, 2016-10-13 15:03:16=3, 2014-12-04 20:18:55=1, 2017-08-04 16:29:22=1, nulls=6
`deleted_at` datetime: 2016-07-07 03:08:27=1, 2016-09-28 23:44:55=1, 2017-02-16 21:47:48=1, 2017-02-16 21:56:42=1, 2017-08-04 16:29:22=1, nulls=16
`id` int PK: unique identifier, 1..21
`name` varchar255: 20 distinct
`deleted` int: 0=16, 7=1, 8=1, 12=1, 13=1, 16=1, 0..16
`uuid` varchar36: "094d9b67-6185-4adf-84b0-133402c4f190"=1, "0cf382be-16ff-4622-b83c-5183bc990b1b"=1, "0db2e90b-ddf9-4044-87b7-3a864b5e4329"=1, "1015ff87-4766-451b-867f-cc2f617e179b"=1, "27f99211-b2c5-47cb-a1a5-e9e1dd1b8ace"=1, "51594b5b-0011-4568-8370-e3d188302040"=1, "5a914b0d-30f0-4a22-bf8a-c4eedbaca0e3"=1, "66806f0e-1afc-422e-8f83-464a9f6226c3"=1, "706bb206-a340-4144-85ba-b78ca38b018f"=1, "74703873-8ec4-4183-bc76-99bca4686fe1"=1, "7ecfc17d-efad-4d26-a2d2-cc1b9a032a0c"=1, "a2475632-4dca-41b9-b102-a28966002418"=1, "ae39debd-2ba7-4ac5-ab22-432669532571"=1, "bfdb2a6d-bba0-4fc4-8030-b3544843480e"=1, "c3ecbf5d-21e8-4c84-9cb3-810f99fd8aa1"=1, "c5c3b947-39b7-470e-8e97-2d07ec7f5997"=1, "cbe731e6-bb27-4f6c-b782-fed83ca7ed8f"=1, "e2097396-feb9-4727-92fd-58b53436287c"=1, "ec980ea8-57d5-4808-b914-cfad25f348d3"=1, nulls=2

indexes: `uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-12-23T19:47:47 | 2014-02-07T18:00:36 | 2014-05-20T20:36:08 |
| updated_at | null | 2016-10-13T15:03:15 | 2016-10-13T15:03:15 |
| deleted_at | null | null | null |
| id | 21 | 5 | 6 |
| name | align-track | proto4 | aurum |
| deleted | 0 | 0 | 0 |
| uuid | 7ecfc17d-efad-4d26-a2d2-cc1b9a032a0c | bfdb2a6d-bba0-4fc4-8030-b3544843480e | 0cf382be-16ff-4622-b83c-5183bc990b1b |

# `all_instances`  (rows=717814)

```sql
CREATE VIEW nova.all_instances AS select `nova`.`instances`.`created_at` AS `created_at`,`nova`.`instances`.`updated_at` AS `updated_at`,`nova`.`instances`.`deleted_at` AS `deleted_at`,`nova`.`instances`.`id` AS `id`,`nova`.`instances`.`internal_id` AS `internal_id`,`nova`.`instances`.`user_id` AS `user_id`,`nova`.`instances`.`project_id` AS `project_id`,`nova`.`instances`.`image_ref` AS `image_ref`,`nova`.`instances`.`kernel_id` AS `kernel_id`,`nova`.`instances`.`ramdisk_id` AS `ramdisk_id`,`nova`.`instances`.`launch_index` AS `launch_index`,`nova`.`instances`.`key_name` AS `key_name`,`nova`.`instances`.`key_data` AS `key_data`,`nova`.`instances`.`power_state` AS `power_state`,`nova`.`instances`.`vm_state` AS `vm_state`,`nova`.`instances`.`memory_mb` AS `memory_mb`,`nova`.`instances`.`vcpus` AS `vcpus`,`nova`.`instances`.`hostname` AS `hostname`,`nova`.`instances`.`host` AS `host`,`nova`.`instances`.`user_data` AS `user_data`,`nova`.`instances`.`reservation_id` AS `reservation_id`,`nova`.`instances`.`scheduled_at` AS `scheduled_at`,`nova`.`instances`.`launched_at` AS `launched_at`,`nova`.`instances`.`terminated_at` AS `terminated_at`,`nova`.`instances`.`display_name` AS `display_name`,`nova`.`instances`.`display_description` AS `display_description`,`nova`.`instances`.`availability_zone` AS `availability_zone`,`nova`.`instances`.`locked` AS `locked`,`nova`.`instances`.`os_type` AS `os_type`,`nova`.`instances`.`launched_on` AS `launched_on`,`nova`.`instances`.`instance_type_id` AS `instance_type_id`,`nova`.`instances`.`vm_mode` AS `vm_mode`,`nova`.`instances`.`uuid` AS `uuid`,`nova`.`instances`.`architecture` AS `architecture`,`nova`.`instances`.`root_device_name` AS `root_device_name`,`nova`.`instances`.`access_ip_v4` AS `access_ip_v4`,`nova`.`instances`.`access_ip_v6` AS `access_ip_v6`,`nova`.`instances`.`config_drive` AS `config_drive`,`nova`.`instances`.`task_state` AS `task_state`,`nova`.`instances`.`default_ephemeral_device` AS `default_ephemeral_device`,`nova`.`instances`.`default_swap_device` AS `default_swap_device`,`nova`.`instances`.`progress` AS `progress`,`nova`.`instances`.`auto_disk_config` AS `auto_disk_config`,`nova`.`instances`.`shutdown_terminate` AS `shutdown_terminate`,`nova`.`instances`.`disable_terminate` AS `disable_terminate`,`nova`.`instances`.`root_gb` AS `root_gb`,`nova`.`instances`.`ephemeral_gb` AS `ephemeral_gb`,`nova`.`instances`.`cell_name` AS `cell_name`,`nova`.`instances`.`node` AS `node`,`nova`.`instances`.`deleted` AS `deleted`,`nova`.`instances`.`locked_by` AS `locked_by`,`nova`.`instances`.`cleaned` AS `cleaned`,`nova`.`instances`.`ephemeral_key_uuid` AS `ephemeral_key_uuid` from `nova`.`instances` union select `nova`.`shadow_instances`.`created_at` AS `created_at`,`nova`.`shadow_instances`.`updated_at` AS `updated_at`,`nova`.`shadow_instances`.`deleted_at` AS `deleted_at`,`nova`.`shadow_instances`.`id` AS `id`,`nova`.`shadow_instances`.`internal_id` AS `internal_id`,`nova`.`shadow_instances`.`user_id` AS `user_id`,`nova`.`shadow_instances`.`project_id` AS `project_id`,`nova`.`shadow_instances`.`image_ref` AS `image_ref`,`nova`.`shadow_instances`.`kernel_id` AS `kernel_id`,`nova`.`shadow_instances`.`ramdisk_id` AS `ramdisk_id`,`nova`.`shadow_instances`.`launch_index` AS `launch_index`,`nova`.`shadow_instances`.`key_name` AS `key_name`,`nova`.`shadow_instances`.`key_data` AS `key_data`,`nova`.`shadow_instances`.`power_state` AS `power_state`,`nova`.`shadow_instances`.`vm_state` AS `vm_state`,`nova`.`shadow_instances`.`memory_mb` AS `memory_mb`,`nova`.`shadow_instances`.`vcpus` AS `vcpus`,`nova`.`shadow_instances`.`hostname` AS `hostname`,`nova`.`shadow_instances`.`host` AS `host`,`nova`.`shadow_instances`.`user_data` AS `user_data`,`nova`.`shadow_instances`.`reservation_id` AS `reservation_id`,`nova`.`shadow_instances`.`scheduled_at` AS `scheduled_at`,`nova`.`shadow_instances`.`launched_at` AS `launched_at`,`nova`.`shadow_instances`.`terminated_at` AS `terminated_at`,`nova`.`shadow_instances`.`display_name` AS `display_name`,`nova`.`shadow_instances`.`display_description` AS `display_description`,`nova`.`shadow_instances`.`availability_zone` AS `availability_zone`,`nova`.`shadow_instances`.`locked` AS `locked`,`nova`.`shadow_instances`.`os_type` AS `os_type`,`nova`.`shadow_instances`.`launched_on` AS `launched_on`,`nova`.`shadow_instances`.`instance_type_id` AS `instance_type_id`,`nova`.`shadow_instances`.`vm_mode` AS `vm_mode`,`nova`.`shadow_instances`.`uuid` AS `uuid`,`nova`.`shadow_instances`.`architecture` AS `architecture`,`nova`.`shadow_instances`.`root_device_name` AS `root_device_name`,`nova`.`shadow_instances`.`access_ip_v4` AS `access_ip_v4`,`nova`.`shadow_instances`.`access_ip_v6` AS `access_ip_v6`,`nova`.`shadow_instances`.`config_drive` AS `config_drive`,`nova`.`shadow_instances`.`task_state` AS `task_state`,`nova`.`shadow_instances`.`default_ephemeral_device` AS `default_ephemeral_device`,`nova`.`shadow_instances`.`default_swap_device` AS `default_swap_device`,`nova`.`shadow_instances`.`progress` AS `progress`,`nova`.`shadow_instances`.`auto_disk_config` AS `auto_disk_config`,`nova`.`shadow_instances`.`shutdown_terminate` AS `shutdown_terminate`,`nova`.`shadow_instances`.`disable_terminate` AS `disable_terminate`,`nova`.`shadow_instances`.`root_gb` AS `root_gb`,`nova`.`shadow_instances`.`ephemeral_gb` AS `ephemeral_gb`,`nova`.`shadow_instances`.`cell_name` AS `cell_name`,`nova`.`shadow_instances`.`node` AS `node`,`nova`.`shadow_instances`.`deleted` AS `deleted`,`nova`.`shadow_instances`.`locked_by` AS `locked_by`,`nova`.`shadow_instances`.`cleaned` AS `cleaned`,`nova`.`shadow_instances`.`ephemeral_key_uuid` AS `ephemeral_key_uuid` from `nova`.`shadow_instances`;
```

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=84
`deleted_at` datetime: nulls=1485
`id` int: 1..749387
`internal_id` int: all NULL
`user_id` varchar255: profile metrics skipped
`project_id` varchar255: profile metrics skipped
`image_ref` varchar255: uuid, nulls=4110
`kernel_id` varchar255: uuid, nulls=717695
`ramdisk_id` varchar255: uuid, nulls=717695
`launch_index` int: 0..511, avg=2.7386
`key_name` varchar255: nulls=33056
`key_data` mediumtext: nulls=33061
`power_state` int: 0..5, avg=0.7548
`vm_state` varchar255: profile metrics skipped
`memory_mb` int: 1..98304, avg=4388.6399
`vcpus` int: 1..88, avg=2.4029
`hostname` varchar255: profile metrics skipped
`host` varchar255: profile metrics skipped
`user_data` mediumtext: nulls=369424
`reservation_id` varchar255: profile metrics skipped
`scheduled_at` datetime: nulls=320813
`launched_at` datetime: nulls=173685
`terminated_at` datetime: nulls=142458
`display_name` varchar255: profile metrics skipped
`display_description` varchar255: nulls=434542
`availability_zone` varchar255: nulls=685490
`locked` int: 0..1, avg=0
`os_type` varchar255: all NULL
`launched_on` mediumtext: nulls=143559
`instance_type_id` int: 1..196
`vm_mode` varchar255: all NULL
`uuid` varchar36: uuid
`architecture` varchar255: nulls=717620
`root_device_name` varchar255: nulls=147834
`access_ip_v4` varchar39: all NULL
`access_ip_v6` varchar39: all NULL
`config_drive` varchar255: bool-like, nulls=717415
`task_state` varchar255: nulls=575126
`default_ephemeral_device` varchar255: nulls=409056
`default_swap_device` varchar255: nulls=717260
`progress` int: 0..0, avg=0
`auto_disk_config` int: nulls=481255, 0..1, avg=0.0039
`shutdown_terminate` int: 0..1, avg=0.0269
`disable_terminate` int: 0..0, avg=0
`root_gb` int: 0..100, avg=12.5595
`ephemeral_gb` int: 0..360, avg=24.3553
`cell_name` varchar255: all NULL
`node` varchar255: nulls=472155
`deleted` int: 0..749385, avg=359838.7599
`locked_by` varchar5: nulls=717800
`cleaned` int: 0..1, avg=0.9926
`ephemeral_key_uuid` varchar36: all NULL

- latest rows skipped (query timeout > 10s); random rows skipped (native table sampling is unavailable for views)

# `block_device_mapping`  (rows=16798)

columns:
`created_at` datetime: 15930 distinct
`updated_at` datetime: 15739 distinct, nulls=190
`deleted_at` datetime: 13825 distinct, nulls=1705
`id` int PK: unique identifier, 28326..281398
`device_name` varchar255: 29 distinct, nulls=115, "/dev/vda"=6027, "/dev/vdb"=1709, "/dev/vdd"=1524, "/dev/vdc"=1517, "/dev/vde"=1286, "/dev/vdf"=1058, "/dev/vdg"=854, "/dev/vdh"=597, "/dev/vdi"=488, "/dev/vdj"=368
`delete_on_termination` int: 0=11986, 1=4812
`snapshot_id` varchar36: "f2548d6b-0503-424b-a724-f693164db5a5"=38, "77c31642-cd38-49f1-8699-866ad8d65ad9"=4, "912f4cde-2942-4ebd-b331-479d72026ff9"=4, "455c943a-6cef-45e5-a3c5-367efe6e24c7"=3, "5f88f17d-188c-4988-962f-5c709d235c24"=2, "0e4a03ca-ae1e-4cb6-bce3-7b5a8bbf786c"=1, "44bcca2f-4082-4898-89c0-d146d5b01645"=1, "56c5b012-d380-4694-99c9-455604b9a619"=1, "707161b4-048e-45ca-8bbf-df9175d2ef23"=1, "79d252e0-4d1c-4522-b8b6-7973d32b4eb3"=1, "7b43d435-da52-499b-86e0-f09d91cd6b13"=1, "810c3e0e-84c3-4799-8b6a-ed5b4fb2a8af"=1, "a0100981-2112-450c-acfa-98fc1031a550"=1, "acc984ab-7af5-4f09-b86c-a3d2d8920825"=1, "b21470a9-a635-40b9-93b2-b31da4606cfd"=1, "c4907106-3e73-49ce-8d94-8781a8f963bb"=1, "c5c0d411-12d2-4163-a2ce-5ac6762c032f"=1, "dedb5e1b-7d09-4110-b7be-ebaf06effff5"=1, nulls=16734
`volume_id` varchar36: uuid, 1674 distinct, nulls=4776, "79ea9032-0141-45e4-af84-64796f14d4dd"=217, "19f6274f-e3cb-4700-bd16-a89f9574dffa"=162, "3b4d549a-85d6-4760-a04d-551d30bd8011"=161, "d152b1c5-c6ce-4599-8550-5a5a62961095"=155, "7c12e582-2dac-4904-a5ee-725ffb522ea6"=138, "d19b4658-ddd8-4ac6-bcb5-715c72785893"=134, "23b5f8b7-9de0-4102-9bff-2f7aa3cf3adf"=121, "cef71f67-0988-44e5-b08c-e0cfe4cbcd33"=119, "f16530a1-353b-40e9-a4b0-4fa793345446"=118, "71f8af57-2515-436e-afd3-80cd96888f86"=117
`volume_size` int: 74 distinct, nulls=4805, 1..16384, avg=45.601, median=5
`no_device` int: 0=6240, nulls=10558
`connection_info` text: 2379 distinct, nulls=4860
`instance_uuid` varchar36 FK: uuid, 6143 distinct, "9b309acd-a62c-436e-b116-ff7554e6ec1e"=3313, "f651937a-8bcd-43f1-910e-f5b61fa358ac"=2338, "64d7cd79-6dc6-404c-b603-8cdd4f9263a0"=2014, "0b1e3819-6250-479d-9247-549549fcb712"=933, "501e65b0-b58f-4e7f-b015-30777efd0f31"=712, "c1852e78-3fbe-4cab-bb45-6712f15de351"=582, "c9a2d351-64b2-4b74-af4c-aa71269cad0d"=9, "bf46f261-9857-4915-b8fe-43d9e9cc3a40"=8, "d2836b5f-d5d6-4e04-980d-8f45882a19d2"=8, "d052d786-9b26-4439-ae6b-32a0505fdc12"=7
`deleted` int: 15094 distinct, 0..281398, avg=243885.3779, median=272541.5
`source_type` varchar255: "volume"=11905, "image"=4677, "blank"=152, "snapshot"=64
`destination_type` varchar255: "volume"=12023, "local"=4775
`guest_format` varchar255: "swap"=57, nulls=16741
`device_type` varchar255: "disk"=6604, "cdrom"=11, nulls=10183
`disk_bus` varchar255: "virtio"=2037, "ide"=11, nulls=14750
`boot_index` int: 0=6143, -1=141, 1=65, nulls=10449, -1..1
`image_id` varchar36: uuid, 615 distinct, nulls=12121

indexes: (`instance_uuid`,`device_name`), `instance_uuid`, (`instance_uuid`,`volume_id`), `snapshot_id`, `volume_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-28T01:25:36 | 2015-04-14T15:27:05 | 2015-04-14T15:52:52 |
| updated_at | 2024-06-28T01:25:42 | 2015-04-14T15:27:07 | 2015-04-14T15:52:58 |
| deleted_at | 2024-06-28T01:37:05 | 2022-08-16T14:33:30 | null |
| id | 281398 | 123050 | 123145 |
| device_name | /dev/vdb | /dev/vda | /dev/vda |
| delete_on_termination | 0 | 1 | 1 |
| snapshot_id | null | null | null |
| volume_id | 7308377b-f688-4246-936b-5bd08a204982 | null | null |
| volume_size | 5 | null | null |
| no_device | null | null | null |
| connection_info | {"driver_volume_type": "rbd", "connector": {"initiator": "iqn10.132.246.102/8-10.121.122.184/8org.debian:01:75848bb568e8", "ip": "10.165.53.177/8", "platform": "x86_64", "host": "cosmo3-23", "os_type… | null | null |
| instance_uuid | 7fe281b6-5744-41ca-9f94-9d6f516b4e8b | d9ddf3f4-7749-42a7-98fd-30ca51c5371d | 259bf0b8-8821-46f8-945e-5f24ea559ffd |
| deleted | 281398 | 123050 | 0 |
| source_type | volume | image | image |
| destination_type | volume | local | local |
| guest_format | null | null | null |
| device_type | null | disk | disk |
| disk_bus | null | null | null |
| boot_index | null | 0 | 0 |
| image_id | null | 297a9c1d-75b4-4744-b7e9-47c8a25eab10 | 2a0b1112-7f39-43e6-9a29-5e82dd62713a |

# `certificates`  (rows=127)

columns:
`created_at` datetime: all distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 1..127
`user_id` varchar255: 55 distinct, "3b484308cddd436a87471cd1dcfa53c7"=10, "6360caf9aaaa436c8deee7dbf094f726"=10, "a1ef823458d24a68955fec6f3d390019"=10, "c8490ee0863345f6919b5c63540efca1"=8, "78d8da36e7904928ad34c807390314f3"=7, "011e1ffb210245abbb2ba24be9b4f5be"=6, "d44a0e9978c347e288a218aa6266f38b"=5, "59a5934524c54089af8f35bed2ea7eaa"=4, "0df639d1cf6a48f7b9ddf6cf68772ca8"=3, "715323529b6e488d884944199f24b4c9"=3
`project_id` varchar255: "3008a142e9524f7295b06ea811908f93"=77, "71322eb9ba804fc4ae74cefde3ad0742"=9, "98333a1a28e746fa8c629c83a818ad57"=9, "2a9b495932c64d80b1fac28d1416a921"=5, "97107d3284a848a4a4ea0345bd05cbef"=5, "70b2507b8cc44fcb917ddfb85f5079d9"=4, "b7188a889c6a4800893445d969673bab"=4, "bfd50153a2e9476f93e33e30e922cd06"=3, "dba6cc0fec6845a58f4dd5e84ef8dca5"=3, "4e101cf5264b4e739b7b5ebe0f6b5c68"=2, "1124c2b7959f4101a662875fd5581c19"=1, "1140b46602e84c47838f707b060d6fd2"=1, "6f5103a9ae434375a92a1de24a19ca56"=1, "d0ebc85936794a30b65bb6dae5687404"=1, "deecf4e22b4244ffa09aa8ce7748e976"=1, "fc1b446cad9e4849a41f9160664e3781"=1
`file_name` varchar255: 124 distinct
`deleted` int: 0=127

indexes: (`project_id`,`deleted`), (`user_id`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2014-12-30T18:36:51 | 2014-04-23T21:45:40 | 2014-04-23T21:46:04 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 127 | 99 | 100 |
| user_id | a1ef823458d24a68955fec6f3d390019 | 6360caf9aaaa436c8deee7dbf094f726 | 6360caf9aaaa436c8deee7dbf094f726 |
| project_id | bfd50153a2e9476f93e33e30e922cd06 | 3008a142e9524f7295b06ea811908f93 | 3008a142e9524f7295b06ea811908f93 |
| file_name | /var/lib/nova/CA/newcerts/8B.pem | /var/lib/nova/CA/newcerts/72.pem | /var/lib/nova/CA/newcerts/73.pem |
| deleted | 0 | 0 | 0 |

# `compute_nodes`  (rows=139)

columns:
`created_at` datetime: all distinct
`updated_at` datetime: 126 distinct
`deleted_at` datetime: all distinct, nulls=43
`id` int PK: unique identifier, 1..149
`service_id` int: 104 distinct, nulls=33, 6..261
`vcpus` int NOTNULL: 24=66, 32=48, 40=20, 88=5, 24..88
`memory_mb` int NOTNULL: 48292=48, 193403=21, 193404=20, 257720=19, 48294=6, 48295=5, 96676=5, 774004=5, 128893=2, 181307=2, 40228=1, 48164=1, 145019=1, 161147=1, 181308=1, 257719=1, 40228..774004
`local_gb` int NOTNULL: 379868=61, 686780=33, 376144=11, 507931=8, 223452=5, 510310=5, 642559=5, 510717=4, 186210=3, 790=1, 916=1, 511508=1, 752475=1, 790..752475
`vcpus_used` int NOTNULL: 45 distinct, 0..585, avg=36.777, median=0
`memory_mb_used` int NOTNULL: 44 distinct, 512..1912832, avg=76442.705, median=512
`local_gb_used` int NOTNULL: 44 distinct, 0..3328, avg=190.1727, median=0
`hypervisor_type` text NOTNULL: "QEMU"=139
`hypervisor_version` int NOTNULL: 2005000=128, 2000000=6, 2002000=3, 1005000=2, 1005000..2005000
`cpu_info` text NOTNULL: "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["pge", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "monitor", "smx", "pb…"=55, "{"vendor": "Intel", "model": "Broadwell-IBRS", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xt…"=20, "{"vendor": "Intel", "model": "SandyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "m…"=14, "{"vendor": "Intel", "model": "IvyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "smep",…"=13, "{"vendor": "Intel", "model": "IvyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "s…"=10, "{"vendor": "Intel", "model": "SandyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "md-clear",…"=6, "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["ssse3", "pge", "clflush", "sep", "syscall", "vme", "dtes64", "tsc", "vmx", "xtpr", "cmov", "pcid", "est", "pat", "monitor", "s…"=6, "{"vendor": "Intel", "model": "Broadwell-IBRS", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xt…"=5, "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["pge", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "monitor", "smx", "pb…"=3, "{"vendor": "Intel", "model": "Broadwell", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr",…"=2, "{"vendor": "Intel", "model": "IvyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "fsgsbase", "xsave", "vmx", "erms", "xtpr", "cmov", "s…"=2, "{"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pcid", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe…"=2, "{"vendor": "Intel", "model": "SandyBridge-IBRS", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "est", "pat…"=1
`disk_available_least` int: 57 distinct, 496..396651, avg=210288.3741, median=195844
`free_ram_mb` int: 33 distinct, 0..539508, avg=31066.6906, median=0
`free_disk_gb` int: 58 distinct, 620..752475, avg=465892.6475, median=379868
`current_workload` int: 0=134, 1=4, 2=1, 0..2
`running_vms` int: 26 distinct, 0..55, avg=5.6475, median=0
`hypervisor_hostname` varchar255: 133 distinct
`deleted` int: 97 distinct, 0..144, avg=36.4892, median=28, 0=43, 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1
`host_ip` varchar39: 125 distinct
`supported_instances` text: "[["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "…"=128, "[["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "hvm"], ["microblaze", "qemu"…"=7, "[["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["x86_64", "qemu", "hvm"], ["x86_64", "kvm", "hvm"]]"=4
`pci_stats` text: "{"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": []}, "nova_object.namespace": "nova"}"=130, "[]"=7, "{"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": [{"nova_object.version": "1.1", "nova_object.changes": ["co…"=2
`metrics` text: "[]"=131, "[{"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.user.percent", "value": 0.3661098901098901, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-03-30T00:55:22.292540", "name": "cpu.kern…"=1, "[{"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.user.percent", "value": 0.021698235158046565, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-05-15T19:39:32.209945", "name": "cpu.ke…"=1, "[{"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.user.percent", "value": 0.04069171794959948, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-10-02T01:28:01.260391", "name": "cpu.ker…"=1, "[{"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.user.percent", "value": 0.26660726525017137, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2015-11-21T14:56:47.022248", "name": "cpu.ker…"=1, "[{"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.user.percent", "value": 0.000685562334235875, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-02-24T05:20:27.089567", "name": "cpu.ke…"=1, "[{"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.user.percent", "value": 0.0007583611051199811, "source": "libvirt.LibvirtDriver"}, {"timestamp": "2016-09-28T13:16:37.527552", "name": "cpu.k…"=1, nulls=2
`extra_resources` text: all NULL
`stats` text: 49 distinct
`numa_topology` text: 50 distinct, nulls=5
`host` varchar255: 126 distinct, ""=8, "lumen4-89"=3, "blitz7-74"=2, "cubic-10"=2, "quark-5"=2, "streak5-74"=2, "align-73"=1, "align-79"=1, "align-86"=1, "alpha-80"=1
`ram_allocation_ratio` float: 0=128, nulls=11
`cpu_allocation_ratio` float: 0=128, nulls=11
`uuid` varchar36: uuid, all distinct, nulls=7
`disk_allocation_ratio` float: 0=128, nulls=11

indexes: UNIQUE (`host`,`hypervisor_hostname`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-01-09T18:22:21 | 2014-05-22T19:46:04 | 2014-05-22T19:47:20 |
| updated_at | 2019-01-09T18:22:21 | 2018-02-15T16:10:14 | 2018-02-15T16:10:33 |
| deleted_at | null | 2018-11-05T19:07:44 | 2018-11-05T19:07:39 |
| id | 149 | 72 | 73 |
| service_id | null | 156 | 157 |
| vcpus | 32 | 32 | 32 |
| memory_mb | 128893 | 193404 | 193404 |
| local_gb | 642559 | 510717 | 510717 |
| vcpus_used | 0 | 0 | 0 |
| memory_mb_used | 512 | 512 | 512 |
| local_gb_used | 0 | 0 | 0 |
| hypervisor_type | QEMU | QEMU | QEMU |
| hypervisor_version | 2005000 | 2005000 | 2005000 |
| cpu_info | {"vendor": "Intel", "model": "Broadwell", "arch": "x86_64", "features": ["smap", "avx", "clflush", "sep", "rtm", "vme", "dtes64", "invpcid", "tsc", "fsgsbase", "xsave", "pge", "vmx", "erms", "xtpr",… | {"vendor": "Intel", "model": "SandyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "m… | {"vendor": "Intel", "model": "SandyBridge", "arch": "x86_64", "features": ["pge", "avx", "clflush", "sep", "syscall", "vme", "dtes64", "msr", "xsave", "vmx", "xtpr", "cmov", "ssse3", "est", "pat", "m… |
| disk_available_least | 364779 | 281505 | 281506 |
| free_ram_mb | 0 | 0 | 0 |
| free_disk_gb | 642559 | 510717 | 510717 |
| current_workload | 0 | 0 | 0 |
| running_vms | 0 | 0 | 0 |
| hypervisor_hostname | cubic-10.yahoo.ca.com | space1-89.yahoo.ca.com | layer-86.yahoo.ca.com |
| deleted | 0 | 72 | 73 |
| host_ip | 10.76.186.207/8 | 10.39.218.201/8 | 10.190.70.80/8 |
| supported_instances | [["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "… | [["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "… | [["alpha", "qemu", "hvm"], ["armv7l", "qemu", "hvm"], ["aarch64", "qemu", "hvm"], ["cris", "qemu", "hvm"], ["i686", "qemu", "hvm"], ["i686", "kvm", "hvm"], ["lm32", "qemu", "hvm"], ["m68k", "qemu", "… |
| pci_stats | {"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": [{"nova_object.version": "1.1", "nova_object.changes": ["co… | {"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": []}, "nova_object.namespace": "nova"} | {"nova_object.version": "1.1", "nova_object.changes": ["objects"], "nova_object.name": "PciDevicePoolList", "nova_object.data": {"objects": []}, "nova_object.namespace": "nova"} |
| metrics | [] | [] | [] |
| extra_resources | null | null | null |
| stats | {} | {} | {} |
| numa_topology | {"nova_object.version": "1.2", "nova_object.changes": ["cells"], "nova_object.name": "NUMATopology", "nova_object.data": {"cells": [{"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage",… | {"nova_object.version": "1.2", "nova_object.changes": ["cells"], "nova_object.name": "NUMATopology", "nova_object.data": {"cells": [{"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage",… | {"nova_object.version": "1.2", "nova_object.changes": ["cells"], "nova_object.name": "NUMATopology", "nova_object.data": {"cells": [{"nova_object.version": "1.2", "nova_object.changes": ["cpu_usage",… |
| host | cubic-10 | space1-89 | layer-86 |
| ram_allocation_ratio | 0 | 0 | 0 |
| cpu_allocation_ratio | 0 | 0 | 0 |
| uuid | 5b0b8cb5-84e6-4cdf-9721-dffb37549727 | 2bf4cbfa-a204-4547-ba1d-b0b7cf6dadf6 | ab410fe7-cb83-4af9-9a51-84683283ee3b |
| disk_allocation_ratio | 0 | 0 | 0 |

# `fixed_ips`  (rows=63724)

columns:
`created_at` datetime: 34 distinct
`updated_at` datetime: 531 distinct, nulls=62716, 2013-05-01 20:51:55=25, 2013-08-09 21:13:26=24, 2013-08-09 02:42:12=23, 2013-05-01 19:07:40=21, 2013-05-01 19:08:40=13, 2013-05-01 20:49:55=13, 2013-05-01 19:13:41=11, 2013-05-01 19:06:40=10, 2013-05-01 19:09:40=10, 2013-05-01 19:12:41=10
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 769..66304
`address` varchar39: all distinct
`network_id` int: 1=63724
`allocated` int: 0=63724
`leased` int: 0=63724
`reserved` int: 0=63721, 1=3
`virtual_interface_id` int: all NULL
`host` varchar255: 62 distinct, ""=63663, "align-73"=1, "align-79"=1, "arrow-57"=1, "astro1-40"=1, "blaze1-11"=1, "blitz7-74"=1, "celes-28"=1, "dash3-6"=1, "drift-42"=1
`instance_uuid` varchar36 FK: all NULL
`deleted` int: 0=63724

indexes: `address`, (`address`,`reserved`,`network_id`,`deleted`), (`address`,`deleted`,`allocated`), (`deleted`,`allocated`,`updated_at`), `host`, `instance_uuid`, (`network_id`,`host`,`deleted`), `virtual_interface_id`, UNIQUE (`address`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2012-09-07T13:52:47 | 2012-09-07T13:52:15 | 2012-09-07T13:52:15 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 66304 | 4112 | 4113 |
| address | 10.223.191.20/8 | 10.54.219.186/8 | 10.216.219.141/8 |
| network_id | 1 | 1 | 1 |
| allocated | 0 | 0 | 0 |
| leased | 0 | 0 | 0 |
| reserved | 1 | 0 | 0 |
| virtual_interface_id | null | null | null |
| host |  |  |  |
| instance_uuid | null | null | null |
| deleted | 0 | 0 | 0 |

# `floating_ips`  (rows=8190)

columns:
`created_at` datetime: 208 distinct
`updated_at` datetime: 150 distinct, nulls=8019
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 1..8190
`address` varchar39: all distinct
`fixed_ip_id` int: all NULL
`project_id` varchar255: 24 distinct, nulls=8020, "3008a142e9524f7295b06ea811908f93"=37, "292c70904ce7415c8626f801bbf1ed0c"=30, "6f5103a9ae434375a92a1de24a19ca56"=25, "98333a1a28e746fa8c629c83a818ad57"=11, "71322eb9ba804fc4ae74cefde3ad0742"=10, "956ae20bbb444a8c8f149729198aec63"=7, "4e101cf5264b4e739b7b5ebe0f6b5c68"=6, "34f87362758043a98ea19c5a5e9217c9"=5, "b7188a889c6a4800893445d969673bab"=5, "d0ebc85936794a30b65bb6dae5687404"=5
`host` varchar255: all NULL
`auto_assigned` int: 0=8190
`pool` varchar255: "nova"=8190
`interface` varchar255: "eth0"=8190
`deleted` int: 0=8190

indexes: `fixed_ip_id`, `host`, (`pool`,`deleted`,`fixed_ip_id`,`project_id`), `project_id`, UNIQUE (`address`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2012-07-05T19:22:43 | 2012-07-05T19:19:21 | 2012-07-05T19:19:21 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 8190 | 181 | 182 |
| address | 10.13.139.247/8 | 10.138.193.17/8 | 10.87.207.158/8 |
| fixed_ip_id | null | null | null |
| project_id | null | null | null |
| host | null | null | null |
| auto_assigned | 0 | 0 | 0 |
| pool | nova | nova | nova |
| interface | eth0 | eth0 | eth0 |
| deleted | 0 | 0 | 0 |

# `instance_actions`  (rows=27472)

columns:
`created_at` datetime: 23931 distinct
`updated_at` datetime: 884 distinct, nulls=26399
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 115259..650157
`action` varchar255: 23 distinct
`instance_uuid` varchar36 FK: uuid, 7218 distinct, "74334240-be67-4c1c-8295-9b6fcbbf8b9e"=196, "d2175cc8-2291-4575-bd91-6ad630003504"=104, "712a70cf-d00c-4c5b-8951-459012e56c08"=81, "3a428bb4-d4c2-4bd7-9433-b4b7a7ba9735"=60, "6869e646-0794-4207-8c16-cd196b535713"=52, "b78f7192-68f4-4cc1-a6a1-6a66692b612b"=50, "7cc17fdb-b107-4d13-ad5c-32c9dfec5abe"=49, "b8e529b0-87c9-4bb3-bdcb-9b83ceceea87"=45, "9b47723a-f295-451f-80ae-5d68e70fe9f7"=44, "a5b3463c-91c3-447a-b054-b89483e5ed75"=42
`request_id` varchar255: 25464 distinct, "req-ba99e8ba-67eb-4893-a936-32e652f4f51f"=97, "req-255f06b8-f402-4698-b842-2f590902ab7e"=80, "req-bdafb6e5-08eb-481e-a088-04af324a2555"=40, "req-b653c71e-6dc3-4d24-a291-4bb8a75b1dfa"=28, "req-bf7e9a8c-1e78-4afa-baf3-c78709ed6368"=27, "req-29d94e17-61f2-4b59-af54-b6a2318bb521"=26, "req-0c18809b-a8a1-443e-a6a8-9d928458bbd8"=25, "req-0f3f7178-36fb-4a50-bc8e-fadf66bf03ad"=24, "req-2c261d80-529c-461b-b7be-a368686262a0"=22, "req-fc6fc800-1a62-43ef-a25a-401a7b7b65e6"=22
`user_id` varchar255: 568 distinct, nulls=1701
`project_id` varchar255: 481 distinct, nulls=1701
`start_time` datetime: 23719 distinct
`finish_time` datetime: all NULL
`message` varchar255: "Error"=1073, nulls=26399
`deleted` int: 0=27472

indexes: `instance_uuid`, `request_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-07-05T20:28:18 | 2016-06-17T00:26:29 | 2016-06-17T00:37:42 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 650157 | 499575 | 499576 |
| action | stop | reboot | stop |
| instance_uuid | 81606363-89ce-4172-93ff-63d26cdbd0b1 | 6b1e60c3-898a-4526-8bd3-e80c5128ea88 | 6b1e60c3-898a-4526-8bd3-e80c5128ea88 |
| request_id | req-6b9be970-4f72-48b2-ad39-a545b9506c41 | req-c2c0886e-236a-44bd-94aa-a56325abfeca | req-2a149a2a-5e68-4d0b-a589-031cbcaa32ed |
| user_id | 16d15017af6749c89af3cb547a3a28ff | d77a44110635476796a1cfbb631f155a | null |
| project_id | a5c6a169183342b989557bb95c7b8e0b | fc1b446cad9e4849a41f9160664e3781 | null |
| start_time | 2024-07-05T20:28:17 | 2016-06-17T00:26:28 | 2016-06-17T00:37:41 |
| finish_time | null | null | null |
| message | null | null | null |
| deleted | 0 | 0 | 0 |

# `instance_actions_events`  (rows=41690)

columns:
`created_at` datetime: 33215 distinct
`updated_at` datetime: 32409 distinct, nulls=2522
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 181740..795647
`event` varchar255: 35 distinct
`action_id` int FK: 26251 distinct, 115259..650157, 635476=27, 641794=27, 635226=23, 636850=15, 636904=15, 637012=15, 637015=15, 639025=15, 639027=15, 640039=15
`start_time` datetime: 33213 distinct
`finish_time` datetime: 32406 distinct, nulls=2522
`result` varchar255: "Success"=38080, "Error"=1088, nulls=2522
`traceback` text: 167 distinct, nulls=40579
`deleted` int: 0=41690
`host` varchar255: all NULL
`details` text: all NULL

indexes: `action_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-07-05T20:28:18 | 2015-03-03T14:59:29 | 2015-03-04T21:15:27 |
| updated_at | 2024-07-05T20:28:25 | 2015-03-03T14:59:48 | 2015-03-04T21:15:36 |
| deleted_at | null | null | null |
| id | 795647 | 308012 | 316182 |
| event | compute_stop_instance | compute__do_build_and_run_instance | compute_reboot_instance |
| action_id | 650157 | 197162 | 204782 |
| start_time | 2024-07-05T20:28:18 | 2015-03-03T14:59:29 | 2015-03-04T21:15:27 |
| finish_time | 2024-07-05T20:28:25 | 2015-03-03T14:59:48 | 2015-03-04T21:15:36 |
| result | Success | Success | Success |
| traceback | null | null | null |
| deleted | 0 | 0 | 0 |
| host | null | null | null |
| details | null | null | null |

# `instance_extra`  (rows=7253)

columns:
`created_at` datetime: 6330 distinct
`updated_at` datetime: 6480 distinct, nulls=9
`deleted_at` datetime: 4999 distinct, nulls=1512
`deleted` int: 5742 distinct, 0..218597, avg=166267.5532, median=213320
`id` int PK: unique identifier, 1505..218599
`instance_uuid` varchar36 NOTNULL FK: uuid, 7226 distinct
`numa_topology` text: all distinct, nulls=7189
`pci_requests` text: "[]"=7171, "[{"count": 1, "request_id": null, "alias_name": "gpu", "spec": [{"vendor_id": "10de", "product_id": "102d"}], "is_new": false}]"=4, "[{"count": 2, "request_id": null, "alias_name": "gpu", "spec": [{"vendor_id": "10de", "product_id": "102d"}], "is_new": false}]"=1, nulls=77
`flavor` text: 199 distinct
`vcpu_model` text: "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=1780, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=1661, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=1418, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=957, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=497, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=235, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=225, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=57, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=50, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=6, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=4, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=3, "{"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f…"=3, nulls=357
`migration_context` text: 214 distinct, nulls=7038

indexes: `instance_uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2016-09-16T18:12:55 | 2016-09-17T17:36:18 |
| updated_at | 2024-06-26T20:40:27 | 2022-09-01T14:48:48 | 2023-01-15T20:08:28 |
| deleted_at | null | null | null |
| deleted | 0 | 0 | 0 |
| id | 218599 | 174996 | 175004 |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | c759ce3b-5053-4b39-b474-c385b68e2ce2 | 6ca45308-1502-4e8b-8583-4be5fd8b7e63 |
| numa_topology | null | null | null |
| pci_requests | [] | [] | [] |
| flavor | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 32, "name": "… | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 16, "name": "… | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 16, "name": "… |
| vcpu_model | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f… | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f… | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f… |
| migration_context | null | null | null |

# `instance_faults`  (rows=5624)

columns:
`created_at` datetime: 4562 distinct, 2021-10-05 14:35:37=12, 2021-10-05 15:53:01=12, 2015-10-02 14:31:19=10, 2016-10-12 16:56:19=9, 2021-10-05 12:52:33=9, 2021-10-05 13:43:16=9, 2021-10-05 14:34:26=9, 2021-10-05 15:15:32=9, 2021-10-05 15:36:15=9, 2015-11-02 19:26:06=8
`updated_at` datetime: all NULL
`deleted_at` datetime: 822 distinct, nulls=1388
`id` int PK: unique identifier, 175047..209903
`instance_uuid` varchar36 FK: uuid, 1252 distinct, "64d7cd79-6dc6-404c-b603-8cdd4f9263a0"=1010, "f651937a-8bcd-43f1-910e-f5b61fa358ac"=919, "075cd164-eac4-451d-9e8b-f88f96b20b41"=308, "e945b2b7-da17-4e24-ab43-de3c3360eea4"=295, "023de0aa-70a8-42f8-892c-be860e3f2890"=36, "3bc21419-2061-42eb-bc48-8417001cfbdc"=34, "5de2ff89-ff04-4cbe-8e00-3837479ba2f1"=29, "85aafec6-1b2e-423a-b834-d4a526068dec"=28, "ca7d8583-76b2-42f8-a8c6-102ce9ce56b1"=28, "7f7db4fc-3f92-4f90-9a34-7034fe0f3e90"=23
`code` int NOTNULL: 500=4004, 400=1610, 404=10, 400..500
`message` varchar255: 921 distinct
`details` text: 885 distinct, nulls=1670
`host` varchar255: 121 distinct, "spark9-96"=1964, "gamut-16"=441, "shine-94"=415, "glint3-93"=308, "flare4-57"=130, "forge-23"=128, "blaze8-12"=111, "align-86"=98, "blitz1-32"=90, "beam8-22"=83
`deleted` int: 4237 distinct, 0..209903, avg=155071.6981, median=206629.5, 0=1388, 190215=1, 190246=1, 190248=1, 190249=1, 190252=1, 190262=1, 190263=1, 190424=1, 190501=1

indexes: `host`, (`instance_uuid`,`deleted`,`created_at`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-22T20:00:45 | 2024-01-30T05:52:28 | 2024-01-30T05:52:28 |
| updated_at | null | null | null |
| deleted_at | 2024-06-22T20:00:59 | 2024-01-30T05:56:36 | 2024-01-30T05:56:36 |
| id | 209903 | 209776 | 209777 |
| instance_uuid | 80ad4b7a-d2ff-46d2-b5e9-e88a357b6d74 | ae8f7558-22fc-4b57-aac6-d2a2df6bb0e2 | ae8f7558-22fc-4b57-aac6-d2a2df6bb0e2 |
| code | 500 | 400 | 400 |
| message | 5ad43fc335ae8814d8ebe3345626860a | b994d987f044d07734a259e5582f0dcf | 63dade7fe94555e5478e9ecf7d9e6283 |
| details | fb2141c5c0978bee9f87d0e1a0b4fe39 | null | null |
| host | cosmo3-23 | beam8-22 | beam8-22 |
| deleted | 209903 | 209776 | 209777 |

# `instance_group_member`  (rows=4085)

columns:
`created_at` datetime: 2866 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 2210 distinct, nulls=56
`deleted` int: 4030 distinct, 0..4167, avg=2100.1053, median=2110
`id` int PK: unique identifier, 1..4169
`instance_id` varchar255: uuid, unique identifier
`group_id` int NOTNULL FK: 210 distinct, 1..230, 32=228, 33=207, 1=200, 34=95, 99=90, 128=88, 39=79, 46=74, 41=60, 31=54

indexes: `group_id`, `instance_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-05-06T17:00:37 | 2021-01-25T21:04:33 | 2021-01-25T21:04:34 |
| updated_at | null | null | null |
| deleted_at | null | 2021-05-01T20:47:26 | 2021-05-01T20:47:13 |
| deleted | 0 | 3235 | 3236 |
| id | 4169 | 3235 | 3236 |
| instance_id | fe849f1d-bfa7-4b76-95fb-37e5b83920cf | 56f780bc-3e78-4ad5-b7d7-828c33308f85 | 7e0ef99b-c025-4219-82a1-c3271513d35c |
| group_id | 216 | 129 | 129 |

# `instance_group_policy`  (rows=228)

columns:
`created_at` datetime: 151 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 159 distinct, nulls=28
`deleted` int: 201 distinct, 0..230, avg=103.7368, median=106.5
`id` int PK: unique identifier, 1..230
`policy` varchar255: "anti-affinity"=225, "affinity"=3
`group_id` int NOTNULL FK: unique identifier, 1..230

indexes: `group_id`, `policy`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2023-10-01T15:36:55 | 2020-04-11T17:18:48 | 2020-04-11T17:18:49 |
| updated_at | null | null | null |
| deleted_at | 2024-01-20T18:06:45 | 2020-05-30T03:49:02 | 2020-05-30T03:49:02 |
| deleted | 230 | 125 | 126 |
| id | 230 | 125 | 126 |
| policy | anti-affinity | anti-affinity | anti-affinity |
| group_id | 230 | 125 | 126 |

# `instance_groups`  (rows=230)

columns:
`created_at` datetime: 154 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 161 distinct, nulls=28
`deleted` int: 203 distinct, 0..230, avg=102.9348, median=105.5, 0=28, 1=1, 2=1, 3=1, 4=1, 11=1, 12=1, 13=1, 14=1, 15=1
`id` int PK: unique identifier, 1..230
`user_id` varchar255: "a1ef823458d24a68955fec6f3d390019"=187, "77047e1a20db46b2b8d8daebb9e39fe8"=25, "5302e30e168c4db283fc8e07009bb98f"=8, "c0a5d12d08874376a517eca2db78c3ca"=6, "7632ba71167341ff9697e116553c90f3"=2, "0be8fa0d641a4e778b9262bd2e5f40b5"=1, "ed22eaa324ea4dff812c57a199d3abd4"=1
`project_id` varchar255: "17ea94ad74b64b9d92f4888336a598c7"=140, "98333a1a28e746fa8c629c83a818ad57"=48, "5b92ec1146d04f9091ab48b6cdba3eff"=25, "d7abb5f8e61a48e1a411b07aa2aeb152"=6, "47c0857cf5b5452a86f640fd44be1d40"=5, "bfd50153a2e9476f93e33e30e922cd06"=4, "09ad05432f914e26bc417bf58f1cb4d2"=2
`uuid` varchar36 NOTNULL: uuid, unique identifier
`name` varchar255: 36 distinct

indexes: UNIQUE (`uuid`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2023-10-01T15:36:55 | 2023-06-16T23:17:40 | 2023-06-17T19:04:29 |
| updated_at | null | null | null |
| deleted_at | 2024-01-20T18:06:45 | 2023-06-16T23:39:53 | 2023-06-17T23:12:16 |
| deleted | 230 | 199 | 200 |
| id | 230 | 199 | 200 |
| user_id | 77047e1a20db46b2b8d8daebb9e39fe8 | 77047e1a20db46b2b8d8daebb9e39fe8 | 77047e1a20db46b2b8d8daebb9e39fe8 |
| project_id | 5b92ec1146d04f9091ab48b6cdba3eff | 5b92ec1146d04f9091ab48b6cdba3eff | 5b92ec1146d04f9091ab48b6cdba3eff |
| uuid | 6857e997-f7b1-437c-b63b-2b93227f454d | 9e14e1d7-bee5-4ce0-8551-5db1757e18cb | 8967d2e5-6329-4ee5-9935-dcaaa712f6df |
| name | alpha4-glyph | alpha4-glyph | alpha4-glyph |

# `instance_id_mappings`  (rows=277653)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: all NULL
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 446931..749369
`uuid` varchar36 NOTNULL: uuid, unique identifier
`deleted` int: 0..0, avg=0

indexes: `uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2015-04-17T01:25:44 | 2015-04-17T01:25:45 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 749369 | 614704 | 614705 |
| uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | 4acc1573-6476-4b74-a41a-0de3d5e13267 | 895a2d20-857b-4f3a-948c-de23ae491510 |
| deleted | 0 | 0 | 0 |

# `instance_info_caches`  (rows=7226)

columns:
`created_at` datetime: 6340 distinct
`updated_at` datetime: 6142 distinct, nulls=321
`deleted_at` datetime: 5021 distinct, nulls=1485
`id` int PK: unique identifier, 509070..749459
`network_info` text: 1501 distinct
`instance_uuid` varchar36 UNIQ NOTNULL FK: uuid, unique identifier
`deleted` int: 5742 distinct, 0..749457, avg=588578.269, median=744200

indexes: UNIQUE `instance_uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2016-01-11T21:55:46 | 2016-01-12T20:53:18 |
| updated_at | 2024-07-08T06:17:59 | 2020-02-03T16:00:45 | 2023-06-20T16:56:07 |
| deleted_at | null | 2020-02-03T16:00:49 | 2023-06-20T16:56:08 |
| id | 749459 | 684706 | 688704 |
| network_info | [{"profile": {}, "ovs_interfaceid": "0639c4ce-dc51-4d07-baa5-109c5db4a609", "preserve_on_delete": false, "network": {"bridge": "br-int", "subnets": [{"ips": [{"meta": {}, "version": 4, "type": "fixed… | [] | [] |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | 3ec0f293-879d-456b-89f9-c6a418a33c1f | b2aaddc9-ea16-48c8-8bd7-3ab0a837f436 |
| deleted | 0 | 684706 | 688704 |

# `instance_metadata`  (rows=36)

columns:
`created_at` datetime: 35 distinct
`updated_at` datetime: 2022-10-21 13:55:20=1, nulls=35
`deleted_at` datetime: 29 distinct, nulls=5
`id` int PK: unique identifier, 538..573
`key` varchar255: "csail"=22, "hostname"=5, "sweep"=3, "image_version"=1, "release"=1, "RT"=1, "system"=1, "system_role"=1, "verified"=1
`value` varchar255: "true"=22, "1"=2, "testy-mcansibleface-1"=2, "testy-mcansibleface-2"=2, "0"=1, "191716"=1, "2024-03-26"=1, "bionic"=1, "bionic_cloudimg"=1, "igorprod"=1, "igorprod_master"=1, "testy-mcansibleface-3"=1
`instance_uuid` varchar36 FK: uuid, 34 distinct
`deleted` int: 32 distinct, 0..572, avg=479.5, median=554.5

indexes: `instance_uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2023-03-27T18:46:52 | 2023-03-27T19:07:38 |
| updated_at | null | null | null |
| deleted_at | null | 2023-04-18T16:34:16 | 2023-04-18T16:34:17 |
| id | 573 | 549 | 550 |
| key | csail | hostname | hostname |
| value | true | testy-mcansibleface-2 | testy-mcansibleface-3 |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | be0d62b5-bdc4-47b4-9e67-3189e5ddecdd | 4a6031cc-7b44-4e64-bd2a-09970e4715dc |
| deleted | 0 | 549 | 550 |

# `instance_system_metadata`  (rows=76723)

columns:
`created_at` datetime: 13321 distinct
`updated_at` datetime: 1424 distinct, nulls=75102
`deleted_at` datetime: 4997 distinct, nulls=17997
`id` int PK: unique identifier, 8417981..12281805
`instance_uuid` varchar36 NOTNULL FK: uuid, 7226 distinct, "7aa0b283-fb49-4cc1-85aa-69e9c23bea62"=34, "f84c1ec8-cc70-49da-9955-88fbc44b1990"=30, "7711aa9b-492f-4620-8414-c5fc09c1f3fa"=29, "2be350ed-edab-4734-b721-7dd36ee03286"=28, "51e32669-00b1-4d79-a93b-05a92b2fa747"=28, "af938383-e6ff-4444-9f3b-3f6bcb118840"=28, "bd67d93a-c153-41b3-9ec9-64c8082fc8ed"=28, "f3d0b8e7-5867-4c4a-bdc0-c7eab1a1e713"=28, "047088e3-7e80-4e23-b33c-65ff168b35b9"=27, "0d1fe166-36ea-4f5d-926f-b8aa385e353f"=27
`key` varchar255 NOTNULL: 60 distinct
`value` varchar255: 2598 distinct, nulls=2562
`deleted` int: 58727 distinct, 0..12281803, avg=9327251.1266, median=12223005

indexes: `instance_uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2015-03-15T04:52:21 | 2015-03-15T04:52:21 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 12281805 | 9475851 | 9475852 |
| instance_uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | af938383-e6ff-4444-9f3b-3f6bcb118840 | af938383-e6ff-4444-9f3b-3f6bcb118840 |
| key | image_base_image_ref | image_instance_type_root_gb | image_clean_attempts |
| value | null | axiom-lumen | comet-star-gamma |
| deleted | 0 | 0 | 0 |

# `instance_type_extra_specs`  (rows=135)

columns:
`created_at` datetime: 129 distinct
`updated_at` datetime: 2017-08-04 14:40:14=1, 2017-08-04 14:40:18=1, 2017-08-04 14:40:21=1, 2017-08-04 15:29:32=1, 2017-11-16 21:42:11=1, 2018-01-08 21:23:06=1, 2018-04-26 19:51:27=1, 2018-04-27 17:39:18=1, 2018-09-25 03:22:22=1, 2023-02-23 17:06:21=1, nulls=125
`deleted_at` datetime: 29 distinct, nulls=104
`id` int PK: unique identifier, 29..188
`instance_type_id` int NOTNULL FK: 104 distinct, 51..196, 192=6, 57=5, 172=5, 171=4, 173=4, 84=3, 175=3, 78=2, 79=2, 80=2
`key` varchar255: "overcommit"=50, "generation"=22, "ups"=11, "tig"=10, "switch"=8, "test"=7, "hw:cpu_sockets"=4, "hw:numa_nodes"=4, "pci_passthrough:alias"=4, "hw:cpu_cores"=3, "hw:cpu_policy"=3, "is_public"=2, "pci_passthrough"=2, "RT"=1, "hi_mem_use"=1, "hw:mem_page_size"=1, "os-flavor-access:is_public"=1, "titan_xp"=1
`value` varchar255: 22 distinct
`deleted` int: 32 distinct, 0..184, avg=24.1037, median=0, 0=104, 30=1, 31=1, 33=1, 34=1, 36=1, 57=1, 58=1, 59=1, 60=1

indexes: (`instance_type_id`,`key`), UNIQUE (`instance_type_id`,`key`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-02-23T14:18:22 | 2014-02-14T19:18:54 | 2014-02-14T19:41:29 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 188 | 74 | 75 |
| instance_type_id | 196 | 104 | 105 |
| key | generation | test | test |
| value | 5 | true | true |
| deleted | 0 | 0 | 0 |

# `instance_type_projects`  (rows=232)

columns:
`created_at` datetime: 194 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 61 distinct, nulls=140
`id` int PK: unique identifier, 1..352
`instance_type_id` int NOTNULL FK: 71 distinct, 9..196, 154=19, 155=12, 111=9, 125=8, 53=7, 51=6, 52=6, 55=6, 56=6, 139=6
`project_id` varchar255: 39 distinct, "98333a1a28e746fa8c629c83a818ad57"=44, "6f9adccbd03e4d2186756896957a14bf"=32, "7691c9955ce1444ab366d041f5bdf33c"=26, "17ea94ad74b64b9d92f4888336a598c7"=18, "09ad05432f914e26bc417bf58f1cb4d2"=13, "717cc16840494e8795e2ee25c46fe797"=9, "0dc175871e05482b9aff22616534c199"=8, "47c0857cf5b5452a86f640fd44be1d40"=8, "292c70904ce7415c8626f801bbf1ed0c"=7, "3c0c9fa6bb85454784416297a250be7a"=7
`deleted` int: 93 distinct, 0..337, avg=76.9828, median=0, 0=140, 3=1, 4=1, 5=1, 8=1, 10=1, 11=1, 12=1, 15=1, 19=1

indexes: `instance_type_id`, UNIQUE (`instance_type_id`,`project_id`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-02-23T14:18:22 | 2015-08-17T18:41:58 | 2015-08-17T18:41:58 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 352 | 198 | 199 |
| instance_type_id | 196 | 150 | 150 |
| project_id | ccf2065a88074df09526d5dd5c361845 | 7691c9955ce1444ab366d041f5bdf33c | 98333a1a28e746fa8c629c83a818ad57 |
| deleted | 0 | 0 | 0 |

# `instance_types`  (rows=190)

columns:
`created_at` datetime: 172 distinct, nulls=5
`updated_at` datetime: all distinct, nulls=137
`deleted_at` datetime: 64 distinct, nulls=92
`name` varchar255: 120 distinct, "spire.xenon_drive"=4, "zenta.3glint"=4, "alpha.aurum"=3, "blaze.5align"=3, "flare.0omega"=3, "flash.4flick"=3, "flash.layer"=3, "glyph.spind"=3, "shine.cubic_shift"=3, "solar.flux"=3
`id` int PK: unique identifier, 1..196
`memory_mb` int NOTNULL: 30 distinct, 1..98304, avg=17287.6947, median=8192
`vcpus` int NOTNULL: 2=45, 1=33, 4=27, 8=21, 16=20, 24=16, 12=15, 32=5, 88=5, 44=2, 64=1, 1..88
`swap` int NOTNULL: 0=167, 4=14, 2048=4, 1024=3, 4096=1, 16384=1, 0..16384
`vcpu_weight` int: all NULL
`flavorid` varchar255: 176 distinct, "901"=5, "6"=3, "bd48d209-4cdf-4fdd-a950-ea1b6adcb567"=3, "d00fa5cf-8cf9-45f3-aebe-f71c942ed3c1"=3, "000001"=2, "9"=2, "9016"=2, "f4ce6c9e-f6e0-4edd-b83e-8269b5351c6b"=2, "000000"=1, "00bf3c77-473e-4844-ae0b-f76164bf9667"=1
`rxtx_factor` float: 1=190
`root_gb` int: 32=88, 16=49, 10=23, 64=18, 0=10, 40=1, 100=1, 0..100
`ephemeral_gb` int: 0=173, 160=5, 80=3, 8=2, 360=2, 16=1, 20=1, 40=1, 64=1, 200=1, 0..360
`disabled` int: 0=190
`is_public` int: 1=104, 0=86
`deleted` int: 99 distinct, 0..189, avg=37.2895, median=3.5, 0=92, 1=1, 2=1, 3=1, 4=1, 5=1, 6=1, 7=1, 8=1, 9=1

indexes: UNIQUE (`flavorid`,`deleted`), UNIQUE (`name`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-02-23T14:18:22 | null | null |
| updated_at | null | null | null |
| deleted_at | null | 2013-08-08T17:48:04 | 2013-08-08T17:48:04 |
| name | axiom.0mover | light.comet_spark | vortx.warp_quark |
| id | 196 | 4 | 5 |
| memory_mb | 90112 | 16384 | 2048 |
| vcpus | 88 | 8 | 1 |
| swap | 0 | 0 | 0 |
| vcpu_weight | null | null | null |
| flavorid | d20eaff8-d13b-44de-a65f-2cbe9a42ff8c | 5 | 2 |
| rxtx_factor | 1 | 1 | 1 |
| root_gb | 32 | 10 | 10 |
| ephemeral_gb | 0 | 160 | 20 |
| disabled | 0 | 0 | 0 |
| is_public | 0 | 1 | 1 |
| deleted | 0 | 4 | 5 |

# `instances`  (rows=7922)

columns:
`created_at` datetime: 6987 distinct, 2021-06-14 15:21:46=6, 2021-05-07 13:18:46=5, 2021-06-08 12:56:09=5, 2021-06-15 11:52:31=5, 2016-03-02 01:12:05=4, 2020-02-10 16:47:43=4, 2020-06-15 15:56:47=4, 2021-05-18 14:03:57=4, 2021-05-18 14:38:48=4, 2021-11-15 20:21:55=4
`updated_at` datetime: 7036 distinct, nulls=8, 2020-01-29 20:32:20=6, 2021-10-06 02:13:03=6, 2022-08-10 20:52:49=6, 2024-05-31 13:19:02=6, 2019-07-17 10:42:53=5, 2020-01-29 20:32:03=5, 2020-01-29 20:32:07=5, 2020-02-02 14:44:46=5, 2020-02-10 16:40:42=5, 2020-02-19 17:08:03=5
`deleted_at` datetime: 5580 distinct, nulls=1485
`id` int PK: unique identifier, 509070..749387
`internal_id` int: all NULL
`user_id` varchar255: 560 distinct
`project_id` varchar255: 479 distinct, "98333a1a28e746fa8c629c83a818ad57"=1593, "34c8d5cd44cc4b179c27892ec7596364"=514, "dba6cc0fec6845a58f4dd5e84ef8dca5"=397, "3008a142e9524f7295b06ea811908f93"=319, "c6d36b416dac49f193b4a209546ce370"=250, "5b92ec1146d04f9091ab48b6cdba3eff"=229, "daa18fdafdf04b5eac18e04aa19ee214"=229, "e3fb2659584e436a832461dac02835f0"=229, "6f5103a9ae434375a92a1de24a19ca56"=148, "bfe6b439cb834e79a3d8adbf23b5a92d"=127
`image_ref` varchar255: uuid, 672 distinct, nulls=1670
`kernel_id` varchar255: all NULL
`ramdisk_id` varchar255: all NULL
`launch_index` int: 97 distinct, 0..96, avg=1.7492, median=0
`key_name` varchar255: 854 distinct, nulls=2083
`key_data` text: 1082 distinct, nulls=2087
`power_state` int: 0=6106, 4=1081, 1=731, 3=4, 0..4
`vm_state` varchar255: "deleted"=5899, "active"=722, "shelved_offloaded"=674, "error"=483, "stopped"=92, "building"=47, "suspended"=4, "paused"=1
`memory_mb` int: 1024=1369, 2048=1292, 8192=1291, 16384=962, 4096=874, 512=741, 32768=325, 98304=298, 49152=230, 65536=188, 6144=133, 24576=129, 12288=72, 90112=7, 15360=4, 32=3, 45056=3, 30720=1, 32..98304
`vcpus` int: 2=2150, 1=1814, 4=1554, 8=1124, 24=576, 16=352, 12=284, 32=52, 88=9, 64=4, 44=3, 1..88
`hostname` varchar255: 3000 distinct
`host` varchar255: 43 distinct, ""=1416, "blaze8-12"=355, "ether-18"=349, "shine-94"=336, "flare4-57"=316, "align-86"=308, "flux-60"=290, "blitz1-32"=289, "forge-23"=287, "prime3-77"=277
`user_data` text: all distinct
`reservation_id` varchar255: 6793 distinct, "r-g3ha1q02"=97, "r-6ie9f5mn"=80, "r-y3hq11fm"=40, "r-bxc7dex6"=26, "r-80i9irgf"=25, "r-t8v9wyrj"=22, "r-6a4ozutv"=21, "r-b2cpy92b"=21, "r-cleywtkz"=21, "r-ix13jf0z"=21
`scheduled_at` datetime: 49 distinct, nulls=7872
`launched_at` datetime: 6982 distinct, nulls=486, 2022-08-04 15:36:07=11, 2022-08-10 20:54:51=8, 2022-08-10 20:59:08=8, 2020-02-10 19:21:48=7, 2022-10-04 13:22:46=7, 2020-02-10 19:21:25=6, 2022-08-04 11:58:54=6, 2022-08-10 21:17:50=6, 2020-02-10 19:30:34=5, 2020-02-10 19:31:14=5
`terminated_at` datetime: 5327 distinct, nulls=1963, 2024-05-31 13:18:18=6, 2019-07-17 10:42:53=5, 2020-01-29 20:32:03=5, 2020-02-10 16:40:42=5, 2020-03-16 23:54:26=5, 2020-06-25 19:56:24=5, 2022-08-04 15:26:52=5, 2019-05-28 13:52:09=4, 2019-05-28 14:18:03=4, 2019-05-28 15:29:34=4
`display_name` varchar255: 2913 distinct
`display_description` varchar255: 2361 distinct, nulls=286
`availability_zone` varchar255: "flare3"=5218, "dash_plasm"=1, nulls=2703
`locked` int: 0=7916, 1=6
`os_type` varchar255: all NULL
`launched_on` text: 126 distinct, nulls=145
`instance_type_id` int: 70 distinct, 56..196
`vm_mode` varchar255: all NULL
`uuid` varchar36 UNIQ NOTNULL: uuid, unique identifier
`architecture` varchar255: "amd64"=20, "x86_64"=16, nulls=7886
`root_device_name` varchar255: "/dev/vda"=7749, "/dev/hda"=12, "/dev/sda"=1, nulls=160
`access_ip_v4` varchar39: all NULL
`access_ip_v6` varchar39: all NULL
`config_drive` varchar255: "True"=54, nulls=7868
`task_state` varchar255: "deleting"=470, "scheduling"=8, "shelving"=7, "image_snapshot_pending"=1, nulls=7436
`default_ephemeral_device` varchar255: "/dev/vdb"=2, nulls=7920
`default_swap_device` varchar255: "/dev/vdb"=62, "/dev/vdc"=15, nulls=7845
`progress` int: 0=7922
`auto_disk_config` int: 0=7507, 1=415
`shutdown_terminate` int: 0=7922
`disable_terminate` int: 0=7922
`root_gb` int: 32=2403, 16=2292, 64=1616, 10=1586, 0=25, 0..64
`ephemeral_gb` int: 0=7812, 64=49, 8=46, 16=15, 0..64
`cell_name` varchar255: all NULL
`node` varchar255: 42 distinct, nulls=1416, "blaze8-12.yahoo.ca.com"=355, "ether-18.yahoo.ca.com"=349, "shine-94.yahoo.ca.com"=336, "flare4-57.yahoo.ca.com"=316, "align-86.yahoo.ca.com"=308, "flux-60.yahoo.ca.com"=290, "blitz1-32.yahoo.ca.com"=289, "forge-23.yahoo.ca.com"=287, "prime3-77.yahoo.ca.com"=277, "prime5-78.yahoo.ca.com"=271
`deleted` int: 6438 distinct, 0..749385, avg=601978.0746, median=743604.5, 0=1485, 512376=1, 529835=1, 530624=1, 530679=1, 530923=1, 586957=1, 586976=1, 589919=1, 589939=1
`locked_by` enum: "owner"=6, nulls=7916
`cleaned` int: 1=7098, 0=824
`ephemeral_key_uuid` varchar36: all NULL

indexes: (`deleted`,`created_at`), (`host`,`deleted`,`cleaned`), (`host`,`node`,`deleted`), (`project_id`,`deleted`), `reservation_id`, (`task_state`,`updated_at`), (`terminated_at`,`launched_at`), (`uuid`,`deleted`), UNIQUE `uuid`, UNIQUE `uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2015-11-30T18:07:56 | 2015-11-30T18:20:40 |
| updated_at | 2024-06-26T20:40:27 | 2023-01-30T21:37:19 | 2022-01-07T03:21:28 |
| deleted_at | null | 2023-01-30T21:37:19 | 2022-01-07T03:21:28 |
| id | 749387 | 654620 | 654624 |
| internal_id | null | null | null |
| user_id | 64f64393530d486da6d548710ca2990c | 191e0364cec940478bd34b390c090475 | 4e4f5c1f38554dd6b3f750ee6b9ca9d2 |
| project_id | b3c6072810a24f67a7ac48e49a960e51 | 967bfd447eba40c78fd293143c77b6b1 | e3fb2659584e436a832461dac02835f0 |
| image_ref | null | 91dac2d5-1d0c-4b68-8182-e122e1050d55 | cb0375e6-d4b8-481f-8cf8-17898a67b1f3 |
| kernel_id | null | null | null |
| ramdisk_id | null | null | null |
| launch_index | 0 | 0 | 0 |
| key_name | null | star | null |
| key_data | null | 4578dcff6d4a0cee82e35668fe7c897b | null |
| power_state | 1 | 4 | 0 |
| vm_state | active | deleted | deleted |
| memory_mb | 4096 | 4096 | 8192 |
| vcpus | 2 | 8 | 4 |
| hostname | lumen-comet-axis | galax-zeph | grav-astro |
| host | cosmo3-23 |  | spark-75 |
| user_data | replaced_user_data.749387 | replaced_user_data.654620 | replaced_user_data.654624 |
| reservation_id | r-as21013g | r-gfvilgoz | r-hseeosjb |
| scheduled_at | null | null | null |
| launched_at | 2024-06-26T20:40:24 | 2015-12-02T15:52:39 | 2018-12-26T18:26:36 |
| terminated_at | null | 2023-01-30T21:37:19 | 2022-01-07T03:21:36 |
| display_name | lumen-comet-axis | beam-delta | grav-astro |
| display_description | lumen-comet-axis | beam-delta | grav-astro |
| availability_zone | null | flare3 | null |
| locked | 0 | 0 | 0 |
| os_type | null | null | null |
| launched_on | cosmo3-23 | shine2-89 | celes-18 |
| instance_type_id | 72 | 60 | 135 |
| vm_mode | null | null | null |
| uuid | 88ae78e8-3331-40bc-b294-95d446a1dfab | cdb05996-ce74-4947-ae98-dda92f600e5a | 4265edc5-99aa-4a4d-8bdb-4fe302855fb6 |
| architecture | null | null | null |
| root_device_name | /dev/vda | /dev/vda | /dev/vda |
| access_ip_v4 | null | null | null |
| access_ip_v6 | null | null | null |
| config_drive | null | null | True |
| task_state | null | null | null |
| default_ephemeral_device | null | null | null |
| default_swap_device | null | null | null |
| progress | 0 | 0 | 0 |
| auto_disk_config | 0 | 1 | 0 |
| shutdown_terminate | 0 | 0 | 0 |
| disable_terminate | 0 | 0 | 0 |
| root_gb | 32 | 10 | 16 |
| ephemeral_gb | 0 | 0 | 0 |
| cell_name | null | null | null |
| node | cosmo3-23.yahoo.ca.com | null | spark-75.yahoo.ca.com |
| deleted | 0 | 654620 | 654624 |
| locked_by | null | null | null |
| cleaned | 0 | 1 | 1 |
| ephemeral_key_uuid | null | null | null |

# `key_pairs`  (rows=3132)

columns:
`created_at` datetime: 2953 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 1507 distinct, nulls=1423
`id` int PK: unique identifier, 1..3391
`name` varchar255 NOTNULL: all distinct
`user_id` varchar255: 764 distinct, "8dff92c968c94d8093e087d13565c1b1"=235, "a1ef823458d24a68955fec6f3d390019"=165, "526d71f9d9994362b701ecff70daa258"=162, "b39f00e75fd84e0d8c870222f9066dff"=144, "e34af343637941dc8603f36f279ba30c"=69, "0b2717d52e56454298168c59e6b006b7"=49, "77047e1a20db46b2b8d8daebb9e39fe8"=44, "5302e30e168c4db283fc8e07009bb98f"=26, "81d81f7f17834951a1dc5ee8aa8b4e49"=25, "540e6feab1bf4c4bafad1bb59daf3c31"=24
`fingerprint` varchar255: 2809 distinct
`public_key` text: all distinct
`deleted` int: 1710 distinct, 0..3386, avg=967.3024, median=525, 0=1423, 22=1, 23=1, 34=1, 46=1, 50=1, 51=1, 101=1, 118=1, 141=1
`type` enum NOTNULL: "ssh"=3132

indexes: UNIQUE (`user_id`,`name`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-24T16:09:39 | 2018-05-09T17:36:44 | 2018-05-16T03:56:12 |
| updated_at | null | null | null |
| deleted_at | null | 2018-05-09T18:33:00 | 2018-05-16T03:56:36 |
| id | 3391 | 2147 | 2148 |
| name | plasm_helio.433cosmo | beam_spike.681netix | quark_lyric.322celes |
| user_id | 7a6e4676819c4cd2bce6ae812f0fc6e9 | 1de0d5702f1d49bfb9242dfb9572a207 | c34278f44087498fbc5fc662c63e491e |
| fingerprint | 63:f0:c8:48:3e:eb:d6:32:e6:f9:04:8c:a4:83:a5:e8 | d2:12:49:e8:9f:48:f5:69:77:fa:b5:a3:25:e7:9b:0a | 9d:93:c6:b6:1f:f9:54:09:7d:1e:d8:4e:26:ea:1a:06 |
| public_key | xenon_twist.315alpha | flare_spire.366vortex | helix_speed.18pivot |
| deleted | 0 | 2147 | 2148 |
| type | ssh | ssh | ssh |

# `migrate_version`  (rows=1)

columns:
`repository_id` varchar250 PK
`repository_path` text
`version` int

indexes: none

all rows:
| column | row 1 |
|---|---|
| repository_id | nova |
| repository_path | /usr/lib/python2.7/dist-packages/nova/db/sqlalchemy/migrate_repo |
| version | 319 |

# `networks`  (rows=1)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`id` int PK
`injected` int
`cidr` varchar43
`netmask` varchar39
`bridge` varchar255
`gateway` varchar39
`broadcast` varchar39
`dns1` varchar39
`vlan` int
`vpn_public_address` varchar39
`vpn_public_port` int
`vpn_private_address` varchar39
`dhcp_start` varchar39
`project_id` varchar255
`host` varchar255
`cidr_v6` varchar43
`gateway_v6` varchar39
`label` varchar255
`netmask_v6` varchar39
`bridge_interface` varchar255
`multi_host` int
`dns2` varchar39
`uuid` varchar36
`priority` int
`rxtx_base` int
`deleted` int
`mtu` int
`dhcp_server` varchar39
`enable_dhcp` int
`share_address` int

indexes: (`bridge`,`deleted`), `cidr_v6`, `host`, (`project_id`,`deleted`), (`uuid`,`project_id`,`deleted`), (`vlan`,`deleted`), UNIQUE (`vlan`,`deleted`)

all rows:
| column | row 1 |
|---|---|
| created_at | 2012-09-07T13:52:06 |
| updated_at | 2013-08-09T21:26:49 |
| deleted_at | null |
| id | 1 |
| injected | 0 |
| cidr | 10.116.184.94/8 |
| netmask | 255.255.0.0 |
| bridge | br100 |
| gateway | 10.0.0.1 |
| broadcast | 10.0.255.255 |
| dns1 | 128.30.2.23 |
| vlan | null |
| vpn_public_address | 10.36.62.183/8 |
| vpn_public_port | null |
| vpn_private_address | null |
| dhcp_start | 10.0.0.2 |
| project_id | null |
| host | neon-63 |
| cidr_v6 | null |
| gateway_v6 | null |
| label | private |
| netmask_v6 | null |
| bridge_interface | eth1 |
| multi_host | 1 |
| dns2 | 128.30.2.24 |
| uuid | 8d825f56-4836-43df-ae85-e5f376325441 |
| priority | null |
| rxtx_base | null |
| deleted | 0 |
| mtu | null |
| dhcp_server | null |
| enable_dhcp | 1 |
| share_address | 0 |

# `pci_devices`  (rows=16)

columns:
`created_at` datetime: 2016-10-18 18:01:35=6, 2019-01-09 18:22:21=4, 2019-01-09 18:22:22=4, 2016-10-18 18:01:36=2
`updated_at` datetime: 2019-01-09 17:51:11=4, 2019-01-09 17:51:12=4, nulls=8
`deleted_at` datetime: all NULL
`deleted` int: 0=16
`id` int PK: unique identifier, 9..24
`compute_node_id` int NOTNULL FK: 90=8, 149=8
`address` varchar12 NOTNULL: "0000:04:56.0"=2, "0000:06:33.0"=2, "0000:43:32.0"=2, "0000:54:12.0"=2, "0000:64:31.0"=2, "0000:75:06.0"=2, "0000:83:59.0"=2, "0000:93:95.0"=2
`product_id` varchar4 NOTNULL: "102d"=16
`vendor_id` varchar4 NOTNULL: "10de"=16
`dev_type` varchar8 NOTNULL: "type-PCI"=16
`dev_id` varchar255: "pci_0000_04_00_0"=2, "pci_0000_05_00_0"=2, "pci_0000_08_00_0"=2, "pci_0000_09_00_0"=2, "pci_0000_83_00_0"=2, "pci_0000_84_00_0"=2, "pci_0000_87_00_0"=2, "pci_0000_88_00_0"=2
`label` varchar255 NOTNULL: "label_10de_102d"=16
`status` varchar36 NOTNULL: "available"=16
`extra_info` text: "{}"=16
`instance_uuid` varchar36: all NULL
`request_id` varchar36: all NULL
`numa_node` int: 0=8, 1=8
`parent_addr` varchar12: all NULL

indexes: (`compute_node_id`,`deleted`), (`compute_node_id`,`parent_addr`,`deleted`), (`instance_uuid`,`deleted`), UNIQUE (`compute_node_id`,`address`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-01-09T18:22:22 | 2016-10-18T18:01:35 | 2016-10-18T18:01:35 |
| updated_at | null | 2019-01-09T17:51:12 | 2019-01-09T17:51:12 |
| deleted_at | null | null | null |
| deleted | 0 | 0 | 0 |
| id | 24 | 13 | 14 |
| compute_node_id | 149 | 90 | 90 |
| address | 0000:43:32.0 | 0000:04:56.0 | 0000:93:95.0 |
| product_id | 102d | 102d | 102d |
| vendor_id | 10de | 10de | 10de |
| dev_type | type-PCI | type-PCI | type-PCI |
| dev_id | pci_0000_88_00_0 | pci_0000_83_00_0 | pci_0000_84_00_0 |
| label | label_10de_102d | label_10de_102d | label_10de_102d |
| status | available | available | available |
| extra_info | {} | {} | {} |
| instance_uuid | null | null | null |
| request_id | null | null | null |
| numa_node | 1 | 1 | 1 |
| parent_addr | null | null | null |

# `quota_classes`  (rows=13)

columns:
`created_at` datetime: 2017-07-07 15:19:43=4, 2013-09-23 01:46:15=3, 2015-02-13 15:48:10=3, 2015-02-13 15:49:46=3
`updated_at` datetime: 2015-03-23 14:32:09=3, nulls=10
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 1..13
`class_name` varchar255: "default"=7, "personal"=3, "usersandbox"=3
`resource` varchar255: "cores"=3, "instances"=3, "ram"=3, "security_groups"=1, "security_group_rules"=1, "server_groups"=1, "server_group_members"=1
`hard_limit` int: 8=4, 32=3, 64=3, 8192=2, 131072=1, 8..131072
`deleted` int: 0=13

indexes: `class_name`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2017-07-07T15:19:43 | 2017-07-07T15:19:43 | 2017-07-07T15:19:43 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 13 | 11 | 12 |
| class_name | default | default | default |
| resource | server_group_members | security_groups | security_group_rules |
| hard_limit | 32 | 64 | 32 |
| deleted | 0 | 0 | 0 |

# `quota_usages`  (rows=3619)

columns:
`created_at` datetime: 1155 distinct
`updated_at` datetime: 1554 distinct
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 7..3852
`project_id` varchar255: 559 distinct, nulls=2, "3008a142e9524f7295b06ea811908f93"=365, "98333a1a28e746fa8c629c83a818ad57"=57, "70b2507b8cc44fcb917ddfb85f5079d9"=50, "190ad02e1faa494a8ab7153c6d2e56c1"=49, "97107d3284a848a4a4ea0345bd05cbef"=45, "09ad05432f914e26bc417bf58f1cb4d2"=41, "daa18fdafdf04b5eac18e04aa19ee214"=40, "dba6cc0fec6845a58f4dd5e84ef8dca5"=32, "d7d16dd7c387425b80c001832884b6de"=30, "47c0857cf5b5452a86f640fd44be1d40"=29
`resource` varchar255 NOTNULL: "cores"=1022, "instances"=1022, "ram"=1022, "security_groups"=494, "floating_ips"=26, "fixed_ips"=18, "server_groups"=11, "gigabytes"=2, "volumes"=2
`in_use` int NOTNULL: 174 distinct, -512..1081344, avg=5862.5742, median=1
`reserved` int NOTNULL: 0=3605, -2048=3, 2048=3, -2=2, 2=2, -35328=1, -15=1, -1=1, 1=1, -35328..2048
`until_refresh` int: 0=330, nulls=3289
`deleted` int: 0=3619
`user_id` varchar255: 739 distinct, nulls=48, "a1ef823458d24a68955fec6f3d390019"=101, "0be8fa0d641a4e778b9262bd2e5f40b5"=61, "ce3ea89d3bf34882b2666853f1474575"=50, "e1b9fa1bb2f44cc88f8a6fa63dc389a9"=28, "ed22eaa324ea4dff812c57a199d3abd4"=24, "016a57c3112643b9be2a295e9d9c6e90"=23, "36783874ab9946a18ee493f64443b2dc"=21, "5302e30e168c4db283fc8e07009bb98f"=20, "5c467be0707545338c91fc00d5a9914c"=17, "07d3187f379a4fe6a556c63c6131b2ac"=16

indexes: `project_id`, (`user_id`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-18T15:09:07 | 2014-01-18T15:57:48 | 2014-01-18T17:03:29 |
| updated_at | 2024-06-18T15:09:07 | 2015-10-30T15:52:26 | 2014-02-07T16:36:56 |
| deleted_at | null | null | null |
| id | 3852 | 212 | 213 |
| project_id | 5e35676c2c6947f29e1402b31c5b87a7 | 3008a142e9524f7295b06ea811908f93 | fb790702ec7d4fcb96ec14d0daa575f8 |
| resource | cores | cores | instances |
| in_use | 2 | 0 | 0 |
| reserved | 0 | 0 | 0 |
| until_refresh | null | null | null |
| deleted | 0 | 0 | 0 |
| user_id | 3a1ff089c33740358d0ce80cc5f801f9 | 59a5934524c54089af8f35bed2ea7eaa | 5cdf075359cf48a582b0b2c41b4957ca |

# `quotas`  (rows=3579)

columns:
`id` int PK: unique identifier, 1..6259
`created_at` datetime: 1078 distinct
`updated_at` datetime: 254 distinct, nulls=2581
`deleted_at` datetime: all NULL
`project_id` varchar255: 941 distinct, "98333a1a28e746fa8c629c83a818ad57"=12, "17ea94ad74b64b9d92f4888336a598c7"=10, "9e2200862b674b3098afc897b0fbb977"=10, "02c3a636066b45faa84760bbaa76d8a8"=9, "0d16687ae70645678cbe037065831a32"=9, "292c70904ce7415c8626f801bbf1ed0c"=9, "2a9b495932c64d80b1fac28d1416a921"=9, "3008a142e9524f7295b06ea811908f93"=9, "347e25c219354db38c6662e4ab9a9c84"=9, "34f87362758043a98ea19c5a5e9217c9"=9
`resource` varchar255 NOTNULL: "cores"=940, "ram"=940, "instances"=937, "injected_files"=225, "injected_file_content_bytes"=225, "metadata_items"=225, "floating_ips"=25, "gigabytes"=23, "volumes"=23, "fixed_ips"=7, "security_groups"=3, "server_group_members"=3, "server_groups"=2, "security_group_rules"=1
`hard_limit` int: 91 distinct, -1..50331648, avg=44392.4647, median=16
`deleted` int: 0=3579

indexes: UNIQUE (`project_id`,`resource`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| id | 6259 | 422 | 423 |
| created_at | 2024-06-17T15:53:29 | 2014-04-15T19:57:06 | 2014-04-15T19:57:06 |
| updated_at | null | 2015-09-14T18:53:20 | 2015-09-14T18:53:20 |
| deleted_at | null | null | null |
| project_id | 7b3609decd234ec2852503d64e334e3f | 578e020880f7452d95f6059dee14b335 | 578e020880f7452d95f6059dee14b335 |
| resource | cores | instances | injected_files |
| hard_limit | 8 | 128 | 5 |
| deleted | 0 | 0 | 0 |

# `reservations`  (rows=42003)

columns:
`created_at` datetime: 12008 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 12184 distinct
`id` int PK: unique identifier, 1614700..1656702
`uuid` varchar36 NOTNULL: uuid, unique identifier
`usage_id` int NOTNULL FK: 1534 distinct, 159..3852, 168=3271, 169=3271, 170=3271, 3285=1001, 3286=996, 3284=991, 163=890, 164=883, 162=877, 510=437
`project_id` varchar255: 321 distinct, "17ea94ad74b64b9d92f4888336a598c7"=10016, "98333a1a28e746fa8c629c83a818ad57"=5879, "34c8d5cd44cc4b179c27892ec7596364"=3084, "dba6cc0fec6845a58f4dd5e84ef8dca5"=1602, "3008a142e9524f7295b06ea811908f93"=1527, "5b92ec1146d04f9091ab48b6cdba3eff"=1367, "daa18fdafdf04b5eac18e04aa19ee214"=1199, "e3fb2659584e436a832461dac02835f0"=850, "6f5103a9ae434375a92a1de24a19ca56"=732, "190ad02e1faa494a8ab7153c6d2e56c1"=585
`resource` varchar255: "ram"=14051, "cores"=13968, "instances"=13702, "server_groups"=282
`delta` int NOTNULL: 132 distinct, -98304..360448, avg=55.6183, median=-1
`expire` datetime: 11918 distinct, 2020-02-20 18:09:04=30, 2021-05-13 16:53:07=30, 2020-02-20 18:09:15=27, 2020-03-10 18:38:44=27, 2020-05-31 03:48:18=27, 2021-05-13 16:46:32=27, 2021-05-13 16:46:46=27, 2021-05-13 16:53:41=27, 2020-03-10 18:38:55=24, 2021-05-02 20:46:43=24
`deleted` int: all distinct, 1614700..1656702, avg=1635701, median=1635701
`user_id` varchar255: 395 distinct, "a1ef823458d24a68955fec6f3d390019"=13187, "8dff92c968c94d8093e087d13565c1b1"=3099, "77047e1a20db46b2b8d8daebb9e39fe8"=1361, "5302e30e168c4db283fc8e07009bb98f"=1297, "08e9506592fc4819b2cd7a54d93fa8ae"=1098, "4e4f5c1f38554dd6b3f750ee6b9ca9d2"=813, "e1b9fa1bb2f44cc88f8a6fa63dc389a9"=620, "ce3ea89d3bf34882b2666853f1474575"=601, "016a57c3112643b9be2a295e9d9c6e90"=587, "0be8fa0d641a4e778b9262bd2e5f40b5"=492

indexes: `project_id`, (`user_id`,`deleted`), (`deleted`,`expire`), `uuid`, `usage_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-26T20:39:03 | 2020-02-19T18:09:04 | 2020-02-19T18:09:04 |
| updated_at | null | null | null |
| deleted_at | 2024-06-26T20:39:05 | 2020-02-19T18:09:10 | 2020-02-19T18:09:10 |
| id | 1656702 | 1620497 | 1620498 |
| uuid | 73ad8ef0-ffde-4057-a571-adbde829e0ee | cd787265-e547-45a2-ba65-5ac916c09909 | cae49d66-ca4d-493e-bb06-526cf0f79cc8 |
| usage_id | 2546 | 169 | 170 |
| project_id | b3c6072810a24f67a7ac48e49a960e51 | 17ea94ad74b64b9d92f4888336a598c7 | 17ea94ad74b64b9d92f4888336a598c7 |
| resource | cores | ram | cores |
| delta | 2 | -8192 | -16 |
| expire | 2024-06-27T20:39:03 | 2020-02-20T18:09:04 | 2020-02-20T18:09:04 |
| deleted | 1656702 | 1620497 | 1620498 |
| user_id | 64f64393530d486da6d548710ca2990c | a1ef823458d24a68955fec6f3d390019 | a1ef823458d24a68955fec6f3d390019 |

# `s3_images`  (rows=2419)

columns:
`created_at` datetime: 2305 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 1..2497
`uuid` varchar36 NOTNULL: uuid, 2410 distinct
`deleted` int: 0=2419

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-24T16:43:06 | 2015-07-15T20:36:18 | 2015-07-15T22:00:44 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 2497 | 969 | 970 |
| uuid | 754667d2-7f09-4958-a2bf-505d410a99e5 | 4ec4e0f0-72ba-4356-aec1-97244c481d8d | d4d5cd38-59d5-46b3-b42b-751c216fe231 |
| deleted | 0 | 0 | 0 |

# `security_group_rules`  (rows=152)

columns:
`created_at` datetime: 151 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 1..192
`parent_group_id` int FK: 51 distinct, 1..67, 62=20, 64=9, 54=8, 55=8, 45=7, 9=6, 23=6, 63=6, 22=4, 50=4
`protocol` varchar255: "tcp"=115, "icmp"=19, "udp"=18
`from_port` int: 46 distinct, -1..60000, avg=3598.9079, median=22
`to_port` int: 49 distinct, -1..65535, avg=12722.7434, median=654
`cidr` varchar43: "10.71.29.205/8"=135, "10.152.54.152/8"=3, "10.227.134.94/8"=3, "10.116.184.94/8"=2, "10.150.130.197/8"=2, "10.216.18.158/8"=1, nulls=6
`group_id` int FK: 23=3, 63=3, nulls=146
`deleted` int: 0=152

indexes: `group_id`, `parent_group_id`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-07-23T02:51:26 | 2013-01-23T00:36:18 | 2013-02-06T16:07:43 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 192 | 63 | 65 |
| parent_group_id | 64 | 44 | 47 |
| protocol | tcp | tcp | tcp |
| from_port | 1 | 22 | 22 |
| to_port | 65535 | 22 | 22 |
| cidr | 10.71.29.205/8 | 10.71.29.205/8 | 10.71.29.205/8 |
| group_id | null | null | null |
| deleted | 0 | 0 | 0 |

# `security_groups`  (rows=601)

columns:
`created_at` datetime: 600 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 2012-07-09 15:38:51=1, 2012-09-13 02:28:33=1, 2012-11-09 18:54:54=1, 2012-11-20 01:59:21=1, 2012-11-29 17:18:11=1, 2012-11-29 17:19:41=1, 2012-12-25 01:15:01=1, 2013-01-10 16:27:00=1, 2013-01-23 01:35:49=1, nulls=592
`id` int PK: unique identifier, 1..621
`name` varchar255: 29 distinct, "aurum-xenon"=561, "helio-galax-solar"=9, "gamut"=4, "proto"=2, "align-mover"=1, "alpha-mover-meter"=1, "cosmo-novae"=1, "credo"=1, "cubic"=1, "dash"=1
`description` varchar255: 39 distinct
`user_id` varchar255: 488 distinct
`project_id` varchar255: 561 distinct, "6f5103a9ae434375a92a1de24a19ca56"=7, "70b2507b8cc44fcb917ddfb85f5079d9"=6, "3008a142e9524f7295b06ea811908f93"=5, "98333a1a28e746fa8c629c83a818ad57"=4, "292c70904ce7415c8626f801bbf1ed0c"=3, "3a8a2c70884d474aa1d3aeebeb800f7e"=3, "4e101cf5264b4e739b7b5ebe0f6b5c68"=3, "6f9adccbd03e4d2186756896957a14bf"=3, "84d0ab8dd0b44f61981e4dc218daab3f"=3, "d0ebc85936794a30b65bb6dae5687404"=3
`deleted` int: 0=592, 7=1, 21=1, 24=1, 29=1, 35=1, 37=1, 38=1, 39=1, 41=1, 0..41

indexes: UNIQUE (`project_id`,`name`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2024-06-17T21:06:37 | 2017-06-14T16:36:04 | 2017-06-15T06:32:59 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 621 | 347 | 348 |
| name | aurum-xenon | aurum-xenon | aurum-xenon |
| description | c21f969b5f03d33d43e04f8f136e7682 | c21f969b5f03d33d43e04f8f136e7682 | c21f969b5f03d33d43e04f8f136e7682 |
| user_id | 7a6e4676819c4cd2bce6ae812f0fc6e9 | 98c98c0016fc4d3096780f378f2f4453 | edd799156c4d49b6a60231ce456b4daf |
| project_id | 5e35676c2c6947f29e1402b31c5b87a7 | 2b0612b677df42b59f7ff08c9753365e | 07c9e0afeeb648d3830ba68ca84f595e |
| deleted | 0 | 0 | 0 |

# `services`  (rows=149)

columns:
`created_at` datetime: 146 distinct
`updated_at` datetime: 86 distinct, nulls=3
`deleted_at` datetime: all distinct, nulls=58
`id` int PK: unique identifier, 6..336
`host` varchar255: 142 distinct, "gamut-16"=4, "layer-19"=3, "cubic-10"=2, "lumen4-89"=2, "align-73"=1, "align-79"=1, "align-86"=1, "align-zenta-align"=1, "alpha-80"=1, "arrow-57"=1
`binary` varchar255: "nova-compute"=129, "nova-conductor"=13, "nova-scheduler"=2, "nova-cert"=1, "nova-consoleauth"=1, "nova-ec2"=1, "nova-metadata"=1, "nova-osapi_compute"=1
`topic` varchar255: "compute"=129, "conductor"=13, "scheduler"=2, "cert"=1, "consoleauth"=1, nulls=3
`report_count` int NOTNULL: 146 distinct, 0..31320673, avg=14194824.7383, median=14297305
`disabled` int: 0=92, 1=57
`deleted` int: 92 distinct, 0..331, avg=74.2282, median=45, 0=58, 6=1, 9=1, 12=1, 15=1, 19=1, 22=1, 23=1, 25=1, 28=1
`disabled_reason` varchar255: "AUTO: Connection to libvirt lost: 0"=44, "retired"=11, "constantly rebooting"=1, nulls=93
`last_seen_up` datetime: 82 distinct, nulls=8
`forced_down` int: 0=149
`version` int: 9=143, 0=6

indexes: UNIQUE (`host`,`binary`,`deleted`), UNIQUE (`host`,`topic`,`deleted`)

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-01-09T18:22:20 | 2013-03-29T18:08:19 | 2014-02-06T19:23:20 |
| updated_at | 2019-01-09T18:22:30 | 2017-08-04T20:20:32 | 2018-02-08T14:46:08 |
| deleted_at | null | 2017-08-04T20:27:29 | 2018-11-05T19:08:00 |
| id | 336 | 131 | 135 |
| host | cubic-10 | starx0-27 | delta-67 |
| binary | nova-compute | nova-compute | nova-compute |
| topic | compute | compute | compute |
| report_count | 1 | 13497283 | 12457289 |
| disabled | 1 | 1 | 0 |
| deleted | 0 | 131 | 135 |
| disabled_reason | AUTO: Connection to libvirt lost: 0 | AUTO: Connection to libvirt lost: 0 | null |
| last_seen_up | 2019-01-09T18:22:27 | 2017-08-04T20:20:30 | 2018-02-08T14:46:08 |
| forced_down | 0 | 0 | 0 |
| version | 9 | 9 | 9 |

# `shadow_aggregate_hosts`  (rows=516)

columns:
`created_at` datetime: 498 distinct, nulls=5
`updated_at` datetime: all NULL
`deleted_at` datetime: 494 distinct
`id` int PK: unique identifier, 11..742
`host` varchar255: 106 distinct
`aggregate_id` int NOTNULL: 2=258, 7=100, 4=41, 13=41, 3=18, 16=16, 12=11, 5=10, 6=9, 1=5, 17=5, 8=1, 18=1, 1..18
`deleted` int: all distinct, 11..742, avg=337.7345, median=318.5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2017-07-13T20:23:43 | 2013-08-08T18:43:29 | 2013-08-08T18:43:30 |
| updated_at | null | null | null |
| deleted_at | 2017-07-15T04:21:47 | 2014-02-08T01:11:36 | 2014-02-08T01:11:36 |
| id | 742 | 111 | 112 |
| host | grav9-5 | meter-74 | grav6-70 |
| aggregate_id | 18 | 2 | 2 |
| deleted | 742 | 111 | 112 |

# `shadow_aggregate_metadata`  (rows=4)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`id` int PK
`aggregate_id` int NOTNULL
`key` varchar255 NOTNULL
`value` varchar255 NOTNULL
`deleted` int

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 |
|---|---|---|---|---|
| created_at | 2014-10-07T14:31:40 | 2014-10-07T14:31:40 | 2016-07-07T01:41:18 | 2016-08-03T13:47:15 |
| updated_at | null | null | null | null |
| deleted_at | 2016-09-28T23:44:55 | 2016-09-28T23:44:55 | 2016-07-07T03:08:27 | 2017-02-16T21:56:42 |
| id | 20 | 21 | 23 | 27 |
| aggregate_id | 7 | 7 | 8 | 12 |
| key | ram_allocation_ratio | cpu_allocation_ratio | ram_allocation_ratio | switch |
| value | 1 | 1 | 1.2 | os-1g-1 |
| deleted | 20 | 21 | 23 | 27 |

# `shadow_block_device_mapping`  (rows=212755)

columns:
`created_at` datetime: nulls=78
`updated_at` datetime: nulls=3960
`deleted_at` datetime: nulls=3210
`id` int PK: unique identifier, 108..263628
`device_name` varchar255: nulls=3553
`delete_on_termination` int: nulls=78, 0..1, avg=0.9842
`snapshot_id` varchar36: uuid, nulls=212311
`volume_id` varchar36: uuid, nulls=209241
`volume_size` int: nulls=211417, 0..16384, avg=258.0135
`no_device` int: nulls=156707, 0..0, avg=0
`connection_info` text: nulls=209606
`instance_uuid` varchar36: uuid
`deleted` int: nulls=78, 0..263628, avg=110126.5061
`source_type` varchar255: profile metrics skipped
`destination_type` varchar255: nulls=24
`guest_format` varchar255: nulls=212661
`device_type` varchar255: nulls=1724
`disk_bus` varchar255: nulls=210306
`boot_index` int: nulls=1516, -1..1, avg=-0.0008
`image_id` varchar36: uuid, nulls=3484

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:45:47 | 2014-07-29T02:07:48 | 2014-07-29T02:08:20 |
| updated_at | 2019-11-08T16:45:49 | 2014-07-29T02:07:51 | 2014-07-29T02:08:22 |
| deleted_at | 2019-11-08T16:49:58 | 2014-07-29T05:29:59 | 2014-07-29T05:30:05 |
| id | 263628 | 24251 | 24252 |
| device_name | /dev/vda | /dev/vda | /dev/vda |
| delete_on_termination | 1 | 1 | 1 |
| snapshot_id | null | null | null |
| volume_id | null | null | null |
| volume_size | null | null | null |
| no_device | 0 | null | null |
| connection_info | null | null | null |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | fbd341ef-9076-4a31-9b6c-7ad336663401 | 532cba24-35e1-4c19-b974-c8fff2e6d813 |
| deleted | 263628 | 24251 | 24252 |
| source_type | image | image | image |
| destination_type | local | local | local |
| guest_format | null | null | null |
| device_type | disk | disk | disk |
| disk_bus | null | null | null |
| boot_index | 0 | 0 | 0 |
| image_id | 0a4641df-191f-44d7-b79b-13d26e7c5218 | 44b7d6d5-a205-4cc0-ba0f-4ed9b9a5ce00 | 44b7d6d5-a205-4cc0-ba0f-4ed9b9a5ce00 |

# `shadow_compute_nodes`  (rows=3)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`id` int PK
`service_id` int
`vcpus` int NOTNULL
`memory_mb` int NOTNULL
`local_gb` int NOTNULL
`vcpus_used` int NOTNULL
`memory_mb_used` int NOTNULL
`local_gb_used` int NOTNULL
`hypervisor_type` text NOTNULL
`hypervisor_version` int NOTNULL
`cpu_info` text NOTNULL
`disk_available_least` int
`free_ram_mb` int
`free_disk_gb` int
`current_workload` int
`running_vms` int
`hypervisor_hostname` varchar255
`deleted` int
`host_ip` varchar39
`supported_instances` text
`pci_stats` text
`metrics` text
`extra_resources` text
`stats` text
`numa_topology` text
`host` varchar255
`ram_allocation_ratio` float
`cpu_allocation_ratio` float
`uuid` varchar36
`disk_allocation_ratio` float

indexes: none

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| created_at | 2012-07-12T15:18:57 | 2012-12-14T18:18:23 | 2013-02-19T17:18:34 |
| updated_at | 2012-12-15T22:37:43 | 2012-12-14T18:36:10 | 2013-03-15T12:19:00 |
| deleted_at | 2013-04-29T16:11:57 | 2013-04-29T16:11:46 | 2013-04-29T16:12:15 |
| id | 11 | 45 | 61 |
| service_id | 30 | 96 | 129 |
| vcpus | 24 | 24 | 24 |
| memory_mb | 48295 | 48295 | 96679 |
| local_gb | 869 | 869 | 916 |
| vcpus_used | 0 | 0 | 0 |
| memory_mb_used | 512 | 512 | 512 |
| local_gb_used | 0 | 0 | 0 |
| hypervisor_type | QEMU | QEMU | QEMU |
| hypervisor_version | 1000000 | 1000000 | 1000000 |
| cpu_info | {"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm",… | {"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm",… | {"vendor": "Intel", "model": "Westmere", "arch": "x86_64", "features": ["rdtscp", "pdpe1gb", "dca", "pdcm", "xtpr", "tm2", "est", "smx", "vmx", "ds_cpl", "monitor", "dtes64", "pclmuldq", "pbe", "tm",… |
| disk_available_least | 839 | 867 | 786 |
| free_ram_mb | 47783 | 47783 | 96167 |
| free_disk_gb | 869 | 869 | 916 |
| current_workload | 0 | 0 | 0 |
| running_vms | 0 | 0 | 0 |
| hypervisor_hostname | flare-59.yahoo.ca.com | sonic4-45.yahoo.ca.com | shine-16.yahoo.ca.com |
| deleted | 11 | 45 | 61 |
| host_ip | null | null | null |
| supported_instances | null | null | null |
| pci_stats | null | null | null |
| metrics | null | null | null |
| extra_resources | null | null | null |
| stats | {} | {} | {} |
| numa_topology | null | null | null |
| host | null | null | null |
| ram_allocation_ratio | null | null | null |
| cpu_allocation_ratio | null | null | null |
| uuid | null | null | null |
| disk_allocation_ratio | null | null | null |

# `shadow_fixed_ips`  (rows=15)

columns:
`created_at` datetime: 2012-09-07 13:52:14=15
`updated_at` datetime: 2013-09-17 02:37:24=2, 2013-09-17 02:42:59=2, 2013-09-17 02:05:54=1, 2013-09-17 02:06:01=1, 2013-09-17 02:37:17=1, 2013-09-17 02:38:06=1, 2013-09-17 02:38:10=1, 2013-09-17 02:38:11=1, 2013-09-17 02:42:54=1, 2013-09-17 02:45:17=1, 2013-09-17 02:45:24=1, 2013-09-17 02:45:25=1, 2013-09-17 02:45:32=1
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 901..1338
`address` varchar39: "10.10.93.33/8"=1, "10.101.127.213/8"=1, "10.112.224.229/8"=1, "10.124.113.78/8"=1, "10.136.20.110/8"=1, "10.165.8.116/8"=1, "10.176.161.167/8"=1, "10.198.115.85/8"=1, "10.232.120.47/8"=1, "10.253.100.135/8"=1, "10.26.198.227/8"=1, "10.28.229.58/8"=1, "10.29.111.109/8"=1, "10.87.199.189/8"=1, "10.90.203.211/8"=1
`network_id` int: 1=15
`allocated` int: 0=11, 1=4
`leased` int: 0=11, 1=4
`reserved` int: 0=15
`virtual_interface_id` int: 414191=1, 414192=1, 414193=1, 414194=1, nulls=11, 414191..414194
`host` varchar255: all NULL
`instance_uuid` varchar36: uuid, unique identifier
`deleted` int: 0=15

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2012-09-07T13:52:14 | 2012-09-07T13:52:14 | 2012-09-07T13:52:14 |
| updated_at | 2013-09-17T02:45:25 | 2013-09-17T02:42:59 | 2013-09-17T02:42:59 |
| deleted_at | null | null | null |
| id | 1338 | 1293 | 1305 |
| address | 10.26.198.227/8 | 10.136.20.110/8 | 10.165.8.116/8 |
| network_id | 1 | 1 | 1 |
| allocated | 1 | 0 | 0 |
| leased | 1 | 0 | 0 |
| reserved | 0 | 0 | 0 |
| virtual_interface_id | 414194 | null | null |
| host | null | null | null |
| instance_uuid | 6154483e-317a-43bc-9563-cd945f59a242 | d249089d-51c5-4c38-9cba-051dc9693381 | 557b97b9-4d92-4846-9b47-7b5103fa239d |
| deleted | 0 | 0 | 0 |

# `shadow_instance_actions`  (rows=523265)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=48354
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 3978..600508
`action` varchar255: profile metrics skipped
`instance_uuid` varchar36: uuid
`request_id` varchar255: profile metrics skipped
`user_id` varchar255: nulls=3886
`project_id` varchar255: nulls=3886
`start_time` datetime: profile metrics skipped
`finish_time` datetime: all NULL
`message` varchar255: nulls=514702
`deleted` int: 0..539568, avg=227050.9764

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:49:50 | 2018-07-02T22:28:15 | 2018-07-02T22:28:18 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 600508 | 579347 | 579348 |
| action | delete | delete | delete |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | 05d21e74-0309-4644-a03a-af78ca829b51 | 10738913-537a-42bd-bf96-1374092ebabf |
| request_id | req-56139ae9-20dc-4c93-a28b-d0b4f32fb85d | req-fc77cd8e-e3e3-40d8-9edf-8cbf42b425d0 | req-85d3e526-6b09-4d32-81d1-17ed46cd5989 |
| user_id | a1ef823458d24a68955fec6f3d390019 | 0881c8820abe46cb8b7454f78c8e21d0 | 0881c8820abe46cb8b7454f78c8e21d0 |
| project_id | bfd50153a2e9476f93e33e30e922cd06 | d3ac3958f14941cdb205e76ba43bbe49 | d3ac3958f14941cdb205e76ba43bbe49 |
| start_time | 2019-11-08T16:49:49 | 2018-07-02T22:28:14 | 2018-07-02T22:28:17 |
| finish_time | null | null | null |
| message | null | null | null |
| deleted | 0 | 0 | 0 |

# `shadow_instance_actions_events`  (rows=663442)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=563
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 5618..737363
`event` varchar255: profile metrics skipped
`action_id` int: 3978..600508
`start_time` datetime: profile metrics skipped
`finish_time` datetime: nulls=58400
`result` varchar255: nulls=58400
`traceback` text: nulls=654508
`deleted` int: 0..728497, avg=341353.9424
`host` varchar255: all NULL
`details` text: all NULL

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:49:50 | 2016-01-10T02:50:37 | 2016-01-10T02:50:39 |
| updated_at | 2019-11-08T16:49:59 | 2017-07-19T16:35:46 | 2017-07-19T16:35:46 |
| deleted_at | null | null | null |
| id | 737363 | 581338 | 581340 |
| event | compute_terminate_instance | compute_terminate_instance | compute_terminate_instance |
| action_id | 600508 | 459264 | 459294 |
| start_time | 2019-11-08T16:49:50 | 2016-01-10T02:50:37 | 2016-01-10T02:50:39 |
| finish_time | 2019-11-08T16:49:59 | 2016-01-10T02:51:22 | 2016-01-10T02:51:21 |
| result | Success | Success | Success |
| traceback | null | null | null |
| deleted | 0 | 581338 | 581340 |
| host | null | null | null |
| details | null | null | null |

# `shadow_instance_extra`  (rows=179772)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=53
`deleted_at` datetime: nulls=63
`deleted` int: 0..211264, avg=98615.3022
`id` int PK: unique identifier, 1..211264
`instance_uuid` varchar36 NOTNULL: uuid, 179720 distinct
`numa_topology` text: nulls=179754
`pci_requests` text: nulls=184
`flavor` text: nulls=105364
`vcpu_model` text: nulls=111869
`migration_context` text: nulls=179634

indexes: `instance_uuid`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:45:47 | 2015-04-17T07:25:48 | 2015-04-17T07:26:00 |
| updated_at | 2019-11-08T16:49:58 | 2015-04-17T07:26:19 | 2015-04-17T07:26:27 |
| deleted_at | 2019-11-08T16:49:58 | 2015-04-17T07:40:35 | 2015-04-17T07:54:20 |
| deleted | 211264 | 84518 | 84519 |
| id | 211264 | 84518 | 84519 |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | 7036fdd5-bb36-4330-8cf0-112621b9934a | ad76228f-7a3c-41c3-b4f4-a0d710df5c88 |
| numa_topology | null | null | null |
| pci_requests | [] | [] | [] |
| flavor | {"new": null, "old": null, "cur": {"nova_object.version": "1.1", "nova_object.changes": ["extra_specs"], "nova_object.name": "Flavor", "nova_object.data": {"disabled": false, "root_gb": 10, "name": "… | null | null |
| vcpu_model | {"nova_object.version": "1.0", "nova_object.changes": ["vendor", "features", "model", "topology", "arch", "match", "mode"], "nova_object.name": "VirtCPUModel", "nova_object.data": {"vendor": null, "f… | null | null |
| migration_context | null | null | null |

# `shadow_instance_faults`  (rows=201285)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: all NULL
`deleted_at` datetime: nulls=27912
`id` int PK: unique identifier, 1..204828
`instance_uuid` varchar36: uuid
`code` int NOTNULL: 400..500
`message` varchar255: profile metrics skipped
`details` text: nulls=3281
`host` varchar255: profile metrics skipped
`deleted` int: 0..446923, avg=275318.1017

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-07T16:55:40 | 2013-07-03T09:51:04 | 2013-07-03T09:51:15 |
| updated_at | null | null | null |
| deleted_at | 2019-11-07T18:28:41 | 2013-07-03T09:51:09 | 2013-07-03T09:51:21 |
| id | 204828 | 134418 | 134419 |
| instance_uuid | fe6c2d4d-d26d-4816-80cf-6baf2989203b | fa2b82a7-87e2-40d9-a77c-dfa1ea7cf466 | d786b150-b819-4b0d-af96-5f40c92b6b33 |
| code | 500 | 500 | 500 |
| message | 22c323b0493531e2b749b9918d7483da | 2f0ffe5e898249e3506367ee07ce4835 | 2f0ffe5e898249e3506367ee07ce4835 |
| details | 1d7bcac64380dd31e129a1fd15e3f795 | ee9f89f55405ff6ada25fefabe558dda | ee9f89f55405ff6ada25fefabe558dda |
| host | gamut-16 |  |  |
| deleted | 204828 | 439319 | 439320 |

# `shadow_instance_group_member`  (rows=84)

columns:
`created_at` datetime: 52 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 67 distinct
`deleted` int: all distinct, 241..332, avg=282.6905, median=282.5
`id` int PK: unique identifier, 241..332
`instance_id` varchar255: uuid, unique identifier
`group_id` int NOTNULL: 11=81, 14=2, 12=1, 11..14

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2017-07-11T16:14:30 | 2017-07-06T22:36:30 | 2017-07-06T22:41:16 |
| updated_at | null | null | null |
| deleted_at | 2017-07-11T16:15:13 | 2017-07-06T23:12:29 | 2017-07-06T23:18:13 |
| deleted | 332 | 306 | 307 |
| id | 332 | 306 | 307 |
| instance_id | 9e7d58a9-2fae-45c3-b94f-68839d0fee21 | 7e1077d1-f7ec-4ec9-9bb4-f5ede5c4fae5 | 6a2804cf-55e4-483b-a521-36e6b303398e |
| group_id | 14 | 11 | 11 |

# `shadow_instance_group_policy`  (rows=2)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`deleted` int
`id` int PK
`policy` varchar255
`group_id` int NOTNULL

indexes: none

all rows:
| column | row 1 | row 2 |
|---|---|---|
| created_at | 2016-11-07T17:54:03 | 2016-11-07T20:59:35 |
| updated_at | null | null |
| deleted_at | 2017-07-06T23:18:19 | 2016-11-07T22:09:55 |
| deleted | 11 | 12 |
| id | 11 | 12 |
| policy | anti-affinity | anti-affinity |
| group_id | 11 | 12 |

# `shadow_instance_info_caches`  (rows=263732)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=26182
`deleted_at` datetime: nulls=5
`id` int PK: unique identifier, 3084..742114
`network_info` text: profile metrics skipped
`instance_uuid` varchar36 NOTNULL: uuid
`deleted` int: 0..742114, avg=584619.6283

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:45:47 | 2012-10-15T20:50:44 | 2012-10-15T20:50:44 |
| updated_at | 2019-11-08T16:49:58 | 2012-10-15T20:51:00 | 2012-10-15T20:58:30 |
| deleted_at | 2019-11-08T16:49:58 | 2012-10-22T11:23:39 | 2012-10-22T11:23:39 |
| id | 742114 | 27683 | 27684 |
| network_info | [] | [{"network": {"bridge": "br100", "subnets": [{"ips": [{"meta": {}, "version": 4, "type": "fixed", "floating_ips": [], "address": "10.22.215.7/8"}], "version": 4, "meta": {"dhcp_server": "10.129.224.2… | [{"network": {"bridge": "br100", "subnets": [{"ips": [{"meta": {}, "version": 4, "type": "fixed", "floating_ips": [], "address": "10.129.1.10/8"}], "version": 4, "meta": {"dhcp_server": "10.129.224.2… |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | cfdf0510-2a9e-4034-a0a5-820b22c5331e | e2e6c114-6803-4eac-9fd6-221b30e8d7fd |
| deleted | 742114 | 27683 | 27684 |

# `shadow_instance_metadata`  (rows=1554)

columns:
`created_at` datetime: 674 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 464 distinct
`id` int PK: unique identifier, 1..2028
`key` varchar255: 21 distinct
`value` varchar255: 76 distinct
`instance_uuid` varchar36: uuid, 777 distinct
`deleted` int: all distinct, 1..2028, avg=1077.1705, median=1251.5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-05-25T02:48:30 | 2019-05-17T22:05:42 | 2019-05-17T22:05:45 |
| updated_at | null | null | null |
| deleted_at | 2019-05-27T05:30:33 | 2019-05-22T15:44:31 | 2019-05-22T15:44:52 |
| id | 2028 | 1605 | 1606 |
| key | role | flight | role |
| value | theta_point | spark_spind | theta_point |
| instance_uuid | 626ca30f-656f-4763-9de8-6927e9c23171 | a2be2f37-b1cf-4f16-9dc1-d9c964df9de1 | 9dc5d901-37b1-41dc-ae8b-409537e75da8 |
| deleted | 2028 | 1605 | 1606 |

# `shadow_instance_system_metadata`  (rows=4879813)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=4819075
`deleted_at` datetime: nulls=4499466
`id` int PK: unique identifier, 6918265..12204053
`instance_uuid` varchar36 NOTNULL: uuid
`key` varchar255 NOTNULL: profile metrics skipped
`value` varchar255: nulls=231539
`deleted` int: 0..12204053

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T16:49:56 | 2015-04-22T13:35:39 | 2015-04-22T13:35:39 |
| updated_at | null | null | null |
| deleted_at | 2019-11-08T16:49:58 | null | null |
| id | 12204053 | 10760170 | 10760171 |
| instance_uuid | 25a90600-fabf-44d2-b14c-72b7004411c8 | 57135b9b-c7ff-4d92-af57-846cf02fc9ed | 57135b9b-c7ff-4d92-af57-846cf02fc9ed |
| key | clean_attempts | instance_type_vcpu_weight | instance_type_root_gb |
| value | comet-star-gamma | null | phase |
| deleted | 12204053 | 0 | 0 |

# `shadow_instance_type_extra_specs`  (rows=53)

columns:
`created_at` datetime: 46 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 28 distinct
`id` int PK: unique identifier, 1..111
`instance_type_id` int NOTNULL: unique identifier, 15..149
`key` varchar255: "overcommit"=32, "tig"=11, "ups"=6, "test"=4
`value` varchar255: "default"=28, "true"=21, "false"=4
`deleted` int: all distinct, 1..111, avg=46.1887, median=27

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2015-08-17T18:40:38 | 2014-02-07T19:13:37 | 2014-02-07T20:05:03 |
| updated_at | null | null | null |
| deleted_at | 2015-08-17T18:41:58 | 2014-02-14T19:17:47 | 2014-02-14T19:41:29 |
| id | 111 | 65 | 69 |
| instance_type_id | 149 | 98 | 96 |
| key | tig | test | test |
| value | true | true | true |
| deleted | 111 | 65 | 69 |

# `shadow_instance_type_projects`  (rows=104)

columns:
`created_at` datetime: 63 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 40 distinct
`id` int PK: unique identifier, 2..220
`instance_type_id` int NOTNULL: 37 distinct, 50..152
`project_id` varchar255: "6f9adccbd03e4d2186756896957a14bf"=27, "98333a1a28e746fa8c629c83a818ad57"=22, "17ea94ad74b64b9d92f4888336a598c7"=20, "717cc16840494e8795e2ee25c46fe797"=10, "7691c9955ce1444ab366d041f5bdf33c"=7, "292c70904ce7415c8626f801bbf1ed0c"=4, "47c0857cf5b5452a86f640fd44be1d40"=4, "09ad05432f914e26bc417bf58f1cb4d2"=3, "tig"=3, "a3ccd76b29264bbe94415833015c9379"=2, "4f5d702fa8674268be123e7df3eb9faa"=1, "e3fb2659584e436a832461dac02835f0"=1
`deleted` int: all distinct, 2..220, avg=102.1827, median=103.5

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2015-12-17T16:58:14 | 2015-04-10T15:34:30 | 2015-04-10T15:38:38 |
| updated_at | null | null | null |
| deleted_at | 2015-12-17T17:06:10 | 2015-04-10T15:34:56 | 2015-04-10T15:39:53 |
| id | 220 | 167 | 169 |
| instance_type_id | 152 | 138 | 138 |
| project_id | tig | tig | 7691c9955ce1444ab366d041f5bdf33c |
| deleted | 220 | 167 | 169 |

# `shadow_instances`  (rows=709892)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: nulls=76
`deleted_at` datetime: profile metrics skipped
`id` int PK: unique identifier, 1..741069
`internal_id` int: all NULL
`user_id` varchar255: profile metrics skipped
`project_id` varchar255: profile metrics skipped
`image_ref` varchar255: uuid, nulls=2440
`kernel_id` varchar255: uuid, nulls=709773
`ramdisk_id` varchar255: uuid, nulls=709773
`launch_index` int: 0..511, avg=2.7497
`key_name` varchar255: nulls=30973
`key_data` text: nulls=30974
`power_state` int: 0..5, avg=0.7561
`vm_state` varchar255: profile metrics skipped
`memory_mb` int: 1..98304, avg=4291.6139
`vcpus` int: 1..32, avg=2.3635
`hostname` varchar255: profile metrics skipped
`host` varchar255: profile metrics skipped
`user_data` text: nulls=369424
`reservation_id` varchar255: profile metrics skipped
`scheduled_at` datetime: nulls=312941
`launched_at` datetime: nulls=173199
`terminated_at` datetime: nulls=140495
`display_name` varchar255: profile metrics skipped
`display_description` varchar255: nulls=434256
`availability_zone` varchar255: nulls=682787
`locked` int: 0..1, avg=0
`os_type` varchar255: all NULL
`launched_on` text: nulls=143414
`instance_type_id` int: 1..174
`vm_mode` varchar255: all NULL
`uuid` varchar36 NOTNULL: uuid
`architecture` varchar255: nulls=709734
`root_device_name` varchar255: nulls=147674
`access_ip_v4` varchar39: all NULL
`access_ip_v6` varchar39: all NULL
`config_drive` varchar255: bool-like, nulls=709547
`task_state` varchar255: nulls=567690
`default_ephemeral_device` varchar255: nulls=401136
`default_swap_device` varchar255: nulls=709415
`progress` int: 0..0, avg=0
`auto_disk_config` int: nulls=481255, 0..1, avg=0.0023
`shutdown_terminate` int: 0..1, avg=0.0272
`disable_terminate` int: 0..0, avg=0
`root_gb` int: 0..100, avg=12.3716
`ephemeral_gb` int: 0..360, avg=24.6218
`cell_name` varchar255: all NULL
`node` varchar255: nulls=470739
`deleted` int: 1..741069, avg=357136.6198
`locked_by` enum: nulls=709884
`cleaned` int: 0..1, avg=0.9936
`ephemeral_key_uuid` varchar36: all NULL

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-05-25T02:48:07 | 2012-11-20T05:41:59 | 2012-11-20T05:42:00 |
| updated_at | 2019-05-27T05:29:18 | 2012-11-20T05:50:18 | 2012-11-20T06:00:11 |
| deleted_at | 2019-05-27T05:29:18 | 2012-11-20T05:50:50 | 2012-11-20T06:00:33 |
| id | 741069 | 180075 | 180076 |
| internal_id | null | null | null |
| user_id | a1ef823458d24a68955fec6f3d390019 | c8490ee0863345f6919b5c63540efca1 | c8490ee0863345f6919b5c63540efca1 |
| project_id | 17ea94ad74b64b9d92f4888336a598c7 | 3008a142e9524f7295b06ea811908f93 | 3008a142e9524f7295b06ea811908f93 |
| image_ref | d74d6560-3a34-4ae6-bd89-ec4dc354b922 | 52a1451b-8311-4be2-b148-c7ee578a78eb | 52a1451b-8311-4be2-b148-c7ee578a78eb |
| kernel_id | null | null | null |
| ramdisk_id | null | null | null |
| launch_index | 0 | 0 | 0 |
| key_name | null | flare_cvgr-feyl-nuws-tenn-pwyt | flare_cvgr-feyl-nuws-tenn-pwyt |
| key_data | null | 73e6cd4cbdc667c8e27bcf089ffda82a | 73e6cd4cbdc667c8e27bcf089ffda82a |
| power_state | 0 | 1 | 1 |
| vm_state | deleted | deleted | deleted |
| memory_mb | 4096 | 2048 | 2048 |
| vcpus | 8 | 1 | 1 |
| hostname | helix | arrow2-66 | nexis-beam-drift |
| host | beam8-22 | space7-54 | space7-54 |
| user_data | 557863e33d149078ec6e1a03e609495d | 668b9e9165bc740a9b75aa174d4620db | 967a421a32ad6998c5d8bbc1776e5275 |
| reservation_id | r-92gre1nf | r-jsnxb87g | r-f09wk6qr |
| scheduled_at | null | 2012-11-20T05:42:11 | 2012-11-20T05:42:11 |
| launched_at | 2019-05-25T02:48:59 | 2012-11-20T05:43:18 | 2012-11-20T05:43:11 |
| terminated_at | 2019-05-27T05:29:29 | 2012-11-20T05:50:18 | 2012-11-20T06:00:11 |
| display_name | helix | 10.49.197.142/8 | 10.215.227.7/8 |
| display_description | helix | null | null |
| availability_zone | null | null | null |
| locked | 0 | 0 | 0 |
| os_type | null | null | null |
| launched_on | beam8-22 | space7-54 | space7-54 |
| instance_type_id | 60 | 5 | 5 |
| vm_mode | null | null | null |
| uuid | 5381e77a-b474-4f22-8729-3fdf0bfbcd18 | 1e6dd5ba-da07-4670-8ca3-9bfccaabf7cd | 3b799e2d-753c-4308-a861-686216e637a4 |
| architecture | null | null | null |
| root_device_name | /dev/vda | /dev/vda | /dev/vda |
| access_ip_v4 | null | null | null |
| access_ip_v6 | null | null | null |
| config_drive | null | null | null |
| task_state | null | null | null |
| default_ephemeral_device | null | /dev/vdb | /dev/vdb |
| default_swap_device | null | null | null |
| progress | 0 | 0 | 0 |
| auto_disk_config | 0 | null | null |
| shutdown_terminate | 0 | 0 | 0 |
| disable_terminate | 0 | 0 | 0 |
| root_gb | 10 | 10 | 10 |
| ephemeral_gb | 0 | 20 | 20 |
| cell_name | null | null | null |
| node | beam8-22.yahoo.ca.com | null | null |
| deleted | 741069 | 180075 | 180076 |
| locked_by | null | null | null |
| cleaned | 1 | 1 | 1 |
| ephemeral_key_uuid | null | null | null |

# `shadow_key_pairs`  (rows=51)

columns:
`created_at` datetime: all distinct
`updated_at` datetime: 48 distinct
`deleted_at` datetime: 48 distinct
`id` int PK: unique identifier, 2..151
`name` varchar255: 38 distinct
`user_id` varchar255: 23 distinct
`fingerprint` varchar255: all distinct
`public_key` text: all distinct
`deleted` int: all distinct, 2..151, avg=73.6275, median=71
`type` enum NOTNULL: "ssh"=51

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-07-29T21:03:17 | 2012-08-09T16:36:18 | 2012-08-09T16:44:56 |
| updated_at | 2013-07-29T21:03:34 | 2012-08-09T16:43:56 | 2012-08-09T17:02:19 |
| deleted_at | 2013-07-29T21:03:34 | 2012-08-09T16:43:56 | 2012-08-09T17:02:19 |
| id | 151 | 14 | 15 |
| name | axiom-dash | plane-scope | warp-warp |
| user_id | e754f357f72c43ad9301478cb2ccf3aa | be851dce01da4b3ebbe8149bdb59527c | be851dce01da4b3ebbe8149bdb59527c |
| fingerprint | b1:9f:70:51:7f:b3:bd:7d:28:8d:cc:9d:ff:1a:10:71 | 8f:9d:b1:10:0a:50:5f:5f:96:dd:b5:ff:4f:48:39:12 | c8:b8:25:1d:27:06:c2:bf:83:98:56:de:d4:6a:aa:7e |
| public_key | 63b3992a6ad94ee9a0c224d89dbd150e | 053d107a5c8a90529ab0e0dfbb49cf91 | faabcce7cd2ec2163dffa6b243e662cd |
| deleted | 151 | 14 | 15 |
| type | ssh | ssh | ssh |

# `shadow_migrations`  (rows=2112)

columns:
`created_at` datetime: 2093 distinct
`updated_at` datetime: 1965 distinct, nulls=109
`deleted_at` datetime: 2018-09-06 14:55:17=307, 2018-09-06 14:58:53=60, nulls=1745
`id` int PK: unique identifier, 6..4386
`source_compute` varchar255: 125 distinct
`dest_compute` varchar255: 129 distinct, nulls=26
`dest_host` varchar255: 115 distinct, nulls=1133
`status` varchar255: "completed"=813, "confirmed"=580, "error"=400, "pre-migrating"=104, "failed"=93, "confirming"=31, "migrating"=26, "cancelled"=19, "preparing"=15, "reverted"=9, "finished"=7, "post-migrating"=7, "accepted"=5, "running"=2, "done"=1
`instance_uuid` varchar36: uuid, 1253 distinct
`old_instance_type_id` int: 57 distinct, nulls=30, 48..162
`new_instance_type_id` int: 55 distinct, nulls=30, 48..172
`source_node` varchar255: 120 distinct, nulls=1126
`dest_node` varchar255: 117 distinct, nulls=1133
`deleted` int: 0=1745, 1=367
`migration_type` enum: "live-migration"=1126, "resize"=306, "migration"=113, "evacuation"=30, nulls=537
`hidden` int: 0=2112
`memory_total` bigint: 31 distinct, nulls=1146, 0..103088463872, avg=9420985833.74, median=2156732416
`memory_processed` bigint: 542 distinct, nulls=1146, 0..317583106422, avg=6434959658.93, median=391201103.5
`memory_remaining` bigint: 541 distinct, nulls=1146, 0..40323997696, avg=1056798669.12, median=98648064
`disk_total` bigint: 0=966, nulls=1146
`disk_processed` bigint: 0=966, nulls=1146
`disk_remaining` bigint: 0=966, nulls=1146

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-08-13T19:01:58 | 2016-09-28T00:34:45 | 2016-09-28T13:12:30 |
| updated_at | 2019-08-13T19:02:31 | 2016-09-28T14:36:17 | 2016-11-26T03:39:08 |
| deleted_at | null | null | null |
| id | 4386 | 1007 | 1009 |
| source_compute | prime3-77 | starx0-27 | flare7-39 |
| dest_compute | cosmo3-23 | star-76 | zeph-15 |
| dest_host | 10.165.53.177/8 | 10.79.217.241/8 | 10.176.178.91/8 |
| status | confirmed | confirmed | confirming |
| instance_uuid | 19ae8899-9ed9-4880-bb19-f9e3a22354af | 594816a6-cc6b-4ae2-ae0f-244e124f0785 | 4ef1868c-5440-4799-8743-8d719e5f2d80 |
| old_instance_type_id | 66 | 71 | 80 |
| new_instance_type_id | 73 | 71 | 80 |
| source_node | prime3-77.yahoo.ca.com | starx0-27.yahoo.ca.com | flare7-39.yahoo.ca.com |
| dest_node | cosmo3-23.yahoo.ca.com | star-76.yahoo.ca.com | zeph-15.yahoo.ca.com |
| deleted | 0 | 0 | 0 |
| migration_type | resize | null | null |
| hidden | 0 | 0 | 0 |
| memory_total | null | null | null |
| memory_processed | null | null | null |
| memory_remaining | null | null | null |
| disk_total | null | null | null |
| disk_processed | null | null | null |
| disk_remaining | null | null | null |

# `shadow_pci_devices`  (rows=8)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`deleted` int NOTNULL
`id` int PK
`compute_node_id` int NOTNULL
`address` varchar12 NOTNULL
`product_id` varchar4
`vendor_id` varchar4
`dev_type` varchar8
`dev_id` varchar255
`label` varchar255 NOTNULL
`status` varchar36 NOTNULL
`extra_info` text
`instance_uuid` varchar36
`request_id` varchar36
`numa_node` int
`parent_addr` varchar12

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 |
|---|---|---|---|---|---|---|---|---|
| created_at | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 | 2016-07-06T00:12:30 |
| updated_at | 2016-10-18T15:08:41 | 2016-10-18T15:08:58 | 2016-10-18T15:11:34 | 2016-10-18T15:09:26 | 2016-10-13T14:12:40 | 2016-10-13T14:12:40 | 2016-10-13T14:12:40 | 2016-10-13T14:12:40 |
| deleted_at | 2016-10-13T21:02:54 | 2016-10-13T21:03:55 | 2016-10-13T21:02:54 | 2016-10-13T21:04:53 | 2016-10-13T21:02:54 | 2016-10-13T21:03:55 | 2016-10-13T21:02:54 | 2016-10-13T21:05:55 |
| deleted | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| id | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| compute_node_id | 90 | 90 | 90 | 90 | 90 | 90 | 90 | 90 |
| address | 0000:64:31.0 | 0000:06:33.0 | 0000:75:06.0 | 0000:54:12.0 | 0000:04:56.0 | 0000:93:95.0 | 0000:83:59.0 | 0000:43:32.0 |
| product_id | 102d | 102d | 102d | 102d | 102d | 102d | 102d | 102d |
| vendor_id | 10de | 10de | 10de | 10de | 10de | 10de | 10de | 10de |
| dev_type | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI | type-PCI |
| dev_id | pci_0000_04_00_0 | pci_0000_05_00_0 | pci_0000_08_00_0 | pci_0000_09_00_0 | pci_0000_83_00_0 | pci_0000_84_00_0 | pci_0000_87_00_0 | pci_0000_88_00_0 |
| label | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d | label_10de_102d |
| status | allocated | allocated | available | allocated | available | available | available | available |
| extra_info | {} | {} | {} | {} | {} | {} | {} | {} |
| instance_uuid | 66fe2820-0a93-4e89-8575-650e1b18e037 | eb15a522-752f-4658-82bd-8521bed2c612 | null | 9269391a-4ce4-4c8d-993d-5ad7a9c3879b | null | null | null | null |
| request_id | null | null | null | null | null | null | null | null |
| numa_node | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| parent_addr | null | null | null | null | null | null | null | null |

# `shadow_reservations`  (rows=1297676)

columns:
`created_at` datetime: profile metrics skipped
`updated_at` datetime: all NULL
`deleted_at` datetime: profile metrics skipped
`id` int PK: unique identifier, 1..1614699
`uuid` varchar36 NOTNULL: uuid
`usage_id` int NOTNULL: 1..2940
`project_id` varchar255: profile metrics skipped
`resource` varchar255: profile metrics skipped
`delta` int NOTNULL: -98304..761856
`expire` datetime: profile metrics skipped
`deleted` int: 1..1614699
`user_id` varchar255: nulls=1176

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2019-11-08T18:16:30 | 2014-07-24T01:09:04 | 2014-07-24T01:09:09 |
| updated_at | null | null | null |
| deleted_at | 2019-11-08T18:16:31 | 2014-07-24T01:09:08 | 2014-07-24T01:09:09 |
| id | 1614699 | 274400 | 274401 |
| uuid | 7912a75e-ca94-42ed-9867-a1b451d02ac7 | a03a8938-600e-4f4f-a391-c9750a5568e3 | 6f5419a4-e11f-403c-aa4d-00005e6aca59 |
| usage_id | 2879 | 245 | 243 |
| project_id | da4266d0e4f24017b0dc114ea64ad422 | 3008a142e9524f7295b06ea811908f93 | 3008a142e9524f7295b06ea811908f93 |
| resource | ram | cores | instances |
| delta | 65536 | -4 | 1 |
| expire | 2019-11-09T18:16:30 | 2014-07-25T01:09:04 | 2014-07-25T01:09:09 |
| deleted | 1614699 | 274400 | 274401 |
| user_id | 38fe63ea602f4200aa85186291d39df1 | 0df639d1cf6a48f7b9ddf6cf68772ca8 | 0df639d1cf6a48f7b9ddf6cf68772ca8 |

# `shadow_security_group_rules`  (rows=40)

columns:
`created_at` datetime: all distinct
`updated_at` datetime: 33 distinct
`deleted_at` datetime: 33 distinct
`id` int PK: unique identifier, 6..187
`parent_group_id` int: 64=13, 55=5, 63=4, 9=3, 5=2, 19=2, 66=2, 15=1, 21=1, 22=1, 39=1, 46=1, 47=1, 50=1, 51=1, 58=1, 5..66
`protocol` varchar255: "tcp"=26, "udp"=11, "icmp"=3
`from_port` int: 22=9, 1=6, 445=5, 9000=4, -1=2, 137=2, 139=2, 389=2, 8080=2, 8=1, 80=1, 123=1, 138=1, 446=1, 9010=1, -1..9010
`to_port` int: 22=8, 65535=6, 445=5, 10000=4, 137=2, 139=2, 255=2, 389=2, 8080=2, -1=1, 23=1, 80=1, 138=1, 446=1, 456=1, 9020=1, -1..65535
`cidr` varchar43: "10.71.29.205/8"=29, "10.122.66.108/8"=4, "10.216.18.158/8"=3, "10.139.2.255/8"=1, nulls=3
`group_id` int: 22=1, 39=1, 58=1, nulls=37, 22..58
`deleted` int: all distinct, 6..187, avg=112.05, median=111

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-06-12T22:05:18 | 2012-11-08T00:00:46 | 2012-11-29T17:23:59 |
| updated_at | 2013-06-12T22:06:40 | 2012-11-08T00:01:32 | 2012-11-29T17:24:19 |
| deleted_at | 2013-06-12T22:06:40 | 2012-11-08T00:01:32 | 2013-01-23T01:35:49 |
| id | 187 | 39 | 53 |
| parent_group_id | 66 | 22 | 39 |
| protocol | tcp | tcp | tcp |
| from_port | 446 | 8080 | 123 |
| to_port | 446 | 8080 | 456 |
| cidr | 10.71.29.205/8 | null | null |
| group_id | null | 22 | 39 |
| deleted | 187 | 39 | 53 |

# `shadow_services`  (rows=110)

columns:
`created_at` datetime: 105 distinct
`updated_at` datetime: 105 distinct
`deleted_at` datetime: 43 distinct, nulls=61
`id` int PK: unique identifier, 1..242
`host` varchar255: 94 distinct
`binary` varchar255: "nova-network"=61, "nova-conductor"=33, "nova-compute"=8, "nova-volume"=5, "nova-cert"=1, "nova-consoleauth"=1, "nova-scheduler"=1
`topic` varchar255: "network"=61, "conductor"=33, "compute"=8, "volume"=5, "cert"=1, "consoleauth"=1, "scheduler"=1
`report_count` int NOTNULL: 109 distinct, 1..8648106, avg=2111383.1636, median=1700060
`disabled` int: 1=76, 0=34
`deleted` int: 49 distinct, 1..242, avg=59.4182, median=1
`disabled_reason` varchar255: "heat death"=1, "old-version"=1, nulls=108
`last_seen_up` datetime: all NULL
`forced_down` int: 0=110
`version` int: 0=110

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2016-08-11T15:47:19 | 2015-11-23T20:13:11 | 2015-11-23T20:50:26 |
| updated_at | 2016-08-11T15:57:05 | 2015-11-23T20:18:45 | 2015-11-30T21:45:33 |
| deleted_at | 2016-08-11T15:58:28 | 2016-01-21T16:53:05 | 2016-01-21T16:53:07 |
| id | 242 | 182 | 186 |
| host | blaze-shift | twist-light-flux | flick-shine-flare |
| binary | nova-conductor | nova-conductor | nova-conductor |
| topic | conductor | conductor | conductor |
| report_count | 59 | 18 | 60738 |
| disabled | 0 | 0 | 0 |
| deleted | 242 | 182 | 186 |
| disabled_reason | null | null | null |
| last_seen_up | null | null | null |
| forced_down | 0 | 0 | 0 |
| version | 0 | 0 | 0 |

# `shadow_snapshots`  (rows=1)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`id` varchar36 PK
`volume_id` varchar36 NOTNULL
`user_id` varchar255
`project_id` varchar255
`status` varchar255
`progress` varchar255
`volume_size` int
`scheduled_at` datetime
`display_name` varchar255
`display_description` varchar255
`deleted` varchar36

indexes: none

all rows:
| column | row 1 |
|---|---|
| created_at | 2012-10-06T01:34:31 |
| updated_at | 2012-10-06T01:34:51 |
| deleted_at | 2012-10-06T01:34:57 |
| id | c5896a01-0f52-4d27-8e63-8b35f03ea197 |
| volume_id | 98ac28f5-77d8-476b-b3e1-c90a0fd3e880 |
| user_id | a1ef823458d24a68955fec6f3d390019 |
| project_id | 98333a1a28e746fa8c629c83a818ad57 |
| status | deleting |
| progress | 0% |
| volume_size | 32 |
| scheduled_at | null |
| display_name | celes-spark-gamma |
| display_description | null |
| deleted | c5896a01-0f52-4d27-8e63-8b35f03ea197 |

# `shadow_virtual_interfaces`  (rows=742)

columns:
`created_at` datetime: 429 distinct
`updated_at` datetime: all NULL
`deleted_at` datetime: 455 distinct, nulls=4
`id` int PK: unique identifier, 914..414194
`address` varchar255: all distinct
`network_id` int: 1=742
`uuid` varchar36: uuid, unique identifier
`instance_uuid` varchar36: uuid, unique identifier
`deleted` int: 735 distinct, 0..357436, avg=71492.8598, median=44084

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2013-09-17T02:44:27 | 2013-04-21T10:27:39 | 2013-04-29T17:33:31 |
| updated_at | null | null | null |
| deleted_at | null | 2013-08-08T11:04:14 | 2013-04-29T17:42:50 |
| id | 414194 | 389156 | 395382 |
| address | m1:c2:w7:oq:s5:sn | i6:pb:y4:5s:xq:gu | 72:21:23:ce:6s:vt |
| network_id | 1 | 1 | 1 |
| uuid | 19495c14-0877-43c3-95db-af103f6d47a6 | 14df6261-1aa6-4cbe-888c-02c5e8f5f4e2 | 6f49c5d3-1248-4252-afe5-0aa4d648ef43 |
| instance_uuid | 6154483e-317a-43bc-9563-cd945f59a242 | d2ca4501-0406-4a7f-b097-b913c35080f9 | 11eaca2f-70b3-49c7-ab1c-71a28f6d5f8c |
| deleted | 0 | 1 | 357436 |

# `snapshot_id_mappings`  (rows=1)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`id` int PK
`uuid` varchar36 NOTNULL
`deleted` int

indexes: none

all rows:
| column | row 1 |
|---|---|
| created_at | null |
| updated_at | null |
| deleted_at | null |
| id | 1 |
| uuid | 1285e294-bece-489e-a40d-eb64b2f0ee7b |
| deleted | 0 |

# `snapshots`  (rows=1)

columns:
`created_at` datetime
`updated_at` datetime
`deleted_at` datetime
`id` varchar36 PK
`volume_id` varchar36 NOTNULL
`user_id` varchar255
`project_id` varchar255
`status` varchar255
`progress` varchar255
`volume_size` int
`scheduled_at` datetime
`display_name` varchar255
`display_description` varchar255
`deleted` varchar36

indexes: none

all rows:
| column | row 1 |
|---|---|
| created_at | 2012-07-19T16:31:59 |
| updated_at | 2012-07-19T16:32:00 |
| deleted_at | null |
| id | 1285e294-bece-489e-a40d-eb64b2f0ee7b |
| volume_id | 98ac28f5-77d8-476b-b3e1-c90a0fd3e880 |
| user_id | 0be8fa0d641a4e778b9262bd2e5f40b5 |
| project_id | 6f9adccbd03e4d2186756896957a14bf |
| status | available |
| progress | 100% |
| volume_size | 32 |
| scheduled_at | null |
| display_name | novae-spear-flare |
| display_description | 3449069e92d320280a69b6f0a8175d55 |
| deleted | null |

# `volume_id_mappings`  (rows=65)

columns:
`created_at` datetime: 2014-12-08 21:45:01=6, 2014-12-08 21:45:02=6, 2014-05-29 13:53:00=4, 2012-11-11 02:08:44=3, 2013-10-09 18:54:44=3, 2014-12-08 21:45:03=3, 2013-09-26 01:41:18=2, 2013-10-17 20:41:25=2, 2014-05-29 13:53:01=2, 2012-12-17 20:48:21=1, 2013-09-25 22:25:09=1, 2013-10-03 22:42:14=1, 2013-10-03 22:43:33=1, 2013-10-18 04:41:06=1, 2014-12-08 21:45:04=1, nulls=28
`updated_at` datetime: all NULL
`deleted_at` datetime: all NULL
`id` int PK: unique identifier, 1..65
`uuid` varchar36 NOTNULL: uuid, unique identifier
`deleted` int: 0=65

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| created_at | 2014-12-08T21:45:04 | 2014-12-08T21:45:02 | 2014-12-08T21:45:02 |
| updated_at | null | null | null |
| deleted_at | null | null | null |
| id | 65 | 56 | 57 |
| uuid | a62fdf5f-b89d-472e-aab3-8c0bf393c905 | 32f005b0-4c4f-4b51-a6fb-357995e0f2d5 | a4762995-60fc-4eaf-959a-fe76efada723 |
| deleted | 0 | 0 | 0 |

- Skipped 45 empty table(s): `agent_builds`, `allocations`, `bw_usage_cache`, `cells`, `console_pools`, `consoles`, `dns_domains`, `inventories`, `project_user_quotas`, `provider_fw_rules`, `resource_provider_aggregates`, `resource_providers`, `security_group_default_rules`, `security_group_instance_association`, `shadow_agent_builds`, `shadow_aggregates`, `shadow_bw_usage_cache`, `shadow_cells`, `shadow_certificates`, `shadow_console_pools`, `shadow_consoles`, `shadow_dns_domains`, `shadow_floating_ips`, `shadow_instance_groups`, `shadow_instance_id_mappings`, `shadow_instance_types`, `shadow_migrate_version`, `shadow_networks`, `shadow_project_user_quotas`, `shadow_provider_fw_rules`, `shadow_quota_classes`, `shadow_quota_usages`, `shadow_quotas`, `shadow_s3_images`, `shadow_security_group_default_rules`, `shadow_security_group_instance_association`, `shadow_security_groups`, `shadow_snapshot_id_mappings`, `shadow_task_log`, `shadow_volume_id_mappings`, `shadow_volume_usage_cache`, `tags`, `task_log`, `virtual_interfaces`, `volume_usage_cache`
