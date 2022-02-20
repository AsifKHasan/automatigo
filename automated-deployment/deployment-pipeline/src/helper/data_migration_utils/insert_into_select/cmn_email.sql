INSERT INTO cmn.email(oid, created_by, created_on, updated_by, updated_on, row_status, subject, message_content, tag, token, status_txt, request_oid, hasattachment, scheduled_time, departure_time)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, subject, message_content, tag, token, status_txt, request_oid, hasattachment, scheduled_time, departure_time
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, subject, message_content, tag, token, status_txt, request_oid, hasattachment, scheduled_time, departure_time
FROM cmn.email')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, subject character varying, message_content text, tag character varying, token character varying, status_txt character varying, request_oid character varying, hasattachment character varying, scheduled_time timestamp without time zone, departure_time timestamp without time zone);
