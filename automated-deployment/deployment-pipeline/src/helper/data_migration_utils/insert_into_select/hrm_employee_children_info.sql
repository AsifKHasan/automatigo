INSERT INTO hrm.employee_children_info(oid, employee_oid, name_en, name_bn, birth_date, is_widow, has_disability, gender, relation, birth_certificate_url, institution_name, school_admission_url, school_receipt_url, result_cg, level_in_school, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, name_en, name_bn, birth_date, is_widow, has_disability, gender, relation, birth_certificate_url, institution_name, school_admission_url, school_receipt_url, result_cg, level_in_school, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, name_en, name_bn, birth_date, is_widow, has_disability, gender, relation, birth_certificate_url, institution_name, school_admission_url, school_receipt_url, result_cg, level_in_school, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_children_info')
AS x(oid character varying, employee_oid character varying, name_en character varying, name_bn character varying, birth_date timestamp without time zone, is_widow character varying, has_disability character varying, gender character varying, relation character varying, birth_certificate_url character varying, institution_name character varying, school_admission_url character varying, school_receipt_url character varying, result_cg character varying, level_in_school character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);