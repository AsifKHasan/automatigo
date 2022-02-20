INSERT INTO inv.review_job_type(id, job_name, table_name)
SELECT id, job_name, table_name
FROM dblink('dbname=grp_bcc_live',
'SELECT id, job_name, table_name
FROM inv.review_job_type')
AS x(id uuid, job_name character varying, table_name character varying);
