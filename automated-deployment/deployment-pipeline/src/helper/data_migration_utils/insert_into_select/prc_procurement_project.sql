INSERT INTO prc.procurement_project(oid, project_code, name_en, name_bn, description, start_date, end_date, commitment_amount, status, created_by, created_on, updated_by, updated_on, approval_date)
SELECT oid, project_code, name_en, name_bn, description, start_date, end_date, commitment_amount, status, created_by, created_on, updated_by, updated_on, approval_date
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, project_code, name_en, name_bn, description, start_date, end_date, commitment_amount, status, created_by, created_on, updated_by, updated_on, approval_date
FROM prc.procurement_project')
AS x(oid character varying, project_code character varying, name_en character varying, name_bn character varying, description character varying, start_date date, end_date date, commitment_amount numeric, status character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, approval_date date);
