INSERT INTO hrm.employee_confirmation(oid, employee_oid, confirmation_date, confirmation_by, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, confirmation_date, confirmation_by, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, confirmation_date, confirmation_by, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_confirmation')
AS x(oid character varying, employee_oid character varying, confirmation_date timestamp without time zone, confirmation_by character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
