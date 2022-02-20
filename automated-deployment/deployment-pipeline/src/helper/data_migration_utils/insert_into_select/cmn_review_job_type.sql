INSERT INTO cmn.review_job_type(oid, job_name, table_name, is_deleted, created_by, created_on, updated_by, updated_on)
SELECT oid, job_name, table_name, is_deleted, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, job_name, table_name, is_deleted, created_by, created_on, updated_by, updated_on
FROM cmn.review_job_type')
AS x(oid character varying, job_name character varying, table_name character varying, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
