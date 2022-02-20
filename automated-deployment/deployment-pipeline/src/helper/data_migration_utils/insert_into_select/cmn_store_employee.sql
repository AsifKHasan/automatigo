INSERT INTO cmn.store_employee(oid, active_date, is_deleted, created_by, created_on, updated_by, updated_on, store_oid, store_designation_oid, employee_oid)
SELECT oid, active_date, is_deleted, created_by, created_on, updated_by, updated_on, store_oid, store_designation_oid, employee_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, active_date, is_deleted, created_by, created_on, updated_by, updated_on, store_oid, store_designation_oid, employee_oid
FROM cmn.store_employee')
AS x(oid character varying, active_date timestamp without time zone, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, store_oid character varying, store_designation_oid character varying, employee_oid character varying);
