INSERT INTO hrm.at_leave(oid, employee_oid, leave_status_oid)
SELECT oid, employee_oid, leave_status_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, leave_status_oid
FROM hrm.at_leave')
AS x(oid character varying, employee_oid character varying, leave_status_oid character varying);
