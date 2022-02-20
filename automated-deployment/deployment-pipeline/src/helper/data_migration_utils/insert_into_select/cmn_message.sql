INSERT INTO cmn.message(oid, created_by, created_on, updated_by, updated_on, row_status, tag, token, request_oid, message_content)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, tag, token, request_oid, message_content
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, tag, token, request_oid, message_content
FROM cmn.message')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, tag character varying, token character varying, request_oid character varying, message_content text);
