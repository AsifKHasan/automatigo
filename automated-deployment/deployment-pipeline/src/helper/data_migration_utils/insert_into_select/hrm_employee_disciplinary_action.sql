INSERT INTO hrm.employee_disciplinary_action(oid, employee_oid, nature_of_offence, punishment, date, remarks, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, nature_of_offence, punishment, date, remarks, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, nature_of_offence, punishment, date, remarks, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_disciplinary_action')
AS x(oid character varying, employee_oid character varying, nature_of_offence character varying, punishment character varying, date timestamp without time zone, remarks text, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
