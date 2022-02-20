INSERT INTO hrm.employeel_leave_details(oid, employee_oid, leave_type_oid, total_working_days, total_leave_days, remaining_leave_amount, remaining_leave_unit, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, leave_type_oid, total_working_days, total_leave_days, remaining_leave_amount, remaining_leave_unit, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, leave_type_oid, total_working_days, total_leave_days, remaining_leave_amount, remaining_leave_unit, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employeel_leave_details')
AS x(oid character varying, employee_oid character varying, leave_type_oid character varying, total_working_days numeric, total_leave_days numeric, remaining_leave_amount numeric, remaining_leave_unit character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
