INSERT INTO cmn.email_recipient(oid, created_by, created_on, updated_by, updated_on, row_status, emp_id, org_id, email_address, recipient_type, email_id, field_type)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, emp_id, org_id, email_address, recipient_type, email_id, field_type
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, emp_id, org_id, email_address, recipient_type, email_id, field_type
FROM cmn.email_recipient')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, emp_id character varying, org_id character varying, email_address character varying, recipient_type character varying, email_id character varying, field_type character varying);
