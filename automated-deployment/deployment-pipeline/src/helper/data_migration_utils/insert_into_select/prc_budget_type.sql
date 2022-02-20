INSERT INTO prc.budget_type(oid, code, name_en, name_bn, description, created_by, created_on, updated_by, updated_on)
SELECT oid, code, name_en, name_bn, description, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, name_en, name_bn, description, created_by, created_on, updated_by, updated_on
FROM prc.budget_type')
AS x(oid character varying, code character varying, name_en character varying, name_bn character varying, description text, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
