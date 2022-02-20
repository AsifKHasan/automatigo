INSERT INTO cmn.file(oid, created_by, created_on, updated_by, updated_on, row_status, title, stored_name, file_size, description, dir_id, org_name)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, title, stored_name, file_size, description, dir_id, org_name
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, title, stored_name, file_size, description, dir_id, org_name
FROM cmn.file')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, title character varying, stored_name character varying, file_size numeric, description text, dir_id character varying, org_name character varying);
