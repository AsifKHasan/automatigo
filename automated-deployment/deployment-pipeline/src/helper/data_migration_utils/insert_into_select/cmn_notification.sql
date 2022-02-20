INSERT INTO cmn.notification(oid, created_by, created_on, updated_by, updated_on, row_status, tag, token, message_content, url, request_oid, callbackapi)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, tag, token, message_content, url, request_oid, callbackapi
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, tag, token, message_content, url, request_oid, callbackapi
FROM cmn.notification')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, tag character varying, token character varying, message_content text, url character varying, request_oid character varying, callbackapi character varying);
