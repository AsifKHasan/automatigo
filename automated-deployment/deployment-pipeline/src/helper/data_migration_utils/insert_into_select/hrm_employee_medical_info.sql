INSERT INTO hrm.employee_medical_info(oid, employee_oid, illness, from_date, till_date, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, illness, from_date, till_date, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, illness, from_date, till_date, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_medical_info')
AS x(oid character varying, employee_oid character varying, illness character varying, from_date timestamp without time zone, till_date timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
