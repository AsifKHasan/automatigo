INSERT INTO hrm.create_short_list(oid, short_list_code, application_code, application_name, educational_qualification, experience, short_list_created_by_oid, district)
SELECT oid, short_list_code, application_code, application_name, educational_qualification, experience, short_list_created_by_oid, district
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, short_list_code, application_code, application_name, educational_qualification, experience, short_list_created_by_oid, district
FROM hrm.create_short_list')
AS x(oid character varying, short_list_code character varying, application_code character varying, application_name character varying, educational_qualification text, experience text, short_list_created_by_oid character varying, district character varying);
