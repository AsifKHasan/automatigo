INSERT INTO hrm.vesting_of_magisterial_power(oid, employee_oid, area_of_work, work_description, reason_of_vesting, substitute_department, substitute_code, duration, start_date, end_date, go_code, government_order, notes)
SELECT oid, employee_oid, area_of_work, work_description, reason_of_vesting, substitute_department, substitute_code, duration, start_date, end_date, go_code, government_order, notes
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, area_of_work, work_description, reason_of_vesting, substitute_department, substitute_code, duration, start_date, end_date, go_code, government_order, notes
FROM hrm.vesting_of_magisterial_power')
AS x(oid character varying, employee_oid character varying, area_of_work character varying, work_description text, reason_of_vesting character varying, substitute_department character varying, substitute_code character varying, duration numeric, start_date timestamp without time zone, end_date timestamp without time zone, go_code character varying, government_order character varying, notes text);
