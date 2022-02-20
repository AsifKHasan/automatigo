INSERT INTO hrm.job_circular_approval(oid, circular_oid, approved_by_oid, approved_by_post_oid, approval_code, approval_status, comments)
SELECT oid, circular_oid, approved_by_oid, approved_by_post_oid, approval_code, approval_status, comments
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, circular_oid, approved_by_oid, approved_by_post_oid, approval_code, approval_status, comments
FROM hrm.job_circular_approval')
AS x(oid character varying, circular_oid character varying, approved_by_oid character varying, approved_by_post_oid character varying, approval_code character varying, approval_status character varying, comments text);
