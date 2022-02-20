INSERT INTO hrm.employee_award(oid, employee_oid, award_title, ground, date_of_award, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, award_title, ground, date_of_award, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, award_title, ground, date_of_award, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_award')
AS x(oid character varying, employee_oid character varying, award_title character varying, ground text, date_of_award timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
