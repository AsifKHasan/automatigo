INSERT INTO cmn.file_request(oid, created_by, created_on, updated_by, updated_on, row_status, file_oid, request_oid)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, file_oid, request_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, file_oid, request_oid
FROM cmn.file_request')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, file_oid character varying, request_oid character varying);
