INSERT INTO ast.requisition_purpose(oid, name_en, name_bn, description, created_by, created_on, updated_by, updated_on)
SELECT oid, name_en, name_bn, description, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, description, created_by, created_on, updated_by, updated_on
FROM ast.requisition_purpose')
AS x(oid character varying, name_en character varying, name_bn character varying, description text, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
