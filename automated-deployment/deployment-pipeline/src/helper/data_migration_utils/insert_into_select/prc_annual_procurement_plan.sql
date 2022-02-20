INSERT INTO prc.annual_procurement_plan(oid, app_code, status, app_path, created_by, created_on, updated_by, updated_on, fiscal_year_oid, app_for, budget_type_oid, office_oid, declaration_oid)
SELECT oid, app_code, status, app_path, created_by, created_on, updated_by, updated_on, fiscal_year_oid, app_for, budget_type_oid, office_oid, declaration_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, app_code, status, app_path, created_by, created_on, updated_by, updated_on, fiscal_year_oid, app_for, budget_type_oid, office_oid, declaration_oid
FROM prc.annual_procurement_plan')
AS x(oid character varying, app_code character varying, status character varying, app_path character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, fiscal_year_oid character varying, app_for character varying, budget_type_oid character varying, office_oid character varying, declaration_oid character varying);
