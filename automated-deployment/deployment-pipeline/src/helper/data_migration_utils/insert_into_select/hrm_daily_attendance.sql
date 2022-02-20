INSERT INTO hrm.daily_attendance(oid, employee_oid, date, is_present)
SELECT oid, employee_oid, date, is_present
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, date, is_present
FROM hrm.daily_attendance')
AS x(oid character varying, employee_oid character varying, date timestamp without time zone, is_present character varying);
