INSERT INTO hrm.award_setup(oid, award_title, award_code, description, department, notes)
SELECT oid, award_title, award_code, description, department, notes
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, award_title, award_code, description, department, notes
FROM hrm.award_setup')
AS x(oid character varying, award_title character varying, award_code character varying, description text, department character varying, notes text);
