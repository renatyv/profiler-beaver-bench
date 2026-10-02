---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:19:49.586226Z
dialect: mysql
database: dw
schema: dw
profile_lines: 3756
profile_sha256: b4bd59add51fb30d9adf91417597206308d2f7128357bd4d0cab86bcac2020df
enriched_model: openrouter/openai/gpt-6-luna
enriched_at_utc: 2026-09-29T14:47:42.709920+00:00
toc_sha256: 6169dadf0159bbeee70ae2c9664df59127314a239d24a682f1e1bee97ef37477

---

`academic_term_parameter` (rows=3): lines 10-34 — SIS parameters identifying current, previous, and upcoming terms; compact selector distinct from the full term calendar.
`academic_terms` (rows=144): lines 36-92 — Recent academic-term calendar with dates, selectors, regular-term flags, and status metadata.
`academic_terms_all` (rows=300): lines 94-142 — Expanded historical and future term calendar; unlike academic_terms, omits regular-term flags and spans broader years.
`buildings` (rows=211): lines 144-170 — Building directory with names, street addresses, and gross and assignable floor area.
`cip` (rows=3059): lines 172-198 — CIP program classification entries from mixed versions; unlike cip_with_version, version is not part of its key.
`cip_with_version` (rows=6350): lines 200-226 — CIP program classifications keyed by program and version, retaining multiple classification revisions.
`cis_course_catalog` (rows=10000): lines 228-352 — Historical CIS course catalog metadata, including annual offerings and course attributes, without term-specific sections.
`cis_hass_attribute` (rows=17): lines 354-384 — Reference descriptions and display metadata for HASS attributes and earlier GIR categories.
`course_catalog_subject_offered` (rows=10000): lines 386-532 — Comprehensive course catalog and term offering records, including section, instructor, meeting, and course attributes.
`drupal_course_catalog` (rows=10000): lines 534-686 — Drupal course catalog feed, including bundled offered-term and section details; restricted to its catalog subset.
`drupal_employee_directory` (rows=10000): lines 688-732 — Drupal-sourced employee contact directory with HR unit and employee classification, distinct from the richer employee_directory.
`employee_directory` (rows=10000): lines 734-790 — Employee contact directory with preferred names, Kerberos names, and department; lacks the HR classifications in drupal_employee_directory.
`fac_building` (rows=242): lines 792-864 — Current facilities building inventory with area, location, occupancy, ownership, and construction details.
`fac_building_address` (rows=785): lines 866-904 — Current facilities addresses by building and address purpose, unlike the single-address building directory.
`fac_floor` (rows=1079): lines 906-936 — Current facilities floor areas and access metadata, keyed to buildings.
`fac_major_use` (rows=14): lines 938-956 — Current reference codes defining facilities major-use categories and assignability.
`fac_organization` (rows=169): lines 958-1004 — Current facilities organization hierarchy linked to HR departments and major organizations.
`fac_rooms` (rows=10000): lines 1006-1064 — Current facilities room inventory with area, major use, organization, floor, and access level.
`fclt_building` (rows=242): lines 1066-1138 — Current FCLT building inventory, matching fac_building with FCLT-specific keys and facility attributes.
`fclt_building_address` (rows=785): lines 1140-1180 — Current FCLT building addresses by purpose; the current counterpart to fclt_building_address_hist.
`fclt_building_address_hist` (rows=10000): lines 1182-1226 — Fiscal-period snapshots of FCLT building addresses, unlike the current address table.
`fclt_building_hist` (rows=10000): lines 1228-1304 — Fiscal-period history of FCLT building characteristics; parallel historical copy of current fclt_building.
`fclt_building_hist_1` (rows=10000): lines 1306-1382 — Duplicate-shaped fiscal-period building history copy, distinct from fclt_building_hist by its alternate loaded dataset.
`fclt_floor` (rows=1079): lines 1384-1414 — Current FCLT floor-area inventory with floor ordering, wings, and access metadata.
`fclt_floor_hist` (rows=10000): lines 1416-1450 — Fiscal-period snapshots of FCLT floor areas and access, unlike current fclt_floor.
`fclt_major_use` (rows=14): lines 1452-1470 — Current FCLT reference codes describing room-use categories and assignability.
`fclt_major_use_hist` (rows=1680): lines 1472-1494 — Fiscal-period history of FCLT major-use descriptions and assignability.
`fclt_org_dlc_key` (rows=168): lines 1496-1508 — Crosswalk from FCLT organization keys to DLC identifiers, separate from organization descriptions.
`fclt_organization` (rows=180): lines 1510-1558 — Current FCLT organization hierarchy enriched with DLC and HR department mappings.
`fclt_organization_hist` (rows=10000): lines 1560-1612 — Fiscal-period snapshots of FCLT organizations and their HR/DLC mappings.
`fclt_rooms` (rows=10000): lines 1614-1674 — Current FCLT room inventory with area, floor, major use, organization, and access.
`fclt_rooms_hist` (rows=10000): lines 1676-1740 — Historical FCLT room inventory for a fiscal period, unlike the current room table.
`frc_fiscal_periods` (rows=10): lines 1742-1756 — Fiscal reporting period lookup mapping time-month keys to calendar and fiscal period labels.
`hr_faculty_roster` (rows=681): lines 1758-1798 — Faculty roster with appointment type, academic rank, degree, and HR organization.
`hr_org_unit` (rows=641): lines 1800-1882 — HR organization hierarchy with department codes, levels, and DLC mapping; predecessor-style version to hr_org_unit_new.
`hr_org_unit_new` (rows=691): lines 1884-1952 — Revised HR organization hierarchy with updated department coding and expanded top-level areas.
`iap_subject_category` (rows=49): lines 1954-1970 — Reference categories and descriptions classifying Independent Activities Period offerings.
`iap_subject_detail` (rows=465): lines 1972-2018 — IAP activity catalog with enrollment rules, fees, category, sponsor, term, and session/person links.
`iap_subject_person` (rows=1113): lines 2020-2046 — People associated with IAP activities, their roles, affiliations, and contact details.
`iap_subject_session` (rows=1199): lines 2048-2076 — Scheduled IAP activity sessions with dates, times, locations, and optional session descriptions.
`iap_subject_sponsor` (rows=68): lines 2078-2094 — Reference list of organizations sponsoring IAP activities, categorized by sponsor type.
`ir_institution` (rows=10000): lines 2096-2130 — Postsecondary institution directory with names, addresses, country, and Carnegie category classification.
`library_course_instructor` (rows=10000): lines 2132-2158 — Historical library course-instructor directory with teaching dates and associated library unit.
`library_material_status` (rows=6): lines 2160-2176 — Lookup translating library course-reserve material status codes into descriptions.
`library_reserve_catalog` (rows=10000): lines 2178-2210 — Library catalog records for materials placed on course reserve, with bibliographic details.
`library_reserve_matrl_detail` (rows=10000): lines 2212-2234 — Links course reserves to catalog materials and library status for a term.
`library_subject_offered` (rows=10000): lines 2236-2284 — Library-oriented course offerings by term, including enrolled students and responsible faculty.
`master_dept_dcode_parent` (rows=340): lines 2286-2308 — Department code hierarchy mapping each master department code to its parent.
`master_dept_hierarchy` (rows=310): lines 2310-2346 — Standard master DLC hierarchy, arranging departments across named levels.
`master_dept_hierarchy_links` (rows=10000): lines 2348-2370 — Crosswalk connecting master DLCs to linked objects from finance, HR, facilities, and SIS.
`mit_holiday_closing_calendar` (rows=580): lines 2372-2388 — MIT holiday, emergency closing, and special closure dates with closing classifications.
`mit_student_directory` (rows=10000): lines 2390-2422 — Student contact directory with department and student year, distinct from employee and general-person directories.
`moira_list` (rows=10000): lines 2424-2450 — Moira mailing lists and groups with visibility, activity, and group-type flags.
`moira_list_detail` (rows=10000): lines 2452-2476 — Moira list membership records with member identity and last-update date.
`moira_list_owner` (rows=10000): lines 2478-2494 — Moira list-owner identities and owner types, separate from list membership.
`person_auth_area` (rows=10000): lines 2496-2516 — User-level indicators for financial, HR, and payroll authorization areas.
`roles_fin_pa` (rows=1395): lines 2518-2530 — Mapping of usernames to DLCs for financial planning and analysis roles.
`se_person` (rows=10000): lines 2532-2564 — Active-person directory with MIT ID, Kerberos name, organization, employee type, and payroll rank.
`sis_admin_department` (rows=179): lines 2566-2588 — SIS administrative departments with department contact and clearing cost-collector information.
`sis_course_description` (rows=695): lines 2590-2642 — SIS course descriptions and degree-granting metadata effective across term ranges.
`sis_department` (rows=128): lines 2644-2678 — SIS department reference with school, degree-granting, budget, and historical name metadata.
`sis_lookup` (rows=67): lines 2680-2696 — SIS code-description lookup for registration, enrollment, load-level, and HGN categories.
`sis_subject_code` (rows=221): lines 2698-2722 — SIS subject/course-number mapping with department and school descriptions.
`sis_term_address_category` (rows=112): lines 2724-2748 — SIS term-address categories identifying residential groups and validity dates.
`space_detail` (rows=10000): lines 2750-2780 — Room-level space inventory with square footage, usage, floor, building, and space-unit assignment.
`space_floor` (rows=49): lines 2782-2798 — Reference labels for facilities floor codes used by the space inventory.
`space_supervisor_usage` (rows=2135): lines 2800-2826 — Supervisor-level space and research-volume measures with supervisee counts and departments.
`space_unit` (rows=150): lines 2828-2848 — Current space-unit crosswalk from facilities organizations to DLCs and unit names.
`space_unit2` (rows=139): lines 2850-2868 — Alternate space-unit reference of unit codes and DLCs, without the facilities organization key mapping.
`space_usage` (rows=88): lines 2870-2884 — Reference descriptions for coded room and space usage types.
`student_degree_program` (rows=1202): lines 2886-2932 — Degree, department, course, and term-validity combinations used to describe student programs.
`student_department` (rows=79): lines 2934-2952 — Student-system department and school lookup, a narrower directory than sis_department.
`student_ethnic_subgroup` (rows=46): lines 2954-2974 — Reference hierarchy of student ethnicity groups, subgroups, and codes.
`subject_attribute` (rows=104): lines 2976-2998 — SIS subject attribute codes with descriptions, type, and reporting labels.
`subject_enrollable` (rows=10000): lines 3000-3030 — Enrollable historical Harvard cross-registration subjects and their cluster memberships by term.
`subject_grouping` (rows=10000): lines 3032-3054 — Term-specific subject grouping directory associating departments and schools with group identifiers.
`subject_iap_schedule` (rows=1199): lines 3056-3084 — IAP schedule dates, meeting times, places, and remarks; activity/session identifiers are not populated.
`subject_offered` (rows=10000): lines 3086-3188 — Detailed term-level offered subject sections and enrollment, primarily Harvard cross-registration records.
`subject_offered_summary` (rows=10000): lines 3190-3256 — Term-level subject offering summary with course units, cluster details, and enrollment counts.
`subject_summary` (rows=10000): lines 3258-3348 — Term-level subject and cluster enrollment snapshots, including first- and fifth-week counts.
`time_day` (rows=10000): lines 3350-3388 — Daily calendar linking fiscal and calendar periods to academic terms and financial-aid years.
`time_month` (rows=640): lines 3390-3444 — Monthly fiscal/calendar periods with closing-period flags and academic-term mappings.
`time_quarter` (rows=144): lines 3446-3494 — Fiscal and calendar quarter calendar with certification dates and past/current/future indicators.
`tip_detail` (rows=10000): lines 3496-3520 — Course-term links to textbook materials, material statuses, and ISBNs for TIP records.
`tip_material` (rows=10000): lines 3522-3554 — Textbook bibliographic and pricing reference for materials used in course offerings.
`tip_material_status` (rows=12): lines 3556-3572 — Lookup translating TIP course-material status codes into descriptions.
`tip_subject_offered` (rows=10000): lines 3574-3624 — Term-specific course offerings used by TIP, including course, department, faculty, and enrollment.
`top_level_domain` (rows=249): lines 3626-3642 — Reference of internet top-level domain codes and country or domain descriptions.
`warehouse_users` (rows=10000): lines 3644-3682 — Warehouse user directory combining employee/student type, unit, contact, and appointment details.
`zip_canada` (rows=10000): lines 3684-3704 — Canadian postal-code lookup for city and province, represented here for Newfoundland.
`zip_usa` (rows=10000): lines 3706-3730 — US ZIP-code lookup with city, county, state, and ZIP/city classifications.
`zpm_rooms_load` (rows=10000): lines 3732-3754 — Loaded room-use assignments linking building-room locations to space unit and HR organization codes.
Summary: lines 3756-3756
