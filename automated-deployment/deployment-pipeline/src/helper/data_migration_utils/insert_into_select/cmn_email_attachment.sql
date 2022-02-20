INSERT INTO cmn.email_attachment(oid, created_by, created_on, updated_by, updated_on, row_status, file_name, location, file_unique_name, email_id)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, file_name, location, file_unique_name, email_id
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, file_name, location, file_unique_name, email_id
FROM cmn.email_attachment')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, file_name character varying, location character varying, file_unique_name character varying, email_id character varying);
