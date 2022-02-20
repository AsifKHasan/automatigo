INSERT INTO hrm.training_type(oid, type_name, type_code, type_description, principal_department)
SELECT oid, type_name, type_code, type_description, principal_department
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, type_name, type_code, type_description, principal_department
FROM hrm.training_type')
AS x(oid character varying, type_name character varying, type_code character varying, type_description text, principal_department character varying);
