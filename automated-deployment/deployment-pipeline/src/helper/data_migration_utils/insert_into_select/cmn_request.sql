INSERT INTO cmn.request(oid, created_by, created_on, updated_by, updated_on, row_status, request_oid, requested_by)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, request_oid, requested_by
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, request_oid, requested_by
FROM cmn.request')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, request_oid character varying, requested_by character varying);
