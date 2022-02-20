INSERT INTO cmn.notification_recipient(oid, created_by, created_on, updated_by, updated_on, row_status, emp_id, org_id, u_id, status, n_id)
SELECT oid, created_by, created_on, updated_by, updated_on, row_status, emp_id, org_id, u_id, status, n_id
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, row_status, emp_id, org_id, u_id, status, n_id
FROM cmn.notification_recipient')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, row_status character varying, emp_id character varying, org_id character varying, u_id character varying, status character varying, n_id character varying);
