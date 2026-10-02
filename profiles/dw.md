---
generator: db-snooper
version: 0.0.34
generated_at_utc: 2026-08-24T21:19:49.586226Z
dialect: mysql
database: dw
schema: dw
---

# `academic_term_parameter`  (rows=3)

columns:
`TERM_PARAMETER` varchar127
`TERM_INDICATOR` varchar127
`TERM_CODE` varchar127
`TERM_DESCRIPTION` varchar127
`TERM_START_DATE` varchar255
`TERM_END_DATE` varchar255
`TERM_LAST_DAY_BEFORE_NEXT_TERM` varchar255
`IS_CURRENT_TERM` varchar127

indexes: `TERM_CODE`

all rows:
| column | row 1 | row 2 | row 3 |
|---|---|---|---|
| TERM_PARAMETER | SIS_CURRENT_TERM | SIS_PREVIOUS_TERM | SIS_UPCOMING_TERM |
| TERM_INDICATOR | C | P | F |
| TERM_CODE | 2025FA | 2024SU | 2025JA |
| TERM_DESCRIPTION | Fall Term 2024-2025 | Summer Term 2024 | January Term 2024-2025 |
| TERM_START_DATE | 03-SEP-24 | 10-JUN-24 | 06-JAN-25 |
| TERM_END_DATE | 20-DEC-24 | 20-AUG-24 | 31-JAN-25 |
| TERM_LAST_DAY_BEFORE_NEXT_TERM | 05-JAN-25 | 02-SEP-24 | 31-JAN-25 |
| IS_CURRENT_TERM | Y | N | N |

# `academic_terms`  (rows=144)

columns:
`ACADEMIC_TERMS_KEY` varchar127: all distinct
`TERM_CODE` varchar127: all distinct
`TERM_DESCRIPTION` varchar127: all distinct
`TERM_SELECTOR` varchar127: all distinct
`TERM_START_DATE` varchar255: all distinct
`TERM_END_DATE` varchar255: all distinct
`ACADEMIC_YEAR` varchar127: digits, 36 distinct
`ACADEMIC_YEAR_DESC` varchar127: 36 distinct
`IS_CURRENT_TERM` varchar127: "N"=143, "Y"=1
`IS_REGULAR_TERM` varchar127: "N"=72, "Y"=72
`TERM_STATUS_INDICATOR` varchar127: "P"=120, "F"=2, "C"=1, nulls=21
`TERM_STATUS` varchar127: "Previous"=120, "Unspecified"=21, "Future"=2, "Current"=1
`FINANCIAL_AID_YEAR` varchar127: digits, 37 distinct, nulls=17
`DEGREE_YEAR` varchar127: digits, 37 distinct, nulls=17
`LAST_DAY_OF_FINAL_EXAM` varchar255: all distinct
`PRE_REGISTRATION_START_DAY` varchar255: 73 distinct, nulls=6
`REGISTRATION_DAY` varchar255: all distinct
`FIRST_DAY_OF_CLASSES` varchar255: all distinct, nulls=21
`LAST_DAY_OF_CLASSES` varchar255: all distinct, nulls=21
`ADD_DATE` varchar255: all distinct, nulls=72
`DROP_DATE` varchar255: all distinct, nulls=72
`GRADUATE_AWARD_START_DATE` varchar255: all distinct, nulls=51
`GRADUATE_AWARD_END_DATE` varchar255: all distinct, nulls=51
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=144

indexes: `ACADEMIC_TERMS_KEY`, `TERM_CODE`, `TERM_START_DATE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ACADEMIC_TERMS_KEY | 2030SU | 2029SU | 2025SP |
| TERM_CODE | 2030SU | 2029SU | 2025SP |
| TERM_DESCRIPTION | Summer Term 2030 | Summer Term 2029 | Spring Term 2024-2025 |
| TERM_SELECTOR | 2030SU-Summer Term 2030 | 2029SU-Summer Term 2029 | 2025SP-Spring Term 2024-2025 |
| TERM_START_DATE | 10-JUN-30 | 05-JUN-29 | 01-FEB-25 |
| TERM_END_DATE | 20-AUG-30 | 15-AUG-29 | 21-MAY-25 |
| ACADEMIC_YEAR | 2030 | 2029 | 2025 |
| ACADEMIC_YEAR_DESC | Academic Year 2029-2030 | Academic Year 2028-2029 | Academic Year 2024-2025 |
| IS_CURRENT_TERM | N | N | N |
| IS_REGULAR_TERM | N | N | Y |
| TERM_STATUS_INDICATOR | null | null | F |
| TERM_STATUS | Unspecified | Unspecified | Future |
| FINANCIAL_AID_YEAR | 2031 | 2030 | 2025 |
| DEGREE_YEAR | 2031 | 2030 | 2025 |
| LAST_DAY_OF_FINAL_EXAM | 18-AUG-30 | 18-AUG-29 | 21-MAY-25 |
| PRE_REGISTRATION_START_DAY | 01-MAY-30 | 01-MAY-29 | 01-DEC-24 |
| REGISTRATION_DAY | 08-JUN-30 | 08-JUN-29 | 31-JAN-25 |
| FIRST_DAY_OF_CLASSES | null | null | 03-FEB-25 |
| LAST_DAY_OF_CLASSES | null | null | 13-MAY-25 |
| ADD_DATE | null | null | 07-MAR-25 |
| DROP_DATE | null | null | 22-APR-25 |
| GRADUATE_AWARD_START_DATE | null | null | 16-JAN-25 |
| GRADUATE_AWARD_END_DATE | null | null | 31-MAY-25 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `academic_terms_all`  (rows=300)

columns:
`ACADEMIC_TERMS_KEY` varchar127: all distinct
`TERM_CODE` varchar127: all distinct
`TERM_DESCRIPTION` varchar127: all distinct
`TERM_SELECTOR` varchar127: all distinct
`TERM_START_DATE` varchar255: all distinct
`TERM_END_DATE` varchar255: all distinct
`ACADEMIC_YEAR` varchar127: digits, 80 distinct
`ACADEMIC_YEAR_DESC` varchar127: 80 distinct
`IS_CURRENT_TERM` varchar127: "N"=299, "Y"=1
`TERM_STATUS_INDICATOR` varchar127: "P"=276, "F"=2, "C"=1, nulls=21
`FINANCIAL_AID_YEAR` varchar127: 73 distinct, nulls=41
`DEGREE_YEAR` varchar127: 73 distinct, nulls=41
`LAST_DAY_OF_FINAL_EXAM` varchar255: all distinct
`PRE_REGISTRATION_START_DAY` varchar255: 117 distinct, nulls=118
`REGISTRATION_DAY` varchar255: all distinct
`FIRST_DAY_OF_CLASSES` varchar255: all distinct, nulls=48
`LAST_DAY_OF_CLASSES` varchar255: 232 distinct, nulls=48
`GRADUATE_AWARD_START_DATE` varchar255: all distinct, nulls=156
`GRADUATE_AWARD_END_DATE` varchar255: all distinct, nulls=156
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=300

indexes: `ACADEMIC_TERMS_KEY`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ACADEMIC_TERMS_KEY | 2030SU | 1955SP | 2021FA |
| TERM_CODE | 2030SU | 1955SP | 2021FA |
| TERM_DESCRIPTION | Summer Term 2030 | Spring Term 1954-1955 | Fall Term 2020-2021 |
| TERM_SELECTOR | 2030SU-Summer Term 2030 | 1955SP-Spring Term 1954-1955 | 2021FA-Fall Term 2020-2021 |
| TERM_START_DATE | 10-JUN-30 | 01-FEB-55 | 31-AUG-20 |
| TERM_END_DATE | 20-AUG-30 | 05-JUN-55 | 18-DEC-20 |
| ACADEMIC_YEAR | 2030 | 1955 | 2021 |
| ACADEMIC_YEAR_DESC | Academic Year 2029-2030 | Academic Year 1954-1955 | Academic Year 2020-2021 |
| IS_CURRENT_TERM | N | N | N |
| TERM_STATUS_INDICATOR | null | P | P |
| FINANCIAL_AID_YEAR | 2031 | 1960 | 2021 |
| DEGREE_YEAR | 2031 | 1960 | 2021 |
| LAST_DAY_OF_FINAL_EXAM | 18-AUG-30 | 30-MAY-55 | 18-DEC-20 |
| PRE_REGISTRATION_START_DAY | 01-MAY-30 | null | 20-JUL-20 |
| REGISTRATION_DAY | 08-JUN-30 | 05-FEB-55 | 31-AUG-20 |
| FIRST_DAY_OF_CLASSES | null | null | 01-SEP-20 |
| LAST_DAY_OF_CLASSES | null | null | 09-DEC-20 |
| GRADUATE_AWARD_START_DATE | null | null | 01-SEP-20 |
| GRADUATE_AWARD_END_DATE | null | null | 15-JAN-21 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `buildings`  (rows=211)

columns:
`BUILDING_KEY` varchar127: all distinct
`BUILDING_NUMBER` varchar127: all distinct
`BUILDING_NAME` varchar127: 204 distinct
`BUILDING_STREET_ADDRESS` varchar127: 147 distinct
`BUILDING_MAILING_ADDRESS` varchar127: all NULL
`BLDG_GROSS_SQUARE_FOOTAGE` int: 202 distinct, 0..466722, avg=66391.2417, median=36051
`BLDG_ASSIGNABLE_SQUARE_FOOTAGE` int: 197 distinct, 0..285682, avg=40643.218, median=22856
`BUILDING_COUNTER` int: 1=211
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=211

indexes: `BUILDING_KEY`, `BUILDING_NUMBER`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| BUILDING_KEY | WW15 | W87 | NE18 |
| BUILDING_NUMBER | WW15 | W87 | NE18 |
| BUILDING_NAME | Building WW15 | Graduate Junction (W87) | 255 Main Street |
| BUILDING_STREET_ADDRESS | 350  BROOKLINE ST | 269 VASSAR ST | 255 MAIN ST |
| BUILDING_MAILING_ADDRESS | null | null | null |
| BLDG_GROSS_SQUARE_FOOTAGE | 42146 | 0 | 33045 |
| BLDG_ASSIGNABLE_SQUARE_FOOTAGE | 37271 | 0 | 28129 |
| BUILDING_COUNTER | 1 | 1 | 1 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `cip`  (rows=3059)

columns:
`PROGRAM_CODE` varchar127: all distinct
`PROGRAM_TITLE` varchar127: 2773 distinct, nulls=1
`CATEGORY_CODE` varchar127: digits, 52 distinct
`CATEGORY_TITLE` varchar127: 86 distinct
`FOUR_DIGIT_CODE` varchar127: digits, 582 distinct
`FOUR_DIGIT_TITLE` varchar127: 729 distinct, nulls=2
`NOTE` varchar127: 342 distinct, nulls=628
`WAREHOUSE_LOAD_DATE` varchar255: "17-MAY-23"=2142, "11-JUN-14"=917
`VERSION` varchar127: "2020"=2142, "1990"=606, "2000"=159, "2010"=152

indexes: `PROGRAM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| PROGRAM_CODE | 619999 | 030404 | 305301 |
| PROGRAM_TITLE | Medical Residency/Fellowship Programs, Other | Forest Products Technology/Technician | Thanatology |
| CATEGORY_CODE | 61 | 3 | 30 |
| CATEGORY_TITLE | MEDICAL RESIDENCY/FELLOWSHIP PROGRAMS | CONSERVATION AND RENEWABLE NATURAL RESOURCES | MULTI/INTERDISCIPLINARY STUDIES |
| FOUR_DIGIT_CODE | 6199 | 0304 | 3053 |
| FOUR_DIGIT_TITLE | Medical Residency/Fellowship Programs, Other | Forest Production and Processing | Thanatology |
| NOTE | New in 2020 | null | New in 2020 |
| WAREHOUSE_LOAD_DATE | 17-MAY-23 | 11-JUN-14 | 17-MAY-23 |
| VERSION | 2020 | 1990 | 2020 |

# `cip_with_version`  (rows=6350)

columns:
`CIP_WITH_VERSION_KEY` varchar127: digits, all distinct
`VERSION` varchar127: "2020"=2142, "2010"=1720, "2000"=1432, "1990"=1056
`PROGRAM_CODE` varchar127: digits, 2759 distinct
`PROGRAM_TITLE` varchar127: 3226 distinct
`CATEGORY_CODE` varchar127: digits, 53 distinct
`CATEGORY_TITLE` varchar127: 94 distinct
`FOUR_DIGIT_CODE` varchar127: digits, 561 distinct
`FOUR_DIGIT_TITLE` varchar127: 767 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "17-MAY-23"=2142, "17-OCT-10"=1720, "27-MAR-03"=1432, "09-JAN-02"=1056

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| CIP_WITH_VERSION_KEY | 999992020 | 1439012000 | 5118042000 |
| VERSION | 2020 | 2000 | 2000 |
| PROGRAM_CODE | 99999 | 143901 | 511804 |
| PROGRAM_TITLE | Communication, Journalism, and Related Programs, Other | Geological/Geophysical Engineering | Orthoptics/Orthoptist |
| CATEGORY_CODE | 9 | 14 | 51 |
| CATEGORY_TITLE | COMMUNICATION, JOURNALISM, AND RELATED PROGRAMS | ENGINEERING | HEALTH PROFESSIONS AND RELATED CLINICAL SCIENCES |
| FOUR_DIGIT_CODE | 999 | 1439 | 5118 |
| FOUR_DIGIT_TITLE | Communication, Journalism, and Related Programs, Other | Geological/Geophysical Engineering | Ophthalmic and Optometric Support Services and Allied Professions |
| WAREHOUSE_LOAD_DATE | 17-MAY-23 | 27-MAR-03 | 27-MAR-03 |

# `cis_course_catalog`  (rows=10000)

columns:
`IS_OFFERED_FALL_TERM` varchar127: "Y"=7321, "N"=2679
`IS_OFFERED_IAP` varchar127: "N"=7206, "Y"=2794
`IS_OFFERED_SPRING_TERM` varchar127: "Y"=7440, "N"=2560
`IS_OFFERED_SUMMER_TERM` varchar127: "N"=7645, "Y"=2355
`FALL_INSTRUCTORS` varchar127: 1254 distinct, nulls=2644
`SPRING_INSTRUCTORS` varchar127: 1254 distinct, nulls=2644
`STATUS_CHANGE` varchar127: all NULL
`LAST_ACTIVITY_DATE` varchar255: 695 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000
`MASTER_SUBJECT_ID` varchar127: all NULL
`HASS_ATTRIBUTE` varchar127: all NULL
`HASS_ATTRIBUTE_DESC` varchar127: all NULL
`TERM_DURATION` varchar127: all NULL
`GLOBAL_REGIONS` varchar127: all NULL
`GLOBAL_COUNTRIES` varchar127: all NULL
`ON_LINE_PAGE_NUMBER` varchar127: all NULL
`ACADEMIC_YEAR` varchar127: "2008"=1444, "2007"=1429, "2006"=1377, "2005"=1369, "2009"=1353, "2004"=1185, "2003"=1018, "2002"=825
`SUBJECT_ID` varchar127: 2269 distinct
`SUBJECT_CODE` varchar127: digits, 41 distinct, "15"=1033, "6"=757, "12"=750, "SP"=746, "11"=714, "4"=685, "1"=371, "7"=363, "HST"=359, "10"=345
`SUBJECT_NUMBER` varchar127: 928 distinct
`SOURCE_SUBJECT_ID` varchar127: 2269 distinct
`PRINT_SUBJECT_ID` varchar127: 2283 distinct
`IS_PRINTED_IN_BULLETIN` varchar127: "Y"=6376, "N"=3624
`DEPARTMENT_CODE` varchar127: digits, 47 distinct, "15"=1041, "6"=757, "12"=750, "11"=714, "4"=685, "ESG"=372, "1"=371, "7"=363, "HST"=359, "10"=345
`DEPARTMENT_NAME` varchar127: 43 distinct, nulls=21
`EFFECTIVE_TERM_CODE` varchar127: 25 distinct
`SUBJECT_SHORT_TITLE` varchar127: 1568 distinct
`SUBJECT_TITLE` varchar127: 1527 distinct
`IS_VARIABLE_UNITS` varchar127: "Y"=6286, "N"=3714
`LECTURE_UNITS` int: 0=6307, 3=2256, 2=888, 4=300, 1=176, 5=47, 6=26, 0..6
`LAB_UNITS` int: 0=10000
`PREPARATION_UNITS` int: 0=6348, 9=1443, 4=685, 6=599, 8=278, 3=190, 2=125, 5=104, 1=102, 7=68, 10=37, 12=13, 18=7, 11=1, 0..18
`TOTAL_UNITS` int: 0=6286, 12=1791, 6=943, 9=635, 3=162, 2=61, 4=56, 8=20, 15=15, 1=8, 18=7, 24=7, 5=5, 7=4, 0..24
`DESIGN_UNITS` int: 0=9953, 4=22, 6=17, 3=4, 8=4, 0..8
`GRADE_TYPE` varchar127: "L"=7043, "P"=2957
`GRADE_TYPE_DESC` varchar127: "Letter graded"=7043, "P/D/F"=2957
`GRADE_RULE` varchar127: "R"=5454, "N"=3294, "J"=1232, "T"=20
`GRADE_RULE_DESC` varchar127: "Can be repeated for credit"=5454, "Not repeatable for credit"=3294, "Continuing and Repeatable"=1232, "Continuing"=20
`HGN_CODE` varchar127: "H"=4654, "U"=3772, "G"=1574
`HGN_DESC` varchar127: "High Graduate"=4654, "Undergraduate"=3772, "Graduate"=1574
`HGN_EXCEPT` varchar127: all NULL
`GIR_ATTRIBUTE` varchar127: all NULL
`GIR_ATTRIBUTE_DESC` varchar127: all NULL
`COMM_REQ_ATTRIBUTE` varchar127: "CIM"=94, nulls=9906
`COMM_REQ_ATTRIBUTE_DESC` varchar127: "Communication Intensive Major"=94, nulls=9906
`TUITION_ATTRIBUTE` varchar127: "RESH"=478, "NTRN"=15, nulls=9507
`TUITION_ATTRIBUTE_DESC` varchar127: "Pre-thesis Research Subject"=478, "Internship"=15, nulls=9507
`WRITE_REQ_ATTRIBUTE` varchar127: "WRT2"=9, nulls=9991
`WRITE_REQ_ATTRIBUTE_DESC` varchar127: "Writing Requirement, Phase II"=9, nulls=9991
`SUPERVISOR_ATTRIBUTE` varchar127: "UROP"=508, "THG"=187, "THU"=158, nulls=9147
`SUPERVISOR_ATTRIBUTE_DESC` varchar127: "UROP subject"=508, "Grad Thesis"=187, "Undergrad Thesis"=158, nulls=9147
`PREREQUISITES` varchar127: 660 distinct, nulls=5027
`SUBJECT_DESCRIPTION` varchar127: 1761 distinct, nulls=3045
`JOINT_SUBJECTS` varchar127: all NULL
`SCHOOL_WIDE_ELECTIVES` varchar127: all NULL
`MEETS_WITH_SUBJECTS` varchar127: all NULL
`EQUIVALENT_SUBJECTS` varchar127: all NULL
`IS_OFFERED_THIS_YEAR` varchar127: "Y"=8903, "N"=371, nulls=726

indexes: `DEPARTMENT_CODE`, `HGN_CODE`, `MASTER_SUBJECT_ID`, `SUBJECT_CODE`, `SUBJECT_ID`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IS_OFFERED_FALL_TERM | Y | Y | Y |
| IS_OFFERED_IAP | Y | N | Y |
| IS_OFFERED_SPRING_TERM | Y | N | Y |
| IS_OFFERED_SUMMER_TERM | Y | N | Y |
| FALL_INSTRUCTORS | Z. Graham | J. Hayden | E. O'Gallagher |
| SPRING_INSTRUCTORS | Z. Graham | J. Hayden | E. O'Gallagher |
| STATUS_CHANGE | null | null | null |
| LAST_ACTIVITY_DATE | 19-OCT-06 | 05-OCT-05 | 18-OCT-07 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| MASTER_SUBJECT_ID | null | null | null |
| HASS_ATTRIBUTE | null | null | null |
| HASS_ATTRIBUTE_DESC | null | null | null |
| TERM_DURATION | null | null | null |
| GLOBAL_REGIONS | null | null | null |
| GLOBAL_COUNTRIES | null | null | null |
| ON_LINE_PAGE_NUMBER | null | null | null |
| ACADEMIC_YEAR | 2008 | 2007 | 2009 |
| SUBJECT_ID | HST.989 | 14.122 | 3.595 |
| SUBJECT_CODE | HST | 14 | 3 |
| SUBJECT_NUMBER | 989 | 122 | 595 |
| SOURCE_SUBJECT_ID | HST.989 | 14.122 | 3.595 |
| PRINT_SUBJECT_ID | HST.986-HST.989 | 14.122 | 3.595 |
| IS_PRINTED_IN_BULLETIN | Y | Y | Y |
| DEPARTMENT_CODE | HST | 14 | 3 |
| DEPARTMENT_NAME | Health Sciences & Technology | Economics | Materials Science and Eng |
| EFFECTIVE_TERM_CODE | 2006FA | 2005FA | 2008FA |
| SUBJECT_SHORT_TITLE | Spec Subjs  Biomedical Ent | Microeconomic Theory II | Sp Probs: Strctl & Envrnt Mats |
| SUBJECT_TITLE | Special Subjects in Biomedical Enterprise | Microeconomic Theory II | Special Problems in Structural and Environmental Materials |
| IS_VARIABLE_UNITS | Y | N | Y |
| LECTURE_UNITS | 0 | 2 | 0 |
| LAB_UNITS | 0 | 0 | 0 |
| PREPARATION_UNITS | 0 | 4 | 0 |
| TOTAL_UNITS | 0 | 6 | 0 |
| DESIGN_UNITS | 0 | 0 | 0 |
| GRADE_TYPE | L | L | L |
| GRADE_TYPE_DESC | Letter graded | Letter graded | Letter graded |
| GRADE_RULE | R | N | R |
| GRADE_RULE_DESC | Can be repeated for credit | Not repeatable for credit | Can be repeated for credit |
| HGN_CODE | H | H | H |
| HGN_DESC | High Graduate | High Graduate | High Graduate |
| HGN_EXCEPT | null | null | null |
| GIR_ATTRIBUTE | null | null | null |
| GIR_ATTRIBUTE_DESC | null | null | null |
| COMM_REQ_ATTRIBUTE | null | null | null |
| COMM_REQ_ATTRIBUTE_DESC | null | null | null |
| TUITION_ATTRIBUTE | null | null | null |
| TUITION_ATTRIBUTE_DESC | null | null | null |
| WRITE_REQ_ATTRIBUTE | null | null | null |
| WRITE_REQ_ATTRIBUTE_DESC | null | null | null |
| SUPERVISOR_ATTRIBUTE | null | null | null |
| SUPERVISOR_ATTRIBUTE_DESC | null | null | null |
| PREREQUISITES | Permission of instructor | 14.121 and permission of instructor | Permission of instructor |
| SUBJECT_DESCRIPTION | Opportunity for group study of advanced subjects relating to Biomedical Enterprise not otherwise included in the curriculum. Of | Introduction to game theory. Class size limited. | null |
| JOINT_SUBJECTS | null | null | null |
| SCHOOL_WIDE_ELECTIVES | null | null | null |
| MEETS_WITH_SUBJECTS | null | null | null |
| EQUIVALENT_SUBJECTS | null | null | null |
| IS_OFFERED_THIS_YEAR | Y | Y | Y |

# `cis_hass_attribute`  (rows=17)

columns:
`HASS_ATTRIBUTE` varchar127: "HE"=2, "HA"=1, "HA,HH"=1, "HA,HS"=1, "HA2"=1, "HD1"=1, "HD2"=1, "HD3"=1, "HD4"=1, "HD5"=1, "HDL"=1, "HH"=1, "HH,HS"=1, "HH2"=1, "HS"=1, "HS2"=1
`DESCRIPTION_ON_FORM` varchar127: "HASS Elective"=2, "1/2 HASS Arts"=1, "1/2 HASS Humanities"=1, "1/2 HASS Social Sciences"=1, "Arts + Humanities"=1, "Arts + Social Sciences"=1, "HASS Arts"=1, "HASS Humanities"=1, "HASS Social Sciences"=1, "HASS-D Language Option"=1, "HASS-D, Category 1"=1, "HASS-D, Category 2"=1, "HASS-D, Category 3"=1, "HASS-D, Category 4"=1, "HASS-D, Category 5"=1, "Humanities + Social Sciences"=1
`DESCRIPTION_IN_BULLETIN` varchar127: "HASS-E"=2, "HASS-A"=1, "HASS-A, HASS-H"=1, "HASS-A, HASS-S"=1, "HASS-A/2"=1, "HASS-D 1"=1, "HASS-D 2"=1, "HASS-D 3"=1, "HASS-D 4"=1, "HASS-D 5"=1, "HASS-H"=1, "HASS-H, HASS-S"=1, "HASS-H/2"=1, "HASS-L"=1, "HASS-S"=1, "HASS-S/2"=1
`CIS_ATTRIBUTE_GROUP` varchar127: "H"=10, "G"=7
`CIS_ATTRIBUTE_GROUP_NOTE` varchar127: "HASS_ATTRIBUTE, for students entering in Fall 2010 or later"=10, "GIR_ATTRIBUTE, for students entering prior to Fall 2010"=7
`ICON_GIF_NAME` varchar127: "hass1.gif"=1, "hass2.gif"=1, "hass3.gif"=1, "hass4.gif"=1, "hass5.gif"=1, "hassA.gif"=1, "hassAH.gif"=1, "hassAS.gif"=1, "hassE.gif"=1, "hassH.gif"=1, "hassHS.gif"=1, "hassL.gif"=1, "hassS.gif"=1, "hassT.gif"=1, nulls=3
`ICON_HEIGHT` varchar127: "16"=14, nulls=3
`ICON_WIDTH` varchar127: "16"=11, "35"=3, nulls=3
`LAST_ACTIVITY_DATE` varchar255: "05-MAR-10"=11, "22-FEB-12"=3, "26-APR-10"=3
`LAST_UPDATE_USER` varchar127: "PETECHOI"=17
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=17

indexes: `HASS_ATTRIBUTE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| HASS_ATTRIBUTE | HS2 | HD2 | HS2 |
| DESCRIPTION_ON_FORM | 1/2 HASS Social Sciences | HASS-D, Category 2 | 1/2 HASS Social Sciences |
| DESCRIPTION_IN_BULLETIN | HASS-S/2 | HASS-D 2 | HASS-S/2 |
| CIS_ATTRIBUTE_GROUP | H | G | H |
| CIS_ATTRIBUTE_GROUP_NOTE | HASS_ATTRIBUTE, for students entering in Fall 2010 or later | GIR_ATTRIBUTE, for students entering prior to Fall 2010 | HASS_ATTRIBUTE, for students entering in Fall 2010 or later |
| ICON_GIF_NAME | null | hass2.gif | null |
| ICON_HEIGHT | null | 16 | null |
| ICON_WIDTH | null | 16 | null |
| LAST_ACTIVITY_DATE | 22-FEB-12 | 05-MAR-10 | 22-FEB-12 |
| LAST_UPDATE_USER | PETECHOI | PETECHOI | PETECHOI |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `course_catalog_subject_offered`  (rows=10000)

columns:
`ACADEMIC_YEAR` varchar127: digits, 24 distinct
`TERM_CODE` varchar127: 95 distinct, nulls=1079, "2021SP"=215, "2025SP"=202, "2022SP"=200, "2024SP"=197, "2020FA"=196, "2017FA"=194, "2018FA"=191, "2023FA"=190, "2021FA"=189, "2020SP"=188
`SUBJECT_ID` varchar127: 4969 distinct, "18.03"=36, "18.02"=26, "3.091"=25, "5.111"=25, "18.06"=24, "5.12"=24, "8.01"=21, "18.062"=19, "6.046"=19, "18.410"=18
`SUBJECT_CODE` varchar127: digits, 55 distinct, "15"=902, "6"=797, "2"=523, "4"=484, "18"=470, "11"=423, "1"=376, "12"=371, "10"=344, "HST"=314
`SUBJECT_NUMBER` varchar127: 1450 distinct
`SOURCE_SUBJECT_ID` varchar127: 4568 distinct
`PRINT_SUBJECT_ID` varchar127: 5050 distinct
`IS_PRINTED_IN_BULLETIN` varchar127: "Y"=9274, "N"=725, "S"=1
`DEPARTMENT_CODE` varchar127: digits, 60 distinct, "15"=902, "6"=797, "2"=523, "4"=484, "18"=470, "11"=423, "1"=376, "12"=371, "10"=344, "HST"=314
`DEPARTMENT_NAME` varchar127: 51 distinct, nulls=22
`EFFECTIVE_TERM_CODE` varchar127: 50 distinct, "2016FA"=804, "2018FA"=734, "2017FA"=582, "2012FA"=515, "2021FA"=455, "2009FA"=450, "2015FA"=441, "2007FA"=408, "2020FA"=396, "2013FA"=391
`SUBJECT_SHORT_TITLE` varchar127: 3890 distinct
`SUBJECT_TITLE` varchar127: 3749 distinct
`IS_VARIABLE_UNITS` varchar127: "N"=7852, "Y"=2148
`LECTURE_UNITS` int: 3=4113, 0=2477, 4=1436, 2=1000, 5=674, 1=239, 6=54, 9=6, 8=1, 0..9
`LAB_UNITS` int: 0=7994, 2=514, 3=467, 1=458, 4=169, 6=135, 8=79, 12=62, 9=32, 7=26, 5=21, 10=14, 20=10, 16=6, 24=4, 11=3, 19=3, 25=3, 0..25
`PREPARATION_UNITS` int: 9=2522, 0=2394, 8=1290, 6=1006, 7=864, 4=597, 3=366, 5=345, 2=268, 1=175, 10=108, 12=31, 11=21, 18=7, 15=4, 14=1, 16=1, 0..18
`TOTAL_UNITS` int: 24 distinct, 0..46, avg=8.4022, median=12
`DESIGN_UNITS` int: 0=9829, 4=73, 12=47, 6=28, 2=13, 3=5, 8=4, 9=1, 0..12
`GRADE_TYPE` varchar127: "L"=8597, "P"=1403
`GRADE_TYPE_DESC` varchar127: "Letter graded"=8597, "P/D/F"=1403
`GRADE_RULE` varchar127: "N"=7092, "R"=2242, "J"=557, "T"=109
`GRADE_RULE_DESC` varchar127: "Not repeatable for credit"=7092, "Can be repeated for credit"=2242, "Continuing and Repeatable"=557, "Continuing"=109
`HGN_CODE` varchar127: "U"=5092, "G"=2824, "H"=2084
`HGN_DESC` varchar127: "Undergraduate"=5092, "Graduate"=2824, "High Graduate"=2084
`HGN_EXCEPT` varchar127: "(H except 18)"=15, "(H except XVIII)"=6, "(H except 2, 6, 8, 12, 13, 16, 18, 22)"=2, "(H except II, VI, VIII, XII, XIII, XVI, XVIII, XXII)"=1, "H except XVIII"=1, nulls=9975
`GIR_ATTRIBUTE` varchar127: "HE"=528, "REST"=422, "LAB"=189, "LAB2"=59, "CAL2"=58, "CHEM"=58, "HD4"=53, "BIOL"=47, "PHY1"=44, "HD2"=39, "PHY2"=37, "HD3"=35, "RST2"=32, "CAL1"=31, "HDL"=26, "HD1"=23, "HD5"=21, nulls=8298
`GIR_ATTRIBUTE_DESC` varchar127: "HASS Elective"=528, "Rest Elec in Sci & Tech"=422, "Institute Lab"=189, "Calculus II"=58, "Chemistry"=58, "HASS-D, Category 4"=53, "Biology"=47, "Physics I"=44, "HASS-D, Category 2"=39, "Physics II"=37, "HASS-D, Category 3"=35, "1/2 Institute Lab"=32, "1/2 Rest Elec in Sci & Tech"=32, "Calculus I"=31, "Partial Lab"=27, "HASS-D Language Option"=26, "HASS-D, Category 1"=23, "HASS-D, Category 5"=21, nulls=8298
`COMM_REQ_ATTRIBUTE` varchar127: "CIM"=469, "CIH"=347, "CIHW"=37, nulls=9147
`COMM_REQ_ATTRIBUTE_DESC` varchar127: "Communication Intensive Major"=469, "Communication Intensive HASS"=347, "Communication Intensive Writing"=37, nulls=9147
`TUITION_ATTRIBUTE` varchar127: "RESH"=288, "NTRN"=96, "COOP"=2, nulls=9614
`TUITION_ATTRIBUTE_DESC` varchar127: "Pre-thesis Research Subject"=288, "Internship"=96, "Co-op Subject"=2, nulls=9614
`WRITE_REQ_ATTRIBUTE` varchar127: "WRT2"=5, "WRT1"=2, nulls=9993
`WRITE_REQ_ATTRIBUTE_DESC` varchar127: "Writing Requirement, Phase II"=5, "Writing Requirement, Phase I"=2, nulls=9993
`SUPERVISOR_ATTRIBUTE` varchar127: "UROP"=214, "INDP"=208, "THG"=120, "THU"=65, nulls=9393
`SUPERVISOR_ATTRIBUTE_DESC` varchar127: "UROP subject"=214, "Independent Study"=208, "Grad Thesis"=120, "Undergrad Thesis"=65, nulls=9393
`PREREQUISITES` varchar127: 1941 distinct, nulls=3125
`SUBJECT_DESCRIPTION` varchar127: 4339 distinct, nulls=476
`JOINT_SUBJECTS` varchar127: 1117 distinct, nulls=8169
`SCHOOL_WIDE_ELECTIVES` varchar127: 51 distinct, nulls=9843
`MEETS_WITH_SUBJECTS` varchar127: 922 distinct, nulls=8304
`EQUIVALENT_SUBJECTS` varchar127: 383 distinct, nulls=9179
`IS_OFFERED_THIS_YEAR` varchar127: "Y"=8911, "N"=958, nulls=131
`IS_OFFERED_FALL_TERM` varchar127: "Y"=6653, "N"=3347
`IS_OFFERED_IAP` varchar127: "N"=8512, "Y"=1488
`IS_OFFERED_SPRING_TERM` varchar127: "Y"=6860, "N"=3140
`IS_OFFERED_SUMMER_TERM` varchar127: "N"=8782, "Y"=1218
`FALL_INSTRUCTORS` varchar127: 3486 distinct, nulls=471
`SPRING_INSTRUCTORS` varchar127: 3489 distinct, nulls=471
`STATUS_CHANGE` varchar127: 294 distinct, nulls=9150
`LAST_ACTIVITY_DATE` varchar255: 2674 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000
`MASTER_SUBJECT_ID` varchar127: 3473 distinct, nulls=2849, "10.01"=27, "2.96"=24, "2.EPE"=23, "5.111"=22, "6.021"=22, "18.02"=21, "18.03"=20, "3.091"=19, "7.02"=19, "10.26"=18
`HASS_ATTRIBUTE` varchar127: "HH"=479, "HS"=298, "HA"=234, "HE"=9, "HA,HH"=8, nulls=8972
`HASS_ATTRIBUTE_DESC` varchar127: "HASS Humanities"=479, "HASS Social Sciences"=298, "HASS Arts"=234, "HASS Elective"=9, "Arts + Humanities"=8, nulls=8972
`TERM_DURATION` varchar127: "Full Term Subject"=6724, "Second Half Term Subject"=187, "First Half Term Subject"=175, "Partial Term Subject"=65, nulls=2849
`GLOBAL_REGIONS` varchar127: 27 distinct, nulls=9767
`GLOBAL_COUNTRIES` varchar127: "China"=15, "France"=14, "Japan"=12, "United States of America"=12, "Spain"=11, "Developing Countries"=10, "Germany"=8, "Brazil|Uruguay|Vietnam|Russia|Australia"=5, "Mexico|Spain"=4, "China|India"=3, "Indonesia"=3, "France|Russia|United Kingdom|Germany"=2, "Italy"=2, "Jordan"=2, "United States of America|India|South Africa"=2, "United States of America|Japan"=2, "Brazil|Mexico|Chile"=1, "Brazil|United States of America"=1, "India"=1, nulls=9890
`ON_LINE_PAGE_NUMBER` varchar127: 110 distinct, nulls=2885
`SECTION_ID` varchar127: digits, 68 distinct, nulls=1079, "000"=4239, "L01"=2478, "R01"=484, "B01"=276, "R02"=251, "L02"=193, "R03"=149, "R04"=86, "R05"=74, "L03"=69
`IS_MASTER_SECTION` varchar127: "N"=4682, "Y"=4239, nulls=1079
`IS_LECTURE_SECTION` varchar127: "N"=6106, "Y"=2815, nulls=1079
`IS_LAB_SECTION` varchar127: "N"=8445, "Y"=476, nulls=1079
`IS_RECITATION_SECTION` varchar127: "N"=7580, "Y"=1341, nulls=1079
`IS_DESIGN_SECTION` varchar127: "N"=8879, "Y"=42, nulls=1079
`RESPONSIBLE_FACULTY_NAME` varchar127: 2402 distinct, nulls=1741
`RESPONSIBLE_FACULTY_MIT_ID` varchar127: digits, 2418 distinct, nulls=1741, "920324608"=75, "916610219"=32, "964758013"=29, "908856167"=28, "925785734"=28, "993673204"=28, "975916420"=25, "949310910"=24, "953227596"=23, "975186706"=23
`MEET_TIME` varchar127: 823 distinct, nulls=5369
`MEET_PLACE` varchar127: 553 distinct, nulls=5526, "VIRTUAL"=202, "E51-350"=43, "2-113G"=35, "14N-315"=34, "E51-385D"=34, "1-337A"=33, "E51-357E"=33, "14E-362"=32, "E51-364A"=32, "TBA"=32

indexes: `DEPARTMENT_CODE`, `EFFECTIVE_TERM_CODE`, `HASS_ATTRIBUTE`, `HGN_CODE`, `MASTER_SUBJECT_ID`, `MEET_PLACE`, `RESPONSIBLE_FACULTY_MIT_ID`, `SECTION_ID`, `SUBJECT_CODE`, `SUBJECT_ID`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ACADEMIC_YEAR | 2025 | 2012 | 2018 |
| TERM_CODE | 2025SP | null | 2018SU |
| SUBJECT_ID | WGS.UR | STS.074 | 2.THG |
| SUBJECT_CODE | WGS | STS | 2 |
| SUBJECT_NUMBER | UR | 074 | THG |
| SOURCE_SUBJECT_ID | WGS.UR | 21A.370 | 2.THG |
| PRINT_SUBJECT_ID | WGS.UR | STS.074J | 2.THG |
| IS_PRINTED_IN_BULLETIN | Y | Y | Y |
| DEPARTMENT_CODE | WGS | STS | 2 |
| DEPARTMENT_NAME | Women's and Gender Studies | Science, Technology & Society | Mechanical Engineering |
| EFFECTIVE_TERM_CODE | 2013FA | 2012FA | 2016FA |
| SUBJECT_SHORT_TITLE | Undergraduate Research | Art, Craft, Science | Thesis |
| SUBJECT_TITLE | Undergraduate Research in Women's and Gender Studies | Art, Craft, Science | Graduate Thesis |
| IS_VARIABLE_UNITS | Y | N | Y |
| LECTURE_UNITS | 0 | 3 | 0 |
| LAB_UNITS | 0 | 0 | 0 |
| PREPARATION_UNITS | 0 | 9 | 0 |
| TOTAL_UNITS | 0 | 12 | 0 |
| DESIGN_UNITS | 0 | 0 | 0 |
| GRADE_TYPE | P | L | L |
| GRADE_TYPE_DESC | P/D/F | Letter graded | Letter graded |
| GRADE_RULE | J | N | J |
| GRADE_RULE_DESC | Continuing and Repeatable | Not repeatable for credit | Continuing and Repeatable |
| HGN_CODE | U | U | G |
| HGN_DESC | Undergraduate | Undergraduate | Graduate |
| HGN_EXCEPT | null | null | null |
| GIR_ATTRIBUTE | null | HE | null |
| GIR_ATTRIBUTE_DESC | null | HASS Elective | null |
| COMM_REQ_ATTRIBUTE | null | null | null |
| COMM_REQ_ATTRIBUTE_DESC | null | null | null |
| TUITION_ATTRIBUTE | null | null | null |
| TUITION_ATTRIBUTE_DESC | null | null | null |
| WRITE_REQ_ATTRIBUTE | null | null | null |
| WRITE_REQ_ATTRIBUTE_DESC | null | null | null |
| SUPERVISOR_ATTRIBUTE | UROP | null | THG |
| SUPERVISOR_ATTRIBUTE_DESC | UROP subject | null | Grad Thesis |
| PREREQUISITES | Permission of instructor | null | Permission of advisor |
| SUBJECT_DESCRIPTION | Undergraduate research opportunities in the Women's and Gender Studies Program. | Examines how people learn, practice, and evaluate traditional and contemporary craft techniques. Social science theories of des | Program of research leading to the writing of an SM, PhD, or ScD thesis; to be arranged by the student and an appropriate MIT f |
| JOINT_SUBJECTS | null | 21A.370J | null |
| SCHOOL_WIDE_ELECTIVES | null | null | null |
| MEETS_WITH_SUBJECTS | null | null | null |
| EQUIVALENT_SUBJECTS | null | null | null |
| IS_OFFERED_THIS_YEAR | Y | N | Y |
| IS_OFFERED_FALL_TERM | Y | Y | Y |
| IS_OFFERED_IAP | Y | N | Y |
| IS_OFFERED_SPRING_TERM | Y | N | Y |
| IS_OFFERED_SUMMER_TERM | Y | N | Y |
| FALL_INSTRUCTORS | Staff | L. R. Weeks | T. P. Richards |
| SPRING_INSTRUCTORS | Staff | L. R. Weeks | T. P. Richards |
| STATUS_CHANGE | null | null | null |
| LAST_ACTIVITY_DATE | 26-OCT-23 | 02-FEB-11 | 10-NOV-16 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| MASTER_SUBJECT_ID | WGS.UR | 21A.370 | 2.THG |
| HASS_ATTRIBUTE | null | HS | null |
| HASS_ATTRIBUTE_DESC | null | HASS Social Sciences | null |
| TERM_DURATION | Full Term Subject | Full Term Subject | Full Term Subject |
| GLOBAL_REGIONS | null | null | null |
| GLOBAL_COUNTRIES | null | null | null |
| ON_LINE_PAGE_NUMBER | http://student.mit.edu/catalog/mWGSa.html | http://student.mit.edu/catalog/mSTSa.html | http://student.mit.edu/catalog/m2c.html |
| SECTION_ID | 000 | null | 000 |
| IS_MASTER_SECTION | Y | null | Y |
| IS_LECTURE_SECTION | N | null | N |
| IS_LAB_SECTION | N | null | N |
| IS_RECITATION_SECTION | N | null | N |
| IS_DESIGN_SECTION | N | null | N |
| RESPONSIBLE_FACULTY_NAME | Kirby, Barney | null | Hutchinson, Jan |
| RESPONSIBLE_FACULTY_MIT_ID | 934724720 | null | 941663890 |
| MEET_TIME | null | null | null |
| MEET_PLACE | null | null | null |

# `drupal_course_catalog`  (rows=10000)

columns:
`ACADEMIC_YEAR` varchar127: digits, 24 distinct
`SUBJECT_ID` varchar127: 687 distinct
`SUBJECT_CODE` varchar127: "1"=4173, "7"=1405, "5"=968, "9"=934, "2"=783, "3"=783, "8"=677, "6"=174, "4"=103
`SUBJECT_NUMBER` varchar127: 379 distinct
`SOURCE_SUBJECT_ID` varchar127: 726 distinct
`PRINT_SUBJECT_ID` varchar127: 758 distinct
`IS_PRINTED_IN_BULLETIN` varchar127: "Y"=9591, "N"=409
`DEPARTMENT_CODE` varchar127: "1"=4173, "7"=1405, "5"=968, "9"=934, "2"=783, "3"=783, "8"=677, "6"=174, "4"=103
`DEPARTMENT_NAME` varchar127: "Civil and Environmental Eng"=4173, "Biology"=1405, "Chemistry"=968, "Brain and Cognitive Sciences"=934, "Materials Science and Eng"=783, "Mechanical Engineering"=783, "Physics"=677, "Electrical Eng & Computer Sci"=174, "Architecture"=103
`EFFECTIVE_TERM_CODE` varchar127: 43 distinct
`SUBJECT_SHORT_TITLE` varchar127: 891 distinct
`SUBJECT_TITLE` varchar127: 806 distinct
`IS_VARIABLE_UNITS` varchar127: "N"=7211, "Y"=2789
`LECTURE_UNITS` int: 3=3584, 0=3035, 4=1550, 2=908, 5=745, 1=152, 6=26, 0..6
`LAB_UNITS` int: 0=8123, 1=591, 2=435, 4=263, 3=248, 6=95, 12=70, 16=67, 8=62, 5=20, 7=20, 13=6, 0..16
`PREPARATION_UNITS` int: 0=2958, 9=2329, 8=1694, 7=952, 6=652, 4=595, 2=254, 10=245, 3=143, 5=70, 12=70, 1=36, 16=2, 0..16
`TOTAL_UNITS` int: 12=5424, 0=2789, 6=712, 9=483, 15=168, 18=134, 3=86, 4=72, 30=49, 1=33, 24=20, 2=17, 20=7, 21=6, 0..30
`DESIGN_UNITS` int: 0=9896, 6=47, 3=36, 2=14, 9=5, 12=2, 0..12
`GRADE_TYPE` varchar127: "L"=8280, "P"=1720
`GRADE_TYPE_DESC` varchar127: "Letter graded"=8280, "P/D/F"=1720
`GRADE_RULE` varchar127: "N"=7075, "R"=1952, "J"=945, "T"=28
`GRADE_RULE_DESC` varchar127: "Not repeatable for credit"=7075, "Can be repeated for credit"=1952, "Continuing and Repeatable"=945, "Continuing"=28
`HGN_CODE` varchar127: "U"=4943, "H"=2844, "G"=2213
`HGN_DESC` varchar127: "Undergraduate"=4943, "High Graduate"=2844, "Graduate"=2213
`HGN_EXCEPT` varchar127: "(H except 1, 18)"=1, nulls=9999
`GIR_ATTRIBUTE` varchar127: "REST"=575, "LAB"=245, "LAB2"=145, "HE"=120, "PHY1"=54, "PHY2"=53, "HD4"=5, "HD2"=2, nulls=8801
`GIR_ATTRIBUTE_DESC` varchar127: "Rest Elec in Sci & Tech"=575, "Institute Lab"=245, "HASS Elective"=120, "1/2 Institute Lab"=108, "Physics I"=54, "Physics II"=53, "Partial Lab"=37, "HASS-D, Category 4"=5, "HASS-D, Category 2"=2, nulls=8801
`COMM_REQ_ATTRIBUTE` varchar127: "CIM"=510, "CIH"=11, nulls=9479
`COMM_REQ_ATTRIBUTE_DESC` varchar127: "Communication Intensive Major"=510, "Communication Intensive HASS"=11, nulls=9479
`TUITION_ATTRIBUTE` varchar127: "RESH"=737, "NTRN"=32, "COOP"=12, nulls=9219
`TUITION_ATTRIBUTE_DESC` varchar127: "Pre-thesis Research Subject"=737, "Internship"=32, "Co-op Subject"=12, nulls=9219
`WRITE_REQ_ATTRIBUTE` varchar127: all NULL
`WRITE_REQ_ATTRIBUTE_DESC` varchar127: all NULL
`SUPERVISOR_ATTRIBUTE` varchar127: "UROP"=814, "INDP"=97, nulls=9089
`SUPERVISOR_ATTRIBUTE_DESC` varchar127: "UROP subject"=814, "Independent Study"=97, nulls=9089
`PREREQUISITES` varchar127: 801 distinct, nulls=2163
`SUBJECT_DESCRIPTION` varchar127: 1139 distinct, nulls=588
`JOINT_SUBJECTS` varchar127: 354 distinct, nulls=7638
`SCHOOL_WIDE_ELECTIVES` varchar127: 26 distinct, nulls=9879
`MEETS_WITH_SUBJECTS` varchar127: 258 distinct, nulls=8184
`EQUIVALENT_SUBJECTS` varchar127: 53 distinct, nulls=9644
`IS_OFFERED_THIS_YEAR` varchar127: "Y"=9763, "N"=77, nulls=160
`IS_OFFERED_FALL_TERM` varchar127: "Y"=6598, "N"=3402
`IS_OFFERED_IAP` varchar127: "N"=8302, "Y"=1698
`IS_OFFERED_SPRING_TERM` varchar127: "Y"=6614, "N"=3386
`IS_OFFERED_SUMMER_TERM` varchar127: "N"=7998, "Y"=2002
`FALL_INSTRUCTORS` varchar127: 1348 distinct, nulls=499
`SPRING_INSTRUCTORS` varchar127: 1346 distinct, nulls=499
`STATUS_CHANGE` varchar127: 79 distinct, nulls=9471
`LAST_ACTIVITY_DATE` varchar255: 1868 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000
`MASTER_SUBJECT_ID` varchar127: 585 distinct, nulls=3628
`HASS_ATTRIBUTE` varchar127: "HS"=95, "HH"=2, "HE"=1, nulls=9902
`HASS_ATTRIBUTE_DESC` varchar127: "HASS Social Sciences"=95, "HASS Humanities"=2, "HASS Elective"=1, nulls=9902
`TERM_DURATION` varchar127: "Full Term Subject"=6100, "First Half Term Subject"=150, "Second Half Term Subject"=94, "Partial Term Subject"=28, nulls=3628
`GLOBAL_REGIONS` varchar127: "Global (all regions)"=1, nulls=9999
`GLOBAL_COUNTRIES` varchar127: all NULL
`ON_LINE_PAGE_NUMBER` varchar127: 21 distinct, nulls=3633
`SO_SUBJECT_ID` varchar127: 687 distinct
`SO_TERM_CODE` varchar127: 95 distinct
`SO_TERM_DESCRIPTION` varchar127: 95 distinct
`SO_CLUSTER_TYPE` varchar127: "J"=2078, "M"=1536, "S"=119, nulls=6267
`SECTION_ID` varchar127: 1059 distinct
`IS_MASTER_SECTION` varchar127: 92 distinct
`IS_LECTURE_SECTION` varchar127: 188 distinct
`IS_LAB_SECTION` varchar127: 173 distinct
`IS_RECITATION_SECTION` varchar127: 295 distinct
`IS_DESIGN_SECTION` varchar127: 54 distinct
`RESPONSIBLE_FACULTY_NAME` varchar127: 1497 distinct, nulls=813
`RESPONSIBLE_FACULTY_MIT_ID` varchar127: 1551 distinct, nulls=813
`MEET_TIME` varchar127: 2588 distinct, nulls=2952
`MEET_PLACE` varchar127: 2131 distinct, nulls=3056

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ACADEMIC_YEAR | 2025 | 2014 | 2008 |
| SUBJECT_ID | 9.UR | 3.96 | 6.UR |
| SUBJECT_CODE | 9 | 3 | 6 |
| SUBJECT_NUMBER | UR | 96 | UR |
| SOURCE_SUBJECT_ID | 9.UR | 20.441 | 6.UR |
| PRINT_SUBJECT_ID | 9.UR | 3.96J | 6.UR |
| IS_PRINTED_IN_BULLETIN | Y | Y | Y |
| DEPARTMENT_CODE | 9 | 3 | 6 |
| DEPARTMENT_NAME | Brain and Cognitive Sciences | Materials Science and Eng | Electrical Eng & Computer Sci |
| EFFECTIVE_TERM_CODE | 2010FA | 2011FA | 2006FA |
| SUBJECT_SHORT_TITLE | Undergraduate Research | Biomaterials: Tissue Interact | Undergraduate Research |
| SUBJECT_TITLE | Undergraduate Research | Biomaterials: Tissue Interactions | Undergraduate Research in Electrical Engineering and Computer Science |
| IS_VARIABLE_UNITS | Y | N | Y |
| LECTURE_UNITS | 0 | 3 | 0 |
| LAB_UNITS | 0 | 0 | 0 |
| PREPARATION_UNITS | 0 | 9 | 0 |
| TOTAL_UNITS | 0 | 12 | 0 |
| DESIGN_UNITS | 0 | 0 | 0 |
| GRADE_TYPE | P | L | P |
| GRADE_TYPE_DESC | P/D/F | Letter graded | P/D/F |
| GRADE_RULE | J | N | J |
| GRADE_RULE_DESC | Continuing and Repeatable | Not repeatable for credit | Continuing and Repeatable |
| HGN_CODE | U | H | U |
| HGN_DESC | Undergraduate | High Graduate | Undergraduate |
| HGN_EXCEPT | null | null | null |
| GIR_ATTRIBUTE | null | null | null |
| GIR_ATTRIBUTE_DESC | null | null | null |
| COMM_REQ_ATTRIBUTE | null | null | null |
| COMM_REQ_ATTRIBUTE_DESC | null | null | null |
| TUITION_ATTRIBUTE | null | null | null |
| TUITION_ATTRIBUTE_DESC | null | null | null |
| WRITE_REQ_ATTRIBUTE | null | null | null |
| WRITE_REQ_ATTRIBUTE_DESC | null | null | null |
| SUPERVISOR_ATTRIBUTE | UROP | null | UROP |
| SUPERVISOR_ATTRIBUTE_DESC | UROP subject | null | UROP subject |
| PREREQUISITES | null | GIR:CHEM, GIR:BIOL, GIR:PHY1; or permission of instructor | null |
| SUBJECT_DESCRIPTION | Individual participation in an ongoing research project. | Principles of materials science and cell biology underlying the design of medical implants, artificial organs, and matrices for | Extended participation in the work of a faculty member or research group, including independent study of the literature, direct |
| JOINT_SUBJECTS | null | 2.79J, 20.441J, HST.522J | null |
| SCHOOL_WIDE_ELECTIVES | null | null | null |
| MEETS_WITH_SUBJECTS | null | null | null |
| EQUIVALENT_SUBJECTS | null | null | null |
| IS_OFFERED_THIS_YEAR | Y | Y | Y |
| IS_OFFERED_FALL_TERM | Y | Y | Y |
| IS_OFFERED_IAP | Y | N | N |
| IS_OFFERED_SPRING_TERM | Y | N | Y |
| IS_OFFERED_SUMMER_TERM | Y | N | Y |
| FALL_INSTRUCTORS | Staff | N. Thompson, A. Benton | Z. O. Summers |
| SPRING_INSTRUCTORS | Staff | N. Thompson, A. Benton | Z. O. Summers |
| STATUS_CHANGE | null | null | null |
| LAST_ACTIVITY_DATE | 26-OCT-23 | 24-OCT-12 | 19-OCT-06 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| MASTER_SUBJECT_ID | 9.UR | 20.441 | null |
| HASS_ATTRIBUTE | null | null | null |
| HASS_ATTRIBUTE_DESC | null | null | null |
| TERM_DURATION | Full Term Subject | Full Term Subject | null |
| GLOBAL_REGIONS | null | null | null |
| GLOBAL_COUNTRIES | null | null | null |
| ON_LINE_PAGE_NUMBER | http://student.mit.edu/catalog/m9b.html | http://student.mit.edu/catalog/m3b.html | null |
| SO_SUBJECT_ID | 9.UR | 3.96 | 6.UR |
| SO_TERM_CODE | 2025SP | 2014FA | 2008JA |
| SO_TERM_DESCRIPTION | Spring Term 2024-2025 | Fall Term 2013-2014 | January Term 2007-2008 |
| SO_CLUSTER_TYPE | null | J | null |
| SECTION_ID | 000 | L01,000 | 000 |
| IS_MASTER_SECTION | Y | N,Y | Y |
| IS_LECTURE_SECTION | N | Y,N | N |
| IS_LAB_SECTION | N | N,N | N |
| IS_RECITATION_SECTION | N | N,N | N |
| IS_DESIGN_SECTION | N | N,N | N |
| RESPONSIBLE_FACULTY_NAME | Barton, Kevin | Powers, Blanche,Powers, Blanche | null |
| RESPONSIBLE_FACULTY_MIT_ID | 940702290 | 909170297,909170297 | null |
| MEET_TIME | null | TR2.30-4 | null |
| MEET_PLACE | null | 3-309 | null |

# `drupal_employee_directory`  (rows=10000)

columns:
`MIT_ID` varchar127: digits, unique identifier
`LAST_NAME` varchar127: 339 distinct
`FIRST_NAME` varchar127: 364 distinct
`MIDDLE_NAME` varchar127: 361 distinct, nulls=5220
`FULL_NAME` varchar127: 9889 distinct
`EMPLOYEE_GROUP` varchar127: "Exempt"=7971, "Non-Exempt"=1999, "External"=30
`EMPLOYEE_TYPE` varchar127: "Other Academic Group"=3390, "Admin Staff"=2560, "Sponsored Research Staff"=1461, "Support Staff"=1139, "Service Staff"=859, "Faculty"=429, "Medical"=95, "Tech Review Admin Staff"=36, "Affiliate"=30, "Tech Review Support Staff"=1
`HAS_ADDL_APPOINTMENT` varchar127: "N"=9922, "Y"=78
`HAS_DUAL_APPOINTMENT` varchar127: "N"=9997, "Y"=3
`OFFICE_LOCATION` varchar127: 3937 distinct, nulls=1050
`OFFICE_PHONE` varchar127: digits, all distinct, nulls=1832
`HR_ORG_UNIT_ID` varchar127: digits, 324 distinct
`HR_ORG_UNIT_TITLE` varchar127: 323 distinct, nulls=15
`DIRECTORY_TITLE` varchar127: all NULL
`PRIMARY_TITLE` varchar127: all NULL
`EMAIL_ADDRESS` varchar127: 5708 distinct, nulls=275
`PERSONAL_URL` varchar127: "http://www.carag.org"=1, "http://www.owaing.com"=1, "https://www.caraw.net"=1, "https://www.keatonl.com"=1, "https://www.na.org"=1, nulls=9995
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MIT_ID | 999997078 | 944190622 | 943647706 |
| LAST_NAME | Holland | Clark | Mccann |
| FIRST_NAME | Alec | Steffan | Fannie |
| MIDDLE_NAME | null | null | null |
| FULL_NAME | Holland, Alec | Clark, Steffan | Mccann, Fannie |
| EMPLOYEE_GROUP | Exempt | Non-Exempt | Exempt |
| EMPLOYEE_TYPE | Other Academic Group | Support Staff | Other Academic Group |
| HAS_ADDL_APPOINTMENT | N | N | N |
| HAS_DUAL_APPOINTMENT | N | N | N |
| OFFICE_LOCATION | null | W98-373G | 32 |
| OFFICE_PHONE | null | 2706125477 | null |
| HR_ORG_UNIT_ID | 10004284 | 10000661 | 10000338 |
| HR_ORG_UNIT_TITLE | Institute for Medical Eng. and Science | CEDRS | Lab for Information & Decision Systems |
| DIRECTORY_TITLE | null | null | null |
| PRIMARY_TITLE | null | null | null |
| EMAIL_ADDRESS | ah@worker.com | steffanc@worker.com | fanniem@worker.com |
| PERSONAL_URL | null | null | null |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `employee_directory`  (rows=10000)

columns:
`MIT_ID` varchar127: digits, unique identifier
`LAST_NAME` varchar127: 339 distinct
`FIRST_NAME` varchar127: 364 distinct
`MIDDLE_NAME` varchar127: 361 distinct, nulls=3596
`FULL_NAME` varchar127: 9945 distinct
`DIRECTORY_FULL_NAME` varchar127: 9945 distinct
`OFFICE_LOCATION` varchar127: 5396 distinct, nulls=233, "4-022B"=70, "LL-C-128"=70, "16-806D"=66, "10-072A"=65, "NW23-117"=62, "NE49-504"=50, "LL-F-241D"=41, "NE49"=40, "HAYSTCK_OB"=39, "N52-422"=38
`OFFICE_PHONE` varchar127: digits, all distinct, nulls=540
`DIRECTORY_TITLE` varchar127: all NULL
`PRIMARY_TITLE` varchar127: all NULL
`DEPARTMENT_NUMBER` varchar127: digits, 312 distinct, nulls=1
`DEPARTMENT_NAME` varchar127: 322 distinct
`KRB_NAME` varchar127: 5390 distinct, "mb"=27, "mh"=27, "am"=25, "kh"=24, "mc"=23, "ab"=22, "mm"=22, "ac"=20, "ch"=20, "ms"=20
`KRB_NAME_UPPERCASE` varchar127: 5390 distinct
`EMAIL_ADDRESS` varchar127: 6872 distinct, nulls=97
`PERSONAL_URL` varchar127: 1348 distinct, nulls=8628
`NAME_KNOWN_BY` varchar127: 364 distinct
`EMAIL_ADDRESS_UPPERCASE` varchar127: 6872 distinct, nulls=97
`FULL_NAME_UPPERCASE` varchar127: 9945 distinct
`PREFERRED_FIRST_NAME_UPPER` varchar127: 364 distinct
`PREFERRED_LAST_NAME_UPPER` varchar127: 339 distinct
`PREFERRED_FIRST_NAME` varchar127: 364 distinct
`PREFERRED_MIDDLE_NAME` varchar127: 359 distinct, nulls=6869
`PREFERRED_LAST_NAME` varchar127: 339 distinct

indexes: `KRB_NAME`, `MIT_ID`, `OFFICE_LOCATION`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MIT_ID | 999983523 | 975183589 | 978220665 |
| LAST_NAME | Leonard | Sykes | Rocha |
| FIRST_NAME | Hattie | Brooklyn | Marianne |
| MIDDLE_NAME | null | D | Doyle |
| FULL_NAME | Leonard, Hattie | Sykes, Brooklyn D. | Rocha, Marianne Doyle. |
| DIRECTORY_FULL_NAME | Leonard, Hattie | Sykes, Brooklyn D. | Rocha, Marianne Doyle. |
| OFFICE_LOCATION | 4-022B | NW23-201D | E14-278 |
| OFFICE_PHONE | 5325034320 | 6460694931 | 7019083680 |
| DIRECTORY_TITLE | null | null | null |
| PRIMARY_TITLE | null | null | null |
| DEPARTMENT_NUMBER | 861000 | 591100 | 39000 |
| DEPARTMENT_NAME | Housing & Residential Services | Dof Campus Construction | Media Lab |
| KRB_NAME | hattiel | brooklyns | mr |
| KRB_NAME_UPPERCASE | HATTIEL | BROOKLYNS | MR |
| EMAIL_ADDRESS | hattiel@worker.com | brooklyns@worker.com | mr@worker.com |
| PERSONAL_URL | null | null | null |
| NAME_KNOWN_BY | Hattie | Brooklyn | Marianne |
| EMAIL_ADDRESS_UPPERCASE | HATTIEL@WORKER.COM | BROOKLYNS@WORKER.COM | MR@WORKER.COM |
| FULL_NAME_UPPERCASE | LEONARD, HATTIE | SYKES, BROOKLYN D. | ROCHA, MARIANNE DOYLE. |
| PREFERRED_FIRST_NAME_UPPER | HATTIE | BROOKLYN | MARIANNE |
| PREFERRED_LAST_NAME_UPPER | LEONARD | SYKES | ROCHA |
| PREFERRED_FIRST_NAME | Hattie | Brooklyn | Marianne |
| PREFERRED_MIDDLE_NAME | null | null | null |
| PREFERRED_LAST_NAME | Leonard | Sykes | Rocha |

# `fac_building`  (rows=242)

columns:
`DATE_ACQUIRED` varchar127: 25 distinct, nulls=212
`DATE_OCCUPIED` varchar127: 136 distinct, nulls=62
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=242
`NUM_OF_ROOMS` int: 151 distinct, 0..1424, avg=178.4091, median=90.5
`FAC_BUILDING_KEY` varchar127: all distinct
`BUILDING_NUMBER` varchar127: all distinct
`PARENT_BUILDING_NUMBER` varchar127: "W61"=10, "14"=4, "62"=3, "64"=3, "W85ABC"=3, "W85HJK"=3, "W85DE"=2, "W85FG"=2, "42"=1, nulls=211
`PARENT_BUILDING_NAME` varchar127: "MACGREGOR HOUSE"=10, "HAYDEN MEMORIAL LIBRARY"=4, "ALUMNI HOUSES: MUNROE HAYDEN WOOD"=3, "EAST CAMPUS: WALCOTT BEMIS GOODALE"=3, "WESTGATE (ABC)"=3, "WESTGATE (HJK)"=3, "WESTGATE (DE)"=2, "WESTGATE (FG)"=2, "COGENERATION PLANT"=1, nulls=211
`PARENT_BUILDING_NAME_LONG` varchar127: "Frank S MacGregor House"=10, "Charles Hayden Memorial Library"=4, "Alumni Houses: Munroe Hayden Wood"=3, "Alumni Houses: Walcott Bemis Goodale"=3, "Westgate ABC"=3, "Westgate HJK"=3, "Westgate DE"=2, "Westgate FG"=2, "William R. Dickson Cogeneration Plant"=1, nulls=211
`BUILDING_NAME_LONG` varchar127: 235 distinct
`EXT_GROSS_AREA` float: 231 distinct, 0..466722, avg=59615.1, median=25763.6
`ASSIGNABLE_AREA` float: 226 distinct, 0..285682, avg=36556, median=16825
`NON_ASSIGNABLE_AREA` float: 206 distinct, 0..151963, avg=16374.2, median=4810.29
`SITE` varchar127: "MIT"=198, "BATES"=14, "HAY"=12, "LINC"=9, "BOS"=2, "DC"=2, "END"=2, "HOLYOKE"=1, "MED"=1, "WILM"=1
`CAMPUS_SECTOR` varchar127: "WEST"=71, "MAIN GROUP"=60, "OFFCAMPUS"=44, "EAST"=25, "NORTHWEST"=22, "NORTH"=11, "NORTHEAST"=8, "WESTWEST"=1
`ACCESS_LEVEL_CODE` int: 2=185, 1=47, 0=10, 0..2
`ACCESS_LEVEL_NAME` varchar127: "2"=185, "1"=47, "0"=10
`BUILDING_TYPE` varchar127: "ACADEMIC"=126, "SERVICE"=59, "RESIDENT"=57
`OWNERSHIP_TYPE` varchar127: "OWNED"=220, "LEASED"=22
`BUILDING_USE` varchar127: "AER"=124, "DHOA"=54, "OTH"=32, "STAC"=17, "(NULL)"=8, "GAR"=7
`OCCUPANCY_CLASS` varchar127: 20 distinct
`BUILDING_HEIGHT` varchar127: numeric, 110 distinct, nulls=60
`COST_CENTER_CODE` varchar127: digits, 109 distinct, nulls=111
`COST_COLLECTOR_KEY` varchar127: digits, 109 distinct, nulls=111
`LATITUDE_WGS` float: 78 distinct, nulls=104, 42.2539..42.6233, avg=42.3812, median=42.3601
`LONGITUDE_WGS` float: 109 distinct, nulls=104, -71.4937..-70.979, avg=-71.1068, median=-71.0935
`EASTING_X_SPCS` float: 134 distinct, nulls=104, 657854..796445, avg=762408, median=766026
`NORTHING_Y_SPCS` float: 115 distinct, nulls=104, 2.9e+06..3.1e+06, avg=3e+06, median=3e+06
`BUILDING_SORT` varchar127: all distinct
`BUILDING_NAMED_FOR` varchar127: 68 distinct, nulls=41
`BUILDING_NAME` varchar127: 236 distinct
`DATE_BUILT` varchar127: 111 distinct, nulls=92

indexes: `FAC_BUILDING_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| DATE_ACQUIRED | 12/31/1955 | null | null |
| DATE_OCCUPIED | 12/31/1955 | 12/31/1916 | 07/01/1916 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| NUM_OF_ROOMS | 168 | 90 | 311 |
| FAC_BUILDING_KEY | NW12 | 42 | E2 |
| BUILDING_NUMBER | NW12 | 42 | E2 |
| PARENT_BUILDING_NUMBER | null | null | null |
| PARENT_BUILDING_NAME | null | null | null |
| PARENT_BUILDING_NAME_LONG | null | null | null |
| BUILDING_NAME_LONG | Nuclear Reactor Laboratory | William R. Dickson Cogeneration Plant | 70 AMHERST |
| EXT_GROSS_AREA | 50294.2 | 80474.4 | 64847.3 |
| ASSIGNABLE_AREA | 34662.8 | 4209.52 | 36182.3 |
| NON_ASSIGNABLE_AREA | 10096.1 | 66630.4 | 18085.8 |
| SITE | MIT | MIT | MIT |
| CAMPUS_SECTOR | NORTHWEST | MAIN GROUP | EAST |
| ACCESS_LEVEL_CODE | 0 | 0 | 2 |
| ACCESS_LEVEL_NAME | 0 | 0 | 2 |
| BUILDING_TYPE | ACADEMIC | SERVICE | RESIDENT |
| OWNERSHIP_TYPE | OWNED | OWNED | OWNED |
| BUILDING_USE | AER | OTH | DHOA |
| OCCUPANCY_CLASS | UGB | UGF1 | UGR2 |
| BUILDING_HEIGHT | 47.3 | 64.8 | 63.7 |
| COST_CENTER_CODE | 1841200 | 1814200 | 1346000 |
| COST_COLLECTOR_KEY | 1841200 | 1814200 | 1346000 |
| LATITUDE_WGS | 42.3601 | 42.3611 | 42.36 |
| LONGITUDE_WGS | -71.0969 | -71.0935 | -71.0869 |
| EASTING_X_SPCS | 765123 | 766026 | 767825 |
| NORTHING_Y_SPCS | 3e+06 | 3e+06 | 3e+06 |
| BUILDING_SORT | NW12 | 42 | E02 |
| BUILDING_NAMED_FOR | - | - | WARE, ATKINSON,RUNKLE,CRAFTS,NICHOLS,HOLMAN |
| BUILDING_NAME | NUCLEAR REACTOR LAB | COGENERATION PLANT | 70 AMHERST |
| DATE_BUILT | 12/31/1937 | 12/31/1915 | 07/01/1913 |

# `fac_building_address`  (rows=785)

columns:
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=785
`BUILDING_ADDRESS_KEY` varchar127: all distinct
`BUILDING_KEY` varchar127: 242 distinct, "W70"=9, "W4"=7, "E25"=6, "W53"=6, "E15"=5, "E2"=5, "E23"=5, "E53"=5, "N4"=5, "N9"=5
`ADDRESS_PURPOSE` varchar127: "STREET"=242, "E911_1"=240, "MAIL"=159, "PARCL1"=107, "E911_2"=14, "PARCL2"=12, "E911_3"=3, "PARCL3"=3, "DELIVERY"=1, "E911_4"=1, "E911_5"=1, "E911_6"=1, "PARCL4"=1
`ADDRESS_CITY_ID` varchar127: digits, 120 distinct, nulls=336
`IS_E911_ADDRESS` varchar127: all NULL
`STREET_NUMBER` varchar127: 181 distinct
`STREET_NUMBER_SUFFIX` varchar127: "R"=26, nulls=759
`PRE_DIRECTIONAL` varchar127: all NULL
`STREET_NAME` varchar127: 32 distinct, nulls=124
`STREET_SUFFIX` varchar127: "ST"=295, "AVE"=188, "DR"=116, "RD"=36, "SQ"=11, "DRIVE"=5, "AVENUE"=2, "CIR"=2, nulls=130
`POST_DIRECTIONAL` varchar127: "(Rear)"=27, "NE"=2, "NW"=2, nulls=754
`CITY` varchar127: "CAMBRIDGE"=600, "MIDDLETON"=28, "WESTFORD"=27, "LEXINGTON"=18, "TYNGSBOROUGH"=9, "BOSTON"=5, "DEDHAM"=5, "WASHINGTON"=4, "HOLYOKE"=2, "MEDFORD"=2, "WILMINGTON"=2, nulls=83
`STATE` varchar127: "MA"=698, "DC"=4, nulls=83
`POSTAL_CODE` varchar127: "2139"=489, "2142"=194, "1949"=28, "1886"=27, "2421"=18, "1879"=9, "2026"=5, "2110"=3, "1040"=2, "1887"=2, "20002"=2, "20036"=2, "2155"=2, "2210"=2

indexes: `BUILDING_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| BUILDING_ADDRESS_KEY | WW15-STREET | E51-E911_1 | NW10-MAIL |
| BUILDING_KEY | WW15 | E51 | NW10 |
| ADDRESS_PURPOSE | STREET | E911_1 | MAIL |
| ADDRESS_CITY_ID | 25455 | 739 | 24250 |
| IS_E911_ADDRESS | null | null | null |
| STREET_NUMBER | 350 | 70 | 143 |
| STREET_NUMBER_SUFFIX | null | null | null |
| PRE_DIRECTIONAL | null | null | null |
| STREET_NAME | BROOKLINE | MEMORIAL | ALBANY |
| STREET_SUFFIX | ST | DR | ST |
| POST_DIRECTIONAL | null | null | null |
| CITY | CAMBRIDGE | CAMBRIDGE | CAMBRIDGE |
| STATE | MA | MA | MA |
| POSTAL_CODE | 2139 | 2142 | 2139 |

# `fac_floor`  (rows=1079)

columns:
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=1079
`BUILDING_KEY` varchar127: 239 distinct, "E37"=30, "W84"=28, "54"=23, "W61"=21, "W85"=20, "32"=18, "56"=11, "E62"=11, "W79"=11, "16"=10
`FLOOR` varchar127: 51 distinct
`FLOOR_KEY` varchar127: all distinct
`EXT_GROSS_AREA` float: 883 distinct, 0..120074, avg=13370.6, median=10439
`ASSIGNABLE_AREA` float: 868 distinct, 0..109714, avg=8198.84, median=5534.83
`NON_ASSIGNABLE_AREA` float: 926 distinct, 0..55975.8, avg=3672.43, median=2380.23
`FLOOR_SORT_SEQUENCE` varchar127: numeric, 34 distinct
`LEVEL_ID` varchar127: numeric, 30 distinct, nulls=119
`BUILDING_WINGS_ID` varchar127: "W61A.1"=1, "W61A.2"=1, "W61A.3"=1, "W61B.1"=1, "W61B.2"=1, "W61B.3"=1, "W61C.1"=1, "W61C.2"=1, "W61C.3"=1, "W61D.1 W61F.4 W61G.4 W61H.4 W61J.4 W61M.4"=1, "W61D.2"=1, "W61D.3"=1, "W61E.1 W61F.1 W61G.1 W61H.1 W61J.1 W61M.1"=1, "W61E.2 W61F.2 W61G.2 W61H.2 W61J.2 W61M.2"=1, "W61E.3 W61F.3 W61G.3 W61H.3 W61J.3 W61M.3"=1, nulls=1064
`ACCESS_LEVEL` varchar127: "2"=994, "1"=71, "0"=11, "3"=3

indexes: `BUILDING_KEY`, `FLOOR_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| BUILDING_KEY | WW15 | 62 | NW61 |
| FLOOR | 1 | 2 | 0 |
| FLOOR_KEY | WW15-1 | 62-2 | NW61-0 |
| EXT_GROSS_AREA | 40280.1 | 12836 | 7674.18 |
| ASSIGNABLE_AREA | 36378.2 | 8406.33 | 4477.81 |
| NON_ASSIGNABLE_AREA | 2313.55 | 3278.91 | 2012.78 |
| FLOOR_SORT_SEQUENCE | 1 | 2 | 0 |
| LEVEL_ID | 1 | 2 | 0 |
| BUILDING_WINGS_ID | null | null | null |
| ACCESS_LEVEL | 0 | 2 | 2 |

# `fac_major_use`  (rows=14)

columns:
`MAJOR_USE_KEY` varchar127: "101"=1, "102"=1, "103"=1, "104"=1, "105"=1, "106"=1, "107"=1, "108"=1, "109"=1, "110"=1, "111"=1, "112"=1, "113"=1, "114"=1
`MAJOR_USE` varchar127: "BLDG SRV"=1, "CIRCULAT"=1, "CLASSRMS"=1, "GENERAL"=1, "HEALTH"=1, "LABS"=1, "MECHANIC"=1, "OFFICES"=1, "RESIDENT"=1, "SPECIAL"=1, "STUDY"=1, "SUPPORT"=1, "UNCLASS"=1, "ZUSE"=1
`DESCRIPTION` varchar127: "BLDG SERVICE AREA"=1, "CIRCULATION AREA"=1, "CLASSROOMS"=1, "GENERAL USE"=1, "HEALTH CARE"=1, "LABORATORIES"=1, "MECHANICAL AREA"=1, "OFFICES"=1, "RESIDENTIAL"=1, "SPECIAL USE"=1, "STUDY"=1, "SUPPORT"=1, "UNCLASSIFIED"=1, "ZUSE ICR ONLY"=1
`ASSIGNABLE` varchar127: "1"=11, "0"=3
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=14

indexes: `MAJOR_USE_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MAJOR_USE_KEY | 114 | 110 | 101 |
| MAJOR_USE | ZUSE | SPECIAL | BLDG SRV |
| DESCRIPTION | ZUSE ICR ONLY | SPECIAL USE | BLDG SERVICE AREA |
| ASSIGNABLE | 1 | 1 | 0 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `fac_organization`  (rows=169)

columns:
`ORGANIZATION_KEY` varchar127: digits, all distinct
`ORGANIZATION_ID` varchar127: digits, unique identifier
`ORGANIZATION` varchar127: all distinct
`ORGANIZATION_NAME` varchar127: all distinct
`ORG_PARENT_KEY` varchar127: digits, 32 distinct, nulls=2
`ORG_PARENT` varchar127: 32 distinct, nulls=2
`MAJOR_ORG_KEY` varchar127: "230"=89, "129"=37, "163"=26, "271"=6, "267"=3, "216"=2, "105"=1, "125"=1, "210"=1, "217"=1, "224"=1, "275"=1
`MAJOR_ORG` varchar127: "PROVST"=89, "CHNCLR"=37, "EXECVP"=26, "ZORG"=6, "VP-SCP"=3, "OTHMIT"=2, "ALL"=1, "CHAIRM"=1, "OFPRES"=1, "OTHNON"=1, "PRES"=1, "XXXXX"=1
`ORGANIZATION_LEVEL` varchar127: "5"=107, "4"=40, "6"=12, "3"=7, "1"=2, "2"=1
`ORGANIZATION_NUMBER` varchar127: digits, 150 distinct, nulls=9
`ORGANIZATION_SORT` varchar127: digits, 164 distinct, nulls=1
`ASSIGNABLE` varchar127: "1"=166, "0"=3
`COURSE` varchar127: 31 distinct, nulls=137
`DESCRIPTION` varchar127: 64 distinct, nulls=103
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=169
`D_CODE` varchar127: 133 distinct, nulls=13
`HR_DEPARTMENT_CODE_OLD` varchar127: digits, 147 distinct, nulls=12
`HR_ORG_UNIT_ID` varchar127: digits, 147 distinct, nulls=12
`HR_DEPARTMENT_NAME` varchar127: 147 distinct, nulls=12

indexes: `ORGANIZATION_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| ORGANIZATION_KEY | 288 | 285 | 145 |
| ORGANIZATION_ID | 288 | 285 | 145 |
| ORGANIZATION | HEALTH | NANO | DCM |
| ORGANIZATION_NAME | MIT HEALTH | MIT.NANO | DIV OF COMP MED |
| ORG_PARENT_KEY | 163 | 266 | 266 |
| ORG_PARENT | EXECVP | VP-RES | VP-RES |
| MAJOR_ORG_KEY | 163 | 230 | 230 |
| MAJOR_ORG | EXECVP | PROVST | PROVST |
| ORGANIZATION_LEVEL | 4 | 5 | 5 |
| ORGANIZATION_NUMBER | 495000 | 417200 | 402100 |
| ORGANIZATION_SORT | 101030640 | 101060225 | 101060213 |
| ASSIGNABLE | 1 | 1 | 1 |
| COURSE | null | null | null |
| DESCRIPTION | null | MIT.Nano | Division of Comparative Medicine |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| D_CODE | D_MEDICAL | D_MIT.NANO | D_COMPMED |
| HR_DEPARTMENT_CODE_OLD | 495000 | 417200 | 402100 |
| HR_ORG_UNIT_ID | 10000792 | 10005458 | 10000612 |
| HR_DEPARTMENT_NAME | MIT Health | MIT.nano | Division of Comparative Medicine |

# `fac_rooms`  (rows=10000)

columns:
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000
`FAC_ROOM_KEY` varchar127: 9878 distinct
`BUILDING_KEY` varchar127: 188 distinct, "46"=859, "32"=436, "E37"=414, "54"=362, "36"=277, "68"=268, "76"=255, "E62"=201, "13"=192, "12"=188
`FLOOR` varchar127: 47 distinct
`FLOOR_KEY` varchar127: 827 distinct, "46-4"=227, "46-6"=161, "46-5"=128, "46-2"=110, "32-0"=95, "46-3"=77, "46-1"=75, "46-7"=58, "76-0"=48, "32-3"=47
`ROOM` varchar127: 3472 distinct, "137"=136, "282B"=106, "187"=103, "050"=88, "124E"=88, "274"=87, "307D"=87, "121"=84, "197F"=83, "133"=79
`SPACE_ID` varchar127: 9878 distinct
`MAJOR_USE_KEY` varchar127: "102"=4083, "107"=4075, "101"=1104, "106"=269, "109"=238, "108"=225, "110"=6
`MAJOR_USE_DESC` varchar127: "CIRCULAT"=4083, "MECHANIC"=4075, "BLDG SRV"=1104, "LABS"=269, "RESIDENT"=238, "OFFICES"=225, "SPECIAL"=6
`USE_KEY` varchar127: digits, 32 distinct
`USE_DESC` varchar127: all NULL
`MINOR_USE_KEY` varchar127: all NULL
`MINOR_USE_DESC` varchar127: all NULL
`ORGANIZATION_KEY` varchar127: "149"=9090, "203"=241, "236"=238, "235"=172, "221"=125, "115"=118, "145"=12, "246"=3, "133"=1
`ORGANIZATION_NAME` varchar127: "DOF"=9090, "MIBR"=241, "RESIDE"=238, "RESDOF"=172, "PILM"=125, "BCS"=118, "DCM"=12, "S SCI"=3, "CMPACT"=1
`MINOR_ORGANIZATION_KEY` varchar127: all NULL
`MINOR_ORGANIZATION` varchar127: all NULL
`AREA` float: 7328 distinct, 0..24043.4, avg=300.879, median=121.55
`ROOM_FULL_NAME` varchar127: all NULL
`DEPT_CODE` varchar127: all NULL
`ACCESS_LEVEL` varchar127: "3"=3932, "0"=3500, "1"=2018, "2"=550
`LATITUDE_WGS` float: all NULL
`LONGITUDE_WGS` float: all NULL
`NORTHING_SPCS` float: all NULL
`EASTING_SPCS` float: all NULL

indexes: `BUILDING_KEY`, `FAC_ROOM_KEY`, `FLOOR_KEY`, `MAJOR_USE_KEY`, `ORGANIZATION_KEY`, `ROOM`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| FAC_ROOM_KEY | WW15-197H | 32-063 | 46-169F |
| BUILDING_KEY | WW15 | 32 | 46 |
| FLOOR | 1 | 0 | 1 |
| FLOOR_KEY | WW15-1 | 32-0 | 46-1 |
| ROOM | 197H | 063 | 169F |
| SPACE_ID | WW15-1-197H | 32-0-063 | 46-1-169F |
| MAJOR_USE_KEY | 101 | 107 | 101 |
| MAJOR_USE_DESC | BLDG SRV | MECHANIC | BLDG SRV |
| USE_KEY | 106 | 156 | 197 |
| USE_DESC | null | null | null |
| MINOR_USE_KEY | null | null | null |
| MINOR_USE_DESC | null | null | null |
| ORGANIZATION_KEY | 149 | 149 | 149 |
| ORGANIZATION_NAME | DOF | DOF | DOF |
| MINOR_ORGANIZATION_KEY | null | null | null |
| MINOR_ORGANIZATION | null | null | null |
| AREA | 126 | 392.94 | 32.13 |
| ROOM_FULL_NAME | null | null | null |
| DEPT_CODE | null | null | null |
| ACCESS_LEVEL | 3 | 0 | 1 |
| LATITUDE_WGS | null | null | null |
| LONGITUDE_WGS | null | null | null |
| NORTHING_SPCS | null | null | null |
| EASTING_SPCS | null | null | null |

# `fclt_building`  (rows=242)

columns:
`FCLT_BUILDING_KEY` varchar127: all distinct
`BUILDING_NUMBER` varchar127: all distinct
`PARENT_BUILDING_NUMBER` varchar127: "W61"=10, "14"=4, "62"=3, "64"=3, "W85ABC"=3, "W85HJK"=3, "W85DE"=2, "W85FG"=2, "42"=1, nulls=211
`PARENT_BUILDING_NAME` varchar127: "MACGREGOR HOUSE"=10, "HAYDEN MEMORIAL LIBRARY"=4, "ALUMNI HOUSES: MUNROE HAYDEN WOOD"=3, "EAST CAMPUS: WALCOTT BEMIS GOODALE"=3, "WESTGATE (ABC)"=3, "WESTGATE (HJK)"=3, "WESTGATE (DE)"=2, "WESTGATE (FG)"=2, "COGENERATION PLANT"=1, nulls=211
`PARENT_BUILDING_NAME_LONG` varchar127: "Frank S MacGregor House"=10, "Charles Hayden Memorial Library"=4, "Alumni Houses: Munroe Hayden Wood"=3, "Alumni Houses: Walcott Bemis Goodale"=3, "Westgate ABC"=3, "Westgate HJK"=3, "Westgate DE"=2, "Westgate FG"=2, "William R. Dickson Cogeneration Plant"=1, nulls=211
`BUILDING_NAME_LONG` varchar127: 235 distinct
`EXT_GROSS_AREA` float: 231 distinct, 0..466722, avg=59615.1, median=25763.6
`ASSIGNABLE_AREA` float: 226 distinct, 0..285682, avg=36556, median=16825
`NON_ASSIGNABLE_AREA` float: 206 distinct, 0..151963, avg=16374.2, median=4810.29
`SITE` varchar127: "MIT"=198, "BATES"=14, "HAY"=12, "LINC"=9, "BOS"=2, "DC"=2, "END"=2, "HOLYOKE"=1, "MED"=1, "WILM"=1
`CAMPUS_SECTOR` varchar127: "WEST"=71, "MAIN GROUP"=60, "OFFCAMPUS"=44, "EAST"=25, "NORTHWEST"=22, "NORTH"=11, "NORTHEAST"=8, "WESTWEST"=1
`ACCESS_LEVEL_CODE` int: 2=185, 1=47, 0=10, 0..2
`ACCESS_LEVEL_NAME` varchar127: "2"=185, "1"=47, "0"=10
`BUILDING_TYPE` varchar127: "ACADEMIC"=126, "SERVICE"=59, "RESIDENT"=57
`OWNERSHIP_TYPE` varchar127: "OWNED"=220, "LEASED"=22
`BUILDING_USE` varchar127: "AER"=124, "DHOA"=54, "OTH"=32, "STAC"=17, "(NULL)"=8, "GAR"=7
`OCCUPANCY_CLASS` varchar127: 20 distinct
`BUILDING_HEIGHT` varchar127: numeric, 110 distinct, nulls=60
`COST_CENTER_CODE` varchar127: digits, 109 distinct, nulls=111, "1876000"=14, "1348000"=5, "1810700"=3, "1346200"=2, "1810600"=2, "1814200"=2, "1342002"=1, "1345000"=1, "1345300"=1, "1345500"=1
`COST_COLLECTOR_KEY` varchar127: digits, 109 distinct, nulls=111, "1876000"=14, "1348000"=5, "1810700"=3, "1346200"=2, "1810600"=2, "1814200"=2, "1342002"=1, "1345000"=1, "1345300"=1, "1345500"=1
`LATITUDE_WGS` float: 78 distinct, nulls=104, 42.2539..42.6233, avg=42.3812, median=42.3601
`LONGITUDE_WGS` float: 109 distinct, nulls=104, -71.4937..-70.979, avg=-71.1068, median=-71.0935
`EASTING_X_SPCS` float: 134 distinct, nulls=104, 657854..796445, avg=762408, median=766026
`NORTHING_Y_SPCS` float: 115 distinct, nulls=104, 2.9e+06..3.1e+06, avg=3e+06, median=3e+06
`BUILDING_SORT` varchar127: all distinct
`BUILDING_NAMED_FOR` varchar127: 68 distinct, nulls=41
`BUILDING_NAME` varchar127: 236 distinct
`DATE_BUILT` varchar127: 111 distinct, nulls=92
`DATE_ACQUIRED` varchar127: 25 distinct, nulls=212
`DATE_OCCUPIED` varchar127: 136 distinct, nulls=62
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=242
`NUM_OF_ROOMS` int: 151 distinct, 0..1424, avg=178.4091, median=90.5

indexes: `ACCESS_LEVEL_CODE`, `COST_CENTER_CODE`, `COST_COLLECTOR_KEY`, `FCLT_BUILDING_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_BUILDING_KEY | WW15 | OC19C | W33 |
| BUILDING_NUMBER | WW15 | OC19C | W33 |
| PARENT_BUILDING_NUMBER | null | null | null |
| PARENT_BUILDING_NAME | null | null | null |
| PARENT_BUILDING_NAME_LONG | null | null | null |
| BUILDING_NAME_LONG | Building WW15 | BATES LINAC: North Experimental Hall | Rockwell Athletic Cage |
| EXT_GROSS_AREA | 42145.8 | 6081.18 | 34427.7 |
| ASSIGNABLE_AREA | 37271.3 | 5375.22 | 32379.2 |
| NON_ASSIGNABLE_AREA | 3048.68 | 11.05 | 594.57 |
| SITE | MIT | BATES | MIT |
| CAMPUS_SECTOR | WESTWEST | OFFCAMPUS | WEST |
| ACCESS_LEVEL_CODE | 2 | 1 | 2 |
| ACCESS_LEVEL_NAME | 2 | 1 | 2 |
| BUILDING_TYPE | SERVICE | ACADEMIC | SERVICE |
| OWNERSHIP_TYPE | OWNED | OWNED | OWNED |
| BUILDING_USE | AER | AER | STAC |
| OCCUPANCY_CLASS | UGS2 | (NULL) | UGA3 |
| BUILDING_HEIGHT | 16 | null | 22.8 |
| COST_CENTER_CODE | 1846500 | 1876000 | 1833300 |
| COST_COLLECTOR_KEY | 1846500 | 1876000 | 1833300 |
| LATITUDE_WGS | 42.3554 | 42.5984 | 42.3592 |
| LONGITUDE_WGS | -71.1095 | -70.9803 | -71.096 |
| EASTING_X_SPCS | 761724 | 796100 | 765366 |
| NORTHING_Y_SPCS | 3e+06 | 3e+06 | 3e+06 |
| BUILDING_SORT | WW15 | OC19C | W33 |
| BUILDING_NAMED_FOR | - | - | JOHN ARNOLD ROCKWELL M.D. |
| BUILDING_NAME | BUILDING WW15 | BATES LINAC: NORTH EXPERIMENTAL HALL | ROCKWELL CAGE |
| DATE_BUILT | 12/31/1969 | null | 07/01/1947 |
| DATE_ACQUIRED | null | null | null |
| DATE_OCCUPIED | 12/31/1969 | null | 06/01/1948 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| NUM_OF_ROOMS | 109 | 4 | 7 |

# `fclt_building_address`  (rows=785)

columns:
`POSTAL_CODE` varchar127: "2139"=489, "2142"=194, "1949"=28, "1886"=27, "2421"=18, "1879"=9, "2026"=5, "2110"=3, "1040"=2, "1887"=2, "20002"=2, "20036"=2, "2155"=2, "2210"=2
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=785
`FCLT_BUILDING_ADDRESS_KEY` varchar127: all distinct
`FCLT_BUILDING_KEY` varchar127: 242 distinct, "W70"=9, "W4"=7, "E25"=6, "W53"=6, "E15"=5, "E2"=5, "E23"=5, "E53"=5, "N4"=5, "N9"=5
`BUILDING_NUMBER` varchar127: 242 distinct
`ADDRESS_PURPOSE` varchar127: "STREET"=242, "E911_1"=240, "MAIL"=159, "PARCL1"=107, "E911_2"=14, "PARCL2"=12, "E911_3"=3, "PARCL3"=3, "DELIVERY"=1, "E911_4"=1, "E911_5"=1, "E911_6"=1, "PARCL4"=1
`ADDRESS_CITY_ID` varchar127: digits, 120 distinct, nulls=336
`IS_E911_ADDRESS` varchar127: all NULL
`STREET_NUMBER` varchar127: 181 distinct
`STREET_NUMBER_SUFFIX` varchar127: "R"=26, nulls=759
`PRE_DIRECTIONAL` varchar127: all NULL
`STREET_NAME` varchar127: 32 distinct, nulls=124
`STREET_SUFFIX` varchar127: "ST"=295, "AVE"=188, "DR"=116, "RD"=36, "SQ"=11, "DRIVE"=5, "AVENUE"=2, "CIR"=2, nulls=130
`POST_DIRECTIONAL` varchar127: "(Rear)"=27, "NE"=2, "NW"=2, nulls=754
`CITY` varchar127: "CAMBRIDGE"=600, "MIDDLETON"=28, "WESTFORD"=27, "LEXINGTON"=18, "TYNGSBOROUGH"=9, "BOSTON"=5, "DEDHAM"=5, "WASHINGTON"=4, "HOLYOKE"=2, "MEDFORD"=2, "WILMINGTON"=2, nulls=83
`STATE` varchar127: "MA"=698, "DC"=4, nulls=83

indexes: `FCLT_BUILDING_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| POSTAL_CODE | 2421 | 1886 | 2139 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| FCLT_BUILDING_ADDRESS_KEY | OC36A-STREET | OC21C-MAIL | N47-E911_1 |
| FCLT_BUILDING_KEY | OC36A | OC21C | N47 |
| BUILDING_NUMBER | OC36A | OC21C | N47 |
| ADDRESS_PURPOSE | STREET | MAIL | E911_1 |
| ADDRESS_CITY_ID | null | null | null |
| IS_E911_ADDRESS | null | null | null |
| STREET_NUMBER | 244 | 50 | 730 |
| STREET_NUMBER_SUFFIX | null | null | null |
| PRE_DIRECTIONAL | null | null | null |
| STREET_NAME | WOOD | GROTON | MAIN |
| STREET_SUFFIX | ST | RD | ST |
| POST_DIRECTIONAL | null | null | null |
| CITY | LEXINGTON | WESTFORD | CAMBRIDGE |
| STATE | MA | MA | MA |

# `fclt_building_address_hist`  (rows=10000)

columns:
`FCLT_BUILDING_ADDRESS_KEY` varchar127: 785 distinct
`FCLT_BUILDING_KEY` varchar127: 233 distinct
`FISCAL_PERIOD` varchar127: "201511"=776, "201505"=774, "201506"=774, "201507"=774, "201508"=774, "201509"=774, "201510"=774, "201512"=768, "201601"=768, "201602"=768, "201605"=484, "201603"=465, "201604"=426, "201606"=414, "201701"=349, "201610"=138
`FCLT_BUILDING_ADDRESS_HIST_KEY` varchar127: all distinct
`BUILDING_NUMBER` varchar127: 233 distinct
`ADDRESS_PURPOSE` varchar127: "E911_1"=2995, "STREET"=2990, "MAIL"=1919, "PARCL1"=1498, "E911_2"=261, "PARCL2"=153, "E911_3"=78, "PARCL3"=36, "E911_4"=34, "E911_5"=12, "E911_6"=12, "PARCL4"=12
`ADDRESS_CITY_ID` varchar127: digits, 133 distinct, nulls=4265
`IS_E911_ADDRESS` varchar127: all NULL
`STREET_NUMBER` varchar127: 192 distinct
`STREET_NUMBER_SUFFIX` varchar127: "R"=301, nulls=9699
`PRE_DIRECTIONAL` varchar127: all NULL
`STREET_NAME` varchar127: 34 distinct, nulls=1724
`STREET_SUFFIX` varchar127: "ST"=3515, "AVE"=2561, "DR"=1456, "RD"=272, "SQ"=189, "DRIVE"=108, "PARK"=28, nulls=1871
`POST_DIRECTIONAL` varchar127: "(Rear)"=345, "NE"=32, nulls=9623
`CITY` varchar127: "CAMBRIDGE"=7643, "MIDDLETON"=448, "WESTFORD"=272, "LEXINGTON"=231, "BOSTON"=80, "DEDHAM"=80, "SOMERVILLE"=32, "WASHINGTON"=32, "HOLYOKE"=24, nulls=1158
`STATE` varchar127: "MA"=8810, "DC"=32, nulls=1158
`POSTAL_CODE` varchar127: "2139"=6191, "2142"=2580, "1949"=448, "1886"=272, "2421"=231, "2026"=80, "2110"=48, "20002"=32, "2143"=32, "2210"=32, "2141"=30, "1040"=24
`WAREHOUSE_LOAD_DATE` varchar255: "01-JUN-15"=776, "01-APR-15"=774, "01-DEC-14"=774, "01-FEB-15"=774, "01-JAN-15"=774, "01-MAR-15"=774, "01-MAY-15"=774, "01-AUG-15"=768, "01-JUL-15"=768, "01-SEP-15"=768, "01-DEC-15"=484, "01-OCT-15"=465, "31-OCT-15"=426, "01-JAN-16"=414, "01-AUG-16"=349, "01-MAY-16"=138

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_BUILDING_ADDRESS_KEY | WW25-STREET | OC1-E911_1 | 37-E911_1 |
| FCLT_BUILDING_KEY | WW25 | OC1 | 37 |
| FISCAL_PERIOD | 201602 | 201510 | 201505 |
| FCLT_BUILDING_ADDRESS_HIST_KEY | WW25-STREET-201602 | OC1-E911_1-201510 | 37-E911_1-201505 |
| BUILDING_NUMBER | WW25 | OC1 | 37 |
| ADDRESS_PURPOSE | STREET | E911_1 | E911_1 |
| ADDRESS_CITY_ID | 31908 | null | 706 |
| IS_E911_ADDRESS | null | null | null |
| STREET_NUMBER | 142 | 80 | 70 |
| STREET_NUMBER_SUFFIX | null | null | null |
| PRE_DIRECTIONAL | null | null | null |
| STREET_NAME | WAVERLY | HAVEN | VASSAR |
| STREET_SUFFIX | ST | ST | ST |
| POST_DIRECTIONAL | null | null | null |
| CITY | CAMBRIDGE | DEDHAM | CAMBRIDGE |
| STATE | MA | MA | MA |
| POSTAL_CODE | 2139 | 2026 | 2139 |
| WAREHOUSE_LOAD_DATE | 01-SEP-15 | 01-MAY-15 | 01-DEC-14 |

# `fclt_building_hist`  (rows=10000)

columns:
`FCLT_BUILDING_HIST_KEY` varchar127: all distinct
`FISCAL_PERIOD` varchar127: digits, 48 distinct
`FCLT_BUILDING_KEY` varchar127: 255 distinct
`BUILDING_NUMBER` varchar127: 255 distinct
`PARENT_BUILDING_NUMBER` varchar127: "W61"=410, "W70"=287, "14"=172, "62"=129, "64"=127, "W85ABC"=123, "W85HJK"=120, "W85DE"=80, "W85FG"=80, "42"=38, nulls=8434
`PARENT_BUILDING_NAME` varchar127: "MACGREGOR HOUSE"=410, "NEW HOUSE"=287, "HAYDEN MEMORIAL LIBRARY"=172, "ALUMNI HOUSES: MUNROE HAYDEN WOOD"=129, "EAST CAMPUS: WALCOTT BEMIS GOODALE"=127, "WESTGATE (ABC)"=123, "WESTGATE (HJK)"=120, "WESTGATE (DE)"=80, "WESTGATE (FG)"=80, "COGENERATION PLANT"=38, nulls=8434
`PARENT_BUILDING_NAME_LONG` varchar127: "Frank S MacGregor House"=410, "New West Campus Houses"=287, "Charles Hayden Memorial Library"=172, "Alumni Houses: Munroe Hayden Wood"=129, "Alumni Houses: Walcott Bemis Goodale"=127, "Westgate ABC"=123, "Westgate HJK"=120, "Westgate DE"=80, "Westgate FG"=80, "William R. Dickson Cogeneration Plant"=38, nulls=8434
`BUILDING_NAME_LONG` varchar127: 268 distinct
`EXT_GROSS_AREA` float: 363 distinct, 0..464005, avg=59102.4, median=25892.9
`ASSIGNABLE_AREA` float: 654 distinct, 0..287221, avg=37505.3, median=17041.1
`NON_ASSIGNABLE_AREA` float: 577 distinct, 0..152820, avg=15178, median=4724.43
`SITE` varchar127: "MIT"=8397, "BATES"=566, "LINC"=373, "HAY"=363, "BOS"=93, "END"=85, "SOM"=42, "HOLYOKE"=41, "DC"=40
`CAMPUS_SECTOR` varchar127: "WEST"=2912, "MAIN GROUP"=2585, "OFFCAMPUS"=1502, "EAST"=935, "NORTHWEST"=685, "NORTH"=436, "NORTHEAST"=261, "WESTWEST"=80, "EASTEAST"=45, nulls=559
`ACCESS_LEVEL_CODE` int: 2=7572, 1=1762, 0=479, 3=187, 0..3
`ACCESS_LEVEL_NAME` varchar127: "2"=7572, "1"=1762, "0"=479, "3"=187
`BUILDING_TYPE` varchar127: "ACADEMIC"=5057, "RESIDENT"=2563, "SERVICE"=2380
`OWNERSHIP_TYPE` varchar127: "OWNED"=9001, "LEASED"=999
`BUILDING_USE` varchar127: "AER"=5147, "DHOA"=2496, "OTH"=1248, "STAC"=729, "(NULL)"=212, "GAR"=168
`OCCUPANCY_CLASS` varchar127: 25 distinct
`BUILDING_HEIGHT` varchar127: numeric, 124 distinct, nulls=3227
`COST_CENTER_CODE` varchar127: digits, 120 distinct, nulls=3949, "1876000"=566, "1348000"=210, "1810600"=137, "1810700"=137, "1346200"=88, "1814200"=88, "1345000"=46, "1346000"=46, "1346800"=46, "1811000"=46
`COST_COLLECTOR_KEY` varchar127: digits, 120 distinct, nulls=3949, "1876000"=566, "1348000"=210, "1810600"=137, "1810700"=137, "1346200"=88, "1814200"=88, "1345000"=46, "1346000"=46, "1346800"=46, "1811000"=46
`LATITUDE_WGS` float: 81 distinct, nulls=3497, 42.2539..42.6233, avg=42.3783, median=42.3602
`LONGITUDE_WGS` float: 120 distinct, nulls=3497, -71.4937..-70.979, avg=-71.1052, median=-71.0932
`EASTING_X_SPCS` float: 150 distinct, nulls=3497, 922.337..796445, avg=754952, median=766034
`NORTHING_Y_SPCS` float: 128 distinct, nulls=3497, 922.337..3.1e+06, avg=2.9e+06, median=3e+06
`BUILDING_SORT` varchar127: 255 distinct
`BUILDING_NAMED_FOR` varchar127: 66 distinct, nulls=1332
`BUILDING_NAME` varchar127: 264 distinct
`DATE_BUILT` varchar127: 102 distinct, nulls=4073
`DATE_ACQUIRED` varchar127: 30 distinct, nulls=8692
`DATE_OCCUPIED` varchar127: 111 distinct, nulls=4271
`WAREHOUSE_LOAD_DATE` varchar255: 48 distinct
`NUM_OF_ROOMS` int: 358 distinct, 0..1410, avg=179.2031, median=95

indexes: `ACCESS_LEVEL_CODE`, `COST_CENTER_CODE`, `COST_COLLECTOR_KEY`, `FCLT_BUILDING_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_BUILDING_HIST_KEY | WW25-201902 | N52-201704 | OC21A-201806 |
| FISCAL_PERIOD | 201902 | 201704 | 201806 |
| FCLT_BUILDING_KEY | WW25 | N52 | OC21A |
| BUILDING_NUMBER | WW25 | N52 | OC21A |
| PARENT_BUILDING_NUMBER | null | null | null |
| PARENT_BUILDING_NAME | null | null | null |
| PARENT_BUILDING_NAME_LONG | null | null | null |
| BUILDING_NAME_LONG | Building WW25 | MIT Museum | OC21A |
| EXT_GROSS_AREA | 2300.01 | 103874 | 450.17 |
| ASSIGNABLE_AREA | 2300 | 71470.3 | 426.64 |
| NON_ASSIGNABLE_AREA | 0 | 21215.7 | 0 |
| SITE | MIT | MIT | HAY |
| CAMPUS_SECTOR | WESTWEST | NORTH | null |
| ACCESS_LEVEL_CODE | 2 | 2 | 2 |
| ACCESS_LEVEL_NAME | 2 | 2 | 2 |
| BUILDING_TYPE | SERVICE | ACADEMIC | ACADEMIC |
| OWNERSHIP_TYPE | LEASED | OWNED | OWNED |
| BUILDING_USE | OTH | AER | AER |
| OCCUPANCY_CLASS | UGS1 | UGA3B | (NULL) |
| BUILDING_HEIGHT | null | 56.8 | 0 |
| COST_CENTER_CODE | null | 1855200 | null |
| COST_COLLECTOR_KEY | null | 1855200 | null |
| LATITUDE_WGS | 42.3557 | 42.3623 | null |
| LONGITUDE_WGS | -71.1063 | -71.0972 | null |
| EASTING_X_SPCS | 762573 | 765032 | null |
| NORTHING_Y_SPCS | 3e+06 | 3e+06 | null |
| BUILDING_SORT | WW25 | N52 | OC21A |
| BUILDING_NAMED_FOR | - | - | null |
| BUILDING_NAME | BUILDING WW25 | MIT MUSEUM | WALLACE ASTROPHYSICAL OBSERVATORY |
| DATE_BUILT | null | 12/31/1924 | null |
| DATE_ACQUIRED | null | 04/16/1982 | null |
| DATE_OCCUPIED | null | 01/01/1964 | null |
| WAREHOUSE_LOAD_DATE | 01-SEP-18 | 01-NOV-16 | 01-JAN-18 |
| NUM_OF_ROOMS | 2 | 323 | 1 |

# `fclt_building_hist_1`  (rows=10000)

columns:
`FCLT_BUILDING_HIST_KEY` varchar127: all distinct
`FISCAL_PERIOD` varchar127: digits, 48 distinct
`FCLT_BUILDING_KEY` varchar127: 255 distinct
`BUILDING_NUMBER` varchar127: 255 distinct
`PARENT_BUILDING_NUMBER` varchar127: "W61"=410, "W70"=287, "14"=172, "62"=129, "64"=127, "W85ABC"=123, "W85HJK"=120, "W85DE"=80, "W85FG"=80, "42"=38, nulls=8434
`PARENT_BUILDING_NAME` varchar127: "MACGREGOR HOUSE"=410, "NEW HOUSE"=287, "HAYDEN MEMORIAL LIBRARY"=172, "ALUMNI HOUSES: MUNROE HAYDEN WOOD"=129, "EAST CAMPUS: WALCOTT BEMIS GOODALE"=127, "WESTGATE (ABC)"=123, "WESTGATE (HJK)"=120, "WESTGATE (DE)"=80, "WESTGATE (FG)"=80, "COGENERATION PLANT"=38, nulls=8434
`PARENT_BUILDING_NAME_LONG` varchar127: "Frank S MacGregor House"=410, "New West Campus Houses"=287, "Charles Hayden Memorial Library"=172, "Alumni Houses: Munroe Hayden Wood"=129, "Alumni Houses: Walcott Bemis Goodale"=127, "Westgate ABC"=123, "Westgate HJK"=120, "Westgate DE"=80, "Westgate FG"=80, "William R. Dickson Cogeneration Plant"=38, nulls=8434
`BUILDING_NAME_LONG` varchar127: 268 distinct
`EXT_GROSS_AREA` float: 363 distinct, 0..464005, avg=59102.4, median=25892.9
`ASSIGNABLE_AREA` float: 654 distinct, 0..287221, avg=37505.3, median=17041.1
`NON_ASSIGNABLE_AREA` float: 577 distinct, 0..152820, avg=15178, median=4724.43
`SITE` varchar127: "MIT"=8397, "BATES"=566, "LINC"=373, "HAY"=363, "BOS"=93, "END"=85, "SOM"=42, "HOLYOKE"=41, "DC"=40
`CAMPUS_SECTOR` varchar127: "WEST"=2912, "MAIN GROUP"=2585, "OFFCAMPUS"=1502, "EAST"=935, "NORTHWEST"=685, "NORTH"=436, "NORTHEAST"=261, "WESTWEST"=80, "EASTEAST"=45, nulls=559
`ACCESS_LEVEL_CODE` int: 2=7572, 1=1762, 0=479, 3=187, 0..3
`ACCESS_LEVEL_NAME` varchar127: "2"=7572, "1"=1762, "0"=479, "3"=187
`BUILDING_TYPE` varchar127: "ACADEMIC"=5057, "RESIDENT"=2563, "SERVICE"=2380
`OWNERSHIP_TYPE` varchar127: "OWNED"=9001, "LEASED"=999
`BUILDING_USE` varchar127: "AER"=5147, "DHOA"=2496, "OTH"=1248, "STAC"=729, "(NULL)"=212, "GAR"=168
`OCCUPANCY_CLASS` varchar127: 25 distinct
`BUILDING_HEIGHT` varchar127: numeric, 124 distinct, nulls=3227
`COST_CENTER_CODE` varchar127: digits, 120 distinct, nulls=3949
`COST_COLLECTOR_KEY` varchar127: digits, 120 distinct, nulls=3949
`LATITUDE_WGS` float: 81 distinct, nulls=3497, 42.2539..42.6233, avg=42.3783, median=42.3602
`LONGITUDE_WGS` float: 120 distinct, nulls=3497, -71.4937..-70.979, avg=-71.1052, median=-71.0932
`EASTING_X_SPCS` float: 150 distinct, nulls=3497, 922.337..796445, avg=754952, median=766034
`NORTHING_Y_SPCS` float: 128 distinct, nulls=3497, 922.337..3.1e+06, avg=2.9e+06, median=3e+06
`BUILDING_SORT` varchar127: 255 distinct
`BUILDING_NAMED_FOR` varchar127: 66 distinct, nulls=1332
`BUILDING_NAME` varchar127: 264 distinct
`DATE_BUILT` varchar255: 102 distinct, nulls=4073
`DATE_ACQUIRED` varchar255: 30 distinct, nulls=8692
`DATE_OCCUPIED` varchar255: 110 distinct, nulls=4271
`WAREHOUSE_LOAD_DATE` varchar255: 48 distinct
`NUM_OF_ROOMS` int: 358 distinct, 0..1410, avg=179.2031, median=95

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_BUILDING_HIST_KEY | WW25-201902 | 16-201606 | W70-201609 |
| FISCAL_PERIOD | 201902 | 201606 | 201609 |
| FCLT_BUILDING_KEY | WW25 | 16 | W70 |
| BUILDING_NUMBER | WW25 | 16 | W70 |
| PARENT_BUILDING_NUMBER | null | null | null |
| PARENT_BUILDING_NAME | null | null | null |
| PARENT_BUILDING_NAME_LONG | null | null | null |
| BUILDING_NAME_LONG | Building WW25 | Dorrance Building | New West Campus Houses |
| EXT_GROSS_AREA | 2300.01 | 116214 | 114713 |
| ASSIGNABLE_AREA | 2300 | 57877.5 | 68771.2 |
| NON_ASSIGNABLE_AREA | 0 | 46857.9 | 32525.9 |
| SITE | MIT | MIT | MIT |
| CAMPUS_SECTOR | WESTWEST | MAIN GROUP | WEST |
| ACCESS_LEVEL_CODE | 2 | 2 | 2 |
| ACCESS_LEVEL_NAME | 2 | 2 | 2 |
| BUILDING_TYPE | SERVICE | ACADEMIC | RESIDENT |
| OWNERSHIP_TYPE | LEASED | OWNED | OWNED |
| BUILDING_USE | OTH | AER | DHOA |
| OCCUPANCY_CLASS | UGS1 | UGBA3 | UGR2 |
| BUILDING_HEIGHT | null | 122.9 | 46.9 |
| COST_CENTER_CODE | null | 1811600 | 1347500 |
| COST_COLLECTOR_KEY | null | 1811600 | 1347500 |
| LATITUDE_WGS | 42.3557 | 42.3604 | 42.3552 |
| LONGITUDE_WGS | -71.1063 | -71.0906 | -71.1005 |
| EASTING_X_SPCS | 762573 | 766817 | 764140 |
| NORTHING_Y_SPCS | 3e+06 | 3e+06 | 3e+06 |
| BUILDING_SORT | WW25 | 16 | W70 |
| BUILDING_NAMED_FOR | - | JOHN THOMPSON DORRANCE | - |
| BUILDING_NAME | BUILDING WW25 | DORRANCE BUILDING | NEW HOUSE |
| DATE_BUILT | null | 01-NOV-50 | 01-JUN-74 |
| DATE_ACQUIRED | null | null | null |
| DATE_OCCUPIED | null | 01-JUN-52 | 31-DEC-76 |
| WAREHOUSE_LOAD_DATE | 01-SEP-18 | 01-JAN-16 | 01-APR-16 |
| NUM_OF_ROOMS | 2 | 370 | 13 |

# `fclt_floor`  (rows=1079)

columns:
`FCLT_FLOOR_KEY` varchar127: all distinct
`FCLT_BUILDING_KEY` varchar127: 239 distinct, "E37"=30, "W84"=28, "54"=23, "W61"=21, "W85"=20, "32"=18, "56"=11, "E62"=11, "W79"=11, "16"=10
`FLOOR` varchar127: 51 distinct
`EXT_GROSS_AREA` float: 883 distinct, 0..120074, avg=13370.6, median=10439
`ASSIGNABLE_AREA` float: 868 distinct, 0..109714, avg=8198.84, median=5534.83
`NON_ASSIGNABLE_AREA` float: 926 distinct, 0..55975.8, avg=3672.43, median=2380.23
`FLOOR_SORT_SEQUENCE` varchar127: numeric, 34 distinct
`LEVEL_ID` varchar127: numeric, 30 distinct, nulls=119
`BUILDING_WINGS_ID` varchar127: "W61A.1"=1, "W61A.2"=1, "W61A.3"=1, "W61B.1"=1, "W61B.2"=1, "W61B.3"=1, "W61C.1"=1, "W61C.2"=1, "W61C.3"=1, "W61D.1 W61F.4 W61G.4 W61H.4 W61J.4 W61M.4"=1, "W61D.2"=1, "W61D.3"=1, "W61E.1 W61F.1 W61G.1 W61H.1 W61J.1 W61M.1"=1, "W61E.2 W61F.2 W61G.2 W61H.2 W61J.2 W61M.2"=1, "W61E.3 W61F.3 W61G.3 W61H.3 W61J.3 W61M.3"=1, nulls=1064
`ACCESS_LEVEL` varchar127: "2"=994, "1"=71, "0"=11, "3"=3
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=1079

indexes: `FCLT_BUILDING_KEY`, `FCLT_FLOOR_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_FLOOR_KEY | WW15-1 | NE18-5 | W84-13 |
| FCLT_BUILDING_KEY | WW15 | NE18 | W84 |
| FLOOR | 1 | 5 | 13 |
| EXT_GROSS_AREA | 40280.1 | 13425.8 | 5850.4 |
| ASSIGNABLE_AREA | 36378.2 | 12175.5 | 4416.79 |
| NON_ASSIGNABLE_AREA | 2313.55 | 8.42 | 800.19 |
| FLOOR_SORT_SEQUENCE | 1 | 5 | 13 |
| LEVEL_ID | 1 | 5 | 13 |
| BUILDING_WINGS_ID | null | null | null |
| ACCESS_LEVEL | 0 | 2 | 2 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `fclt_floor_hist`  (rows=10000)

columns:
`FCLT_FLOOR_HIST_KEY` varchar127: all distinct
`FISCAL_PERIOD` varchar127: "201511"=1054, "201509"=1052, "201510"=1052, "201512"=1049, "201601"=1049, "201505"=1037, "201506"=1037, "201507"=1037, "201508"=1037, "201602"=596
`FCLT_FLOOR_KEY` varchar127: 1054 distinct
`FCLT_BUILDING_KEY` varchar127: 230 distinct
`FLOOR` varchar127: 49 distinct
`EXT_GROSS_AREA` float: 883 distinct, 0..120074, avg=12994.7, median=8774.44
`ASSIGNABLE_AREA` float: 1065 distinct, 0..109754, avg=8255.7, median=5285.71
`NON_ASSIGNABLE_AREA` float: 1064 distinct, 0..53451.2, avg=3327.5, median=1898.79
`FLOOR_SORT_SEQUENCE` varchar127: numeric, 34 distinct
`LEVEL_ID` varchar127: numeric, 34 distinct, nulls=86
`BUILDING_WINGS_ID` varchar127: "W61A.1"=9, "W61A.2"=9, "W61A.3"=9, "W61B.1"=9, "W61B.2"=9, "W61B.3"=9, "W61C.1"=9, "W61C.2"=9, "W61C.3"=9, "W61D.1 W61F.4 W61G.4 W61H.4 W61J.4 W61M.4"=9, "W61D.2"=9, "W61D.3"=9, "W61E.1 W61F.1 W61G.1 W61H.1 W61J.1 W61M.1"=9, "W61E.2 W61F.2 W61G.2 W61H.2 W61J.2 W61M.2"=9, "W61E.3 W61F.3 W61G.3 W61H.3 W61J.3 W61M.3"=9, nulls=9865
`ACCESS_LEVEL` varchar127: "2"=9418, "3"=286, "1"=155, "0"=141
`WAREHOUSE_LOAD_DATE` varchar255: "01-JUN-15"=1054, "01-APR-15"=1052, "01-MAY-15"=1052, "01-AUG-15"=1049, "01-JUL-15"=1049, "01-DEC-14"=1037, "01-FEB-15"=1037, "01-JAN-15"=1037, "01-MAR-15"=1037, "01-SEP-15"=596

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_FLOOR_HIST_KEY | WW25-1-201601 | N16C-1-201507 | 6-5-201602 |
| FISCAL_PERIOD | 201601 | 201507 | 201602 |
| FCLT_FLOOR_KEY | WW25-1 | N16C-1 | 6-5 |
| FCLT_BUILDING_KEY | WW25 | N16C | 6 |
| FLOOR | 1 | 1 | 5 |
| EXT_GROSS_AREA | 2300.01 | 2925.3 | 482.4 |
| ASSIGNABLE_AREA | 2300 | 155.39 | 0 |
| NON_ASSIGNABLE_AREA | 0 | 2705.41 | 347.22 |
| FLOOR_SORT_SEQUENCE | 1 | 1 | 5 |
| LEVEL_ID | 1 | 1 | 5 |
| BUILDING_WINGS_ID | null | null | null |
| ACCESS_LEVEL | 0 | 2 | 2 |
| WAREHOUSE_LOAD_DATE | 01-AUG-15 | 01-FEB-15 | 01-SEP-15 |

# `fclt_major_use`  (rows=14)

columns:
`FCLT_MAJOR_USE_KEY` varchar127: "101"=1, "102"=1, "103"=1, "104"=1, "105"=1, "106"=1, "107"=1, "108"=1, "109"=1, "110"=1, "111"=1, "112"=1, "113"=1, "114"=1
`MAJOR_USE` varchar127: "BLDG SRV"=1, "CIRCULAT"=1, "CLASSRMS"=1, "GENERAL"=1, "HEALTH"=1, "LABS"=1, "MECHANIC"=1, "OFFICES"=1, "RESIDENT"=1, "SPECIAL"=1, "STUDY"=1, "SUPPORT"=1, "UNCLASS"=1, "ZUSE"=1
`DESCRIPTION` varchar127: "BLDG SERVICE AREA"=1, "CIRCULATION AREA"=1, "CLASSROOMS"=1, "GENERAL USE"=1, "HEALTH CARE"=1, "LABORATORIES"=1, "MECHANICAL AREA"=1, "OFFICES"=1, "RESIDENTIAL"=1, "SPECIAL USE"=1, "STUDY"=1, "SUPPORT"=1, "UNCLASSIFIED"=1, "ZUSE ICR ONLY"=1
`ASSIGNABLE` varchar127: "1"=11, "0"=3
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=14

indexes: `FCLT_MAJOR_USE_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_MAJOR_USE_KEY | 114 | 104 | 105 |
| MAJOR_USE | ZUSE | GENERAL | HEALTH |
| DESCRIPTION | ZUSE ICR ONLY | GENERAL USE | HEALTH CARE |
| ASSIGNABLE | 1 | 1 | 1 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `fclt_major_use_hist`  (rows=1680)

columns:
`FCLT_MAJOR_USE_HIST_KEY` varchar127: 1666 distinct
`FISCAL_PERIOD` varchar127: digits, 119 distinct
`FCLT_MAJOR_USE_KEY` varchar127: "101"=120, "102"=120, "103"=120, "104"=120, "105"=120, "106"=120, "107"=120, "108"=120, "109"=120, "110"=120, "111"=120, "112"=120, "113"=120, "114"=120
`MAJOR_USE` varchar127: "BLDG SRV"=120, "CIRCULAT"=120, "CLASSRMS"=120, "GENERAL"=120, "HEALTH"=120, "LABS"=120, "MECHANIC"=120, "OFFICES"=120, "RESIDENT"=120, "SPECIAL"=120, "STUDY"=120, "SUPPORT"=120, "UNCLASS"=120, "ZUSE"=120
`DESCRIPTION` varchar127: "BLDG SERVICE AREA"=120, "CIRCULATION AREA"=120, "CLASSROOMS"=120, "GENERAL USE"=120, "HEALTH CARE"=120, "LABORATORIES"=120, "MECHANICAL AREA"=120, "OFFICES"=120, "RESIDENTIAL"=120, "SPECIAL USE"=120, "STUDY"=120, "SUPPORT"=120, "UNCLASSIFIED"=120, "ZUSE ICR ONLY"=120
`ASSIGNABLE` varchar127: "1"=1320, "0"=360
`WAREHOUSE_LOAD_DATE` varchar255: 120 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_MAJOR_USE_HIST_KEY | 114-202505 | 110-202110 | 113-202206 |
| FISCAL_PERIOD | 202505 | 202110 | 202206 |
| FCLT_MAJOR_USE_KEY | 114 | 110 | 113 |
| MAJOR_USE | ZUSE | SPECIAL | UNCLASS |
| DESCRIPTION | ZUSE ICR ONLY | SPECIAL USE | UNCLASSIFIED |
| ASSIGNABLE | 1 | 1 | 1 |
| WAREHOUSE_LOAD_DATE | 01-DEC-24 | 01-MAY-21 | 01-JAN-22 |

# `fclt_org_dlc_key`  (rows=168)

columns:
`FCLT_ORGANIZATION_KEY` varchar127: digits, all distinct
`DLC_KEY` varchar127: 136 distinct, nulls=8, "D_RESDEV"=4, "D_IS&T"=3, "D_MECHE"=3, "D_PROVOST"=3, "D_ROTC"=3, "D_UNDEF"=3, "D_CMS"=2, "D_DHSS"=2, "D_DINING"=2, "D_DMSE"=2

indexes: `DLC_KEY`, `FCLT_ORGANIZATION_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_ORGANIZATION_KEY | 288 | 192 | 220 |
| DLC_KEY | null | D_LVA | D_PEP |

# `fclt_organization`  (rows=180)

columns:
`FCLT_ORGANIZATION_KEY` varchar127: digits, 168 distinct, "150"=10, "235"=3, "229"=2, "101"=1, "102"=1, "103"=1, "104"=1, "105"=1, "106"=1, "107"=1
`ORGANIZATION_ID` varchar127: digits, 168 distinct
`ORGANIZATION` varchar127: 168 distinct
`ORGANIZATION_NAME` varchar127: 168 distinct
`FCLT_ORG_PARENT_KEY` varchar127: digits, 32 distinct, nulls=2
`ORG_PARENT` varchar127: 32 distinct, nulls=2
`FCLT_MAJOR_ORG_KEY` varchar127: "230"=89, "129"=38, "163"=35, "271"=6, "216"=3, "267"=3, "105"=1, "125"=1, "210"=1, "217"=1, "224"=1, "275"=1
`MAJOR_ORG` varchar127: "PROVST"=89, "CHNCLR"=38, "EXECVP"=35, "ZORG"=6, "OTHMIT"=3, "VP-SCP"=3, "ALL"=1, "CHAIRM"=1, "OFPRES"=1, "OTHNON"=1, "PRES"=1, "XXXXX"=1
`ORGANIZATION_LEVEL` varchar127: "5"=107, "4"=50, "6"=13, "3"=7, "1"=2, "2"=1
`ORGANIZATION_NUMBER` varchar127: digits, 150 distinct, nulls=9
`ORGANIZATION_SORT` varchar127: digits, 163 distinct, nulls=1
`ASSIGNABLE` varchar127: "1"=175, "0"=5
`COURSE` varchar127: 31 distinct, nulls=148
`DESCRIPTION` varchar127: 64 distinct, nulls=114
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=180
`DLC_KEY` varchar127: 136 distinct, nulls=8, "D_FACILITIES"=11, "D_PROVOST"=4, "D_RESDEV"=4, "D_DOF_RESIDENCE"=3, "D_IS&T"=3, "D_MECHE"=3, "D_ROTC"=3, "D_UNDEF"=3, "D_CMS"=2, "D_DHSS"=2
`DLC_NAME` varchar127: 136 distinct, nulls=8
`HR_DEPARTMENT_CODE_OLD` varchar127: digits, 147 distinct, nulls=12, "591040"=10, "591030"=3, "153000"=2, "401800"=2, "402200"=2, "409000"=2, "410000"=2, "449000"=2, "495000"=2, "591024"=2
`HR_ORG_UNIT_ID` varchar127: digits, 159 distinct, nulls=12
`HR_DEPARTMENT_NAME` varchar127: 159 distinct, nulls=12

indexes: `DLC_KEY`, `FCLT_ORGANIZATION_KEY`, `HR_DEPARTMENT_CODE_OLD`, `HR_ORG_UNIT_ID`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_ORGANIZATION_KEY | 288 | 181 | 147 |
| ORGANIZATION_ID | 288 | 181 | 147 |
| ORGANIZATION | HEALTH | KAVLI | DINING |
| ORGANIZATION_NAME | MIT HEALTH | K I FOR AST&SP R | CAMPUS DINING |
| FCLT_ORG_PARENT_KEY | 163 | 246 | 151 |
| ORG_PARENT | EXECVP | S SCI | DSL |
| FCLT_MAJOR_ORG_KEY | 163 | 230 | 129 |
| MAJOR_ORG | EXECVP | PROVST | CHNCLR |
| ORGANIZATION_LEVEL | 4 | 5 | 5 |
| ORGANIZATION_NUMBER | 495000 | 159600 | 801000 |
| ORGANIZATION_SORT | 101030640 | 101060187 | 101030304 |
| ASSIGNABLE | 1 | 1 | 1 |
| COURSE | null | null | null |
| DESCRIPTION | null | Kavli Institute for Astrophysics & Space Research | null |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| DLC_KEY | null | D_CSR | D_DINING |
| DLC_NAME | null | Kavli Institute for Astrophysics & Space Research | Campus Dining |
| HR_DEPARTMENT_CODE_OLD | 495000 | 159600 | 801000 |
| HR_ORG_UNIT_ID | 10000792 | 10000544 | 10000889 |
| HR_DEPARTMENT_NAME | MIT Health | Kavli Inst for Astrophysics & Space Rsrh | Dining |

# `fclt_organization_hist`  (rows=10000)

columns:
`FCLT_ORGANIZATION_HIST_KEY` varchar127: 9620 distinct
`FISCAL_PERIOD` varchar127: digits, 64 distinct
`FCLT_ORGANIZATION_KEY` varchar127: digits, 169 distinct
`ORGANIZATION_ID` varchar127: digits, 169 distinct
`ORGANIZATION` varchar127: 172 distinct
`ORGANIZATION_NAME` varchar127: 173 distinct
`FCLT_ORG_PARENT_KEY` varchar127: digits, 40 distinct, nulls=68
`ORG_PARENT` varchar127: 38 distinct, nulls=93
`FCLT_MAJOR_ORG_KEY` varchar127: 24 distinct
`MAJOR_ORG` varchar127: 167 distinct, nulls=194
`ORGANIZATION_LEVEL` varchar127: "5"=6206, "4"=2379, "6"=858, "3"=407, "1"=93, "2"=57
`ORGANIZATION_NUMBER` varchar127: digits, 165 distinct, nulls=507
`ORGANIZATION_SORT` varchar127: digits, 177 distinct, nulls=33
`ASSIGNABLE` varchar127: "1"=9747, "0"=253
`COURSE` varchar127: 32 distinct, nulls=8094
`DESCRIPTION` varchar127: "Institute For Medical Engineering & Science"=61, "Leaders for Global Operations-Systems Design Management"=60, "Office Of Corporate Relations"=56, "MIT Institute for Data, Systems, and Society"=36, "MIT Socio-technical Systems Research Center"=20, nulls=9767
`WAREHOUSE_LOAD_DATE` varchar255: 64 distinct
`DLC_KEY` varchar127: 142 distinct, nulls=152
`DLC_NAME` varchar127: 146 distinct, nulls=152
`HR_DEPARTMENT_CODE_OLD` varchar127: digits, 149 distinct, nulls=764
`HR_ORG_UNIT_ID` varchar127: digits, 160 distinct, nulls=764
`HR_DEPARTMENT_NAME` varchar127: 187 distinct, nulls=764

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_ORGANIZATION_HIST_KEY | 277-201912 | 207-201707 | 116-201506 |
| FISCAL_PERIOD | 201912 | 201707 | 201506 |
| FCLT_ORGANIZATION_KEY | 277 | 207 | 116 |
| ORGANIZATION_ID | 277 | 207 | 116 |
| ORGANIZATION | MRL | NRL | BEDEP |
| ORGANIZATION_NAME | MATERIALS RESEARCH LAB | NUCL REACTOR LAB | BIOENG DEPT |
| FCLT_ORG_PARENT_KEY | 266 | 230 | 243 |
| ORG_PARENT | VP-RES | VP-RES | S ENG |
| FCLT_MAJOR_ORG_KEY | 230 | PROVST | 230 |
| MAJOR_ORG | PROVST | 264000 | PROVST |
| ORGANIZATION_LEVEL | 5 | 5 | 5 |
| ORGANIZATION_NUMBER | 417500 | 264000 | 69200 |
| ORGANIZATION_SORT | 101060224 | 101060226 | 101060060 |
| ASSIGNABLE | 1 | 1 | 1 |
| COURSE | null | null | BE |
| DESCRIPTION | null | null | null |
| WAREHOUSE_LOAD_DATE | 01-JUL-19 | 01-FEB-17 | 01-JAN-15 |
| DLC_KEY | D_MRL | D_NRL | D_BIOENG |
| DLC_NAME | Materials Research Laboratory | Nuclear Reactor Laboratory | Biological Engineering |
| HR_DEPARTMENT_CODE_OLD | 417500 | 264000 | 69200 |
| HR_ORG_UNIT_ID | 10005459 | 10000575 | 10000347 |
| HR_DEPARTMENT_NAME | Materials Research Laboratory | Nuclear Reactor Laboratory | Department of Biological Engineering |

# `fclt_rooms`  (rows=10000)

columns:
`FCLT_ROOM_KEY` varchar127: 9872 distinct, "E62-420"=3, "W1-209"=3, "1-353G"=2, "10-297B"=2, "13-314"=2, "13-553"=2, "14S-283"=2, "16-121"=2, "18-229"=2, "2-187"=2
`BUILDING_ROOM` varchar127: 9872 distinct, "E62-420"=3, "W1-209"=3, "1-353G"=2, "10-297B"=2, "13-314"=2, "13-553"=2, "14S-283"=2, "16-121"=2, "18-229"=2, "2-187"=2
`FCLT_BUILDING_KEY` varchar127: 202 distinct, "46"=341, "32"=313, "E37"=271, "76"=222, "68"=197, "W79"=173, "E19"=172, "NE49"=165, "54"=162, "NW86"=155
`FLOOR` varchar127: 48 distinct
`FCLT_FLOOR_KEY` varchar127: 925 distinct, "46-7"=61, "46-4"=58, "46-6"=55, "46-5"=54, "E40-1"=51, "NE49-2"=49, "NE49-4"=49, "32-3"=41, "E90-9"=41, "32-0"=40
`ROOM` varchar127: 3610 distinct
`SPACE_ID` varchar127: 9872 distinct
`FCLT_MAJOR_USE_KEY` varchar127: "108"=3140, "102"=1524, "109"=1355, "107"=1313, "106"=1230, "101"=529, "104"=283, "112"=165, "110"=131, "103"=120, "111"=82, "113"=79, "105"=49
`MAJOR_USE_DESC` varchar127: "OFFICES"=3140, "CIRCULAT"=1524, "RESIDENT"=1355, "MECHANIC"=1313, "LABS"=1230, "BLDG SRV"=529, "GENERAL"=283, "SUPPORT"=165, "SPECIAL"=131, "CLASSRMS"=120, "STUDY"=82, "UNCLASS"=79, "HEALTH"=49
`FCLT_USE_KEY` varchar127: digits, 85 distinct
`USE_DESC` varchar127: all NULL
`FCLT_MINOR_USE_KEY` varchar127: all NULL
`MINOR_USE_DESC` varchar127: all NULL
`FCLT_ORGANIZATION_KEY` varchar127: digits, 126 distinct, "149"=2429, "236"=1497, "235"=937, "245"=317, "150"=188, "199"=166, "145"=157, "126"=144, "182"=132, "229"=129
`ORGANIZATION_NAME` varchar127: 126 distinct
`FCLT_MINOR_ORGANIZATION_KEY` varchar127: all NULL
`MINOR_ORGANIZATION` varchar127: all NULL
`AREA` float: 7926 distinct, 0..108475, avg=312.678, median=139.95
`ROOM_FULL_NAME` varchar127: "WOMENS LOCKER"=2, "CHAN CONFERENCE ROOM, T.H."=1, "CHU ROOM, LAN JEN"=1, "COMPTON LOUNGE"=1, "DE ROTHSCHILD ROOM"=1, "ENGINEERING CONFERENCE ROOM"=1, "EXPERIMENTAL MEDIA FACILITY, PHILIPPE VILLERS (THE CUBE)"=1, "GIVEN ROOM"=1, "HUNTINGTON HALL"=1, "KRESGE LOBBY"=1, "MENS  LOCKER"=1, "MENS TEAM ROOM"=1, "NORTH LOBDELL BALCONY"=1, "SMALL DINING ROOM"=1, "STRATTON BALCONY"=1, "WOMENS TEAM ROOM"=1, nulls=9983
`DEPT_CODE` varchar127: "93700"=17, "93300"=9, "93400"=4, "93600"=4, "93800"=1, nulls=9965
`ACCESS_LEVEL` varchar127: "2"=5455, "1"=1741, "3"=1566, "0"=1238
`LATITUDE_WGS` float: all NULL
`LONGITUDE_WGS` float: all NULL
`NORTHING_SPCS` float: all NULL
`EASTING_SPCS` float: all NULL
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: `BUILDING_ROOM`, `FCLT_BUILDING_KEY`, `FCLT_FLOOR_KEY`, `FCLT_MAJOR_USE_KEY`, `FCLT_ORGANIZATION_KEY`, `FCLT_ROOM_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_ROOM_KEY | WW15-196A | W98-117B | NW16-075A |
| BUILDING_ROOM | WW15-196A | W98-117B | NW16-075A |
| FCLT_BUILDING_KEY | WW15 | W98 | NW16 |
| FLOOR | 1 | 1 | 0 |
| FCLT_FLOOR_KEY | WW15-1 | W98-1 | NW16-0 |
| ROOM | 196A | 117B | 075A |
| SPACE_ID | WW15-1-196A | W98-1-117B | NW16-0-075A |
| FCLT_MAJOR_USE_KEY | 112 | 108 | 106 |
| MAJOR_USE_DESC | SUPPORT | OFFICES | LABS |
| FCLT_USE_KEY | 190 | 158 | 145 |
| USE_DESC | null | null | null |
| FCLT_MINOR_USE_KEY | null | null | null |
| MINOR_USE_DESC | null | null | null |
| FCLT_ORGANIZATION_KEY | 228 | 106 | 231 |
| ORGANIZATION_NAME | PROPTY | ALUMNI | PSFC |
| FCLT_MINOR_ORGANIZATION_KEY | null | null | null |
| MINOR_ORGANIZATION | null | null | null |
| AREA | 180 | 123.4 | 288.12 |
| ROOM_FULL_NAME | null | null | null |
| DEPT_CODE | null | null | null |
| ACCESS_LEVEL | 2 | 2 | 2 |
| LATITUDE_WGS | null | null | null |
| LONGITUDE_WGS | null | null | null |
| NORTHING_SPCS | null | null | null |
| EASTING_SPCS | null | null | null |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `fclt_rooms_hist`  (rows=10000)

columns:
`FCLT_ROOM_HIST_KEY` varchar127: 9327 distinct
`FISCAL_PERIOD` varchar127: "201505"=10000
`FCLT_ROOM_KEY` varchar127: 9327 distinct
`BUILDING_ROOM` varchar127: 9327 distinct
`FCLT_BUILDING_KEY` varchar127: digits, 35 distinct
`FLOOR` varchar127: digits, 26 distinct
`FCLT_FLOOR_KEY` varchar127: 202 distinct
`ROOM` varchar127: 3538 distinct
`SPACE_ID` varchar127: 9327 distinct
`FCLT_MAJOR_USE_KEY` varchar127: "108"=4214, "106"=1691, "107"=1452, "102"=1364, "101"=407, "103"=280, "113"=204, "112"=166, "111"=122, "104"=94, "110"=6
`MAJOR_USE_DESC` varchar127: "OFFICES"=4214, "LABS"=1691, "MECHANIC"=1452, "CIRCULAT"=1364, "BLDG SRV"=407, "CLASSRMS"=280, "UNCLASS"=204, "SUPPORT"=166, "STUDY"=122, "GENERAL"=94, "SPECIAL"=6
`FCLT_USE_KEY` varchar127: digits, 58 distinct
`USE_DESC` varchar127: all NULL
`FCLT_MINOR_USE_KEY` varchar127: all NULL
`MINOR_USE_DESC` varchar127: all NULL
`FCLT_ORGANIZATION_KEY` varchar127: digits, 72 distinct
`ORGANIZATION_NAME` varchar127: 72 distinct
`FCLT_MINOR_ORGANIZATION_KEY` varchar127: all NULL
`MINOR_ORGANIZATION` varchar127: all NULL
`AREA` float: 7760 distinct, 0.11..108885, avg=287.891, median=149.88
`ROOM_FULL_NAME` varchar127: all distinct, nulls=9969
`DEPT_CODE` varchar127: "93700"=75, "93300"=58, "93800"=25, "93600"=21, nulls=9821
`ACCESS_LEVEL` varchar127: "2"=6611, "3"=1613, "0"=1416, "1"=360
`LATITUDE_WGS` float: all NULL
`LONGITUDE_WGS` float: all NULL
`NORTHING_SPCS` float: all NULL
`EASTING_SPCS` float: all NULL
`WAREHOUSE_LOAD_DATE` varchar255: "01-DEC-14"=10000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_ROOM_HIST_KEY | 9-667-201505 | 10-806D-201505 | 13-303-201505 |
| FISCAL_PERIOD | 201505 | 201505 | 201505 |
| FCLT_ROOM_KEY | 9-667 | 10-806D | 13-303 |
| BUILDING_ROOM | 9-667 | 10-806D | 13-303 |
| FCLT_BUILDING_KEY | 9 | 10 | 13 |
| FLOOR | 6 | 8 | 3 |
| FCLT_FLOOR_KEY | 9-6 | 10-8 | 13-3 |
| ROOM | 667 | 806D | 303 |
| SPACE_ID | 9-6-667 | 10-8-806D | 13-3-303 |
| FCLT_MAJOR_USE_KEY | 108 | 111 | 106 |
| MAJOR_USE_DESC | OFFICES | STUDY | LABS |
| FCLT_USE_KEY | 162 | 181 | 148 |
| USE_DESC | null | null | null |
| FCLT_MINOR_USE_KEY | null | null | null |
| MINOR_USE_DESC | null | null | null |
| FCLT_ORGANIZATION_KEY | 262 | 189 | 136 |
| ORGANIZATION_NAME | US&P | LIBRAR | CMSE |
| FCLT_MINOR_ORGANIZATION_KEY | null | null | null |
| MINOR_ORGANIZATION | null | null | null |
| AREA | 64.89 | 790.99 | 417.79 |
| ROOM_FULL_NAME | null | null | null |
| DEPT_CODE | null | null | null |
| ACCESS_LEVEL | 2 | 2 | 2 |
| LATITUDE_WGS | null | null | null |
| LONGITUDE_WGS | null | null | null |
| NORTHING_SPCS | null | null | null |
| EASTING_SPCS | null | null | null |
| WAREHOUSE_LOAD_DATE | 01-DEC-14 | 01-DEC-14 | 01-DEC-14 |

# `frc_fiscal_periods`  (rows=10)

columns:
`TIME_MONTH_KEY` varchar127
`CALENDAR_PERIOD_DESCRIPTION` varchar127
`FISCAL_PERIOD` varchar127

indexes: none

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 | row 7 | row 8 | row 9 | row 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| TIME_MONTH_KEY | 202412 | 202413 | 202414 | 202415 | 202416 | 202501 | 202502 | 202503 | 202504 | 202505 |
| CALENDAR_PERIOD_DESCRIPTION | June 2024 | June 2024, fiscal period 13 | June 2024, fiscal period 14 | June 2024, fiscal period 15 | June 2024, fiscal period 16 | July 2024 | August 2024 | September 2024 | October 2024 | November 2024 |
| FISCAL_PERIOD | 202412 | 202413 | 202414 | 202415 | 202416 | 202501 | 202502 | 202503 | 202504 | 202505 |

# `hr_faculty_roster`  (rows=681)

columns:
`MIT_ID` varchar127: digits, 653 distinct
`LAST_NAME` varchar127: 283 distinct
`FIRST_NAME` varchar127: 308 distinct
`MIDDLE_NAME` varchar127: 142 distinct, nulls=321
`TERMINAL_DEGREE` varchar127: "Doctoral Degree"=612, "Post-Doctoral Degree"=13, "Master's Degree"=8, "Employ Discipline Tr"=4, "Bachelor's Degree"=1, "Professional Degree"=1, nulls=42
`APPOINTMENT_TYPE` varchar127: "Primary Appointment"=676, "Dual Appointment"=5
`JOB_TITLE` varchar127: "Professor"=508, "Assistant Professor"=98, "Associate Professor (wot)"=43, "Associate Professor"=27, "Professor Emeritus"=2, "Professor of the Practice"=1, "Senior Research Scientist"=1, "Visiting Professor"=1
`HR_ORG_UNIT_TITLE` varchar127: 30 distinct, "Sloan School of Management"=103, "Electrical Engineering-Computer Science"=90, "Mechanical Engineering"=44, "Biology"=39, "Economics"=31, "Aeronautics and Astronautics"=30, "Chemical Engineering"=30, "Materials Science and Engineering"=26, "Chemistry"=24, "Brain & Cognitive Sciences"=23
`POSITION_TITLE` varchar127: all NULL
`ADMIN_ORG_UNIT_TITLE` varchar127: all NULL
`ADMIN_POSITION_TITLE` varchar127: all NULL
`ADMIN_JOB_TITLE` varchar127: all NULL
`DIRECTORY_ORG_UNIT_TITLE` varchar127: 34 distinct, nulls=614
`ENDOWED_CHAIR` varchar127: all NULL
`EMERITUS_STATUS` varchar31: "Emeritus"=2, nulls=679
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=681

indexes: `HR_ORG_UNIT_TITLE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MIT_ID | 999779388 | 979334532 | 901541134 |
| LAST_NAME | Bates | Mcclure | Spence |
| FIRST_NAME | Antonia | Lexi | Martha |
| MIDDLE_NAME | W | null | null |
| TERMINAL_DEGREE | Doctoral Degree | Doctoral Degree | Doctoral Degree |
| APPOINTMENT_TYPE | Primary Appointment | Primary Appointment | Primary Appointment |
| JOB_TITLE | Professor | Professor | Professor |
| HR_ORG_UNIT_TITLE | Mechanical Engineering | Political Science | Mechanical Engineering |
| POSITION_TITLE | null | null | null |
| ADMIN_ORG_UNIT_TITLE | null | null | null |
| ADMIN_POSITION_TITLE | null | null | null |
| ADMIN_JOB_TITLE | null | null | null |
| DIRECTORY_ORG_UNIT_TITLE | null | null | null |
| ENDOWED_CHAIR | null | null | null |
| EMERITUS_STATUS | null | null | null |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `hr_org_unit`  (rows=641)

columns:
`HR_ORG_UNIT_KEY` varchar127: all distinct
`HR_ORG_UNIT_ID` varchar127: digits, unique identifier
`HR_ORG_UNIT_TITLE` varchar127: 637 distinct, nulls=1
`HR_ORG_UNIT_LEVEL` varchar127: "DEPARTMENTS"=494, "ORGANIZATION LEVEL"=108, "SUB DEPARTMENT"=17, "NON HIERARCHY ORG UNITS"=4, "TOP LEVEL"=3, "ALL MIT"=1, nulls=14
`HR_DEPARTMENT_ID` varchar127: digits, 492 distinct, nulls=130
`HR_DEPARTMENT_CODE` varchar127: 492 distinct, nulls=130
`HR_DEPARTMENT_CODE_OLD` varchar127: digits, 472 distinct, nulls=130, "310000"=20, "591040"=10, "591022"=4, "591302"=4, "591030"=3, "441310"=2, "591024"=2, "591028"=2, "10000"=1, "121000"=1
`HR_DEPARTMENT_NAME` varchar127: 491 distinct, nulls=130
`HR_DEPARTMENT_NAME_LONG` varchar127: 483 distinct, nulls=130
`HR_DEPARTMENT_NAME_ALPHA` varchar127: 471 distinct, nulls=149
`ORG_HIER_SCHOOL_AREA_NAME` varchar127: 28 distinct, nulls=24
`ORG_HIER_TOP_LEVEL_NAME` varchar127: "Provost Area"=464, "Executive Vice President Area"=142, "President & Chair of the Corporation"=12, "Other Org Units"=2, nulls=21
`ORG_HIER_ROOT_NAME` varchar127: "MIT-All"=640, nulls=1
`HR_ORG_LEVEL1_ID` varchar127: "10000000"=627, nulls=14
`HR_ORG_LEVEL1_SORT` varchar127: "1"=627, nulls=14
`HR_ORG_LEVEL1_NAME` varchar127: "MIT-All"=640, nulls=1
`HR_ORG_LEVEL2_ID` varchar127: "10000001"=464, "10000002"=142, "10000003"=12, "19999000"=8, nulls=15
`HR_ORG_LEVEL2_SORT` varchar127: "2"=464, "3"=142, "4"=12, "623"=8, nulls=15
`HR_ORG_LEVEL2_NAME` varchar127: "Provost Area"=464, "Executive Vice President Area"=142, "President & Chair of the Corporation"=12, "Other Org Units"=8, nulls=15
`HR_ORG_LEVEL3_ID` varchar127: digits, 52 distinct, nulls=19
`HR_ORG_LEVEL3_SORT` varchar127: digits, 52 distinct, nulls=19
`HR_ORG_LEVEL3_NAME` varchar127: 52 distinct, nulls=19
`HR_ORG_LEVEL4_ID` varchar127: digits, 248 distinct, nulls=71
`HR_ORG_LEVEL4_SORT` varchar127: digits, 248 distinct, nulls=71
`HR_ORG_LEVEL4_NAME` varchar127: 248 distinct, nulls=71
`HR_ORG_LEVEL5_ID` varchar127: digits, 221 distinct, nulls=319
`HR_ORG_LEVEL5_SORT` varchar127: digits, 221 distinct, nulls=319
`HR_ORG_LEVEL5_NAME` varchar127: 221 distinct, nulls=319
`HR_ORG_LEVEL6_ID` varchar127: digits, 63 distinct, nulls=540
`HR_ORG_LEVEL6_SORT` varchar127: digits, 63 distinct, nulls=540
`HR_ORG_LEVEL6_NAME` varchar127: 63 distinct, nulls=540
`HR_ORG_LEVEL7_ID` varchar127: digits, all distinct, nulls=603
`HR_ORG_LEVEL7_SORT` varchar127: digits, all distinct, nulls=603
`HR_ORG_LEVEL7_NAME` varchar127: all distinct, nulls=603
`DLC_KEY` varchar127: 231 distinct, nulls=133, "D_SLOAN"=48, "D_FACILITIES"=34, "D_DL"=28, "D_LINCOLN"=20, "D_RESDEV"=18, "D_CAS"=15, "D_ALUM"=10, "D_DSL:HQ"=10, "D_VPRESOFF"=9, "D_ATHLETICS"=6
`DLC_NAME` varchar127: 231 distinct, nulls=133
`WAREHOUSE_LOAD_DATE` varchar255: "03-DEC-24"=640, "13-DEC-24"=1

indexes: `DLC_KEY`, `HR_DEPARTMENT_CODE_OLD`, `HR_ORG_UNIT_ID`, `HR_ORG_UNIT_TITLE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| HR_ORG_UNIT_KEY | O19999999 | O10000357 | O10000670 |
| HR_ORG_UNIT_ID | 19999999 | 10000357 | 10000670 |
| HR_ORG_UNIT_TITLE | HR-Affiliates | School of Humanities, Arts, & Social Sci | Office of Leadership Giving |
| HR_ORG_UNIT_LEVEL | NON HIERARCHY ORG UNITS | DEPARTMENTS | DEPARTMENTS |
| HR_DEPARTMENT_ID | null | 10000357 | 10000670 |
| HR_DEPARTMENT_CODE | null | HR-090000 | HR-410095 |
| HR_DEPARTMENT_CODE_OLD | null | 90000 | 410095 |
| HR_DEPARTMENT_NAME | null | School of Humanities, Arts, & Social Sci | Office of Leadership Giving |
| HR_DEPARTMENT_NAME_LONG | null | School of Humanities, Arts, and Social Sciences | Office of Leadership Giving |
| HR_DEPARTMENT_NAME_ALPHA | null | School of Humanities, Arts, and Social Sciences | Office of Leadership Giving |
| ORG_HIER_SCHOOL_AREA_NAME | null | Humanities, Arts, & Social Sciences Area | VP for Resource Development |
| ORG_HIER_TOP_LEVEL_NAME | null | Provost Area | Executive Vice President Area |
| ORG_HIER_ROOT_NAME | MIT-All | MIT-All | MIT-All |
| HR_ORG_LEVEL1_ID | null | 10000000 | 10000000 |
| HR_ORG_LEVEL1_SORT | null | 1 | 1 |
| HR_ORG_LEVEL1_NAME | MIT-All | MIT-All | MIT-All |
| HR_ORG_LEVEL2_ID | null | 10000001 | 10000002 |
| HR_ORG_LEVEL2_SORT | null | 2 | 3 |
| HR_ORG_LEVEL2_NAME | null | Provost Area | Executive Vice President Area |
| HR_ORG_LEVEL3_ID | null | 10000020 | 10000035 |
| HR_ORG_LEVEL3_SORT | null | 12 | 20 |
| HR_ORG_LEVEL3_NAME | null | Humanities, Arts, & Social Sciences Area | VP for Resource Development |
| HR_ORG_LEVEL4_ID | null | 10004383 | 10000187 |
| HR_ORG_LEVEL4_SORT | null | 380 | 27 |
| HR_ORG_LEVEL4_NAME | null | SHASS area | Office VP Resource Development |
| HR_ORG_LEVEL5_ID | null | 10000357 | 10000670 |
| HR_ORG_LEVEL5_SORT | null | 73 | 167 |
| HR_ORG_LEVEL5_NAME | null | School of Humanities, Arts, & Social Sci | Office of Leadership Giving |
| HR_ORG_LEVEL6_ID | null | null | null |
| HR_ORG_LEVEL6_SORT | null | null | null |
| HR_ORG_LEVEL6_NAME | null | null | null |
| HR_ORG_LEVEL7_ID | null | null | null |
| HR_ORG_LEVEL7_SORT | null | null | null |
| HR_ORG_LEVEL7_NAME | null | null | null |
| DLC_KEY | null | D_DHSS | D_RESDEV |
| DLC_NAME | null | Dean of Humanities & Social Sciences | Vice President for Resource Development |
| WAREHOUSE_LOAD_DATE | 03-DEC-24 | 03-DEC-24 | 03-DEC-24 |

# `hr_org_unit_new`  (rows=691)

columns:
`HR_ORG_UNIT_KEY` varchar127: all distinct
`HR_ORG_UNIT_ID` varchar127: digits, unique identifier
`HR_ORG_UNIT_TITLE` varchar127: 669 distinct, nulls=1
`HR_ORG_UNIT_LEVEL` varchar127: "DEPARTMENTS"=544, "ORGANIZATION LEVEL"=108, "SUB DEPARTMENT"=17, "NON HIERARCHY ORG UNITS"=4, "TOP LEVEL"=3, "ALL MIT"=1, nulls=14
`HR_DEPARTMENT_CODE` varchar127: digits, 542 distinct, nulls=130
`HR_DEPARTMENT_ABBR` varchar127: 538 distinct, nulls=130
`HR_DEPARTMENT_CODE_OLD` varchar127: digits, 518 distinct, nulls=130
`HR_DEPARTMENT_NAME` varchar127: 523 distinct, nulls=130
`HR_DEPARTMENT_NAME_LONG` varchar127: 515 distinct, nulls=130
`HR_DEPARTMENT_NAME_ALPHA` varchar127: 503 distinct, nulls=149
`ORG_HIER_SCHOOL_AREA_NAME` varchar127: 32 distinct, nulls=24
`ORG_HIER_TOP_LEVEL_NAME` varchar127: "Provost Area"=470, "Executive Vice President Area"=145, "President & Chair of the Corporation"=13, "Engineering Area"=10, "Science Area"=7, "Office VP Resource Development"=6, "VP Research"=6, "Humanities, Arts, & Social Sciences Area"=4, "Other Org Units"=2, "Sloan School of Management Area"=2, "Architecture & Planning Area"=1, "Department of Facilities"=1, "Information Systems Area"=1, "Office of Provost Area"=1, "Office of Undergraduate Education Area"=1, nulls=21
`ORG_HIER_ROOT_NAME` varchar127: "MIT-All"=690, nulls=1
`HR_ORG_LEVEL1_ID` varchar127: "10000000"=627, nulls=64
`HR_ORG_LEVEL1_SORT` varchar127: "1"=627, nulls=64
`HR_ORG_LEVEL1_NAME` varchar127: "MIT-All"=690, nulls=1
`HR_ORG_LEVEL2_ID` varchar127: "10000001"=464, "10000002"=142, "10000003"=12, "19999000"=8, nulls=65
`HR_ORG_LEVEL2_SORT` varchar127: "2"=464, "3"=142, "4"=12, "623"=8, nulls=65
`HR_ORG_LEVEL2_NAME` varchar127: "Provost Area"=464, "Executive Vice President Area"=142, "President & Chair of the Corporation"=12, "Other Org Units"=8, nulls=65
`HR_ORG_LEVEL3_ID` varchar127: digits, 52 distinct, nulls=69
`HR_ORG_LEVEL3_SORT` varchar127: digits, 52 distinct, nulls=69
`HR_ORG_LEVEL3_NAME` varchar127: 52 distinct, nulls=69
`HR_ORG_LEVEL4_ID` varchar127: digits, 248 distinct, nulls=121
`HR_ORG_LEVEL4_SORT` varchar127: digits, 248 distinct, nulls=121
`HR_ORG_LEVEL4_NAME` varchar127: 248 distinct, nulls=121
`HR_ORG_LEVEL5_ID` varchar127: digits, 221 distinct, nulls=369
`HR_ORG_LEVEL5_SORT` varchar127: digits, 221 distinct, nulls=369
`HR_ORG_LEVEL5_NAME` varchar127: 221 distinct, nulls=369
`DLC_KEY` varchar127: 231 distinct, nulls=200
`WAREHOUSE_LOAD_DATE` varchar255: "03-DEC-24"=690, "13-DEC-24"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| HR_ORG_UNIT_KEY | O19999999 | O10000669 | O10005533 |
| HR_ORG_UNIT_ID | 19999999 | 10000669 | 10005533 |
| HR_ORG_UNIT_TITLE | HR-Affiliates | Strategic Program Development | Residential Education |
| HR_ORG_UNIT_LEVEL | NON HIERARCHY ORG UNITS | DEPARTMENTS | DEPARTMENTS |
| HR_DEPARTMENT_CODE | null | 10000669 | 10005533 |
| HR_DEPARTMENT_ABBR | null | HR-410090 | HR-0001910 |
| HR_DEPARTMENT_CODE_OLD | null | 410090 | 191 |
| HR_DEPARTMENT_NAME | null | Strategic Program Development | Residential Education |
| HR_DEPARTMENT_NAME_LONG | null | Strategic Program Development | Residential Education |
| HR_DEPARTMENT_NAME_ALPHA | null | Strategic Program Development | Residential Education |
| ORG_HIER_SCHOOL_AREA_NAME | null | VP for Resource Development | Dean for Student Life Area |
| ORG_HIER_TOP_LEVEL_NAME | null | Executive Vice President Area | Provost Area |
| ORG_HIER_ROOT_NAME | MIT-All | MIT-All | MIT-All |
| HR_ORG_LEVEL1_ID | null | 10000000 | 10000000 |
| HR_ORG_LEVEL1_SORT | null | 1 | 1 |
| HR_ORG_LEVEL1_NAME | MIT-All | MIT-All | MIT-All |
| HR_ORG_LEVEL2_ID | null | 10000002 | 10000001 |
| HR_ORG_LEVEL2_SORT | null | 3 | 2 |
| HR_ORG_LEVEL2_NAME | null | Executive Vice President Area | Provost Area |
| HR_ORG_LEVEL3_ID | null | 10000035 | 10000012 |
| HR_ORG_LEVEL3_SORT | null | 20 | 7 |
| HR_ORG_LEVEL3_NAME | null | VP for Resource Development | Dean for Student Life Area |
| HR_ORG_LEVEL4_ID | null | 10000187 | 10000223 |
| HR_ORG_LEVEL4_SORT | null | 27 | 31 |
| HR_ORG_LEVEL4_NAME | null | Office VP Resource Development | Residential Education Area |
| HR_ORG_LEVEL5_ID | null | 10000669 | 10005533 |
| HR_ORG_LEVEL5_SORT | null | 166 | 481 |
| HR_ORG_LEVEL5_NAME | null | Strategic Program Development | Residential Education |
| DLC_KEY | null | D_RESDEV | D_RE |
| WAREHOUSE_LOAD_DATE | 03-DEC-24 | 03-DEC-24 | 03-DEC-24 |

# `iap_subject_category`  (rows=49)

columns:
`IAP_SUBJECT_CATEGORY_KEY` varchar127: all distinct
`IAP_CATEGORY_NAME` varchar127: all distinct, nulls=1
`IAP_CATEGORY_DESC` varchar127: all distinct, nulls=12
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=49

indexes: `IAP_SUBJECT_CATEGORY_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IAP_SUBJECT_CATEGORY_KEY | B9953FF477EE12EFE0440003BAB016E8 | B9953FF477C912EFE0440003BAB016E8 | B9953FF477C812EFE0440003BAB016E8 |
| IAP_CATEGORY_NAME | Research Skills | Religion and Ethics | Music |
| IAP_CATEGORY_DESC | null | Exploring different religions, examining religion as it relates to science, political life, etc. | Lectures and concerts, music workshops, vocal classes, etc. |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `iap_subject_detail`  (rows=465)

columns:
`IAP_SUBJECT_CATEGORY_KEY` varchar127: 46 distinct, "B9953FF477C112EFE0440003BAB016E8"=25, "B9953FF477DB12EFE0440003BAB016E8"=24, "B9953FF477C812EFE0440003BAB016E8"=22, "B9953FF477E512EFE0440003BAB016E8"=22, "B9953FF477EE12EFE0440003BAB016E8"=21, "9289af8f517c291d0151921beca0022b"=20, "B9953FF477BC12EFE0440003BAB016E8"=20, "B9953FF477C412EFE0440003BAB016E8"=17, "9289af8f50a3a6fb0150a483f24c0000"=15, "9289af8f517c291d0151921c1c02022c"=15
`IAP_SUBJECT_SPONSOR_KEY` varchar127: 68 distinct, "9289af8f5fd92585015fe0471ab7007c"=24, "B979A5B907F3644BE0440003BAB016E8"=22, "B979A5B90873644BE0440003BAB016E8"=22, "B979A5B907F0644BE0440003BAB016E8"=21, "B979A5B90810644BE0440003BAB016E8"=21, "B979A5B907E6644BE0440003BAB016E8"=19, "9289af8f4909030401491a7599e30077"=15, "B979A5B907EC644BE0440003BAB016E8"=13, "9289af8d3ba8cc8d013bb3910ef00114"=12, "9289af8d4a29b055014a34ac4ebe00ed"=12
`IAP_SUBJECT_SESSION_KEY` varchar127: 142 distinct, "9289afec754ffaf2017662ccd63b0708"=9, "9289afec754ffaf2017662e4b2a8071c"=9, "9289afec754ffaf2017676cb1f340877"=9, "9289afec754ffaf2017676cf29f40889"=9, "9289afec754ffaf20176ced73f1a0bdb"=9, "9289afec76e200210176f233edc00167"=9, "9289afec76e20021017702b62c5a01e9"=9, "9289afec76e20021017726cba96702c6"=9, "9289afed754ffd470175795788070033"=9, "9289afed754ffd470175e610959301a2"=9
`IAP_SUBJECT_PERSON_KEY` varchar127: 142 distinct, "9289afec754ffaf2017662ccd63b0708"=9, "9289afec754ffaf2017662e4b2a8071c"=9, "9289afec754ffaf2017676cb1f340877"=9, "9289afec754ffaf2017676cf29f40889"=9, "9289afec754ffaf20176ced73f1a0bdb"=9, "9289afec76e200210176f233edc00167"=9, "9289afec76e20021017702b62c5a01e9"=9, "9289afec76e20021017726cba96702c6"=9, "9289afed754ffd470175795788070033"=9, "9289afed754ffd470175e610959301a2"=9
`ACTIVITY_TITLE` varchar127: 105 distinct
`ACTIVITY_DESCRIPTION` varchar127: 107 distinct
`TERM_CODE` varchar127: "2021JA"=465
`ENROLLMENT_TYPE` varchar127: "Advance sign-up required"=310, "No advance sign-up"=106, "Other"=42, "First come, first served (no advance sign-up)"=7
`MAX_ENROLLMENT` int: 30=46, 20=27, 200=24, 40=18, 60=15, 6=3, 12=3, 25=3, 8=2, nulls=324, 6..200
`ATTENDANCE` varchar127: "Participants welcome at individual sessions"=249, "Participants must attend all sessions"=134, "Other"=82
`PREREQUISITES` varchar127: 25 distinct, nulls=328
`FEE` int: 10=24, 25=3, 168=2, 36=1, nulls=435, 10..168
`FEE_REASON` varchar127: "Class Registration"=24, "kit and fabricated parts"=3, "employee, $105 stu/postdoc/spouse, $136.50 trad/retiree"=2, "one lesson, packages of lessons have a discount per lesson"=1, nulls=435
`PREREG_DEADLINE` varchar255: 26 distinct, nulls=230
`CREATE_DATE` varchar255: 55 distinct
`LAST_ACTIVITY_DATE` varchar255: 39 distinct
`IS_MULTIPLE_SESSION` varchar127: "Y"=426, "N"=39
`IS_CANCELLED` varchar127: "N"=463, "Y"=2
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=465

indexes: `IAP_SUBJECT_CATEGORY_KEY`, `IAP_SUBJECT_PERSON_KEY`, `IAP_SUBJECT_SESSION_KEY`, `IAP_SUBJECT_SPONSOR_KEY`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IAP_SUBJECT_CATEGORY_KEY | B9953FF477EE12EFE0440003BAB016E8 | B9953FF477DB12EFE0440003BAB016E8 | B9953FF477E812EFE0440003BAB016E8 |
| IAP_SUBJECT_SPONSOR_KEY | B979A5B908FF644BE0440003BAB016E8 | B979A5B90857644BE0440003BAB016E8 | B979A5B908CF644BE0440003BAB016E8 |
| IAP_SUBJECT_SESSION_KEY | 9289afed754ffd4701764d88c6e0054c | 9289afec76e20021017702b62c5a01e9 | 9289afed754ffd470175e610959301a2 |
| IAP_SUBJECT_PERSON_KEY | 9289afed754ffd4701764d88c6e0054c | 9289afec76e20021017702b62c5a01e9 | 9289afed754ffd470175e610959301a2 |
| ACTIVITY_TITLE | GIS Level 3: Automating Arcgis Using Python | The Power Series: Exploration Through Case Studies | AIChallenge - Developing the Next Generation of AI Challenge Problems |
| ACTIVITY_DESCRIPTION | <p>Learn to automate GIS tool using Python. You'll learn just enough Python scripting to work with the ArcPy module. These tool | <p>From the COVID-19 pandemic to the racial justice reckoning, 2020 brought a number of challenges that disproportionately impa | <p>AI challenges such as ImageNet, CIFAR, Graph Challenge, Moments in Time have resulted in major advances in image recognition |
| TERM_CODE | 2021JA | 2021JA | 2021JA |
| ENROLLMENT_TYPE | Advance sign-up required | Advance sign-up required | Advance sign-up required |
| MAX_ENROLLMENT | null | null | 40 |
| ATTENDANCE | Participants must attend all sessions | Participants welcome at individual sessions | Participants must attend all sessions |
| PREREQUISITES | experience with GIS software | null | Programming experience, deep learning environments |
| FEE | null | null | null |
| FEE_REASON | null | null | null |
| PREREG_DEADLINE | null | 18-JAN-21 | 18-DEC-20 |
| CREATE_DATE | 10-DEC-20 | 14-JAN-21 | 20-NOV-20 |
| LAST_ACTIVITY_DATE | 10-DEC-20 | 15-JAN-21 | 01-DEC-20 |
| IS_MULTIPLE_SESSION | N | Y | Y |
| IS_CANCELLED | N | N | N |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `iap_subject_person`  (rows=1113)

columns:
`IAP_SUBJECT_PERSON_KEY` varchar127: 390 distinct, "9289afec76e20021017726cba96702c6"=15, "9289afed754ffd47017625038ba50344"=15, "9289afec754ffaf20176d55e61b10cd2"=14, "9289afed754ffd47017688b60415096f"=13, "9289afec754ffaf2017676e5ed8008ac"=12, "9289afed754ffd4701761f2173500287"=12, "9289afec754ffaf20175dcce64b101dd"=10, "9289afec754ffaf20176daa211260d3f"=10, "9289afec76e2002101771bf8a9d7025f"=10, "9289afed754ffd470175795788070033"=10
`PERSON_ROLE` varchar127: "Activity leader"=506, "Contact person"=389, "Session leader"=193, nulls=25
`PERSON_MIT_AFFILIATION` varchar127: "Staff"=231, "Non-MIT"=117, "Research Staff"=82, "Other MIT"=80, "MIT Professor"=58, "Grad Student"=56, "Instruct. Staff"=38, "Senior Lecturer"=13, "Senior"=11, "Junior"=6, "Sophomore"=6, "Freshman"=1, nulls=414
`PERSON_NAME` varchar127: 1084 distinct, nulls=25
`PERSON_LOCATION` varchar127: 76 distinct, nulls=964
`PERSON_EMAIL` varchar127: 377 distinct, nulls=727
`PERSON_ORGANIZATION` varchar127: all NULL
`PERSON_TITLE` varchar127: all NULL
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=1113

indexes: `IAP_SUBJECT_PERSON_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IAP_SUBJECT_PERSON_KEY | 9289afed772f5a47017746bb27790021 | 9289afed76e1ff43017725a58d710133 | 9289afed754ffd47017649036b1004f3 |
| PERSON_ROLE | Contact person | Activity leader | Contact person |
| PERSON_MIT_AFFILIATION | null | Staff | null |
| PERSON_NAME | Rihanna Ashley | Rico Moreno | Lexi Vincent |
| PERSON_LOCATION | null | null | 26-474 |
| PERSON_EMAIL | null | null | lexiv@worker.com |
| PERSON_ORGANIZATION | null | null | null |
| PERSON_TITLE | null | null | null |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `iap_subject_session`  (rows=1199)

columns:
`IAP_SUBJECT_SESSION_KEY` varchar127: 421 distinct, "9289afed754ffd470175dc0d4847014a"=33, "9289afed754ffd470176b0132c600ab4"=31, "9289afed754ffd470175c34fa53100e9"=29, "9289afec754ffaf20175fb71bc0c022e"=19, "9289afec754ffaf20176783305810901"=19, "9289afed754ffd470176afed669a0a96"=19, "9289afec754ffaf20175d7df701d0144"=16, "9289afec754ffaf20175d7ec7e7a016e"=16, "9289afed754ffd4701756b398bdf0002"=14, "9289afed754ffd470176d44d64c70c9e"=14
`SESSION_SEQUENCE` int: all NULL
`SESSION_TITLE` varchar127: 227 distinct, nulls=534
`SESSION_DESCRIPTION` varchar127: 195 distinct, nulls=606
`SESSION_LOCATION` varchar127: 41 distinct, nulls=116, "Zoom"=407, "Virtual"=341, "Online"=115, "via Zoom"=33, "On Zoom"=27, "remote"=14, "https://mit.zoom.us/"=13, "On line"=12, "TBD"=11, "NE45"=10
`SESSION_DATE` varchar255: 35 distinct, nulls=69
`SESSION_START_TIME` varchar127: 31 distinct, nulls=62
`SESSION_END_TIME` varchar127: 42 distinct, nulls=62
`HAS_SESSION_INFO` varchar127: "Y"=1181, "N"=18
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=1199

indexes: `IAP_SUBJECT_SESSION_KEY`, `SESSION_LOCATION`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IAP_SUBJECT_SESSION_KEY | 9289afed772f5a47017746bb27790021 | 9289afed76e1ff4301771d34c4fd010d | 9289afec754ffaf20175dc39554701ce |
| SESSION_SEQUENCE | null | null | null |
| SESSION_TITLE | null | null | Understanding Racial Identity |
| SESSION_DESCRIPTION | null | null | null |
| SESSION_LOCATION | virtual | via Zoom | Zoom |
| SESSION_DATE | 29-JAN-21 | 28-JAN-21 | 06-JAN-21 |
| SESSION_START_TIME | 0200PM | 0200PM | 0200PM |
| SESSION_END_TIME | 0400PM | 0300PM | 0300PM |
| HAS_SESSION_INFO | Y | Y | Y |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `iap_subject_sponsor`  (rows=68)

columns:
`IAP_SUBJECT_SPONSOR_KEY` varchar127: all distinct
`SPONSOR_NAME` varchar127: all distinct, nulls=1
`SPONSOR_TYPE` varchar127: "Academic Department"=25, "Administrative Department"=20, "Student Group"=9, "Center"=6, "Lab"=6, "Other MIT Groups"=2
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=68

indexes: `IAP_SUBJECT_SPONSOR_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IAP_SUBJECT_SPONSOR_KEY | B979A5B90923644BE0440003BAB016E8 | 9289af8f5fd92585015fe0471ab7007c | B979A5B90847644BE0440003BAB016E8 |
| SPONSOR_NAME | MIT Flying Club | MIT.nano | Writing and Communication Center |
| SPONSOR_TYPE | Student Group | Lab | Administrative Department |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `ir_institution`  (rows=10000)

columns:
`INSTITUTION_ID` varchar127: unique identifier
`INSTITUTION_NAME` varchar127: 9820 distinct
`ALTERNATE_INSTITUTION_NAME` varchar127: 1450 distinct, nulls=8473
`STREET_ADDRESS` varchar127: 8742 distinct, nulls=1196
`CITY` varchar127: 4456 distinct, nulls=128
`ZIP` varchar127: 3398 distinct, nulls=5524
`STATE` varchar127: 60 distinct, nulls=5532
`COUNTRY_CODE` varchar127: 158 distinct, nulls=1
`COUNTRY` varchar127: 159 distinct
`INSTITUTION_CATEGORY_VALUE` int: 34 distinct, -3..33, avg=1.7696, median=-3
`INSTITUTION_CATEGORY_LABEL` varchar127: 34 distinct
`INSTITUTION_SORT_ORDER` varchar127: digits, 193 distinct, nulls=5
`RECORD_CREATED_DATE` varchar255: "17-JUL-14"=9064, "16-JUL-24"=930, "01-DEC-24"=5, "10-JUL-24"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| INSTITUTION_ID | M0019 | 495420 | 241720 |
| INSTITUTION_NAME | Penn Foster Career School | Arizona College of Nursing-Tampa | Colegio Universitario de San Juan |
| ALTERNATE_INSTITUTION_NAME | null | null | Colegio Tecnologico de San Juan |
| STREET_ADDRESS | null | 1411 N West Shore Blvd, Suite 200 | 180 Jose Oliver St Tres Monjitas  Ind. Park |
| CITY | SCRANTON | Tampa | SAN JUAN |
| ZIP | null | 33607 | 918 |
| STATE | PA | FL | PR |
| COUNTRY_CODE | US | US | US |
| COUNTRY | UNITED STATES | UNITED STATES | UNITED STATES |
| INSTITUTION_CATEGORY_VALUE | -3 | -3 | 23 |
| INSTITUTION_CATEGORY_LABEL | Not applicable, not in Carnegie universe (not accredited or nondegree-granting)  | Not applicable, not in Carnegie universe (not accredited or nondegree-granting)  | Baccalaureate/Associate's Colleges  |
| INSTITUTION_SORT_ORDER | 900 | 999 | 9 |
| RECORD_CREATED_DATE | 17-JUL-14 | 16-JUL-24 | 17-JUL-14 |

# `library_course_instructor`  (rows=10000)

columns:
`LIBRARY_COURSE_INSTRUCTOR_KEY` varchar127: 9999 distinct
`COURSE_NAME` varchar127: 2998 distinct
`INSTRUCTOR_NAME` varchar127: 9591 distinct, "Blackburn, Gianluca"=3, "Coffey, Nicolas"=3, "Conner, Zayn"=3, "Dorsey, Sydney"=3, "Haines, Khalil"=3, "Mckee, Shauna"=3, "Obrien, Josef"=3, "Randall, Mariya"=3, "Robbins, Barnaby"=3, "Sears, Mia"=3
`DEPARTMENT` varchar127: 128 distinct
`DATE_FROM` varchar255: 266 distinct
`DATE_TO` varchar255: 57 distinct
`UNIT_CODE` varchar127: "Hayden"=4492, "ENG"=1508, "DEW"=1480, "RTC"=659, "MUS"=214, "DEW and Hayden"=3, "DEW + Hayden"=2, "Hayden & ENG"=2, "10Hayden"=1, "DEW & Hayden"=1, "DEW & Hayden & ENG"=1, nulls=1637
`UNIT` varchar127: "Hayden"=4492, "Barker"=1508, "Dewey"=1480, "Rotch"=659, "Lewis Music"=214, nulls=1647
`WAREHOUSE_LOAD_DATE` varchar255: 30 distinct

indexes: `INSTRUCTOR_NAME`, `LIBRARY_COURSE_INSTRUCTOR_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| LIBRARY_COURSE_INSTRUCTOR_KEY | WGS.S10-LINDSEY142014SP:WGS.S10 | 24.245-MARTINEZ2011SP:24.245 | 2.02A-BONNER132013SP:2.02A |
| COURSE_NAME | Special Subject in Women's and Gender Studies, Gender, Power and Leadership in the Workplace | Theory of Models | Engineering Materials: Properties and Applications |
| INSTRUCTOR_NAME | Lindsey, Sion | Martinez, Zoe | Bonner, Elizabeth |
| DEPARTMENT | WGS - Women's and Gender Studies | 24 - Linguistics and Philosophy | 2 - Mechanical Engineering |
| DATE_FROM | 03-FEB-14 | 31-JAN-11 | 04-FEB-13 |
| DATE_TO | 23-MAY-14 | 05-JUN-11 | 24-MAY-13 |
| UNIT_CODE | Hayden | Hayden | ENG |
| UNIT | Hayden | Hayden | Barker |
| WAREHOUSE_LOAD_DATE | 24-APR-14 | 06-MAY-11 | 25-APR-13 |

# `library_material_status`  (rows=6)

columns:
`LIBRARY_MATERIAL_STATUS_KEY` varchar127
`LIBRARY_MATERIAL_STATUS_CODE` varchar127
`LIBRARY_MATERIAL_STATUS` varchar127
`WAREHOUSE_LOAD_DATE` varchar255

indexes: `LIBRARY_MATERIAL_STATUS_KEY`

all rows:
| column | row 1 | row 2 | row 3 | row 4 | row 5 | row 6 |
|---|---|---|---|---|---|---|
| LIBRARY_MATERIAL_STATUS_KEY | N | O | R | U | X | Y |
| LIBRARY_MATERIAL_STATUS_CODE | N | O | R | U | X | Y |
| LIBRARY_MATERIAL_STATUS | Non-Required Course Material | Reserve only | null | Unknown | No Required Textbook | Required Course Material |
| WAREHOUSE_LOAD_DATE | 23-DEC-21 | 23-DEC-21 | 23-DEC-21 | 23-DEC-21 | 23-DEC-21 | 23-DEC-21 |

# `library_reserve_catalog`  (rows=10000)

columns:
`LIBRARY_RESERVE_CATALOG_KEY` varchar127: digits, 9629 distinct, "10491"=3, "106614"=3, "110713"=3, "114216"=3, "27138"=3, "44921"=3, "56024"=3, "68687"=3, "71322"=3, "1"=2
`CATALOG_TITLE` varchar127: 5212 distinct, nulls=2542
`CATALOG_AUTHOR_NAME` varchar127: 3123 distinct, nulls=5293
`CATALOG_YEAR` varchar127: digits, 90 distinct
`CATALOG_PUBLISHER` varchar127: 3434 distinct, nulls=4974
`CATALOG_CALL_NUMBER` varchar127: 4262 distinct, nulls=4554
`CATALOG_ISBN` varchar127: 3794 distinct, nulls=5231
`CATALOG_SYSTEM_NUMBER` varchar127: digits, 9629 distinct
`CATALOG_RECORD_CREATE_DATE` varchar255: 2447 distinct
`CATALOG_RECORD_UPDATE_DATE` varchar255: 1708 distinct
`RECORD_COUNTER` int: 1=10000
`WAREHOUSE_LOAD_DATE` varchar255: 1128 distinct

indexes: `LIBRARY_RESERVE_CATALOG_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| LIBRARY_RESERVE_CATALOG_KEY | 9999 | 102397 | 113909 |
| CATALOG_TITLE | null | A streetcar named Desire / Tennessee Williams ; with an introduction by Arthur Miller. | The winter's tale / edited by John Pitcher. |
| CATALOG_AUTHOR_NAME | null | Williams, Tennessee, 1911-1983. | Shakespeare, William, 1564-1616. |
| CATALOG_YEAR | 0 | 2004 | 2010 |
| CATALOG_PUBLISHER | null | New York : New Directions, c2004. | null |
| CATALOG_CALL_NUMBER | null | PS3545.I5365.S8 2004 | PR2839.A2 P58 2010 |
| CATALOG_ISBN | null | 0811216020 (alk. paper) | 9781903436356 |
| CATALOG_SYSTEM_NUMBER | 9999 | 102397 | 113909 |
| CATALOG_RECORD_CREATE_DATE | 03-SEP-02 | 27-NOV-16 | 10-SEP-19 |
| CATALOG_RECORD_UPDATE_DATE | 24-APR-03 | 27-NOV-16 | 29-JAN-20 |
| RECORD_COUNTER | 1 | 1 | 1 |
| WAREHOUSE_LOAD_DATE | 13-MAR-08 | 28-NOV-16 | 30-JAN-20 |

# `library_reserve_matrl_detail`  (rows=10000)

columns:
`LIBRARY_COURSE_INSTRUCTOR_KEY` varchar127: 1614 distinct, "21M.262-PALMER2009FA:21M.262"=157, "21M.342-GAMBLE2009FA:21M.342"=149, "21M.271-SYKES2009FA:21M.271"=134, "21M.240-RODGERS2009SP:21M.240"=130, "4.303-LYNCH2009FA:4.303"=129, "21M.240-BROCK2008SP:21M.240"=125, "21M.230-BOWMAN2009FA:21M.230"=120, "21M.284-MCLAUGHLIN2009SP:21M.284"=118, "21M.284-ROWE2008SP:21M.284"=112, "21M.273-BUCKLEY2008SP:21M.273"=111
`LIBRARY_RESERVE_CATALOG_KEY` varchar127: digits, 8268 distinct, "47519"=7, "47520"=7, "46579"=6, "46580"=6, "47472"=6, "47561"=6, "51632"=6, "51633"=6, "51833"=6, "51834"=6
`LIBRARY_SUBJECT_OFFERED_KEY` varchar127: 1550 distinct, "21M.2622009FA"=157, "21M.3422009FA"=149, "21M.2712009FA"=134, "21M.2402009SP"=130, "4.3032009FA"=129, "21M.2402008SP"=125, "21M.2302009FA"=120, "21M.2842009SP"=118, "21M.2842008SP"=112, "21M.2732008SP"=111
`LIBRARY_MATERIAL_STATUS_KEY` varchar127: "U"=6663, "N"=1953, "Y"=1338, "O"=32, "X"=14
`TERM_CODE` varchar127: "2009FA"=3311, "2009SP"=2638, "2008SP"=2463, "2010SP"=619, "2008SU"=600, "2009SU"=256, "2011FA"=92, "2009JA"=21
`SUBJECT_ID` varchar127: 1011 distinct, "HST.S11"=313, "21M.240"=275, "21M.284"=230, "21M.273"=218, "21M.262"=157, "21M.342"=149, "21M.271"=134, "21H.421"=131, "4.303"=129, "21M.230"=120
`WAREHOUSE_LOAD_DATE` varchar255: "05-DEC-08"=3311, "08-MAY-09"=2638, "09-MAY-08"=2463, "07-MAY-10"=619, "01-AUG-08"=600, "31-JUL-09"=256, "18-NOV-10"=92, "02-FEB-09"=21

indexes: `LIBRARY_COURSE_INSTRUCTOR_KEY`, `LIBRARY_MATERIAL_STATUS_KEY`, `LIBRARY_RESERVE_CATALOG_KEY`, `LIBRARY_SUBJECT_OFFERED_KEY`, `SUBJECT_ID`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| LIBRARY_COURSE_INSTRUCTOR_KEY | STS.CASTELLS2009SP:STS.CASTELLS-HUMPHREY | 4.619-MCCANN2009FA:4.619 | 10.40-VANCE2009FA:10.40 |
| LIBRARY_RESERVE_CATALOG_KEY | 53319 | 23876 | 49456 |
| LIBRARY_SUBJECT_OFFERED_KEY | STS.CASTELLS2009SP | 4.6192009FA | 10.402009FA |
| LIBRARY_MATERIAL_STATUS_KEY | N | U | Y |
| TERM_CODE | 2009SP | 2009FA | 2009FA |
| SUBJECT_ID | STS.CASTELLS | 4.619 | 10.40 |
| WAREHOUSE_LOAD_DATE | 08-MAY-09 | 05-DEC-08 | 05-DEC-08 |

# `library_subject_offered`  (rows=10000)

columns:
`LIBRARY_SUBJECT_OFFERED_KEY` varchar127: all distinct
`TERM_CODE` varchar127: 52 distinct, "2014FA"=442, "2013FA"=441, "2016FA"=434, "2013SP"=422, "2016SP"=416, "2011FA"=413, "2019FA"=413, "2018FA"=406, "2012SP"=403, "2019SP"=401
`MASTER_COURSE_NUMBER` varchar127: 37 distinct
`MASTER_COURSE_NUMBER_SORT` varchar127: 37 distinct
`MASTER_COURSE_NUMBER_DESC` varchar127: 37 distinct
`MASTER_SUBJECT_ID` varchar127: 1902 distinct, "18.085"=43, "15.501"=41, "21F.301"=41, "21F.401"=40, "15.792"=39, "2.003"=39, "21F.701"=39, "21F.402"=38, "18.100B"=37, "2.EPE"=37
`MASTER_SUBJECT_ID_SORT` varchar127: 1909 distinct, "18.085"=43, "15.501"=41, "21F.301"=41, "21F.401"=40, "15.792"=39, "2.003"=39, "21F.701"=39, "21F.402"=38, "18.100B"=37, "2.EPE"=37
`COURSE_NUMBER` varchar127: "15"=1407, "18"=1127, "21F"=1074, "2"=963, "11"=706, "21G"=684, "1"=601, "17"=501, "16"=492, "21H"=475, "12"=474, "14"=425, "10"=403, "21A"=246, "20"=220, "21L"=202
`COURSE_NUMBER_SORT` varchar127: " 15"=1407, " 18"=1127, "21F"=1074, "  2"=963, " 11"=706, "21G"=684, "  1"=601, " 17"=501, " 16"=492, "21H"=475, " 12"=474, " 14"=425, " 10"=403, "21A"=246, " 20"=220, "21L"=202
`COURSE_NUMBER_DESC` varchar127: "Management"=1407, "Mathematics"=1127, "Foreign Languages/Literatures"=1074, "Mechanical Engineering"=963, "Urban Studies and Planning"=706, "Global Languages"=684, "Civil and Environmental Eng"=601, "Political Science"=501, "Aeronautics and Astronautics"=492, "History"=475, "Earth, Atmos, & Planetary Sci"=474, "Economics"=425, "Chemical Engineering"=403, "Anthropology"=246, "Prog in Applied Biological Sci"=220, "Literature"=202
`SUBJECT_ID` varchar127: 2249 distinct, "18.085"=31, "18.100B"=26, "15.501"=25, "18.06"=24, "14.02"=23, "15.402"=23, "15.535"=23, "15.615"=23, "18.901"=23, "10.10"=22
`SUBJECT_ID_SORT` varchar127: 2249 distinct, " 18.085"=31, " 18.100B"=26, " 15.501"=25, " 18.06"=24, " 14.02"=23, " 15.402"=23, " 15.535"=23, " 15.615"=23, " 18.901"=23, " 10.10"=22
`SUBJECT_TITLE` varchar127: 1783 distinct
`OFFER_DEPT_CODE` varchar127: "15"=1407, "18"=1127, "21F"=1074, "2"=963, "11"=706, "21G"=684, "1"=601, "17"=501, "16"=492, "21H"=475, "12"=474, "14"=425, "10"=403, "21A"=246, "20"=220, "21L"=202
`OFFER_DEPT_NAME` varchar127: "Management"=1407, "Mathematics"=1127, "Global Studies & Languages"=1074, "Mechanical Engineering"=963, "Urban Studies and Planning"=706, "Global Languages"=684, "Civil and Environmental Eng"=601, "Political Science"=501, "Aeronautics and Astronautics"=492, "History"=475, "Earth, Atmos & Planetary Sci"=474, "Economics"=425, "Chemical Engineering"=403, "Anthropology"=246, "Biological Engineering"=220, "Literature"=202
`OFFER_SCHOOL_NAME` varchar127: "Hum, Arts & Social Sciences"=3607, "Engineering"=2679, "Science"=1601, "Sloan School of Management"=1407, "Architecture and Planning"=706
`RESPONSIBLE_FACULTY_NAME` varchar127: 1455 distinct, nulls=105
`RESPONSIBLE_FACULTY_MIT_ID` varchar127: digits, 1464 distinct, nulls=105, "996739932"=82, "956410591"=77, "961787725"=76, "901910874"=68, "937617190"=66, "951489780"=59, "958913072"=59, "982514819"=59, "970976616"=56, "947663483"=55
`NUM_ENROLLED_STUDENTS` int: 285 distinct, 0..673, avg=26.3104, median=12
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: `COURSE_NUMBER`, `LIBRARY_SUBJECT_OFFERED_KEY`, `MASTER_SUBJECT_ID`, `MASTER_SUBJECT_ID_SORT`, `OFFER_DEPT_CODE`, `RESPONSIBLE_FACULTY_MIT_ID`, `SUBJECT_ID`, `SUBJECT_ID_SORT`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| LIBRARY_SUBJECT_OFFERED_KEY | 21L.0232014FA | 21F.5922012FA | 18.7042015SP |
| TERM_CODE | 2014FA | 2012FA | 2015SP |
| MASTER_COURSE_NUMBER | 21M | 21F | 18 |
| MASTER_COURSE_NUMBER_SORT | 21M | 21F |  18 |
| MASTER_COURSE_NUMBER_DESC | Music and Theater Arts | Foreign Languages/Literatures | Mathematics |
| MASTER_SUBJECT_ID | 21M.223 | 21F.064 | 18.704 |
| MASTER_SUBJECT_ID_SORT | 21M.223 | 21F.064 | 18.704 |
| COURSE_NUMBER | 21L | 21F | 18 |
| COURSE_NUMBER_SORT | 21L | 21F |  18 |
| COURSE_NUMBER_DESC | Literature | Foreign Languages/Literatures | Mathematics |
| SUBJECT_ID | 21L.023 | 21F.592 | 18.704 |
| SUBJECT_ID_SORT | 21L.023 | 21F.592 |  18.704 |
| SUBJECT_TITLE | Folk Music: Britain & N Amer | Intro to Japanese Culture | Seminar in Algebra |
| OFFER_DEPT_CODE | 21L | 21F | 18 |
| OFFER_DEPT_NAME | Literature | Global Studies & Languages | Mathematics |
| OFFER_SCHOOL_NAME | Hum, Arts & Social Sciences | Hum, Arts & Social Sciences | Science |
| RESPONSIBLE_FACULTY_NAME | Mata, Martha | Pruitt, Ieuan | Shaw, Siobhan |
| RESPONSIBLE_FACULTY_MIT_ID | 918228668 | 981661423 | 969518852 |
| NUM_ENROLLED_STUDENTS | 1 | 5 | 11 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `master_dept_dcode_parent`  (rows=340)

columns:
`DEPT_ID` int: unique identifier, 11396..16220
`D_CODE` varchar127: all distinct
`D_NAME` varchar127: 339 distinct
`PARENT_ID` int: 31 distinct, 10000..15701
`PARENT_D_CODE` varchar127: 31 distinct
`PARENT_D_NAME` varchar127: 31 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=340

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| DEPT_ID | 16220 | 13617 | 12785 |
| D_CODE | D_TATA-MIT | D_DEFUNCT | D_UPOP |
| D_NAME | TATA-MIT ALLIANCE | Defunct units | Undergrad Practice Op Prog |
| PARENT_ID | 12259 | 13740 | 12259 |
| PARENT_D_CODE | D_SCHOOL_ENG | D_UNDEF_DEFUNCT | D_SCHOOL_ENG |
| PARENT_D_NAME | School of Engineering | Undefined or defunct | School of Engineering |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `master_dept_hierarchy`  (rows=310)

columns:
`HIERARCHY_TYPE` varchar127: "Standard Hierarchy"=310
`DLC_KEY` varchar127: all distinct
`DLC_CODE` varchar127: all distinct
`DLC_NAME` varchar127: 309 distinct
`MASTER_DEPT_HIER_LEVEL_1_CODE` varchar127: "D_ALL"=310
`MASTER_DEPT_HIER_LEVEL_1_NAME` varchar127: "All Departments"=310
`MASTER_DEPT_HIER_LEVEL_2_CODE` varchar127: "D_PROVOST_AREA"=234, "D_EXECVP_AREA"=52, "D_OTHER_ORG"=7, "D_PRES_AREA"=7, "D_INST_REL_AREA"=3, "D_OBSOLETE"=3, "D_UNDEF_DEFUNCT"=3, "D_OUTSIDE_INST"=1
`MASTER_DEPT_HIER_LEVEL_2_NAME` varchar127: "Provost Area"=234, "Executive Vice President's Area"=52, "Outside organizations affiliated with MIT"=7, "President's area"=7, "Miscellaneous Institute Related"=3, "Obsolete DLC codes"=3, "Undefined or defunct"=3, "Other institutions outside of MIT"=1
`MASTER_DEPT_HIER_LEVEL_3_CODE` varchar127: 20 distinct, nulls=56
`MASTER_DEPT_HIER_LEVEL_3_NAME` varchar127: 20 distinct, nulls=56
`MASTER_DEPT_HIER_LEVEL_4_CODE` varchar127: "D_OSATT_AREA"=6, "D_SOURCING_AREA"=3, nulls=301
`MASTER_DEPT_HIER_LEVEL_4_NAME` varchar127: "Office of Strategic Alliances & Tech Transfer Area"=6, "Sourcing Area"=3, nulls=301
`MASTER_DEPT_HIER_LEVEL_5_CODE` varchar127: all NULL
`MASTER_DEPT_HIER_LEVEL_5_NAME` varchar127: all NULL

indexes: `DLC_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| HIERARCHY_TYPE | Standard Hierarchy | Standard Hierarchy | Standard Hierarchy |
| DLC_KEY | D_WHITEHEAD | D_OVPC | D_CSPA |
| DLC_CODE | D_WHITEHEAD | D_OVPC | D_CSPA |
| DLC_NAME | Whitehead Institute | OFFICE OF VICE PRESIDENT FOR COMMUNICATIONS | Career Serv & Pre-Prof Advising |
| MASTER_DEPT_HIER_LEVEL_1_CODE | D_ALL | D_ALL | D_ALL |
| MASTER_DEPT_HIER_LEVEL_1_NAME | All Departments | All Departments | All Departments |
| MASTER_DEPT_HIER_LEVEL_2_CODE | D_OTHER_ORG | D_PRES_AREA | D_PROVOST_AREA |
| MASTER_DEPT_HIER_LEVEL_2_NAME | Outside organizations affiliated with MIT | President's area | Provost Area |
| MASTER_DEPT_HIER_LEVEL_3_CODE | null | null | D_DUE |
| MASTER_DEPT_HIER_LEVEL_3_NAME | null | null | Dean for Undergraduate Education |
| MASTER_DEPT_HIER_LEVEL_4_CODE | null | null | null |
| MASTER_DEPT_HIER_LEVEL_4_NAME | null | null | null |
| MASTER_DEPT_HIER_LEVEL_5_CODE | null | null | null |
| MASTER_DEPT_HIER_LEVEL_5_NAME | null | null | null |

# `master_dept_hierarchy_links`  (rows=10000)

columns:
`HIERARCHY_TYPE` varchar127: "Standard Hierarchy"=10000
`LINK_TYPE_CODE` varchar127: "FC"=8426, "PMIT"=917, "ORG2"=227, "ORGU"=161, "BAG"=103, "FORG"=97, "SIS"=69
`LINK_TYPE` varchar127: "Standard Funds Center"=8426, "PCMIT-0 Profit Center"=917, "New Org. Unit"=227, "Old Org. Unit"=161, "NIMBUS B.A.G."=103, "Facilities Org."=97, "Student Systems Unit"=69
`DLC_KEY` varchar127: 127 distinct
`DLC_CODE` varchar127: 127 distinct
`LINKED_OBJECT_KEY` varchar127: 9942 distinct
`LINKED_OBJECT_CODE` varchar127: 9942 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| HIERARCHY_TYPE | Standard Hierarchy | Standard Hierarchy | Standard Hierarchy |
| LINK_TYPE_CODE | SIS | FC | FC |
| LINK_TYPE | Student Systems Unit | Standard Funds Center | Standard Funds Center |
| DLC_KEY | D_WHIT | D_MECHE | D_CEE |
| DLC_CODE | D_WHIT | D_MECHE | D_CEE |
| LINKED_OBJECT_KEY | WHIT | FC_MECHENG180 | FC_CEE17 |
| LINKED_OBJECT_CODE | WHIT | FC_MECHENG180 | FC_CEE17 |

# `mit_holiday_closing_calendar`  (rows=580)

columns:
`HOLIDAY_CLOSING_DATE` varchar255: 577 distinct
`HOLIDAY_CLOSING_DESCRIPTION` varchar127: "EMER"=86, "SHOL"=62, "MIT Veterans' Day"=42, "MIT Christmas Day"=40, "MIT Independence Day"=40, "MIT New Year's Day"=40, "MIT Day After Thanksgiving"=32, "MIT Indigenous Peoples' Day"=32, "MIT Labor Day"=32, "MIT Martin Luther King Day"=32, "MIT Memorial Day"=32, "MIT Patriots' Day"=32, "MIT Presidents' Day"=32, "MIT Thanksgiving Day"=32, "MIT Juneteenth"=14
`HOLIDAY_CLOSING_TYPE` varchar127: "Standard Holiday"=432, "Emergency Closing"=86, "Special Holiday/Closing"=62
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=580

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| HOLIDAY_CLOSING_DATE | 31-MAY-27 | 04-JUL-03 | 05-JUL-24 |
| HOLIDAY_CLOSING_DESCRIPTION | MIT Memorial Day | MIT Independence Day | SHOL |
| HOLIDAY_CLOSING_TYPE | Standard Holiday | Standard Holiday | Special Holiday/Closing |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `mit_student_directory`  (rows=10000)

columns:
`FIRST_NAME` varchar127: 364 distinct
`MIDDLE_NAME` varchar127: 361 distinct, nulls=5759
`LAST_NAME` varchar127: 339 distinct
`FULL_NAME` varchar127: 8585 distinct, "Cain, Maya"=4, "Avila, Bronwyn"=3, "Best, Reggie"=3, "Blackburn, Anastasia"=3, "Bradford, Rayhan"=3, "Briggs, Jerry"=3, "Bruce, Madison"=3, "Bush, Denise"=3, "Cardenas, Wanda"=3, "Carroll, Keaton"=3
`OFFICE_LOCATION` varchar127: 283 distinct, nulls=9636, "18-128B"=6, "26-226D"=4, "31-300"=4, "7-018"=4, "13-384"=3, "2-412"=3, "26-295"=3, "3-187A"=3, "3-385D"=3, "31-250"=3
`OFFICE_PHONE` varchar127: digits, 51 distinct, nulls=9948
`EMAIL_ADDRESS` varchar127: 3290 distinct, nulls=57
`DEPARTMENT` varchar127: digits, 49 distinct, nulls=8, "6"=1987, "NIH"=1260, "15"=1233, "NONE"=743, "2"=659, "8"=325, "18"=324, "16"=285, "10"=269, "NIW"=249
`DEPARTMENT_NAME` varchar127: 49 distinct, nulls=8
`STUDENT_YEAR` varchar127: "G"=6275, "4"=1041, "3"=965, "2"=924, "1"=783, nulls=12
`FULL_NAME_UPPERCASE` varchar127: 8585 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: `DEPARTMENT`, `FULL_NAME`, `OFFICE_LOCATION`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FIRST_NAME | Zoe | Miguel | Anastasia |
| MIDDLE_NAME | W | D | null |
| LAST_NAME | Fuller | Steele | Blackburn |
| FULL_NAME | Fuller, Zoe | Steele, Miguel | Blackburn, Anastasia |
| OFFICE_LOCATION | null | null | null |
| OFFICE_PHONE | null | null | null |
| EMAIL_ADDRESS | zoef@worker.com | ro@worker.com | anastasiab@worker.com |
| DEPARTMENT | 15 | 15 | NIW |
| DEPARTMENT_NAME | Management | Management | Wellesley Cross-Enrollment Pro |
| STUDENT_YEAR | G | G | 2 |
| FULL_NAME_UPPERCASE | FULLER, ZOE | STEELE, MIGUEL | BLACKBURN, ANASTASIA |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `moira_list`  (rows=10000)

columns:
`MOIRA_LIST_KEY` varchar127: 8815 distinct, "iguana-iguana"=5, "quokka-umbrella"=5, "vivid-prosper"=5, "banana-courage"=4, "cherry-optimism"=4, "dog-quest"=4, "honeydew-destiny"=4, "iris-quokka"=4, "iris-violet"=4, "island-whale"=4
`MOIRA_LIST_NAME` varchar127: 8815 distinct
`MOIRA_LIST_DESCRIPTION` varchar127: all NULL
`IS_ACTIVE` varchar127: "Y"=10000
`IS_MOIRA_MAILING_LIST` varchar127: "Y"=8771, "N"=1229
`IS_MOIRA_GROUP` varchar127: "N"=8509, "Y"=1491
`IS_NFS_GROUP` varchar127: "N"=9533, "Y"=467
`IS_PUBLIC` varchar127: "N"=9473, "Y"=527
`IS_HIDDEN` varchar127: "N"=10000

indexes: `MOIRA_LIST_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MOIRA_LIST_KEY | zephyr-zephyr | notion-dancer | radiant-courage |
| MOIRA_LIST_NAME | zephyr-zephyr | notion-dancer | radiant-courage |
| MOIRA_LIST_DESCRIPTION | null | null | null |
| IS_ACTIVE | Y | Y | Y |
| IS_MOIRA_MAILING_LIST | Y | Y | Y |
| IS_MOIRA_GROUP | N | N | N |
| IS_NFS_GROUP | N | N | N |
| IS_PUBLIC | N | N | N |
| IS_HIDDEN | N | N | N |

# `moira_list_detail`  (rows=10000)

columns:
`MOIRA_LIST_KEY` varchar127: 6395 distinct, "orange-rabbit"=205, "amber-destiny"=95, "panda-blossom-octopus"=88, "quokka-beacon"=78, "cat-mango"=59, "nectarine-orange-xerus"=30, "jungle-elephant"=19, "zebu-panda"=19, "xenon-cat-ant"=18, "beacon-date-date"=16
`MOIRA_LIST_OWNER_KEY` varchar127: 3966 distinct, "LISTradiant-meadow"=205, "LISTlegacy-kindness"=161, "LISTecho-lemon"=126, "LISTiris-kindness"=114, "USERdate-raspberry"=112, "LISTpanda-xerus"=103, "LISTpanda-journey"=92, "LISTvoyage-inspire"=81, "USERlemon-umbrella"=78, "LISTumbrella-umbrella"=74
`MOIRA_LIST_MEMBER` varchar127: 6469 distinct, "ah"=24, "ar"=19, "mm"=17, "rh"=17, "em"=16, "ab"=15, "ac"=15, "am"=15, "kh"=15, "mb"=15
`MOIRA_LIST_MEMBER_FULL_NAME` varchar127: 4830 distinct, nulls=5093
`MOIRA_LIST_MEMBER_MIT_ID` varchar127: digits, 3978 distinct, nulls=5093, "991327503"=22, "969364494"=16, "906116916"=10, "910981628"=8, "937762772"=8, "948563640"=7, "960812101"=7, "906233866"=6, "917297228"=6, "960505841"=6
`LAST_UPDATE_DATE` varchar255: 2819 distinct
`COUNTER` int: 1=10000
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: `MOIRA_LIST_KEY`, `MOIRA_LIST_MEMBER`, `MOIRA_LIST_MEMBER_MIT_ID`, `MOIRA_LIST_OWNER_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MOIRA_LIST_KEY | zephyr-zephyr-tower | orange-rabbit | quokka-beacon |
| MOIRA_LIST_OWNER_KEY | LISTant-kindness | LISTradiant-meadow | USERlemon-umbrella |
| MOIRA_LIST_MEMBER | kl | alejandroh | eileenc |
| MOIRA_LIST_MEMBER_FULL_NAME | Lowe, Kitty | Horn, Alejandro | null |
| MOIRA_LIST_MEMBER_MIT_ID | 910981628 | 933147941 | null |
| LAST_UPDATE_DATE | 14-SEP-08 | 25-NOV-24 | 08-JUL-22 |
| COUNTER | 1 | 1 | 1 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `moira_list_owner`  (rows=10000)

columns:
`MOIRA_LIST_OWNER_KEY` varchar127: 9042 distinct, "LISTbeacon-panda"=5, "LISTocean-umbrella"=4, "LISToptimism-rabbit"=4, "LISTumbrella-yearn"=4, "LISTamber-falcon"=3, "LISTant-vivid"=3, "LISTapple-orange"=3, "LISTbanana-orange"=3, "LISTbanana-umbrella"=3, "LISTblossom-apple"=3
`OWNER` varchar127: 8392 distinct
`OWNER_TYPE` varchar127: "LIST"=7646, "USER"=2349, "KERBEROS"=5
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: `MOIRA_LIST_OWNER_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MOIRA_LIST_OWNER_KEY | USERzephyr-yarrow | LIST98.357-jaguar-courage | LIST14.262-blossom-kangaroo |
| OWNER | zephyr-yarrow | 98.357-jaguar-courage | 14.262-blossom-kangaroo |
| OWNER_TYPE | USER | LIST | LIST |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `person_auth_area`  (rows=10000)

columns:
`USER_NAME` varchar127: 5330 distinct, nulls=2
`HAS_FINANCIAL_AUTH` varchar127: "N"=8967, "Y"=1033
`HAS_HR_FULL_AUTH` varchar127: "N"=9941, "Y"=59
`HAS_HR_LIMITED_AUTH` varchar127: "N"=9966, "Y"=34
`HAS_PAYROLL_AUTH` varchar127: "N"=9917, "Y"=83
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| USER_NAME | ZW | GIANLUCAH | CLARAE |
| HAS_FINANCIAL_AUTH | N | N | N |
| HAS_HR_FULL_AUTH | N | N | N |
| HAS_HR_LIMITED_AUTH | N | N | N |
| HAS_PAYROLL_AUTH | N | N | N |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `roles_fin_pa`  (rows=1395)

columns:
`USERNAME` varchar127: 338 distinct
`DLC_KEY` varchar127: 292 distinct

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| USERNAME | zs | hv | barneyh |
| DLC_KEY | D_SCM | D_LGO | D_D-LAB |

# `se_person`  (rows=10000)

columns:
`MIT_ID` varchar127: digits, unique identifier
`KRB_NAME` varchar127: 5341 distinct
`FULL_NAME` varchar127: 9716 distinct, "Buck, Kayne"=3, "Buckley, Bernice"=3, "Chan, Edmund"=3, "Cook, Natalie"=3, "Davies, Connor"=3, "Downs, Aiza"=3, "Edwards, Ross"=3, "Espinoza, Rihanna"=3, "Harrington, Maddison"=3, "Hines, Riya"=3
`PAYROLL_RANK` varchar127: 26 distinct
`POSITION_TITLE` varchar127: all NULL
`IS_ACTIVE` varchar31: "Y"=10000
`OFFICE_LOCATION` varchar127: 3277 distinct, nulls=3730
`ORGANIZATION` varchar127: 320 distinct
`FIRST_NAME` varchar127: 364 distinct
`LAST_NAME` varchar127: 339 distinct
`MIDDLE_NAME` varchar127: 360 distinct, nulls=5270
`EMPLOYEE_TYPE` varchar127: "Student"=3515, "Other Academic Group"=2140, "Admin Staff"=1587, "Sponsored Research Staff"=979, "Support Staff"=662, "Faculty"=579, "Service Staff"=478, "Medical"=60

indexes: `FULL_NAME`, `MIT_ID`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MIT_ID | 999996252 | 900177264 | 930685462 |
| KRB_NAME | do | zahras | siobhanl |
| FULL_NAME | O'Reilly, Dillan | Stark, Zahra | Lam, Siobhan |
| PAYROLL_RANK | Spon Res-Tech | Grad Std Fellow | Grad Std TA |
| POSITION_TITLE | null | null | null |
| IS_ACTIVE | Y | Y | Y |
| OFFICE_LOCATION | 76-474 | null | null |
| ORGANIZATION | Koch Inst - Integrative Cancer Research | Department of Biological Engineering | Electrical Engineering-Computer Science |
| FIRST_NAME | Dillan | Zahra | Siobhan |
| LAST_NAME | O'Reilly | Stark | Lam |
| MIDDLE_NAME | R | null | null |
| EMPLOYEE_TYPE | Sponsored Research Staff | Student | Student |

# `sis_admin_department`  (rows=179)

columns:
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=179
`SIS_ADMIN_DEPARTMENT_CODE` varchar127: all distinct
`SIS_ADMIN_DEPARTMENT_NAME` varchar127: 162 distinct
`DEPARTMENT_PHONE_AREA_CODE` varchar127: all NULL
`DEPARTMENT_PHONE_NUMBER` varchar127: digits, 63 distinct, nulls=102
`CLEARING_COST_COLLECTOR` varchar127: digits, 49 distinct, nulls=116
`LAST_ACTIVITY_DATE` varchar255: 84 distinct

indexes: `SIS_ADMIN_DEPARTMENT_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| SIS_ADMIN_DEPARTMENT_CODE | WWW | LIB | ODGE |
| SIS_ADMIN_DEPARTMENT_NAME | World Wide Web | Library | Dean for Graduate Education |
| DEPARTMENT_PHONE_AREA_CODE | null | null | null |
| DEPARTMENT_PHONE_NUMBER | null | 6999843 | 2968876 |
| CLEARING_COST_COLLECTOR | null | null | 1646800 |
| LAST_ACTIVITY_DATE | 07-APR-97 | 05-NOV-96 | 22-JUL-08 |

# `sis_course_description`  (rows=695)

columns:
`SIS_COURSE_DESCRIPTION_KEY` varchar127: all distinct
`COURSE` varchar127: 630 distinct
`COURSE_DESCRIPTION` varchar127: 535 distinct
`COURSE_DESCRIPTION_LONG` varchar127: 298 distinct, nulls=5
`DEPARTMENT` varchar127: 72 distinct, "12"=39, "6"=39, "15"=37, "ASP"=33, "UND"=33, "1"=26, "2"=26, "16"=25, "4"=25, "ESD"=21
`DEPARTMENT_NAME` varchar127: 71 distinct
`DEPT_NAME_IN_COMMENCEMENT_BK` varchar127: 45 distinct, nulls=118
`SCHOOL_NAME` varchar127: "Engineering"=321, "Science"=106, "Hum, Arts & Social Sciences"=93, "Architecture and Planning"=46, "MIT, academic"=45, "Sloan School of Management"=42, "Non-MIT"=30, "Schwarzman Coll of Comp"=7, "Whitaker Coll of HST;  HST"=5
`SCHOOL_NAME_IN_COMMENCEMENT_BK` varchar127: "School of Engineering"=321, "School of Science"=106, "School of Humanities, Arts, and Social Sciences"=93, "School of Architecture and Planning"=46, "Sloan School of Management"=42, "Schwarzman College of Computing"=7, "Whitaker College of Health Sciences and Technology"=5, nulls=75
`FROM_TERM` varchar127: 74 distinct
`FROM_TERM_DESCRIPTION` varchar127: 74 distinct
`THRU_TERM` varchar127: 42 distinct
`THRU_TERM_DESCRIPTION` varchar127: 42 distinct
`COURSE_OPTION` varchar127: 207 distinct, nulls=93
`COURSE_LEVEL` varchar127: "G"=477, "U"=218
`CIP_PROGRAM_CODE` varchar127: digits, 64 distinct, "142701"=42, "140501"=36, "123456"=35, "240101"=31, "141901"=27, "141001"=26, "140201"=24, "140801"=21, "141801"=20, "400601"=20
`IS_DEGREE_GRANTING` varchar31: "Y"=390, "N"=305
`DEFAULT_ULTIMATE_DEGREE` varchar127: "NDG"=292, "SM"=129, "SB"=114, "DOC"=99, "MNG"=24, "MBA"=7, "MF"=6, "MAP"=4, "MD"=3, "HA"=2, "DDM"=1, "MA"=1, "MBN"=1, "MCP"=1, nulls=11
`GRADAUTE_LEVEL` varchar127: "Masters"=179, "Doctoral"=106, nulls=410
`GRADUATE_LEVEL` varchar127: "Masters"=179, "Doctoral"=106, nulls=410
`LAST_ACTIVITY_DATE` varchar255: 139 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=695

indexes: `CIP_PROGRAM_CODE`, `COURSE`, `DEPARTMENT`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SIS_COURSE_DESCRIPTION_KEY | WCD::U | 22:TP:G | 8::U |
| COURSE | WCD | 22 TP | 8 |
| COURSE_DESCRIPTION | Wellesley Coll Dbl Degree Prog | Nuclear Eng - SM Tech & Policy | Physics |
| COURSE_DESCRIPTION_LONG | null | Nuclear Engineering (Technology and Policy Program) | Physics (Course 8) |
| DEPARTMENT | WCD | 22 | 8 |
| DEPARTMENT_NAME | Wellesley Double Degree Prog | Nuclear Engineering | Physics |
| DEPT_NAME_IN_COMMENCEMENT_BK | null | Department of Nuclear Science and Engineering | Department of Physics |
| SCHOOL_NAME | MIT, academic | Engineering | Science |
| SCHOOL_NAME_IN_COMMENCEMENT_BK | null | School of Engineering | School of Science |
| FROM_TERM | 000000 | 000000 | 000000 |
| FROM_TERM_DESCRIPTION | Beginning of Time | Beginning of Time | Beginning of Time |
| THRU_TERM | 999999 | 2004FA | 999999 |
| THRU_TERM_DESCRIPTION | End of Time | Fall Term 2003-2004 | End of Time |
| COURSE_OPTION | null | TP | null |
| COURSE_LEVEL | U | G | U |
| CIP_PROGRAM_CODE | 123456 | 142301 | 400801 |
| IS_DEGREE_GRANTING | N | Y | Y |
| DEFAULT_ULTIMATE_DEGREE | NDG | SM | SB |
| GRADAUTE_LEVEL | null | Masters | null |
| GRADUATE_LEVEL | null | Masters | null |
| LAST_ACTIVITY_DATE | 29-OCT-94 | 19-MAR-04 | 12-MAY-20 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `sis_department`  (rows=128)

columns:
`DEPARTMENT_CODE` varchar127: all distinct, nulls=1
`DEPARTMENT_NAME` varchar127: 124 distinct
`DEPARTMENT_FULL_NAME` varchar127: all distinct
`SCHOOL_CODE` varchar127: "Y"=29, "E"=25, "H"=20, "Z"=16, "X"=13, "S"=9, "A"=5, "M"=5, "T"=3, "W"=2, nulls=1
`SCHOOL_NAME` varchar127: "MIT, academic"=29, "Engineering"=25, "Hum, Arts & Social Sciences"=20, "Non-MIT"=16, "MIT, non-academic"=13, "Science"=9, "Architecture and Planning"=5, "Sloan School of Management"=5, "Whitaker Coll of HST;  HST"=3, "Schwarzman Coll of Comp"=2, "Not Available"=1
`DEPT_BUDGET_CODE` varchar127: digits, 59 distinct, nulls=39
`IS_DEGREE_GRANTING` varchar127: "Y"=69, "N"=59
`DEPT_NAME_IN_COMMENCEMENT_BK` varchar127: 52 distinct, nulls=72
`SCHOOL_NAME_IN_COMMENCEMENT_BK` varchar127: "School of Engineering"=25, "School of Humanities, Arts, and Social Sciences"=20, "School of Science"=9, "School of Architecture and Planning"=5, "Sloan School of Management"=5, "Whitaker College of Health Sciences and Technology"=3, "Schwarzman College of Computing"=2, nulls=59
`DEPARTMENT_NAME_HISTORY` varchar127: "Anthropol/Archaeol until 1998-99"=1, "associated with school of engineering through 5th week of 1998SP"=1, "Civil Eng (    )"=1, "Computational Design and Optimization"=1, "For Lang & Lit"=1, "formerly ARC"=1, "formerly UAAO"=1, "Music and Theater Arts"=1, "was Applied Biological Engineering"=1, "was BEH"=1, "was CAES"=1, "Was in Sch of Eng until 12/31/2019"=1, "was TOX"=1, nulls=115
`DEPARTMENT_LAST_ACTIVITY_DATE` varchar255: 70 distinct, nulls=1
`DLC_KEY` varchar127: 71 distinct, nulls=6
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=128

indexes: `DEPARTMENT_CODE`, `SCHOOL_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| DEPARTMENT_CODE | ZZZZ | ZNIW | NIR |
| DEPARTMENT_NAME | Dummy to get sorts | Wellesley dummy to get sorts | Brandeis Cross-Enroll Prog |
| DEPARTMENT_FULL_NAME | ZZZZ-Dummy to get sorts | ZNIW-Wellesley dummy to get sorts | NIR-Brandeis Cross-Enroll Prog |
| SCHOOL_CODE | Y | Z | Z |
| SCHOOL_NAME | MIT, academic | Non-MIT | Non-MIT |
| DEPT_BUDGET_CODE | null | null | null |
| IS_DEGREE_GRANTING | N | N | N |
| DEPT_NAME_IN_COMMENCEMENT_BK | null | null | null |
| SCHOOL_NAME_IN_COMMENCEMENT_BK | null | null | null |
| DEPARTMENT_NAME_HISTORY | null | null | null |
| DEPARTMENT_LAST_ACTIVITY_DATE | 13-APR-95 | 22-JAN-95 | 08-FEB-94 |
| DLC_KEY | D_UNDEF | D_CROSS_REG | D_CROSS_REG |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `sis_lookup`  (rows=67)

columns:
`LOOKUP_TYPE` varchar127: "Registration Status"=23, "Enrollment Status"=21, "Load Level"=8, "Registration Group"=8, "Registration Type"=4, "HGN"=3
`CODE` varchar127: 55 distinct, nulls=2
`DESCRIPTION` varchar127: 62 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=67

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| LOOKUP_TYPE | Registration Type | Registration Status | Registration Status |
| CODE | X | NE | DE |
| DESCRIPTION | Cross-Registered | Dropped on Reg Day, No Tuition | Dropped Early, Not recorded |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `sis_subject_code`  (rows=221)

columns:
`COURSE_NUMBER` varchar127: all distinct
`SUBJECT_CODE` varchar127: all distinct
`SUBJECT_CODE_DESC` varchar127: 184 distinct, nulls=4
`DEPARTMENT_CODE` varchar127: 61 distinct, nulls=31, "NIW"=53, "NIA"=44, "NIH"=21, "NIB"=6, "12"=2, "18"=2, "21"=2, "21F"=2, "BE"=2, "CSE"=2
`DEPARTMENT_NAME` varchar127: 59 distinct, nulls=37
`SCHOOL_CODE` varchar127: "Z"=122, "E"=20, "H"=17, "S"=8, "Y"=7, "A"=4, "W"=3, "M"=2, "T"=1, nulls=37
`SCHOOL_NAME` varchar127: "Non-MIT"=122, "Engineering"=20, "Hum, Arts & Social Sciences"=17, "Science"=8, "MIT, academic"=7, "Architecture and Planning"=4, "Schwarzman Coll of Comp"=3, "Sloan School of Management"=2, "Whitaker Coll of HST;  HST"=1, nulls=37
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=221

indexes: `COURSE_NUMBER`, `DEPARTMENT_CODE`, `SCHOOL_CODE`, `SUBJECT_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| COURSE_NUMBER | WWS | 25 | WWS |
| SUBJECT_CODE | WWS | 25 | WWS |
| SUBJECT_CODE_DESC | Wellesley, Women's and Gender | Interdisciplinary Sci - old | Wellesley, Women's and Gender |
| DEPARTMENT_CODE | NIW | null | NIW |
| DEPARTMENT_NAME | Wellesley Cross-Enrollment Pro | null | Wellesley Cross-Enrollment Pro |
| SCHOOL_CODE | Z | null | Z |
| SCHOOL_NAME | Non-MIT | null | Non-MIT |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `sis_term_address_category`  (rows=112)

columns:
`TERM_ADDRESS_CATEGORY_CODE` varchar127: all distinct
`TERM_ADDRESS_CATEGORY` varchar127: 101 distinct
`LIVING_GROUP_TYPE` varchar127: "D"=43, "F"=40, "S"=12, "I"=7, "O"=1, nulls=9
`LIVING_GROUP_TYPE_DESC` varchar127: "Dormitory"=43, "Fraternity"=40, "Sorority"=12, "Unknown"=9, "ILG"=7, "Off Campus"=1
`VALID_FROM_DATE` varchar255: 41 distinct, nulls=1
`VALID_THRU_DATE` varchar255: "01-JAN-15"=8, "01-JAN-94"=6, "01-JUN-10"=1, "02-JUL-08"=1, "07-SEP-98"=1, nulls=95
`LAST_ACTIVITY_DATE` varchar255: 49 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=112

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TERM_ADDRESS_CATEGORY_CODE | ZP | WOR | WGF |
| TERM_ADDRESS_CATEGORY | Zeta Psi | Worthington Place | Westgate Lowrise |
| LIVING_GROUP_TYPE | F | D | D |
| LIVING_GROUP_TYPE_DESC | Fraternity | Dormitory | Dormitory |
| VALID_FROM_DATE | 17-FEB-94 | 25-JUN-98 | 13-SEP-95 |
| VALID_THRU_DATE | null | null | null |
| LAST_ACTIVITY_DATE | 22-FEB-94 | 26-AUG-98 | 14-SEP-95 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `space_detail`  (rows=10000)

columns:
`BUILDING_KEY` varchar127: digits, 29 distinct, "32"=1319, "36"=624, "13"=578, "10"=571, "3"=547, "18"=529, "4"=503, "14"=491, "37"=415, "1"=406
`FLOOR_KEY` varchar127: bool-like, 27 distinct, "2"=1847, "3"=1723, "1"=1507, "0"=1396, "4"=1223, "5"=725, "6"=371, "7"=181, "8"=138, "G5"=88
`SPACE_UNIT_KEY` varchar127: digits, 66 distinct, nulls=3, "591000"=3551, "65000"=575, "267000"=561, "67900"=521, "152000"=462, "417500"=378, "61000"=359, "271000"=237, "60600"=192, "446700"=185
`SPACE_USAGE_KEY` int: 61 distinct, 1..87, 54=2595, 55=810, 69=785, 36=688, 85=640, 77=485, 71=473, 24=429, 17=397, 25=329
`BUILDING_ROOM` varchar127: 9332 distinct
`BUILDING_ROOM_NAME` varchar127: 9331 distinct
`ROOM_NUMBER` varchar127: 949 distinct
`ROOM_SQUARE_FOOTAGE` int: 1306 distinct, 1..108475, avg=305.0452, median=147
`ROOM_COUNTER` int: 1=10000
`BUILDING_COMPONENT` varchar127: digits, 34 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: `BUILDING_KEY`, `FLOOR_KEY`, `SPACE_UNIT_KEY`, `SPACE_USAGE_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| BUILDING_KEY | 45 | 32 | 2 |
| FLOOR_KEY | 3 | D8 | 1 |
| SPACE_UNIT_KEY | 401930 | 94000 | 152000 |
| SPACE_USAGE_KEY | 55 | 54 | 69 |
| BUILDING_ROOM | 45-398 | 32-D821D | 2-136B |
| BUILDING_ROOM_NAME | 45-398 | 32-D821D | 2-136B |
| ROOM_NUMBER | 98 | 21D | 36B |
| ROOM_SQUARE_FOOTAGE | 13 | 304 | 1229 |
| ROOM_COUNTER | 1 | 1 | 1 |
| BUILDING_COMPONENT | 45 | 32 | 2 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `space_floor`  (rows=49)

columns:
`FLOOR_KEY` varchar127: all distinct
`FLOOR` varchar127: all distinct
`FLOOR_NAME` varchar127: all distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=49

indexes: `FLOOR_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FLOOR_KEY | G9 | 13 | D5 |
| FLOOR | G9 | 13 | D5 |
| FLOOR_NAME | G9 Floor | 13 Floor | D5 Floor |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `space_supervisor_usage`  (rows=2135)

columns:
`MIT_ID` varchar127: digits, unique identifier
`DEPT_COUNT` int: 1=2020, 2=100, 3=13, 4=2, 1..4
`DEPT_NAMES` varchar127: 135 distinct, "D_RESDEV"=188, "D_LIBRARIES"=137, "D_SLOAN"=114, "D_ALUM"=103, "D_LFEE"=97, "D_DUSP"=94, "D_CMS"=92, "D_ECO"=85, "D_MECHE"=84, "D_ARCH"=80
`NUM_OF_SUPERVISEES` int: 51 distinct, 1..121, avg=3.7742, median=1
`SQFT` float: 909 distinct, 0..215723, avg=1834.72, median=159
`RESEARCH_VOLUME` float: 651 distinct, -832234..9.5e+06, avg=305837, median=0
`SQFT_PER_SUPERVISEE` float: 598 distinct, 0..215723, avg=717.312, median=129
`SQFT_PER_RES_VOL` float: 0=2132, -18=1, 1=1, 5=1, -18..5
`RES_VOL_PER_SQFT` float: 538 distinct, -723..41497, avg=313.083, median=0

indexes: `DEPT_NAMES`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MIT_ID | 999874431 | 906415283 | 967123629 |
| DEPT_COUNT | 1 | 1 | 1 |
| DEPT_NAMES | D_MECHE | D_RESDEV | D_EAPS |
| NUM_OF_SUPERVISEES | 3 | 1 | 7 |
| SQFT | 300 | 63 | 680 |
| RESEARCH_VOLUME | 98518.3 | 0 | 1e+06 |
| SQFT_PER_SUPERVISEE | 100 | 63 | 97 |
| SQFT_PER_RES_VOL | 0 | 0 | 0 |
| RES_VOL_PER_SQFT | 328 | 0 | 1476 |

# `space_unit`  (rows=150)

columns:
`FCLT_ORGANIZATION_KEY` varchar127: digits, all distinct
`SPACE_UNIT_KEY` varchar127: digits, all distinct
`SPACE_UNIT_CODE` varchar127: digits, all distinct
`SPACE_UNIT` varchar127: 132 distinct, nulls=4
`DLC_KEY` varchar127: 132 distinct, nulls=4, "D_MECHE"=3, "D_RESDEV"=3, "D_ROTC"=3, "D_CMS"=2, "D_DMSE"=2, "D_FACILITIES"=2, "D_IS&T"=2, "D_LIBRARIES"=2, "D_NUCENG"=2, "D_PROVOST"=2
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=150

indexes: `DLC_KEY`, `FCLT_ORGANIZATION_KEY`, `SPACE_UNIT_CODE`, `SPACE_UNIT_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FCLT_ORGANIZATION_KEY | 287 | 259 | 178 |
| SPACE_UNIT_KEY | 391000 | 60085 | 60300 |
| SPACE_UNIT_CODE | 391000 | 60085 | 60300 |
| SPACE_UNIT | null | Terrascope | Nuclear Science and Engineering |
| DLC_KEY | null | D_TERRASCOPE | D_NUCENG |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `space_unit2`  (rows=139)

columns:
`SPACE_UNIT_KEY` varchar127: digits, 122 distinct
`SPACE_UNIT_CODE` varchar127: digits, 122 distinct
`SPACE_UNIT` varchar127: 122 distinct
`DLC_KEY` varchar127: 110 distinct, nulls=7
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=139

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SPACE_UNIT_KEY | 97500 | 68000 | 68700 |
| SPACE_UNIT_CODE | 97500 | 68000 | 68700 |
| SPACE_UNIT | C FOR INT STUDIE | NUCLEAR SCI & ENG | LAB INFO&DEC SYS |
| DLC_KEY | D_CIS | D_NUCENG | D_LIDS |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `space_usage`  (rows=88)

columns:
`SPACE_USAGE_KEY` int: all distinct, 1..88
`SPACE_USAGE` varchar127: 50 distinct, nulls=1
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=88

indexes: `SPACE_USAGE_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SPACE_USAGE_KEY | 88 | 50 | 73 |
| SPACE_USAGE | null | RESTROOM | RECEIVING AREA |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `student_degree_program`  (rows=1202)

columns:
`DEGREE_CODE` varchar127: 357 distinct
`DEGREE_DESC` varchar127: 382 distinct
`DEGREE_DESC_SHORT` varchar127: 367 distinct
`DEGREE_TYPE` varchar127: "SM"=592, "SB"=319, "PHD"=121, "SCD"=59, "ENG"=51, "MNG"=32, "MBA"=11, "MF"=6, "MAP"=5, "MCP"=3, "MA"=2, "MBN"=1
`DEGREE_TYPE_DESC` varchar127: "Master of Science"=592, "Bachelor of Science"=319, "Doctor of Philosophy"=121, "Doctor of Science"=59, "Engineer Degree"=51, "Master of Engineering"=32, "Master of Business Administration"=11, "Master of Finance"=6, "Master of Applied Science"=5, "Master of City Planning"=3, "Master of Architecture"=2, "Master of Business Analytics"=1
`DEGREE_WEIGHT` int: 3=647, 1=319, 8=180, 6=51, 5=5, 1..8
`FROM_TERM` varchar127: 79 distinct
`THRU_TERM` varchar127: 59 distinct
`DEPARTMENT` varchar127: 54 distinct
`DEPT_NAME_IN_COMMENCEMENT_BK` varchar127: 45 distinct, nulls=16
`SCHOOL_NAME_IN_COMMENCEMENT_BK` varchar127: "School of Engineering"=563, "School of Science"=293, "School of Humanities, Arts, and Social Sciences"=165, "School of Architecture and Planning"=88, "Sloan School of Management"=75, "Whitaker College of Health Sciences and Technology"=9, "Schwarzman College of Computing"=5, nulls=4
`COURSE` varchar127: 399 distinct
`COURSE_LEVEL` varchar127: "G"=883, "U"=319
`IS_DOUBLE_MAJOR` varchar127: "N"=1072, "Y"=130
`COMMENCEMENT_BK_COURSE_ROMAN` varchar127: 128 distinct
`COMMENCEMENT_BK_SEE_ALSO` varchar127: 349 distinct
`DEGREE_LAST_ACTIVITY_DATE` varchar255: 139 distinct
`COURSE_LAST_ACTIVITY_DATE` varchar255: 183 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=1202

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| DEGREE_CODE | SMWSW | EN2W | PHD |
| DEGREE_DESC | Master of Science (without specification of field, recommended Jointly by Massachusetts Institute of Technology and Woods Hole  | Mechanical Engineer Jointly by Massachusetts Institute of Technology and Woods Hole Oceanographic Institution | Doctor of Philosophy |
| DEGREE_DESC_SHORT | Master of Science (w/o spec of field, recommended Jointly by MIT-WHOI) Jointly by MIT-WHOI | Mechanical Engineer Jointly by MIT-WHOI | Doctor of Philosophy |
| DEGREE_TYPE | SM | ENG | PHD |
| DEGREE_TYPE_DESC | Master of Science | Engineer Degree | Doctor of Philosophy |
| DEGREE_WEIGHT | 3 | 6 | 8 |
| FROM_TERM | 1988SP | 000000 | 000000 |
| THRU_TERM | 999999 | 2004SU | 999999 |
| DEPARTMENT | 7 | 2 | STS |
| DEPT_NAME_IN_COMMENCEMENT_BK | Department of Biology | Department of Mechanical Engineering | Program in Science, Technology, and Society |
| SCHOOL_NAME_IN_COMMENCEMENT_BK | School of Science | School of Engineering | School of Humanities, Arts, and Social Sciences |
| COURSE | 7 WM | 2 WM | STS D |
| COURSE_LEVEL | G | G | G |
| IS_DOUBLE_MAJOR | N | N | N |
| COMMENCEMENT_BK_COURSE_ROMAN | Course VII | Course II | Course STS |
| COMMENCEMENT_BK_SEE_ALSO | S.M., Course VII | Mech. E., W.H.O.I. | Ph.D., Science, Technology, and Society |
| DEGREE_LAST_ACTIVITY_DATE | 17-MAR-10 | 12-NOV-04 | 24-SEP-93 |
| COURSE_LAST_ACTIVITY_DATE | 23-APR-94 | 23-NOV-93 | 25-OCT-94 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `student_department`  (rows=79)

columns:
`DEPARTMENT_CODE` varchar127: all distinct
`DEPARTMENT_NAME` varchar127: 78 distinct
`DEPARTMENT_FULL_NAME` varchar127: all distinct
`SCHOOL_CODE` varchar127: "E"=23, "H"=17, "Z"=14, "S"=8, "Y"=7, "A"=4, "M"=2, "T"=2, "W"=2
`SCHOOL_NAME` varchar127: "Engineering"=23, "Hum, Arts & Social Sciences"=17, "Non-MIT"=14, "Science"=8, "MIT, academic"=7, "Architecture and Planning"=4, "Schwarzman Coll of Comp"=2, "Sloan School of Management"=2, "Whitaker Coll of HST;  HST"=2

indexes: `DEPARTMENT_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| DEPARTMENT_CODE | WCD | 13 | 21W |
| DEPARTMENT_NAME | Wellesley Double Degree Prog | Ocean Engineering | Writing & Humanistic Studies |
| DEPARTMENT_FULL_NAME | WCD-Wellesley Double Degree Prog | 13-Ocean Engineering | 21W-Writing & Humanistic Studies |
| SCHOOL_CODE | Y | E | H |
| SCHOOL_NAME | MIT, academic | Engineering | Hum, Arts & Social Sciences |

# `student_ethnic_subgroup`  (rows=46)

columns:
`STUDENT_ETHNIC_SUBGROUP_KEY` varchar127: all distinct
`ETHNIC_GROUP_NAME` varchar127: "Asian"=11, "American Indian or Alaskan Native"=8, "Hispanic or Latino"=8, "Black or African American"=5, "Native Hawaiian or Other Pacific Islander"=5, "White"=4, "International (Not US Citizen or Perm. Resident)"=1, "Race(Hispanic or Latino)"=1, "Race(Other)"=1, "Race/Ethnicity Unknown"=1, "Two or More Races"=1
`ETHNIC_SUBGROUP_NAME` varchar127: 42 distinct
`ETHNIC_CODE` varchar127: "50"=11, "20"=8, "40"=8, "10"=5, "30"=5, "60"=4, "70"=1, "80"=1, "88"=1, "90"=1, "99"=1
`ETHNIC_SUBGROUP_CODE` varchar127: digits, all distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=46

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| STUDENT_ETHNIC_SUBGROUP_KEY | 99:9901 | 30:3003 | 30:3005 |
| ETHNIC_GROUP_NAME | Race/Ethnicity Unknown | Native Hawaiian or Other Pacific Islander | Native Hawaiian or Other Pacific Islander |
| ETHNIC_SUBGROUP_NAME | Race/Ethnicity Unknown | Samoa | Native Hawaiian or Other Pacific Islander |
| ETHNIC_CODE | 99 | 30 | 30 |
| ETHNIC_SUBGROUP_CODE | 9901 | 3003 | 3005 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `subject_attribute`  (rows=104)

columns:
`SUBJECT_ATTRIBUTE_CODE` varchar127: all distinct
`SUBJECT_ATTRIBUTE_TYPE` varchar127: "A"=94, "N"=10
`SUBJECT_ATTRIBUTE_SHORT_DESC` varchar127: 61 distinct, nulls=41
`SUBJECT_ATTRIBUTE_DESC` varchar127: 103 distinct
`SUBJECT_ATTRIBUTE_REPORT_DESC` varchar127: "LINKED"=2, "HD-1"=1, "HD-2"=1, "HD-3"=1, "HD-4"=1, "HD-5"=1, "HD-L"=1, "NTRN"=1, nulls=95
`LAST_ACTIVITY_DATE` varchar255: 33 distinct
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=104

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SUBJECT_ATTRIBUTE_CODE | ZY | ZHUM | 6HDR |
| SUBJECT_ATTRIBUTE_TYPE | A | A | N |
| SUBJECT_ATTRIBUTE_SHORT_DESC | null | null | null |
| SUBJECT_ATTRIBUTE_DESC | HUM-D, Anthropology/Arch | HUM-D, Generic | Course 6 header subject |
| SUBJECT_ATTRIBUTE_REPORT_DESC | null | null | null |
| LAST_ACTIVITY_DATE | 09-MAY-95 | 09-MAY-95 | 02-JAN-00 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `subject_enrollable`  (rows=10000)

columns:
`TERM_CODE` varchar127: "2012FA"=2479, "2011SP"=2414, "2012SP"=2216, "2011FA"=2169, "2013FA"=362, "2010SP"=360
`SUBJECT_ID` varchar127: 2620 distinct
`SUBJECT_TITLE` varchar127: 2682 distinct
`SUBJECT_TITLE_LONG` varchar127: 2682 distinct
`MASTER_SUBJECT_ID` varchar127: "HAA.0000"=10000
`ULT_MASTER_SUBJECT_ID` varchar127: "HAA.0000"=10000
`CLUSTER_LIST` varchar127: "HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0036, HAA.0042, HAA.0062, HAA.0071, HAA.007"=4893, "HAA.0000, HAA.0018, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0036, HAA.0042, HAA.0062, HAA.007"=2578, "HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0042, HAA.0062, HAA.0071, HAA.0074, HAA.009"=2169, "HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0029, HAA.0031, HAA.0042, HAA.0062, HAA.0071, HAA.0074, HAA.0090, HAA.0094, HAA.009"=360
`OFFER_DEPT_CODE` varchar127: "NIH"=10000
`OFFER_SCHOOL_CODE` varchar127: "Z"=10000
`SUBJECT_GROUP_ID` varchar127: "AC9102EC3F184BE9E0440003BACE90BC"=2479, "9B3417E7D7752A7CE0440003BACE90BC"=2414, "B5FFD833D4B01D04E0440003BACE90BC"=2216, "9032EF3FEA135E9FE0440003BACE90BC"=2169, "C90336067F566377E0440003BACE90BC"=362, "86CD64966C110327E0440003BACE90BC"=360
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TERM_CODE | 2013FA | 2011SP | 2011FA |
| SUBJECT_ID | HAA.9587 | HAA.3163 | HAA.8396 |
| SUBJECT_TITLE | Societies Of The World | SLAV Ea:Elem Croatian & Serb I | Eng 151:19th Century Novel |
| SUBJECT_TITLE_LONG | Societies Of The World | SLAV Ea:Elem Croatian & Serb I | Eng 151:19th Century Novel |
| MASTER_SUBJECT_ID | HAA.0000 | HAA.0000 | HAA.0000 |
| ULT_MASTER_SUBJECT_ID | HAA.0000 | HAA.0000 | HAA.0000 |
| CLUSTER_LIST | HAA.0000, HAA.0018, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0036, HAA.0042, HAA.0062, HAA.007 | HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0036, HAA.0042, HAA.0062, HAA.0071, HAA.007 | HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0042, HAA.0062, HAA.0071, HAA.0074, HAA.009 |
| OFFER_DEPT_CODE | NIH | NIH | NIH |
| OFFER_SCHOOL_CODE | Z | Z | Z |
| SUBJECT_GROUP_ID | C90336067F566377E0440003BACE90BC | 9B3417E7D7752A7CE0440003BACE90BC | 9032EF3FEA135E9FE0440003BACE90BC |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `subject_grouping`  (rows=10000)

columns:
`SUBJECT_GROUPING_KEY` varchar127: 9911 distinct
`TERM_CODE` varchar127: 127 distinct
`DEPARTMENT_CODE` varchar127: 64 distinct
`DEPARTMENT_NAME` varchar127: 61 distinct
`DEPARTMENT_FULL_NAME` varchar127: 64 distinct
`SCHOOL_NAME` varchar127: "Engineering"=3473, "Hum, Arts & Social Sciences"=2146, "Science"=1704, "Architecture and Planning"=1257, "Sloan School of Management"=839, "MIT, academic"=330, "Non-MIT"=167, "Schwarzman Coll of Comp"=63, "Whitaker Coll of HST;  HST"=16, "MIT, non-academic"=5
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SUBJECT_GROUPING_KEY | FF172E3F4BBA3CF8E0533D2F09126F27 | 86CD6495EC6F0327E0440003BACE90BC | 12037F37E50D26A4E0533D2F0912DE86 |
| TERM_CODE | 2024FA | 2003SP | 2016FA |
| DEPARTMENT_CODE | 16 | 12 | CMS |
| DEPARTMENT_NAME | Aeronautics and Astronautics | Earth, Atmos & Planetary Sci | Comparative Media Studies |
| DEPARTMENT_FULL_NAME | 16-Aeronautics and Astronautics | 12-Earth, Atmos & Planetary Sci | CMS-Comparative Media Studies |
| SCHOOL_NAME | Engineering | Science | Hum, Arts & Social Sciences |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `subject_iap_schedule`  (rows=1199)

columns:
`TERM_CODE` varchar127: "2021JA"=1199
`SUBJECT_ID` varchar127: all NULL
`SESSION_NUMBER` int: all NULL
`MEET_PLACE` varchar127: 41 distinct, nulls=116
`MEET_START_TIME` varchar127: 31 distinct, nulls=62
`MEET_END_TIME` varchar127: 42 distinct, nulls=62
`IAP_DAY` varchar127: all NULL
`IAP_DATE` varchar255: 35 distinct, nulls=69
`REMARKS` varchar127: 92 distinct, nulls=763
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=1199

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TERM_CODE | 2021JA | 2021JA | 2021JA |
| SUBJECT_ID | null | null | null |
| SESSION_NUMBER | null | null | null |
| MEET_PLACE | Zoom/Virtually | Zoom | virtual via Zoom |
| MEET_START_TIME | 1000AM | 0200PM | 0330PM |
| MEET_END_TIME | 1200PM | 0330PM | 0430PM |
| IAP_DAY | null | null | null |
| IAP_DATE | 29-JAN-21 | 19-JAN-21 | 14-JAN-21 |
| REMARKS | null | null | null |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |

# `subject_offered`  (rows=10000)

columns:
`SUBJECT_KEY` varchar127: all distinct
`SUBJECT_OFFERED_SUMMARY_KEY` varchar127: all distinct
`MASTER_SUBJECT_KEY` varchar127: 27 distinct
`COMPOSITE_SUBJECT_KEY` varchar127: 27 distinct, "HAA.00002014JA"=2069, "HAA.00002012JA"=600, "HAA.00002011JA"=501, "HAA.00002010JA"=494, "HAA.00002009JA"=489, "HAA.00002008JA"=482, "HAA.00002007JA"=346, "HAA.00002006JA"=344, "HAA.00002005JA"=342, "HAA.00002015SU"=320
`TERM_CODE` varchar127: 27 distinct, "2014JA"=2069, "2012JA"=600, "2011JA"=501, "2010JA"=494, "2009JA"=489, "2008JA"=482, "2007JA"=346, "2006JA"=344, "2005JA"=342, "2015SU"=320
`MASTER_COURSE_NUMBER` varchar127: "HAA"=10000
`MASTER_COURSE_NUMBER_SORT` varchar127: "HAA"=10000
`MASTER_COURSE_NUMBER_DESC` varchar127: "Harvard, Arts and Sciences"=10000
`MASTER_SUBJECT_ID` varchar127: "HAA.0000"=10000
`MASTER_SUBJECT_ID_SORT` varchar127: "HAA.0000"=10000
`COURSE_NUMBER` varchar127: "HAA"=10000
`COURSE_NUMBER_SORT` varchar127: "HAA"=10000
`COURSE_NUMBER_DESC` varchar127: "Harvard, Arts and Sciences"=10000
`SUBJECT_ID` varchar127: 2081 distinct, "HAA.0129"=24, "HAA.0149"=24, "HAA.0172"=24, "HAA.0173"=24, "HAA.0180"=24, "HAA.0190"=24, "HAA.0242"=24, "HAA.0247"=24, "HAA.0257"=24, "HAA.0263"=24
`SUBJECT_ID_SORT` varchar127: 2081 distinct, "HAA.0129"=24, "HAA.0149"=24, "HAA.0172"=24, "HAA.0173"=24, "HAA.0180"=24, "HAA.0190"=24, "HAA.0242"=24, "HAA.0247"=24, "HAA.0257"=24, "HAA.0263"=24
`SUBJECT_TITLE` varchar127: 2216 distinct
`SECTION_ID` varchar127: "0"=10000
`IS_MASTER_SECTION` varchar127: "Y"=10000
`IS_LECTURE_SECTION` varchar127: "N"=10000
`IS_LAB_SECTION` varchar127: "N"=10000
`IS_RECITATION_SECTION` varchar127: "N"=10000
`IS_DESIGN_SECTION` varchar127: "N"=10000
`OFFER_DEPT_CODE` varchar127: "NIH"=10000
`OFFER_DEPT_NAME` varchar127: "Harvard Cross-Enrollment Prog"=10000
`OFFER_SCHOOL_NAME` varchar127: "Non-MIT"=10000
`RESPONSIBLE_FACULTY_NAME` varchar127: all NULL
`RESPONSIBLE_FACULTY_MIT_ID` varchar127: all NULL
`MEET_TIME` varchar127: all NULL
`MEET_PLACE` varchar127: all NULL
`CLUSTER_TYPE` varchar127: "S"=10000
`CLUSTER_TYPE_DESC` varchar127: "SWE: School-Wide Electives"=10000
`CLUSTER_LIST` varchar127: "HAA.0000, HAA.0062, HAA.0074, HAA.0090, HAA.0094, HAA.0096, HAA.0104, HAA.0105, HAA.0107, HAA.0119, HAA.0120, HAA.0121, HAA.012"=5361, "HAA.0000, HAA.0023, HAA.0029, HAA.0031, HAA.0042, HAA.0062, HAA.0071, HAA.0074, HAA.0090, HAA.0094, HAA.0096, HAA.0104, HAA.010"=2566, "HAA.0000, HAA.0018, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0036, HAA.0042, HAA.0062, HAA.007"=2069, nulls=4
`HGN_CODE` varchar127: "N"=8557, "H"=1365, "G"=78
`HGN_CODE_DESC` varchar127: "Not for graduate credit"=8557, "Higher level graduate program"=1365, "Graduate program"=78
`FORM_TYPE` varchar127: all NULL
`FORM_TYPE_DESC` varchar127: all NULL
`SUBJECT_ENROLLMENT_NUMBER` int: 0=10000
`SECTION_ENROLLMENT_NUMBER` varchar127: all NULL
`CLUSTER_ENROLLMENT_NUMBER` int: 0=9996, nulls=4
`EVALUATE_THIS_SUBJECT` varchar127: "N"=10000
`IS_OSE_SUBJECT` varchar127: "N"=10000
`IS_CREATED_BY_DATA_WAREHOUSE` varchar127: "N"=10000
`SUBJECT_GROUPING_KEY` varchar127: 27 distinct, "E871D5B8C0BD4E1DE0433D2F0912F67C"=2069, "AF14BDF68B835DB5E0440003BACE90BC"=600, "92A28F1669906EE7E0440003BACE90BC"=501, "86CD649664D30327E0440003BACE90BC"=494, "86CD649652B00327E0440003BACE90BC"=489, "86CD649640AA0327E0440003BACE90BC"=482, "86CD64962F2C0327E0440003BACE90BC"=346, "86CD64961DEB0327E0440003BACE90BC"=344, "86CD64960C370327E0440003BACE90BC"=342, "11B30964B6193D46E0533D2F0912D418"=320
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000
`NUM_ENROLLED_STUDENTS` int: 0=10000
`SUBJECT_SUMMARY_KEY` varchar127: all distinct
`IS_REPEATABLE_SUBJECT` varchar127: "N"=10000

indexes: `COMPOSITE_SUBJECT_KEY`, `COURSE_NUMBER`, `HGN_CODE`, `MASTER_SUBJECT_ID`, `MASTER_SUBJECT_ID_SORT`, `MEET_PLACE`, `OFFER_DEPT_CODE`, `RESPONSIBLE_FACULTY_MIT_ID`, `SECTION_ID`, `SUBJECT_GROUPING_KEY`, `SUBJECT_ID`, `SUBJECT_ID_SORT`, `SUBJECT_OFFERED_SUMMARY_KEY`, `SUBJECT_SUMMARY_KEY`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SUBJECT_KEY | HAAS4830002014JA | HAA01730002003SU | HAA23870002009SU |
| SUBJECT_OFFERED_SUMMARY_KEY | HAA.S4832014JA | HAA.01732003SU | HAA.23872009SU |
| MASTER_SUBJECT_KEY | HAA00000002014JA | HAA00000002003SU | HAA00000002009SU |
| COMPOSITE_SUBJECT_KEY | HAA.00002014JA | HAA.00002003SU | HAA.00002009SU |
| TERM_CODE | 2014JA | 2003SU | 2009SU |
| MASTER_COURSE_NUMBER | HAA | HAA | HAA |
| MASTER_COURSE_NUMBER_SORT | HAA | HAA | HAA |
| MASTER_COURSE_NUMBER_DESC | Harvard, Arts and Sciences | Harvard, Arts and Sciences | Harvard, Arts and Sciences |
| MASTER_SUBJECT_ID | HAA.0000 | HAA.0000 | HAA.0000 |
| MASTER_SUBJECT_ID_SORT | HAA.0000 | HAA.0000 | HAA.0000 |
| COURSE_NUMBER | HAA | HAA | HAA |
| COURSE_NUMBER_SORT | HAA | HAA | HAA |
| COURSE_NUMBER_DESC | Harvard, Arts and Sciences | Harvard, Arts and Sciences | Harvard, Arts and Sciences |
| SUBJECT_ID | HAA.S483 | HAA.0173 | HAA.2387 |
| SUBJECT_ID_SORT | HAA.S483 | HAA.0173 | HAA.2387 |
| SUBJECT_TITLE | ISP 483:Intell,Command &Contrl | French 97:What's "Literature"? | Hist Of Science 281:Flat Sci |
| SECTION_ID | 0 | 0 | 0 |
| IS_MASTER_SECTION | Y | Y | Y |
| IS_LECTURE_SECTION | N | N | N |
| IS_LAB_SECTION | N | N | N |
| IS_RECITATION_SECTION | N | N | N |
| IS_DESIGN_SECTION | N | N | N |
| OFFER_DEPT_CODE | NIH | NIH | NIH |
| OFFER_DEPT_NAME | Harvard Cross-Enrollment Prog | Harvard Cross-Enrollment Prog | Harvard Cross-Enrollment Prog |
| OFFER_SCHOOL_NAME | Non-MIT | Non-MIT | Non-MIT |
| RESPONSIBLE_FACULTY_NAME | null | null | null |
| RESPONSIBLE_FACULTY_MIT_ID | null | null | null |
| MEET_TIME | null | null | null |
| MEET_PLACE | null | null | null |
| CLUSTER_TYPE | S | S | S |
| CLUSTER_TYPE_DESC | SWE: School-Wide Electives | SWE: School-Wide Electives | SWE: School-Wide Electives |
| CLUSTER_LIST | HAA.0000, HAA.0018, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0036, HAA.0042, HAA.0062, HAA.007 | HAA.0000, HAA.0062, HAA.0074, HAA.0090, HAA.0094, HAA.0096, HAA.0104, HAA.0105, HAA.0107, HAA.0119, HAA.0120, HAA.0121, HAA.012 | HAA.0000, HAA.0062, HAA.0074, HAA.0090, HAA.0094, HAA.0096, HAA.0104, HAA.0105, HAA.0107, HAA.0119, HAA.0120, HAA.0121, HAA.012 |
| HGN_CODE | H | N | N |
| HGN_CODE_DESC | Higher level graduate program | Not for graduate credit | Not for graduate credit |
| FORM_TYPE | null | null | null |
| FORM_TYPE_DESC | null | null | null |
| SUBJECT_ENROLLMENT_NUMBER | 0 | 0 | 0 |
| SECTION_ENROLLMENT_NUMBER | null | null | null |
| CLUSTER_ENROLLMENT_NUMBER | 0 | 0 | 0 |
| EVALUATE_THIS_SUBJECT | N | N | N |
| IS_OSE_SUBJECT | N | N | N |
| IS_CREATED_BY_DATA_WAREHOUSE | N | N | N |
| SUBJECT_GROUPING_KEY | E871D5B8C0BD4E1DE0433D2F0912F67C | 86CD6495F1DC0327E0440003BACE90BC | 86CD64965BDC0327E0440003BACE90BC |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| NUM_ENROLLED_STUDENTS | 0 | 0 | 0 |
| SUBJECT_SUMMARY_KEY | HAA.S4832014JA | HAA.01732003SU | HAA.23872009SU |
| IS_REPEATABLE_SUBJECT | N | N | N |

# `subject_offered_summary`  (rows=10000)

columns:
`SUBJECT_OFFERED_SUMMARY_KEY` varchar127: all distinct
`COMPOSITE_SUBJECT_KEY` varchar127: 2714 distinct, "HAA.00002016SP"=1127, "HAA.00002008FA"=382, "HAA.00002005SP"=183, "HAA.00002021SP"=141, "HAA.00002001SP"=133, "HAA.00002006JA"=128, "HAA.00002014FA"=128, "HAA.00002025FA"=128, "HAA.00002024JA"=124, "HAK.00002017FA"=116
`TERM_CODE` varchar127: 123 distinct, "2016SP"=1272, "2008FA"=412, "2010SP"=322, "2005SP"=272, "2014FA"=253, "2015SP"=238, "2017FA"=219, "2021SP"=181, "2001SP"=179, "2012FA"=165
`COURSE_NUMBER` varchar127: digits, 110 distinct, "HAA"=3941, "HAK"=995, "HAS"=478, "HAL"=393, "HAB"=385, "HST"=222, "15"=216, "6"=190, "HAE"=186, "10"=176
`SUBJECT_ID` varchar127: 4122 distinct, "14.198"=61, "1.983"=51, "10.983"=49, "HST.220"=49, "18.704"=41, "5.941"=41, "21F.704"=39, "9.931"=38, "HST.198"=33, "15.351"=32
`SUBJECT_ID_SORT` varchar127: 4122 distinct, " 14.198"=61, "  1.983"=51, " 10.983"=49, "HST.220"=49, "  5.941"=41, " 18.704"=41, "21F.704"=39, "  9.931"=38, "HST.198"=33, " 15.351"=32
`SUBJECT_TITLE` varchar127: 4324 distinct
`MASTER_SUBJECT_ID` varchar127: 344 distinct, "HAA.0000"=3941, "HAK.0000"=995, "HAS.0000"=478, "WCL.0000"=424, "HAL.0000"=393, "HAB.0000"=385, "HAE.0000"=186, "HAV.0000"=162, "HAP.0000"=144, "MC.0000"=143
`MASTER_SUBJECT_ID_SORT` varchar127: 344 distinct, "HAA.0000"=3941, "HAK.0000"=995, "HAS.0000"=478, "WCL.0000"=424, "HAL.0000"=393, "HAB.0000"=385, "HAE.0000"=186, "HAV.0000"=162, "HAP.0000"=144, "MC.0000"=143
`CLUSTER_TYPE` varchar127: "S"=7412, "M"=320, "J"=214, nulls=2054
`CLUSTER_TYPE_DESC` varchar127: "SWE: School-Wide Electives"=7412, "Meeting Together"=320, "Joint subject"=214, nulls=2054
`CLUSTER_LIST` varchar127: 167 distinct, nulls=2447
`HGN_CODE` varchar127: "H"=4334, "N"=3228, "G"=2429, nulls=9
`HGN_CODE_DESC` varchar127: "Higher level graduate program"=4334, "Not for graduate credit"=3228, "Graduate program"=2429, nulls=9
`OFFER_DEPT_CODE` varchar127: digits, 51 distinct, "NIH"=6769, "NIW"=425, "HST"=222, "15"=216, "6"=190, "10"=176, "18"=170, "1"=166, "NIA"=154, "7"=141
`OFFER_DEPT_NAME` varchar127: 50 distinct
`OFFER_SCHOOL_NAME` varchar127: "Non-MIT"=7348, "Engineering"=1062, "Science"=595, "Hum, Arts & Social Sciences"=567, "Sloan School of Management"=216, "Architecture and Planning"=150, "MIT, academic"=57, "Schwarzman Coll of Comp"=4, "Whitaker Coll of HST;  HST"=1
`RESPONSIBLE_FACULTY_NAME` varchar127: 378 distinct, nulls=7085
`RESPONSIBLE_FACULTY_MIT_ID` varchar127: digits, 379 distinct, nulls=7082, "924187164"=1127, "925785734"=50, "975528017"=49, "908856167"=41, "923563486"=34, "921776364"=33, "993771431"=29, "996047327"=24, "954442829"=23, "908785924"=22
`TOTAL_UNITS` int: 12=6353, 1=1691, 6=1053, 3=258, 9=241, 15=226, 4=103, 21=26, 24=19, 7=6, 8=5, 18=5, 0=2, 2=2, 5=1, nulls=9, 0..24
`LECTURE_UNITS` int: 0=6983, 3=1479, 12=454, 2=427, 4=292, 5=138, 1=115, 6=101, 9=1, 24=1, nulls=9, 0..24
`LAB_UNITS` int: 12=4360, 0=2743, 1=1723, 6=637, 3=256, 15=137, 2=52, 4=32, 21=24, 24=14, 8=10, 9=3, nulls=9, 0..24
`PREPARATION_UNITS` int: 0=7513, 9=1026, 6=297, 7=255, 8=241, 2=180, 3=177, 4=145, 1=69, 5=44, 10=40, 18=3, 12=1, nulls=9, 0..18
`SUBJECT_ENROLLMENT_NUMBER` int: 132 distinct, 0..432, avg=5.1891, median=0
`CLUSTER_ENROLLMENT_NUMBER` int: 132 distinct, nulls=2447, 0..347, avg=100.6145, median=63
`WAREHOUSE_LOAD_DATE` varchar255: "19-DEC-24"=10000
`NUM_ENROLLED_STUDENTS` int: 132 distinct, 0..432, avg=5.1891, median=0
`SUBJECT_GROUPING_KEY` varchar127: 2772 distinct, "2AD92B880EB05126E0533D2F091264FF"=1127, "86CD64963ED50327E0440003BACE90BC"=382, "86CD649613A00327E0440003BACE90BC"=183, "BBC01E827FC75A21E0533D2F09120FAD"=141, "86CD6495CE930327E0440003BACE90BC"=133, "251F996A453F1D15E0633D2F09122C4D"=128, "86CD64961DEB0327E0440003BACE90BC"=128, "E5B1C00BAA4A5F15E0433D2F091291A0"=128, "0C0F40D889D42621E0633D2F09124DFF"=124, "3C9AAD041F3B3256E0533D2F0912B0C5"=116
`SUBJECT_SUMMARY_KEY` varchar127: all distinct

indexes: `COMPOSITE_SUBJECT_KEY`, `COURSE_NUMBER`, `HGN_CODE`, `MASTER_SUBJECT_ID`, `MASTER_SUBJECT_ID_SORT`, `OFFER_DEPT_CODE`, `RESPONSIBLE_FACULTY_MIT_ID`, `SUBJECT_GROUPING_KEY`, `SUBJECT_ID`, `SUBJECT_ID_SORT`, `SUBJECT_OFFERED_SUMMARY_KEY`, `SUBJECT_SUMMARY_KEY`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SUBJECT_OFFERED_SUMMARY_KEY | WSP.3502016FA | HAK.A2002005FA | HAA.98552016SP |
| COMPOSITE_SUBJECT_KEY | WCL.00002016FA | HAK.00002005FA | HAA.00002016SP |
| TERM_CODE | 2016FA | 2005FA | 2016SP |
| COURSE_NUMBER | WSP | HAK | HAA |
| SUBJECT_ID | WSP.350 | HAK.A200 | HAA.9855 |
| SUBJECT_ID_SORT | WSP.350 | HAK.A200 | HAA.9855 |
| SUBJECT_TITLE | Research/Individual St | Empirical Analy For Managers | Supervised Reading and Res |
| MASTER_SUBJECT_ID | WCL.0000 | HAK.0000 | HAA.0000 |
| MASTER_SUBJECT_ID_SORT | WCL.0000 | HAK.0000 | HAA.0000 |
| CLUSTER_TYPE | S | S | S |
| CLUSTER_TYPE_DESC | SWE: School-Wide Electives | SWE: School-Wide Electives | SWE: School-Wide Electives |
| CLUSTER_LIST | WAF.225, WAF.307, WAF.319, WAN.212, WAR.100, WAR.105, WAR.108, WAR.165, WAR.203, WAR.204, WAR.208, WAR.209, WAR.211, WAR.212, W | HAK.0000, HAK.0199, HAK.115, HAK.262M, HAK.A101, HAK.A102, HAK.A111, HAK.A112, HAK.A120, HAK.A122, HAK.A125, HAK.A126, HAK.A128 | HAA.0000, HAA.0018, HAA.0021, HAA.0023, HAA.0025, HAA.0026, HAA.0029, HAA.0031, HAA.0033, HAA.0035, HAA.0036, HAA.0042, HAA.006 |
| HGN_CODE | N | H | N |
| HGN_CODE_DESC | Not for graduate credit | Higher level graduate program | Not for graduate credit |
| OFFER_DEPT_CODE | NIW | NIH | NIH |
| OFFER_DEPT_NAME | Wellesley Cross-Enrollment Pro | Harvard Cross-Enrollment Prog | Harvard Cross-Enrollment Prog |
| OFFER_SCHOOL_NAME | Non-MIT | Non-MIT | Non-MIT |
| RESPONSIBLE_FACULTY_NAME | null | null | Downs, Francesco |
| RESPONSIBLE_FACULTY_MIT_ID | null | null | 924187164 |
| TOTAL_UNITS | 12 | 12 | 12 |
| LECTURE_UNITS | 3 | 0 | 0 |
| LAB_UNITS | 0 | 12 | 12 |
| PREPARATION_UNITS | 9 | 0 | 0 |
| SUBJECT_ENROLLMENT_NUMBER | 0 | 0 | 0 |
| CLUSTER_ENROLLMENT_NUMBER | 1 | 49 | 190 |
| WAREHOUSE_LOAD_DATE | 19-DEC-24 | 19-DEC-24 | 19-DEC-24 |
| NUM_ENROLLED_STUDENTS | 0 | 0 | 0 |
| SUBJECT_GROUPING_KEY | 20F1A4BCA3D94237E0533D2F09122E56 | 86CD64960AAE0327E0440003BACE90BC | 2AD92B880EB05126E0533D2F091264FF |
| SUBJECT_SUMMARY_KEY | WSP.3502016FA | HAK.A2002005FA | HAA.98552016SP |

# `subject_summary`  (rows=10000)

columns:
`SUBJECT_SUMMARY_KEY` varchar127: all distinct
`TERM_CODE` varchar127: 120 distinct, "2009SP"=2406, "2010FA"=2314, "2005FA"=1912, "2015SP"=473, "2008FA"=265, "1997SP"=126, "2002FA"=102, "2021SP"=69, "2017FA"=62, "2012SP"=58
`SUBJECT_ID` varchar127: 5251 distinct, "10.85"=5, "12.URN"=5, "14.URG"=5, "17.THG"=5, "17.URW"=5, "18.03"=5, "18.UR"=5, "21M.445"=5, "4.182"=5, "4.566"=5
`SUBJECT_ID_SORT` varchar127: 5251 distinct, "  4.182"=5, "  4.566"=5, "  7.URG"=5, "  8.THG"=5, " 10.85"=5, " 12.URN"=5, " 14.URG"=5, " 17.THG"=5, " 17.URW"=5, " 18.03"=5
`SUBJECT_TITLE` varchar127: 4871 distinct
`SUBJECT_OR_CLUSTER` varchar127: 1764 distinct
`MASTER_SUBJECT_ID` varchar127: 1729 distinct, "HAA.0000"=6501, "HAL.0000"=285, "HAB.0000"=220, "HAE.0000"=201, "HAS.0000"=90, "2.EPW"=16, "10.01"=14, "15.792"=10, "2.EPE"=10, "20.309"=9
`MASTER_SUBJECT_ID_SORT` varchar127: 1737 distinct, nulls=40, "HAA.0000"=6486, "HAL.0000"=283, "HAB.0000"=219, "HAE.0000"=200, "HAS.0000"=86, "  2.EPW"=16, " 10.01"=14, "  2.EPE"=10, " 15.792"=10, " 20.309"=9
`ULT_MASTER_SUBJECT_ID` varchar127: 1726 distinct, nulls=40
`CLUSTER_TYPE` varchar127: "S"=7360, "J"=442, "M"=306, " "=4, nulls=1888
`CLUSTER_TYPE_DESC` varchar127: "SWE: School-Wide Electives"=7360, "Joint subject"=442, "Meeting Together"=306, nulls=1892
`CLUSTER_LIST` varchar127: 299 distinct, nulls=1923
`DEPARTMENT_CODE` varchar127: 58 distinct
`DEPARTMENT_NAME` varchar127: 55 distinct
`SCHOOL_CODE` varchar127: "Z"=7313, "E"=915, "H"=593, "S"=443, "A"=327, "M"=216, "Y"=81, "T"=60, "W"=8, "X"=2, nulls=42
`SCHOOL_NAME` varchar127: "Non-MIT"=7311, "Engineering"=975, "Hum, Arts & Social Sciences"=604, "Science"=454, "Architecture and Planning"=332, "Sloan School of Management"=220, "MIT, academic"=84, "Schwarzman Coll of Comp"=18, "MIT, non-academic"=1, "Whitaker Coll of HST;  HST"=1
`TOTAL_UNITS` int: 22 distinct, nulls=40, 1..60, avg=9.2713, median=12
`LECTURE_UNITS` int: 0=7885, 3=1251, 2=313, 4=299, 5=85, 1=82, 12=23, 6=19, 9=2, 24=1, nulls=40, 0..24
`LAB_UNITS` int: 22 distinct, nulls=40, 0..60, avg=7.1562, median=12
`PREP_UNITS` int: 0=7887, 9=875, 8=282, 6=235, 4=211, 7=126, 3=117, 2=82, 5=71, 1=40, 10=26, 12=3, 18=3, 11=1, 14=1, nulls=40, 0..18
`DESIGN_UNITS` int: 0=9947, 6=5, 4=3, 12=2, nulls=43, 0..12
`SUBJECT_ENROLLMENT_NUMBER` int: 173 distinct, 0..629, avg=5.9737, median=0
`CLUSTER_ENROLLMENT_NUMBER` int: 86 distinct, nulls=1923, 0..431, avg=168.2396, median=192
`SUBJECT_GROUP_ID` varchar127: 2261 distinct
`SUBJECT_ENROLLMENT_FIRST_WEEK` int: 191 distinct, 0..664, avg=6.8185, median=0
`CLUSTER_ENROLLMENT_FIRST_WEEK` int: 198 distinct, 0..664, avg=163.1469, median=220
`SUBJECT_ENROLLMENT_FIFTH_WEEK` int: 183 distinct, 0..647, avg=6.2958, median=0
`CLUSTER_ENROLLMENT_FIFTH_WEEK` int: 187 distinct, 0..647, avg=156.2529, median=210
`SUBJECT_ENROLLMENT_CREDIT` int: 175 distinct, 0..629, avg=5.6488, median=0
`SUBJECT_ENROLLMENT_LISTEN` int: 34 distinct, 0..121, avg=0.3249, median=0
`CLUSTER_ENROLLMENT_CREDIT` int: 178 distinct, 0..629, avg=133.3645, median=179
`CLUSTER_ENROLLMENT_LISTEN` int: 36 distinct, 0..121, avg=7.4484, median=7
`SUBJECT_ENROLLMENT_1ST_CREDIT` int: 191 distinct, 0..664, avg=6.4936, median=0
`SUBJECT_ENROLLMENT_1ST_LISTEN` int: 34 distinct, 0..121, avg=0.3249, median=0
`CLUSTER_ENROLLMENT_1ST_CREDIT` int: 193 distinct, 0..664, avg=155.6985, median=207
`CLUSTER_ENROLLMENT_1ST_LISTEN` int: 36 distinct, 0..121, avg=7.4484, median=7
`SUBJECT_ENROLLMENT_5TH_CREDIT` int: 178 distinct, 0..647, avg=5.9709, median=0
`SUBJECT_ENROLLMENT_5TH_LISTEN` int: 34 distinct, 0..121, avg=0.3249, median=0
`CLUSTER_ENROLLMENT_5TH_CREDIT` int: 179 distinct, 0..647, avg=148.8045, median=197
`CLUSTER_ENROLLMENT_5TH_LISTEN` int: 36 distinct, 0..121, avg=7.4484, median=7
`WAREHOUSE_LOAD_DATE` varchar255: "20-DEC-24"=10000

indexes: `MASTER_SUBJECT_ID`, `MASTER_SUBJECT_ID_SORT`, `SUBJECT_ID`, `SUBJECT_ID_SORT`, `SUBJECT_SUMMARY_KEY`, `TERM_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| SUBJECT_SUMMARY_KEY | WGS.6452019SP | HAA.23682010FA | HAA.99552005FA |
| TERM_CODE | 2019SP | 2010FA | 2005FA |
| SUBJECT_ID | WGS.645 | HAA.2368 | HAA.9955 |
| SUBJECT_ID_SORT | WGS.645 | HAA.2368 | HAA.9955 |
| SUBJECT_TITLE | Feminist Theory | Math 262:Modular Forms | Gov 90eo:Amer Foreign Econ Pol |
| SUBJECT_OR_CLUSTER | WGS.645 | HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0029, HAA.0031, HAA.0042, HAA.0062, HAA.0071, HAA.0074, HAA.0090, HAA.0094, HAA.009 | HAA.0000, HAA.0062, HAA.0074, HAA.0090, HAA.0094, HAA.0096, HAA.0104, HAA.0105, HAA.0107, HAA.0119, HAA.0120, HAA.0121, HAA.012 |
| MASTER_SUBJECT_ID | WGS.645 | HAA.0000 | HAA.0000 |
| MASTER_SUBJECT_ID_SORT | WGS.645 | HAA.0000 | HAA.0000 |
| ULT_MASTER_SUBJECT_ID | WGS.645 | HAA.0000 | HAA.0000 |
| CLUSTER_TYPE | null | S | S |
| CLUSTER_TYPE_DESC | null | SWE: School-Wide Electives | SWE: School-Wide Electives |
| CLUSTER_LIST | null | HAA.0000, HAA.0021, HAA.0023, HAA.0025, HAA.0029, HAA.0031, HAA.0042, HAA.0062, HAA.0071, HAA.0074, HAA.0090, HAA.0094, HAA.009 | HAA.0000, HAA.0062, HAA.0074, HAA.0090, HAA.0094, HAA.0096, HAA.0104, HAA.0105, HAA.0107, HAA.0119, HAA.0120, HAA.0121, HAA.012 |
| DEPARTMENT_CODE | WGS | NIH | NIH |
| DEPARTMENT_NAME | Women's and Gender Studies | Harvard Cross-Enrollment Prog | Harvard Cross-Enrollment Prog |
| SCHOOL_CODE | H | Z | Z |
| SCHOOL_NAME | Hum, Arts & Social Sciences | Non-MIT | Non-MIT |
| TOTAL_UNITS | 12 | 12 | 12 |
| LECTURE_UNITS | 3 | 0 | 0 |
| LAB_UNITS | 0 | 12 | 12 |
| PREP_UNITS | 9 | 0 | 0 |
| DESIGN_UNITS | 0 | 0 | 0 |
| SUBJECT_ENROLLMENT_NUMBER | 1 | 0 | 0 |
| CLUSTER_ENROLLMENT_NUMBER | null | 186 | 235 |
| SUBJECT_GROUP_ID | 787B7F9A984B6870E0533D2F091209C6 | 86CD649663200327E0440003BACE90BC | 86CD64960AA70327E0440003BACE90BC |
| SUBJECT_ENROLLMENT_FIRST_WEEK | 1 | 0 | 0 |
| CLUSTER_ENROLLMENT_FIRST_WEEK | 1 | 226 | 264 |
| SUBJECT_ENROLLMENT_FIFTH_WEEK | 1 | 0 | 0 |
| CLUSTER_ENROLLMENT_FIFTH_WEEK | 1 | 211 | 262 |
| SUBJECT_ENROLLMENT_CREDIT | 1 | 0 | 0 |
| SUBJECT_ENROLLMENT_LISTEN | 0 | 0 | 0 |
| CLUSTER_ENROLLMENT_CREDIT | 1 | 179 | 223 |
| CLUSTER_ENROLLMENT_LISTEN | 0 | 7 | 12 |
| SUBJECT_ENROLLMENT_1ST_CREDIT | 1 | 0 | 0 |
| SUBJECT_ENROLLMENT_1ST_LISTEN | 0 | 0 | 0 |
| CLUSTER_ENROLLMENT_1ST_CREDIT | 1 | 219 | 252 |
| CLUSTER_ENROLLMENT_1ST_LISTEN | 0 | 7 | 12 |
| SUBJECT_ENROLLMENT_5TH_CREDIT | 1 | 0 | 0 |
| SUBJECT_ENROLLMENT_5TH_LISTEN | 0 | 0 | 0 |
| CLUSTER_ENROLLMENT_5TH_CREDIT | 1 | 204 | 250 |
| CLUSTER_ENROLLMENT_5TH_LISTEN | 0 | 7 | 12 |
| WAREHOUSE_LOAD_DATE | 20-DEC-24 | 20-DEC-24 | 20-DEC-24 |

# `time_day`  (rows=10000)

columns:
`FISCAL_PERIOD` varchar127: digits, 1026 distinct
`FISCAL_YEAR` varchar127: digits, 86 distinct
`FISCAL_PERIOD_DESCRIPTION` varchar127: 1026 distinct
`CALENDAR_PERIOD` varchar127: digits, 1026 distinct
`CALENDAR_PERIOD_DESCRIPTION` varchar127: 1026 distinct
`CALENDAR_YEAR` varchar127: digits, 86 distinct
`START_DATE` varchar255: 1026 distinct
`END_DATE` varchar255: 1026 distinct
`CALENDAR_DATE` varchar255: all distinct
`DAY_OF_WEEK` varchar127: "Wednesday"=1466, "Saturday "=1446, "Monday   "=1426, "Tuesday  "=1422, "Sunday   "=1416, "Friday   "=1412, "Thursday "=1412
`FINANCIAL_AID_YEAR` varchar127: digits, 32 distinct, nulls=6315
`FINANCIAL_AID_YEAR_DESC` varchar127: 32 distinct, nulls=6315
`ACADEMIC_YEAR` varchar127: digits, 80 distinct, nulls=1579
`ACADEMIC_TERM_CODE` varchar127: 279 distinct, nulls=2742
`ACADEMIC_TERM_DESCRIPTION` varchar127: 279 distinct, nulls=2742

indexes: `ACADEMIC_TERM_CODE`, `CALENDAR_DATE`, `FISCAL_PERIOD`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FISCAL_PERIOD | 203512 | 199709 | 195406 |
| FISCAL_YEAR | 2035 | 1997 | 1954 |
| FISCAL_PERIOD_DESCRIPTION | FY 2035 Period 12 | FY 1997 Period 9 | FY 1954 Period 6 |
| CALENDAR_PERIOD | 203506 | 199703 | 195312 |
| CALENDAR_PERIOD_DESCRIPTION | June 2035 | March 1997 | December 1953 |
| CALENDAR_YEAR | 2035 | 1997 | 1953 |
| START_DATE | 01-JUN-35 | 01-MAR-97 | 01-DEC-53 |
| END_DATE | 30-JUN-35 | 31-MAR-97 | 31-DEC-53 |
| CALENDAR_DATE | 26-JUN-35 | 04-MAR-97 | 28-DEC-53 |
| DAY_OF_WEEK | Tuesday   | Tuesday   | Monday    |
| FINANCIAL_AID_YEAR | null | 1997 | null |
| FINANCIAL_AID_YEAR_DESC | null | Aid Year 1996-97 | null |
| ACADEMIC_YEAR | null | 1997 | null |
| ACADEMIC_TERM_CODE | null | 1997SP | null |
| ACADEMIC_TERM_DESCRIPTION | null | Spring Term 1996-1997 | null |

# `time_month`  (rows=640)

columns:
`IS_CLOSING_PERIOD` varchar127: "N"=480, "Y"=160
`FISCAL_PERIOD_SELECTOR` varchar127: all distinct
`IS_CURRENT_FISCAL_YEAR` varchar127: "N"=624, "Y"=16
`TIME_MONTH_KEY` varchar127: digits, all distinct
`FISCAL_PERIOD` varchar127: digits, all distinct
`FISCAL_PERIOD_DESCRIPTION` varchar127: all distinct
`FISCAL_YEAR` varchar127: digits, 40 distinct
`FISCAL_YEAR_QUARTER` varchar127: 160 distinct
`FY_QUARTER_CODE` varchar127: 160 distinct
`CALENDAR_PERIOD` varchar127: all distinct
`CALENDAR_PERIOD_DESCRIPTION` varchar127: all distinct
`CALENDAR_YEAR` varchar127: digits, 41 distinct
`START_DATE` varchar255: 480 distinct
`END_DATE` varchar255: 480 distinct
`CALENDAR_MONTH` varchar127: "6"=200, "1"=40, "10"=40, "11"=40, "12"=40, "2"=40, "3"=40, "4"=40, "5"=40, "7"=40, "8"=40, "9"=40
`CALENDAR_MONTH_NAME` varchar127: "June"=200, "April"=40, "August"=40, "December"=40, "February"=40, "January"=40, "July"=40, "March"=40, "May"=40, "November"=40, "October"=40, "September"=40
`IS_CURRENT_FISCAL_PERIOD` varchar127: "N"=639, "Y"=1
`IS_PREVIOUS_FISCAL_PERIOD` varchar127: "N"=639, "Y"=1
`ACADEMIC_YEAR` varchar127: digits, 36 distinct, nulls=78
`ACADEMIC_TERM` varchar127: 141 distinct, nulls=78
`ACADEMIC_TERM_DESCRIPTION` varchar127: 141 distinct, nulls=78
`FINANCIAL_AID_YEAR` varchar127: digits, 30 distinct, nulls=165
`FINANCIAL_AID_YEAR_DESC` varchar127: 30 distinct, nulls=165

indexes: `FISCAL_PERIOD`, `FISCAL_YEAR`, `FY_QUARTER_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| IS_CLOSING_PERIOD | Y | N | Y |
| FISCAL_PERIOD_SELECTOR | 203516 -- June 2035 Closing | 202003 -- September 2019 | 201014 -- June 2010 Closing |
| IS_CURRENT_FISCAL_YEAR | N | N | N |
| TIME_MONTH_KEY | 203516 | 202003 | 201014 |
| FISCAL_PERIOD | 203516 | 202003 | 201014 |
| FISCAL_PERIOD_DESCRIPTION | FY 2035 closing period 4 | FY 2020 Period 3 | FY 2010 closing period 2 |
| FISCAL_YEAR | 2035 | 2020 | 2010 |
| FISCAL_YEAR_QUARTER | FY 2035 Quarter 4 | FY 2020 Quarter 1 | FY 2010 Quarter 4 |
| FY_QUARTER_CODE | FY2035Q4 | FY2020Q1 | FY2010Q4 |
| CALENDAR_PERIOD | 203506P16 | 201909 | 201006P14 |
| CALENDAR_PERIOD_DESCRIPTION | June 2035, fiscal period 16 | September 2019 | June 2010, fiscal period 14 |
| CALENDAR_YEAR | 2035 | 2019 | 2010 |
| START_DATE | 01-JUN-35 | 01-SEP-19 | 01-JUN-10 |
| END_DATE | 30-JUN-35 | 30-SEP-19 | 30-JUN-10 |
| CALENDAR_MONTH | 6 | 9 | 6 |
| CALENDAR_MONTH_NAME | June | September | June |
| IS_CURRENT_FISCAL_PERIOD | N | N | N |
| IS_PREVIOUS_FISCAL_PERIOD | N | N | N |
| ACADEMIC_YEAR | null | 2020 | 2010 |
| ACADEMIC_TERM | null | 2020FA | 2010SU |
| ACADEMIC_TERM_DESCRIPTION | null | Fall Term 2019-2020 | Summer Term 2010 |
| FINANCIAL_AID_YEAR | null | 2020 | 2011 |
| FINANCIAL_AID_YEAR_DESC | null | Aid Year 2019-2020 | Aid Year 2010-2011 |

# `time_quarter`  (rows=144)

columns:
`FISCAL_YEAR` varchar127: digits, 36 distinct
`FY_QUARTER_CODE` varchar127: all distinct
`FY_QUARTER_NAME` varchar127: all distinct
`CY_QUARTER_CODE` varchar127: all distinct
`CY_QUARTER_NAME` varchar127: all distinct
`CALENDAR_YEAR` varchar127: digits, 37 distinct
`QUARTER_START_DATE` varchar255: all distinct
`QUARTER_END_DATE` varchar255: all distinct
`QUARTER_START_FP` varchar127: digits, all distinct
`QUARTER_END_FP` varchar127: digits, all distinct
`QUARTER_CERT_OPEN` varchar255: all distinct
`QUARTER_CERT_EXPECTED` varchar255: all distinct
`QUARTER_CERT_DUE` varchar255: all distinct
`IS_CURRENT_QUARTER` varchar127: "N"=143, "Y"=1
`IS_NEXT_QUARTER` varchar127: "N"=144
`IS_PREVIOUS_QUARTER` varchar127: "N"=144
`IS_PAST_QUARTER` varchar127: "Y"=101, "N"=43
`IS_FUTURE_QUARTER` varchar127: "N"=102, "Y"=42
`PAYROLL_EDACCA_CERT_SCHED_KEY` varchar127: digits, all distinct
`WAREHOUSE_LOAD_DATE` varchar255: "20-DEC-24"=144

indexes: `FISCAL_YEAR`, `FY_QUARTER_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| FISCAL_YEAR | 2035 | 2024 | 2025 |
| FY_QUARTER_CODE | FY2035Q4 | FY2024Q1 | FY2025Q2 |
| FY_QUARTER_NAME | FY 2035 Quarter 4 | FY 2024 Quarter 1 | FY 2025 Quarter 2 |
| CY_QUARTER_CODE | CY2035Q2 | CY2023Q3 | CY2024Q4 |
| CY_QUARTER_NAME | CY 2035 Quarter 2 | CY 2023 Quarter 3 | CY 2024 Quarter 4 |
| CALENDAR_YEAR | 2035 | 2023 | 2024 |
| QUARTER_START_DATE | 01-APR-35 | 01-JUL-23 | 01-OCT-24 |
| QUARTER_END_DATE | 30-JUN-35 | 30-SEP-23 | 31-DEC-24 |
| QUARTER_START_FP | 203510 | 202401 | 202504 |
| QUARTER_END_FP | 203512 | 202403 | 202506 |
| QUARTER_CERT_OPEN | 01-JUL-35 | 01-OCT-23 | 01-JAN-25 |
| QUARTER_CERT_EXPECTED | 31-AUG-35 | 30-NOV-23 | 28-FEB-25 |
| QUARTER_CERT_DUE | 30-SEP-35 | 31-DEC-23 | 31-MAR-25 |
| IS_CURRENT_QUARTER | N | N | Y |
| IS_NEXT_QUARTER | N | N | N |
| IS_PREVIOUS_QUARTER | N | N | N |
| IS_PAST_QUARTER | N | Y | N |
| IS_FUTURE_QUARTER | Y | N | N |
| PAYROLL_EDACCA_CERT_SCHED_KEY | 203504 | 202401 | 202502 |
| WAREHOUSE_LOAD_DATE | 20-DEC-24 | 20-DEC-24 | 20-DEC-24 |

# `tip_detail`  (rows=10000)

columns:
`TIP_SUBJECT_OFFERED_KEY` varchar127: 7340 distinct, nulls=733, "21M2830002010SP"=22, "21M2500002010FA"=15, "21A1130002010FA"=11, "21M0510002010FA"=11, "21M3410002010FA"=11, "21M2260002010FA"=10, "0046110002010SP"=9, "HST4820002019SP"=9, "HSTS110002010FA"=9, "21M0130002010FA"=8
`TIP_MATERIAL_KEY` varchar127: 7360 distinct, "N/ACourse has no materials2024SP"=116, "N/ACourse has no materials2015FA"=111, "N/ACourse has no materials2014SP"=110, "N/ACourse has no materials2017FA"=108, "N/ACourse has no materials2013FA"=105, "N/ACourse has no materials2025FA"=102, "N/ACourse has no materials2015SP"=96, "N/ACourse has no materials2012SP"=85, "N/ACourse has no materials2017SP"=82, "N/ACourse has no materials2016SP"=80
`TIP_MATERIAL_STATUS_KEY` varchar127: "RQ"=3441, "NM"=2249, "EO"=2110, "RC"=1843, "U"=197, "PC"=62, "CL"=50, "NL"=27, "BR"=10, "NS"=6, "NB"=4, "  "=1
`TERM_CODE` varchar127: 63 distinct, nulls=164, "2013SP"=422, "2013FA"=420, "2015FA"=411, "2014FA"=409, "2017FA"=406, "2015SP"=379, "2016SP"=376, "2017SP"=372, "2012FA"=370, "2012SP"=364
`SUBJECT_ID` varchar127: 3623 distinct, "CANC.BARCHARTS"=78, "21L.003"=45, "CANC.SPO"=44, "CANC.BAR"=42, "14.781"=33, "15.401"=32, "15.402"=31, "21L.004"=30, "6.555"=30, "CANC.CHANGE"=30
`ISBN` varchar127: digits, 5128 distinct, nulls=2249
`RECORD_COUNT` int: 1=10000
`WAREHOUSE_LOAD_DATE` varchar255: "20-DEC-24"=10000

indexes: `SUBJECT_ID`, `TERM_CODE`, `TIP_MATERIAL_KEY`, `TIP_MATERIAL_STATUS_KEY`, `TIP_SUBJECT_OFFERED_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TIP_SUBJECT_OFFERED_KEY | WGSURG0002016SP | 005460002025SP | 0085910002016FA |
| TIP_MATERIAL_KEY | N/ACourse has no materials2016SP | 8220107123422EBK HIGH-RESOLUT.NMR TECH.IN ORGANIC...3RD 162025SP | 8220000513894EBK AN INTRODUCTION TO SYSTEMS BIOLOGY2016FA |
| TIP_MATERIAL_STATUS_KEY | NM | EO | EO |
| TERM_CODE | 2016SP | 2025SP | 2016FA |
| SUBJECT_ID | WGS.URG | 5.46 | 8.591 |
| ISBN | null | 8220107123422 | 8220000513894 |
| RECORD_COUNT | 1 | 1 | 1 |
| WAREHOUSE_LOAD_DATE | 20-DEC-24 | 20-DEC-24 | 20-DEC-24 |

# `tip_material`  (rows=10000)

columns:
`TIP_MATERIAL_KEY` varchar127: 9942 distinct, "0 MECHANICS OF MATERIALS-TEXT9TH 142011FA"=11, "0 MECHANICS OF MATERIALS-TEXT9TH 142011SP"=6, "0 MECHANICS OF MATERIALS-TEXT9TH 142013FA"=6, "0 MECHANICS OF MATERIALS-TEXT9TH 142014FA"=6, "0 MECHANICS OF MATERIALS-TEXT9TH 142012SP"=4, "0 MECHANICS OF MATERIALS-TEXT9TH 142013SP"=4, "0 MECHANICS OF MATERIALS-TEXT9TH 142012FA"=3, "9780132857123MICROECONOMICS8TH 13"=3, "0 MECHANICS OF MATERIALS-TEXT9TH 142014SP"=2, "0195057368 The foundations of bioethics / H. Tristram Engelhardt, Jr.Engelhardt, H. Tristram (Hugo Tristram),New York : Oxfo199"=2
`ISBN` varchar127: 6770 distinct, nulls=17
`TITLE` varchar127: 6364 distinct, nulls=1
`AUTHOR` varchar127: 5620 distinct, nulls=230
`EDITION` varchar127: 211 distinct, nulls=7061
`PUBLISHER` varchar127: 1415 distinct, nulls=142
`YEAR` varchar127: digits, 83 distinct, nulls=3259
`NEW_SHELF_PRICE` int: 360 distinct, nulls=1014, 0..694, avg=69.8617, median=44
`USED_SHELF_PRICE` int: 281 distinct, nulls=1014, 0..520, avg=40.6028, median=16
`RENTAL_NEW_PRICE` int: 213 distinct, 0..371, avg=5.7633, median=0
`RENTAL_USED_PRICE` int: 153 distinct, 0..315, avg=3.3915, median=0
`MATERIAL_INFO_SOURCE` varchar127: "ISBN"=5849, "COOP"=3151, "OTI"=1000

indexes: `TIP_MATERIAL_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TIP_MATERIAL_KEY | N/ACourse has no materials2025FA | 9781118692288DISCIPLINED ENTREPRENEURSHIP132015SP | 9781400033416BELOVED-W/NEW FOREWORD042024FA |
| ISBN | null | 9781118692288 | 9781400033416 |
| TITLE | Course Has No Materials | Disciplined Entrepreneurship: 24 Steps to a Successful Startup | Beloved: Pulitzer Prize Winner |
| AUTHOR | Course Has No Materials | Aulet, Bill | Morrison, Toni |
| EDITION | null | null | null |
| PUBLISHER | null | John Wiley & Sons, Incorporated | Knopf Doubleday Publishing Group |
| YEAR | null | 2013 | 2004 |
| NEW_SHELF_PRICE | 0 | 32 | 17 |
| USED_SHELF_PRICE | 0 | 24 | 13 |
| RENTAL_NEW_PRICE | 0 | 0 | 12 |
| RENTAL_USED_PRICE | 0 | 0 | 8 |
| MATERIAL_INFO_SOURCE | COOP | ISBN | ISBN |

# `tip_material_status`  (rows=12)

columns:
`TIP_MATERIAL_STATUS_KEY` varchar127: "  "=1, "BR"=1, "CL"=1, "EO"=1, "NB"=1, "NL"=1, "NM"=1, "NS"=1, "PC"=1, "RC"=1, "RQ"=1, "U"=1
`TIP_MATERIAL_STATUS_CODE` varchar127: "  "=1, "BR"=1, "CL"=1, "EO"=1, "NB"=1, "NL"=1, "NM"=1, "NS"=1, "PC"=1, "RC"=1, "RQ"=1, "U"=1
`TIP_MATERIAL_STATUS` varchar127: "Bookstore recommends"=1, "Course has no materials"=1, "Electronic options"=1, "Go to class first"=1, "Recommended"=1, "Required"=1, "Unknown"=1, "Val-u option"=1, nulls=4
`WAREHOUSE_LOAD_DATE` varchar255: "20-DEC-24"=12

indexes: `TIP_MATERIAL_STATUS_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TIP_MATERIAL_STATUS_KEY | U | NM | NS |
| TIP_MATERIAL_STATUS_CODE | U | NM | NS |
| TIP_MATERIAL_STATUS | Unknown | Course has no materials | null |
| WAREHOUSE_LOAD_DATE | 20-DEC-24 | 20-DEC-24 | 20-DEC-24 |

# `tip_subject_offered`  (rows=10000)

columns:
`TIP_SUBJECT_OFFERED_KEY` varchar127: all distinct
`TERM_CODE` varchar127: 126 distinct, "2019FA"=172, "2009SP"=164, "2018SP"=158, "2011FA"=154, "2020SP"=154, "2015FA"=153, "2024SP"=153, "2006SP"=151, "2025SP"=148, "2004SP"=145
`IS_NO_COURSE_MATERIAL` varchar127: "Y"=1091, "N"=980, nulls=7929
`MASTER_COURSE_NUMBER` varchar127: 58 distinct
`MASTER_COURSE_NUMBER_SORT` varchar127: 58 distinct
`MASTER_COURSE_NUMBER_DESC` varchar127: 58 distinct
`MASTER_SUBJECT_ID` varchar127: 4537 distinct, "2.EPE"=30, "2.EPW"=26, "15.792"=15, "10.THU"=12, "17.THU"=12, "9.921"=12, "14.09"=11, "15.951"=11, "2.96"=11, "20.THG"=11
`MASTER_SUBJECT_ID_SORT` varchar127: 4568 distinct, "2.EPE"=30, "2.EPW"=26, "15.792"=15, "10.THU"=12, "17.THU"=12, "9.921"=12, "14.09"=11, "2.96"=11, "20.THG"=11, "21A.THU"=11
`COURSE_NUMBER` varchar127: 58 distinct
`COURSE_NUMBER_SORT` varchar127: 58 distinct
`COURSE_NUMBER_DESC` varchar127: 58 distinct
`SUBJECT_ID` varchar127: 4974 distinct, "10.THU"=12, "17.THU"=12, "9.921"=12, "14.09"=11, "15.951"=11, "20.THG"=11, "21A.THU"=11, "5.90"=11, "7.UR"=11, "MAS.NIV"=11
`SUBJECT_ID_SORT` varchar127: 4974 distinct, "  9.921"=12, " 10.THU"=12, " 17.THU"=12, "  5.90"=11, "  7.UR"=11, " 14.09"=11, " 15.951"=11, " 20.THG"=11, "21A.THU"=11, "MAS.NIV"=11
`SUBJECT_TITLE` varchar127: 4088 distinct
`OFFER_DEPT_CODE` varchar127: digits, 62 distinct, "15"=805, "6"=693, "4"=604, "12"=446, "11"=434, "1"=412, "2"=394, "10"=372, "18"=354, "HST"=352
`OFFER_DEPT_NAME` varchar127: 59 distinct
`OFFER_SCHOOL_NAME` varchar127: "Engineering"=3536, "Hum, Arts & Social Sciences"=2233, "Science"=1725, "Architecture and Planning"=1253, "Sloan School of Management"=818, "MIT, academic"=364, "Schwarzman Coll of Comp"=51, "Whitaker Coll of HST;  HST"=16, "MIT, non-academic"=4
`RESPONSIBLE_FACULTY_NAME` varchar127: 2441 distinct, nulls=1705
`RESPONSIBLE_FACULTY_MIT_ID` varchar127: digits, 2468 distinct, nulls=1704, "920324608"=144, "983607907"=68, "916610219"=57, "931431942"=56, "949310910"=48, "925785734"=43, "974579073"=40, "964758013"=39, "912446917"=37, "901368961"=31
`NUM_ENROLLED_STUDENTS` int: 253 distinct, 0..648, avg=17.1913, median=5
`WAREHOUSE_LOAD_DATE` varchar255: "20-DEC-24"=10000

indexes: `MASTER_SUBJECT_ID`, `MASTER_SUBJECT_ID_SORT`, `OFFER_DEPT_CODE`, `RESPONSIBLE_FACULTY_MIT_ID`, `SUBJECT_ID`, `SUBJECT_ID_SORT`, `TERM_CODE`, `TIP_SUBJECT_OFFERED_KEY`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TIP_SUBJECT_OFFERED_KEY | WGSURG0002025SP | 013260001994SP | 01890110002025FA |
| TERM_CODE | 2025SP | 1994SP | 2025FA |
| IS_NO_COURSE_MATERIAL | null | null | null |
| MASTER_COURSE_NUMBER | WGS | 2 | 18 |
| MASTER_COURSE_NUMBER_SORT | WGS |   2 |  18 |
| MASTER_COURSE_NUMBER_DESC | Women's & Gender Studies | Mechanical Engineering | Mathematics |
| MASTER_SUBJECT_ID | WGS.URG | 2.601 | 18.901 |
| MASTER_SUBJECT_ID_SORT | WGS.URG | 2.601 | 18.901 |
| COURSE_NUMBER | WGS | 13 | 18 |
| COURSE_NUMBER_SORT | WGS |  13 |  18 |
| COURSE_NUMBER_DESC | Women's & Gender Studies | Ocean Engineering | Mathematics |
| SUBJECT_ID | WGS.URG | 13.26 | 18.9011 |
| SUBJECT_ID_SORT | WGS.URG |  13.26 |  18.9011 |
| SUBJECT_TITLE | Undergraduate Research | Design:Therm Power Syst | Introduction to Topology |
| OFFER_DEPT_CODE | WGS | 13 | 18 |
| OFFER_DEPT_NAME | Women's and Gender Studies | Ocean Engineering | Mathematics |
| OFFER_SCHOOL_NAME | Hum, Arts & Social Sciences | Engineering | Science |
| RESPONSIBLE_FACULTY_NAME | Kirby, Barney | null | Mccarty, Abigail |
| RESPONSIBLE_FACULTY_MIT_ID | 934724720 | null | 941875869 |
| NUM_ENROLLED_STUDENTS | 0 | 0 | 1 |
| WAREHOUSE_LOAD_DATE | 20-DEC-24 | 20-DEC-24 | 20-DEC-24 |

# `top_level_domain`  (rows=249)

columns:
`TOP_LEVEL_DOMAIN_KEY` varchar127: all distinct, nulls=1
`TOP_LEVEL_DOMAIN` varchar127: all distinct, nulls=1
`TOP_LEVEL_DOMAIN_DESCRIPTION` varchar127: all distinct
`WAREHOUSE_LOAD_DATE` varchar255: "17-JUN-99"=248, "21-JUN-99"=1

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| TOP_LEVEL_DOMAIN_KEY | ZW | PH | GE |
| TOP_LEVEL_DOMAIN | ZW | PH | GE |
| TOP_LEVEL_DOMAIN_DESCRIPTION | Zimbabwe | Philippines | Georgia |
| WAREHOUSE_LOAD_DATE | 17-JUN-99 | 17-JUN-99 | 17-JUN-99 |

# `warehouse_users`  (rows=10000)

columns:
`MIT_ID` varchar127: digits, unique identifier
`KRB_NAME` varchar127: 5310 distinct
`KRB_NAME_UPPERCASE` varchar127: 5309 distinct, nulls=1
`LAST_NAME` varchar127: 339 distinct
`FIRST_NAME` varchar127: 364 distinct
`MIDDLE_NAME` varchar127: 361 distinct, nulls=4804
`EMAIL_ADDRESS` varchar127: 6650 distinct
`OFFICE_LOCATION` varchar127: 4026 distinct, nulls=1061
`OFFICE_PHONE` varchar127: digits, all distinct, nulls=1743
`UNIT_ID` varchar127: digits, 314 distinct, nulls=77
`UNIT_NAME` varchar127: 322 distinct, nulls=77
`TITLE` varchar127: all NULL
`YEAR` varchar127: "G"=20, "1"=3, nulls=9977
`TYPE` varchar127: "EMPLOYEE"=9977, "STUDENT"=23
`APPOINTMENT_TYPE` varchar127: "Primary Appointment"=9900, nulls=100

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| MIT_ID | 999999599 | 933441103 | 958064306 |
| KRB_NAME | elisef | claudet | paigem4 |
| KRB_NAME_UPPERCASE | ELISEF | CLAUDET | PAIGEM4 |
| LAST_NAME | Floyd | Taylor | Mayer |
| FIRST_NAME | Elise | Claude | Paige |
| MIDDLE_NAME | C | null | Thornton |
| EMAIL_ADDRESS | elisef@gmail.business.com | claudet@worker.com | paigem4@gmail.business.com |
| OFFICE_LOCATION | LL-S1-238D | NE49 | LL-C-128 |
| OFFICE_PHONE | 7278410613 | 7723293951 | 2894771888 |
| UNIT_ID | 310000 | 406300 | 310000 |
| UNIT_NAME | Lincoln Laboratory | Open Learning, ODL, OpenCourseWare | Lincoln Laboratory |
| TITLE | null | null | null |
| YEAR | null | null | null |
| TYPE | EMPLOYEE | EMPLOYEE | EMPLOYEE |
| APPOINTMENT_TYPE | Primary Appointment | Primary Appointment | Primary Appointment |

# `zip_canada`  (rows=10000)

columns:
`POSTAL_CODE` varchar127: 9987 distinct
`CITY_NAME` varchar127: 445 distinct
`CITY_TYPE` varchar127: "D"=9987, "A"=13
`PROVINCE_ABBR` varchar127: "NL"=10000
`PROVINCE_NAME` varchar127: "Newfoundland"=10000
`WAREHOUSE_LOAD_DATE` varchar255: "25-MAY-23"=10000

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| POSTAL_CODE | A2N 1M6 | A0K 4L0 | A1C 4S7 |
| CITY_NAME | Stephenville | Reefs Harbour | St. John's |
| CITY_TYPE | D | D | D |
| PROVINCE_ABBR | NL | NL | NL |
| PROVINCE_NAME | Newfoundland | Newfoundland | Newfoundland |
| WAREHOUSE_LOAD_DATE | 25-MAY-23 | 25-MAY-23 | 25-MAY-23 |

# `zip_usa`  (rows=10000)

columns:
`STATE_NAME` varchar127: "Puerto Rico"=3093, "New Jersey"=1569, "Massachusetts"=1217, "Maine"=912, "Vermont"=910, "Connecticut"=849, "New Hampshire"=476, "Armed Forces - Europe/Africa/Canada"=410, "New York"=371, "Rhode Island"=164, "Virgin Islands"=29
`WAREHOUSE_LOAD_DATE` varchar255: "25-MAY-23"=10000
`ZIP_CODE` varchar127: digits, 3650 distinct
`ZIP_TYPE` varchar127: "S"=8188, "P"=1035, "M"=410, "U"=367
`CITY_NAME` varchar127: 6990 distinct
`CITY_TYPE` varchar127: "N"=4858, "D"=3648, "A"=1494
`COUNTY_NAME` varchar127: 159 distinct
`STATE_ABBR` varchar127: "PR"=3093, "NJ"=1569, "MA"=1217, "ME"=912, "VT"=910, "CT"=849, "NH"=476, "AE"=410, "NY"=371, "RI"=164, "VI"=29

indexes: none

samples:
| column | latest | sample | sample |
|---|---|---|---|
| STATE_NAME | Virgin Islands | Connecticut | New Jersey |
| WAREHOUSE_LOAD_DATE | 25-MAY-23 | 25-MAY-23 | 25-MAY-23 |
| ZIP_CODE | 851 | 6137 | 7640 |
| ZIP_TYPE | P | P | S |
| CITY_NAME | Kingshill | West Hartfrd | Harrington Park |
| CITY_TYPE | D | A | D |
| COUNTY_NAME | Saint Croix | Hartford | Bergen |
| STATE_ABBR | VI | CT | NJ |

# `zpm_rooms_load`  (rows=10000)

columns:
`BUILDING_ROOM` varchar127: 9334 distinct
`BUILDING_COMPONENT` varchar127: digits, 34 distinct
`FLOOR` varchar127: digits, 27 distinct
`SPACE_USAGE` varchar127: 41 distinct
`SPACE_UNIT_CODE` varchar127: digits, 66 distinct, nulls=3, "591000"=3569, "65000"=575, "267000"=561, "67900"=521, "152000"=462, "417500"=378, "61000"=359, "271000"=237, "60600"=192, "446700"=185
`HR_ORG_UNIT_ID` varchar127: digits, 66 distinct, nulls=3, "10000853"=3569, "10000324"=575, "10000578"=561, "10000957"=521, "10000491"=462, "10005459"=378, "10000299"=359, "10000579"=237, "10000294"=192, "10000760"=185
`ACCESS_LEVEL` varchar127: "2"=5692, "1"=1519, "0"=1458, "3"=1331

indexes: `HR_ORG_UNIT_ID`, `SPACE_UNIT_CODE`

samples:
| column | latest | sample | sample |
|---|---|---|---|
| BUILDING_ROOM | 45-398 | 3-299A | 18-404 |
| BUILDING_COMPONENT | 45 | 3 | 18 |
| FLOOR | 3 | 2 | 4 |
| SPACE_USAGE | IT HLPDSK | STF ROOM | FIL RM |
| SPACE_UNIT_CODE | 401930 | 401000 | 152000 |
| HR_ORG_UNIT_ID | 10005759 | 10000595 | 10000491 |
| ACCESS_LEVEL | 1 | 2 | 2 |

- Skipped 5 empty table(s): `estimated_surcharges_estonly`, `fund_center_hierarchy`, `opa_person_current`, `profit_center_group`, `subject_selector`
