INSERT INTO hrm.employee_additional_prof_qualification(oid, employee_oid, qualification, sort_order, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, qualification, sort_order, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, qualification, sort_order, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_additional_prof_qualification')
AS x(oid character varying, employee_oid character varying, qualification character varying, sort_order numeric, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
