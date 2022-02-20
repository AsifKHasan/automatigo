INSERT INTO hrm.penalty_for_attendance(oid, date, employee_oid, cause, action, remarks, penalty_code)
SELECT oid, date, employee_oid, cause, action, remarks, penalty_code
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, date, employee_oid, cause, action, remarks, penalty_code
FROM hrm.penalty_for_attendance')
AS x(oid character varying, date timestamp without time zone, employee_oid character varying, cause text, action text, remarks text, penalty_code character varying);
