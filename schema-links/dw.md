# Schema Links

- version: 0.0.5
- dialect: mysql
- database: dw
- schema: dw

## Declared PK/FK Links

No declared PK/FK links found.

## Inferred Links

### fclt
- inferred: cis_course_catalog.DEPARTMENT_CODE, cis_course_catalog.SUBJECT_CODE, course_catalog_subject_offered.DEPARTMENT_CODE, course_catalog_subject_offered.SUBJECT_CODE, drupal_course_catalog.DEPARTMENT_CODE, drupal_course_catalog.SUBJECT_CODE, fac_building.ACCESS_LEVEL_NAME, fac_floor.ACCESS_LEVEL, fac_floor.FLOOR, fac_floor.FLOOR_SORT_SEQUENCE, fac_floor.LEVEL_ID, fac_organization.COURSE, fac_organization.MAJOR_ORG, fac_organization.MAJOR_ORG_KEY, fac_organization.ORGANIZATION_ID, fac_organization.ORGANIZATION_LEVEL, fac_organization.ORG_PARENT_KEY, fac_rooms.ACCESS_LEVEL, fac_rooms.FLOOR, fac_rooms.MAJOR_USE_KEY, fac_rooms.ORGANIZATION_KEY, fac_rooms.USE_KEY, fclt_building.ACCESS_LEVEL_NAME, fclt_building_hist.ACCESS_LEVEL_NAME, fclt_building_hist_1.ACCESS_LEVEL_NAME, fclt_floor.ACCESS_LEVEL, fclt_floor.FLOOR, fclt_floor.FLOOR_SORT_SEQUENCE, fclt_floor.LEVEL_ID, fclt_floor_hist.ACCESS_LEVEL, fclt_floor_hist.FLOOR, fclt_floor_hist.FLOOR_SORT_SEQUENCE, fclt_floor_hist.LEVEL_ID, fclt_major_use_hist.FCLT_MAJOR_USE_KEY, fclt_organization.COURSE, fclt_organization.FCLT_MAJOR_ORG_KEY, fclt_organization.FCLT_ORGANIZATION_KEY, fclt_organization.FCLT_ORG_PARENT_KEY, fclt_organization.MAJOR_ORG, fclt_organization.ORGANIZATION_ID, fclt_organization.ORGANIZATION_LEVEL, fclt_organization_hist.COURSE, fclt_organization_hist.FCLT_MAJOR_ORG_KEY, fclt_organization_hist.FCLT_ORGANIZATION_KEY, fclt_organization_hist.FCLT_ORG_PARENT_KEY, fclt_organization_hist.ORGANIZATION_ID, fclt_organization_hist.ORGANIZATION_LEVEL, fclt_rooms.ACCESS_LEVEL, fclt_rooms.FCLT_MAJOR_USE_KEY, fclt_rooms.FCLT_ORGANIZATION_KEY, fclt_rooms.FCLT_USE_KEY, fclt_rooms.FLOOR, fclt_rooms_hist.ACCESS_LEVEL, fclt_rooms_hist.FCLT_MAJOR_USE_KEY, fclt_rooms_hist.FCLT_ORGANIZATION_KEY, fclt_rooms_hist.FCLT_USE_KEY, fclt_rooms_hist.FLOOR, hr_org_unit.HR_ORG_LEVEL1_SORT, hr_org_unit_new.HR_ORG_LEVEL1_SORT, ir_institution.INSTITUTION_SORT_ORDER, library_subject_offered.COURSE_NUMBER, library_subject_offered.COURSE_NUMBER_SORT, library_subject_offered.MASTER_COURSE_NUMBER, library_subject_offered.MASTER_COURSE_NUMBER_SORT, library_subject_offered.OFFER_DEPT_CODE, mit_student_directory.DEPARTMENT, mit_student_directory.STUDENT_YEAR, sis_course_description.COURSE, sis_course_description.COURSE_OPTION, sis_course_description.DEPARTMENT, sis_subject_code.DEPARTMENT_CODE, space_detail.FLOOR_KEY, space_detail.ROOM_NUMBER, student_degree_program.COURSE, student_degree_program.DEPARTMENT, subject_enrollable.OFFER_DEPT_CODE, subject_grouping.DEPARTMENT_CODE, subject_offered.COURSE_NUMBER_SORT, subject_offered.MASTER_COURSE_NUMBER, subject_offered.MASTER_COURSE_NUMBER_SORT, subject_offered.OFFER_DEPT_CODE, subject_offered_summary.COURSE_NUMBER, subject_offered_summary.OFFER_DEPT_CODE, subject_summary.DEPARTMENT_CODE, tip_subject_offered.COURSE_NUMBER, tip_subject_offered.COURSE_NUMBER_SORT, tip_subject_offered.MASTER_COURSE_NUMBER, tip_subject_offered.MASTER_COURSE_NUMBER_SORT, tip_subject_offered.OFFER_DEPT_CODE, warehouse_users.YEAR, zpm_rooms_load.ACCESS_LEVEL, zpm_rooms_load.FLOOR

### is
- inferred: academic_term_parameter.IS_CURRENT_TERM, academic_terms.IS_CURRENT_TERM, academic_terms.IS_REGULAR_TERM, academic_terms_all.IS_CURRENT_TERM, cis_course_catalog.IS_OFFERED_FALL_TERM, cis_course_catalog.IS_OFFERED_IAP, cis_course_catalog.IS_OFFERED_SPRING_TERM, cis_course_catalog.IS_OFFERED_SUMMER_TERM, cis_course_catalog.IS_OFFERED_THIS_YEAR, cis_course_catalog.IS_PRINTED_IN_BULLETIN, cis_course_catalog.IS_VARIABLE_UNITS, course_catalog_subject_offered.IS_DESIGN_SECTION, course_catalog_subject_offered.IS_LAB_SECTION, course_catalog_subject_offered.IS_LECTURE_SECTION, course_catalog_subject_offered.IS_MASTER_SECTION, course_catalog_subject_offered.IS_OFFERED_FALL_TERM, course_catalog_subject_offered.IS_OFFERED_IAP, course_catalog_subject_offered.IS_OFFERED_SPRING_TERM, course_catalog_subject_offered.IS_OFFERED_SUMMER_TERM, course_catalog_subject_offered.IS_OFFERED_THIS_YEAR, course_catalog_subject_offered.IS_PRINTED_IN_BULLETIN, course_catalog_subject_offered.IS_RECITATION_SECTION, course_catalog_subject_offered.IS_VARIABLE_UNITS, drupal_course_catalog.IS_DESIGN_SECTION, drupal_course_catalog.IS_LAB_SECTION, drupal_course_catalog.IS_LECTURE_SECTION, drupal_course_catalog.IS_MASTER_SECTION, drupal_course_catalog.IS_OFFERED_FALL_TERM, drupal_course_catalog.IS_OFFERED_IAP, drupal_course_catalog.IS_OFFERED_SPRING_TERM, drupal_course_catalog.IS_OFFERED_SUMMER_TERM, drupal_course_catalog.IS_OFFERED_THIS_YEAR, drupal_course_catalog.IS_RECITATION_SECTION, drupal_course_catalog.IS_VARIABLE_UNITS, iap_subject_detail.IS_CANCELLED, iap_subject_detail.IS_MULTIPLE_SESSION, library_reserve_matrl_detail.LIBRARY_MATERIAL_STATUS_KEY, moira_list.IS_ACTIVE, moira_list.IS_HIDDEN, moira_list.IS_MOIRA_GROUP, moira_list.IS_MOIRA_MAILING_LIST, moira_list.IS_NFS_GROUP, moira_list.IS_PUBLIC, se_person.IS_ACTIVE, sis_course_description.IS_DEGREE_GRANTING, sis_department.IS_DEGREE_GRANTING, student_degree_program.IS_DOUBLE_MAJOR, subject_offered.IS_CREATED_BY_DATA_WAREHOUSE, subject_offered.IS_DESIGN_SECTION, subject_offered.IS_LAB_SECTION, subject_offered.IS_LECTURE_SECTION, subject_offered.IS_MASTER_SECTION, subject_offered.IS_OSE_SUBJECT, subject_offered.IS_RECITATION_SECTION, subject_offered.IS_REPEATABLE_SUBJECT, time_month.IS_CLOSING_PERIOD, time_month.IS_CURRENT_FISCAL_PERIOD, time_month.IS_CURRENT_FISCAL_YEAR, time_month.IS_PREVIOUS_FISCAL_PERIOD, time_quarter.IS_CURRENT_QUARTER, time_quarter.IS_FUTURE_QUARTER, time_quarter.IS_NEXT_QUARTER, time_quarter.IS_PAST_QUARTER, time_quarter.IS_PREVIOUS_QUARTER, tip_subject_offered.IS_NO_COURSE_MATERIAL

### name
- inferred: drupal_employee_directory.HR_ORG_UNIT_TITLE, employee_directory.DEPARTMENT_NAME, fac_organization.HR_DEPARTMENT_NAME, fclt_organization.HR_DEPARTMENT_NAME, fclt_organization_hist.HR_DEPARTMENT_NAME, hr_faculty_roster.HR_ORG_UNIT_TITLE, hr_org_unit.HR_DEPARTMENT_NAME, hr_org_unit.HR_DEPARTMENT_NAME_ALPHA, hr_org_unit.HR_DEPARTMENT_NAME_LONG, hr_org_unit.HR_ORG_LEVEL1_NAME, hr_org_unit.HR_ORG_LEVEL2_NAME, hr_org_unit.HR_ORG_LEVEL3_NAME, hr_org_unit.HR_ORG_LEVEL4_NAME, hr_org_unit.HR_ORG_LEVEL5_NAME, hr_org_unit.HR_ORG_LEVEL6_NAME, hr_org_unit.ORG_HIER_ROOT_NAME, hr_org_unit.ORG_HIER_SCHOOL_AREA_NAME, hr_org_unit.ORG_HIER_TOP_LEVEL_NAME, hr_org_unit_new.HR_DEPARTMENT_NAME, hr_org_unit_new.HR_DEPARTMENT_NAME_ALPHA, hr_org_unit_new.HR_DEPARTMENT_NAME_LONG, hr_org_unit_new.HR_ORG_LEVEL2_NAME, hr_org_unit_new.HR_ORG_LEVEL3_NAME, hr_org_unit_new.HR_ORG_LEVEL5_NAME, hr_org_unit_new.HR_ORG_UNIT_TITLE, hr_org_unit_new.ORG_HIER_SCHOOL_AREA_NAME, hr_org_unit_new.ORG_HIER_TOP_LEVEL_NAME, se_person.ORGANIZATION, sis_course_description.SCHOOL_NAME_IN_COMMENCEMENT_BK, sis_department.SCHOOL_NAME_IN_COMMENCEMENT_BK, student_degree_program.SCHOOL_NAME_IN_COMMENCEMENT_BK, warehouse_users.UNIT_NAME

### building
- inferred: fac_building.PARENT_BUILDING_NUMBER, fac_building_address.BUILDING_KEY, fac_floor.BUILDING_KEY, fac_rooms.BUILDING_KEY, fclt_building.PARENT_BUILDING_NUMBER, fclt_building_address.BUILDING_NUMBER, fclt_building_address.FCLT_BUILDING_KEY, fclt_building_address_hist.BUILDING_NUMBER, fclt_building_address_hist.FCLT_BUILDING_KEY, fclt_building_hist.BUILDING_NUMBER, fclt_building_hist.BUILDING_SORT, fclt_building_hist.FCLT_BUILDING_KEY, fclt_building_hist.PARENT_BUILDING_NUMBER, fclt_building_hist_1.BUILDING_NUMBER, fclt_building_hist_1.BUILDING_SORT, fclt_building_hist_1.FCLT_BUILDING_KEY, fclt_building_hist_1.PARENT_BUILDING_NUMBER, fclt_floor.FCLT_BUILDING_KEY, fclt_floor_hist.FCLT_BUILDING_KEY, fclt_rooms.FCLT_BUILDING_KEY, fclt_rooms_hist.FCLT_BUILDING_KEY, space_detail.BUILDING_COMPONENT, space_detail.BUILDING_KEY, zpm_rooms_load.BUILDING_COMPONENT

### units
- inferred: cis_course_catalog.DESIGN_UNITS, cis_course_catalog.LAB_UNITS, cis_course_catalog.LECTURE_UNITS, cis_course_catalog.PREPARATION_UNITS, cis_course_catalog.TOTAL_UNITS, course_catalog_subject_offered.DESIGN_UNITS, course_catalog_subject_offered.LAB_UNITS, course_catalog_subject_offered.LECTURE_UNITS, course_catalog_subject_offered.PREPARATION_UNITS, course_catalog_subject_offered.TOTAL_UNITS, drupal_course_catalog.DESIGN_UNITS, drupal_course_catalog.LAB_UNITS, drupal_course_catalog.LECTURE_UNITS, drupal_course_catalog.PREPARATION_UNITS, drupal_course_catalog.TOTAL_UNITS, subject_offered_summary.LAB_UNITS, subject_offered_summary.LECTURE_UNITS, subject_offered_summary.PREPARATION_UNITS, subject_offered_summary.TOTAL_UNITS, subject_summary.DESIGN_UNITS, subject_summary.LAB_UNITS, subject_summary.LECTURE_UNITS, subject_summary.PREP_UNITS, subject_summary.TOTAL_UNITS

### subject
- inferred: iap_subject_detail.MAX_ENROLLMENT, subject_offered.CLUSTER_ENROLLMENT_NUMBER, subject_offered.SUBJECT_ENROLLMENT_NUMBER, subject_offered_summary.CLUSTER_ENROLLMENT_NUMBER, subject_offered_summary.SUBJECT_ENROLLMENT_NUMBER, subject_summary.CLUSTER_ENROLLMENT_1ST_CREDIT, subject_summary.CLUSTER_ENROLLMENT_1ST_LISTEN, subject_summary.CLUSTER_ENROLLMENT_5TH_CREDIT, subject_summary.CLUSTER_ENROLLMENT_5TH_LISTEN, subject_summary.CLUSTER_ENROLLMENT_CREDIT, subject_summary.CLUSTER_ENROLLMENT_FIFTH_WEEK, subject_summary.CLUSTER_ENROLLMENT_FIRST_WEEK, subject_summary.CLUSTER_ENROLLMENT_LISTEN, subject_summary.CLUSTER_ENROLLMENT_NUMBER, subject_summary.SUBJECT_ENROLLMENT_1ST_CREDIT, subject_summary.SUBJECT_ENROLLMENT_1ST_LISTEN, subject_summary.SUBJECT_ENROLLMENT_5TH_CREDIT, subject_summary.SUBJECT_ENROLLMENT_5TH_LISTEN, subject_summary.SUBJECT_ENROLLMENT_CREDIT, subject_summary.SUBJECT_ENROLLMENT_FIFTH_WEEK, subject_summary.SUBJECT_ENROLLMENT_FIRST_WEEK, subject_summary.SUBJECT_ENROLLMENT_LISTEN, subject_summary.SUBJECT_ENROLLMENT_NUMBER

### term
- inferred: cis_course_catalog.EFFECTIVE_TERM_CODE, course_catalog_subject_offered.EFFECTIVE_TERM_CODE, course_catalog_subject_offered.TERM_CODE, drupal_course_catalog.EFFECTIVE_TERM_CODE, drupal_course_catalog.SO_TERM_CODE, iap_subject_detail.TERM_CODE, library_reserve_matrl_detail.TERM_CODE, library_subject_offered.TERM_CODE, sis_course_description.FROM_TERM, sis_course_description.THRU_TERM, student_degree_program.FROM_TERM, student_degree_program.THRU_TERM, subject_enrollable.TERM_CODE, subject_grouping.TERM_CODE, subject_iap_schedule.TERM_CODE, subject_offered.TERM_CODE, subject_offered_summary.TERM_CODE, subject_summary.TERM_CODE, time_day.ACADEMIC_TERM_CODE, time_month.ACADEMIC_TERM, tip_detail.TERM_CODE, tip_subject_offered.TERM_CODE

### unit
- inferred: drupal_employee_directory.HR_ORG_UNIT_ID, fac_organization.HR_ORG_UNIT_ID, fclt_organization.HR_ORG_UNIT_ID, fclt_organization_hist.HR_ORG_UNIT_ID, hr_org_unit.HR_DEPARTMENT_ID, hr_org_unit.HR_ORG_LEVEL1_ID, hr_org_unit.HR_ORG_LEVEL2_ID, hr_org_unit.HR_ORG_LEVEL3_ID, hr_org_unit.HR_ORG_LEVEL4_ID, hr_org_unit.HR_ORG_LEVEL5_ID, hr_org_unit.HR_ORG_LEVEL6_ID, hr_org_unit.HR_ORG_LEVEL7_ID, hr_org_unit.HR_ORG_UNIT_ID, hr_org_unit_new.HR_DEPARTMENT_CODE, hr_org_unit_new.HR_ORG_LEVEL1_ID, hr_org_unit_new.HR_ORG_LEVEL2_ID, hr_org_unit_new.HR_ORG_LEVEL3_ID, hr_org_unit_new.HR_ORG_LEVEL4_ID, hr_org_unit_new.HR_ORG_LEVEL5_ID, hr_org_unit_new.HR_ORG_UNIT_ID, zpm_rooms_load.HR_ORG_UNIT_ID

### year
- inferred: academic_terms.ACADEMIC_YEAR, academic_terms.DEGREE_YEAR, academic_terms.FINANCIAL_AID_YEAR, academic_terms_all.ACADEMIC_YEAR, academic_terms_all.DEGREE_YEAR, academic_terms_all.FINANCIAL_AID_YEAR, cis_course_catalog.ACADEMIC_YEAR, course_catalog_subject_offered.ACADEMIC_YEAR, drupal_course_catalog.ACADEMIC_YEAR, library_reserve_catalog.CATALOG_YEAR, time_day.ACADEMIC_YEAR, time_day.CALENDAR_YEAR, time_day.FINANCIAL_AID_YEAR, time_day.FISCAL_YEAR, time_month.ACADEMIC_YEAR, time_month.CALENDAR_YEAR, time_month.FINANCIAL_AID_YEAR, time_month.FISCAL_YEAR, time_quarter.CALENDAR_YEAR, time_quarter.FISCAL_YEAR, tip_material.YEAR

### date
- inferred: course_catalog_subject_offered.LAST_ACTIVITY_DATE, drupal_course_catalog.LAST_ACTIVITY_DATE, fclt_building_address_hist.WAREHOUSE_LOAD_DATE, fclt_building_hist.WAREHOUSE_LOAD_DATE, fclt_building_hist_1.WAREHOUSE_LOAD_DATE, fclt_floor_hist.WAREHOUSE_LOAD_DATE, fclt_major_use_hist.WAREHOUSE_LOAD_DATE, fclt_organization_hist.WAREHOUSE_LOAD_DATE, fclt_rooms_hist.WAREHOUSE_LOAD_DATE, hr_org_unit.WAREHOUSE_LOAD_DATE, hr_org_unit_new.WAREHOUSE_LOAD_DATE, ir_institution.RECORD_CREATED_DATE, moira_list_detail.LAST_UPDATE_DATE, time_day.START_DATE, time_month.START_DATE, zip_canada.WAREHOUSE_LOAD_DATE, zip_usa.WAREHOUSE_LOAD_DATE

### code
- inferred: employee_directory.DEPARTMENT_NUMBER, fac_organization.HR_DEPARTMENT_CODE_OLD, fac_organization.ORGANIZATION_NUMBER, fclt_organization.HR_DEPARTMENT_CODE_OLD, fclt_organization.ORGANIZATION_NUMBER, fclt_organization_hist.HR_DEPARTMENT_CODE_OLD, fclt_organization_hist.ORGANIZATION_NUMBER, fclt_rooms.DEPT_CODE, fclt_rooms_hist.DEPT_CODE, hr_org_unit.HR_DEPARTMENT_CODE_OLD, hr_org_unit_new.HR_DEPARTMENT_CODE_OLD, sis_department.DEPT_BUDGET_CODE, space_detail.SPACE_UNIT_KEY, space_unit2.SPACE_UNIT_CODE, space_unit2.SPACE_UNIT_KEY, zpm_rooms_load.SPACE_UNIT_CODE

### name
- inferred: cis_course_catalog.DEPARTMENT_NAME, course_catalog_subject_offered.DEPARTMENT_NAME, drupal_course_catalog.DEPARTMENT_NAME, library_course_instructor.DEPARTMENT, library_subject_offered.OFFER_DEPT_NAME, mit_student_directory.DEPARTMENT_NAME, sis_admin_department.SIS_ADMIN_DEPARTMENT_NAME, sis_course_description.DEPARTMENT_NAME, sis_department.DEPARTMENT_NAME, sis_subject_code.DEPARTMENT_NAME, subject_grouping.DEPARTMENT_NAME, subject_offered.OFFER_DEPT_NAME, subject_offered_summary.OFFER_DEPT_NAME, subject_summary.DEPARTMENT_NAME, tip_subject_offered.OFFER_DEPT_NAME

### name
- inferred: drupal_employee_directory.LAST_NAME, drupal_employee_directory.MIDDLE_NAME, employee_directory.LAST_NAME, employee_directory.MIDDLE_NAME, employee_directory.PREFERRED_LAST_NAME, employee_directory.PREFERRED_MIDDLE_NAME, hr_faculty_roster.LAST_NAME, hr_faculty_roster.MIDDLE_NAME, mit_student_directory.LAST_NAME, mit_student_directory.MIDDLE_NAME, se_person.LAST_NAME, se_person.MIDDLE_NAME, warehouse_users.LAST_NAME, warehouse_users.MIDDLE_NAME

### subject
- inferred: subject_enrollable.MASTER_SUBJECT_ID, subject_enrollable.SUBJECT_ID, subject_enrollable.ULT_MASTER_SUBJECT_ID, subject_offered.MASTER_SUBJECT_ID, subject_offered.MASTER_SUBJECT_ID_SORT, subject_offered.SUBJECT_ID, subject_offered.SUBJECT_ID_SORT, subject_offered_summary.MASTER_SUBJECT_ID_SORT, subject_summary.MASTER_SUBJECT_ID_SORT, subject_summary.SUBJECT_ID, subject_summary.SUBJECT_ID_SORT, subject_summary.ULT_MASTER_SUBJECT_ID

### school
- inferred: library_subject_offered.OFFER_SCHOOL_NAME, sis_course_description.SCHOOL_NAME, sis_department.SCHOOL_NAME, sis_subject_code.SCHOOL_NAME, student_department.SCHOOL_NAME, subject_grouping.SCHOOL_NAME, subject_offered.OFFER_SCHOOL_NAME, subject_offered_summary.OFFER_SCHOOL_NAME, subject_summary.SCHOOL_NAME, tip_subject_offered.OFFER_SCHOOL_NAME

### name
- inferred: buildings.BUILDING_NAME, fac_building.BUILDING_NAME_LONG, fac_building.PARENT_BUILDING_NAME_LONG, fclt_building.BUILDING_NAME_LONG, fclt_building.PARENT_BUILDING_NAME_LONG, fclt_building_hist.BUILDING_NAME_LONG, fclt_building_hist.PARENT_BUILDING_NAME_LONG, fclt_building_hist_1.BUILDING_NAME_LONG, fclt_building_hist_1.PARENT_BUILDING_NAME_LONG

### cost
- inferred: fac_building.COST_CENTER_CODE, fac_building.COST_COLLECTOR_KEY, fclt_building.COST_CENTER_CODE, fclt_building.COST_COLLECTOR_KEY, fclt_building_hist.COST_CENTER_CODE, fclt_building_hist.COST_COLLECTOR_KEY, fclt_building_hist_1.COST_CENTER_CODE, fclt_building_hist_1.COST_COLLECTOR_KEY

### name
- inferred: fac_building.BUILDING_NAME, fac_building.PARENT_BUILDING_NAME, fclt_building.BUILDING_NAME, fclt_building.PARENT_BUILDING_NAME, fclt_building_hist.BUILDING_NAME, fclt_building_hist.PARENT_BUILDING_NAME, fclt_building_hist_1.BUILDING_NAME, fclt_building_hist_1.PARENT_BUILDING_NAME

### period
- inferred: fclt_building_address_hist.FISCAL_PERIOD, fclt_building_hist.FISCAL_PERIOD, fclt_building_hist_1.FISCAL_PERIOD, fclt_floor_hist.FISCAL_PERIOD, fclt_major_use_hist.FISCAL_PERIOD, fclt_organization_hist.FISCAL_PERIOD, fclt_rooms_hist.FISCAL_PERIOD, time_day.CALENDAR_PERIOD

### name
- inferred: drupal_employee_directory.FIRST_NAME, employee_directory.NAME_KNOWN_BY, employee_directory.PREFERRED_FIRST_NAME, hr_faculty_roster.FIRST_NAME, mit_student_directory.FIRST_NAME, se_person.FIRST_NAME, warehouse_users.FIRST_NAME

### num
- inferred: fac_building.NUM_OF_ROOMS, fclt_building.NUM_OF_ROOMS, fclt_building_hist.NUM_OF_ROOMS, fclt_building_hist_1.NUM_OF_ROOMS, space_detail.ROOM_COUNTER, space_detail.ROOM_SQUARE_FOOTAGE, subject_offered.NUM_ENROLLED_STUDENTS

### subject
- inferred: library_subject_offered.COURSE_NUMBER_DESC, library_subject_offered.MASTER_COURSE_NUMBER_DESC, sis_subject_code.SUBJECT_CODE_DESC, subject_offered.COURSE_NUMBER_DESC, subject_offered.MASTER_COURSE_NUMBER_DESC, tip_subject_offered.COURSE_NUMBER_DESC, tip_subject_offered.MASTER_COURSE_NUMBER_DESC

### key
- inferred: fac_organization.D_CODE, fclt_org_dlc_key.DLC_KEY, fclt_organization.DLC_KEY, fclt_organization_hist.DLC_KEY, space_unit.DLC_KEY, space_unit2.DLC_KEY

### type
- inferred: drupal_course_catalog.SO_CLUSTER_TYPE, sis_term_address_category.LIVING_GROUP_TYPE, subject_offered.CLUSTER_TYPE, subject_offered_summary.CLUSTER_TYPE, subject_summary.CLUSTER_TYPE, zip_usa.ZIP_TYPE

### height
- inferred: cis_hass_attribute.ICON_HEIGHT, fac_building.BUILDING_HEIGHT, fclt_building.BUILDING_HEIGHT, fclt_building_hist.BUILDING_HEIGHT, fclt_building_hist_1.BUILDING_HEIGHT

### master
- inferred: master_dept_dcode_parent.PARENT_D_CODE, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_1_CODE, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_2_CODE, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_3_CODE, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_4_CODE

### name
- inferred: master_dept_dcode_parent.PARENT_D_NAME, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_1_NAME, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_2_NAME, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_3_NAME, master_dept_hierarchy.MASTER_DEPT_HIER_LEVEL_4_NAME

### organization
- inferred: fac_rooms.ORGANIZATION_NAME, fclt_organization.ORGANIZATION, fclt_organization_hist.ORGANIZATION, fclt_rooms.ORGANIZATION_NAME, fclt_rooms_hist.ORGANIZATION_NAME

### school
- inferred: sis_department.SCHOOL_CODE, sis_subject_code.SCHOOL_CODE, student_department.SCHOOL_CODE, subject_enrollable.OFFER_SCHOOL_CODE, subject_summary.SCHOOL_CODE

### term
- inferred: drupal_course_catalog.SO_TERM_DESCRIPTION, sis_course_description.FROM_TERM_DESCRIPTION, sis_course_description.THRU_TERM_DESCRIPTION, time_day.ACADEMIC_TERM_DESCRIPTION, time_month.ACADEMIC_TERM_DESCRIPTION

### code
- inferred: fac_building_address.POSTAL_CODE, fclt_building_address.POSTAL_CODE, fclt_building_address_hist.POSTAL_CODE, zip_usa.ZIP_CODE

### dlc
- inferred: hr_org_unit.DLC_KEY, hr_org_unit_new.DLC_KEY, master_dept_hierarchy_links.DLC_CODE, roles_fin_pa.DLC_KEY

### key
- inferred: fac_rooms.FLOOR_KEY, fclt_floor_hist.FCLT_FLOOR_KEY, fclt_rooms.FCLT_FLOOR_KEY, fclt_rooms_hist.FCLT_FLOOR_KEY

### num
- inferred: library_subject_offered.NUM_ENROLLED_STUDENTS, space_supervisor_usage.NUM_OF_SUPERVISEES, subject_offered_summary.NUM_ENROLLED_STUDENTS, tip_subject_offered.NUM_ENROLLED_STUDENTS

### subject
- inferred: iap_subject_detail.IAP_SUBJECT_PERSON_KEY, iap_subject_detail.IAP_SUBJECT_SESSION_KEY, iap_subject_person.IAP_SUBJECT_PERSON_KEY, iap_subject_session.IAP_SUBJECT_SESSION_KEY

### use
- inferred: fac_rooms.MAJOR_USE_DESC, fclt_major_use_hist.MAJOR_USE, fclt_rooms.MAJOR_USE_DESC, fclt_rooms_hist.MAJOR_USE_DESC

### city
- inferred: fac_building_address.ADDRESS_CITY_ID, fclt_building_address.ADDRESS_CITY_ID, fclt_building_address_hist.ADDRESS_CITY_ID

### code
- inferred: sis_lookup.CODE, subject_offered.HGN_CODE, subject_offered_summary.HGN_CODE

### organization
- inferred: fclt_organization.DLC_NAME, fclt_organization_hist.DLC_NAME, space_unit.SPACE_UNIT

### wings
- inferred: fac_floor.BUILDING_WINGS_ID, fclt_floor.BUILDING_WINGS_ID, fclt_floor_hist.BUILDING_WINGS_ID

### count
- inferred: space_supervisor_usage.DEPT_COUNT, tip_detail.RECORD_COUNT

### four
- inferred: cip.FOUR_DIGIT_CODE, cip_with_version.FOUR_DIGIT_CODE

### program
- inferred: cip_with_version.PROGRAM_CODE, sis_course_description.CIP_PROGRAM_CODE

### room
- inferred: space_detail.BUILDING_ROOM_NAME, zpm_rooms_load.BUILDING_ROOM

### state
- inferred: ir_institution.STATE, zip_usa.STATE_ABBR

### subject
- inferred: iap_subject_session.SESSION_DATE, subject_iap_schedule.IAP_DATE

### subject
- inferred: iap_subject_session.SESSION_LOCATION, subject_iap_schedule.MEET_PLACE

### subject
- inferred: subject_enrollable.SUBJECT_GROUP_ID, subject_offered_summary.SUBJECT_GROUPING_KEY

### time
- inferred: iap_subject_session.SESSION_END_TIME, subject_iap_schedule.MEET_END_TIME

### time
- inferred: iap_subject_session.SESSION_START_TIME, subject_iap_schedule.MEET_START_TIME

### title
- inferred: subject_enrollable.SUBJECT_TITLE_LONG, subject_offered.SUBJECT_TITLE

### title
- inferred: cip.PROGRAM_TITLE, cip_with_version.PROGRAM_TITLE

### type
- inferred: subject_attribute.SUBJECT_ATTRIBUTE_TYPE, zip_usa.CITY_TYPE

### unit
- inferred: hr_org_unit.HR_DEPARTMENT_CODE, hr_org_unit_new.HR_DEPARTMENT_ABBR

### zip
- inferred: zip_canada.PROVINCE_NAME, zip_usa.CITY_NAME
