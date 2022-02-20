INSERT INTO sec.grp_role(oid, name_en, name_bn, role_type, grp_module_oid, description_en, description_bn, menu_json)
SELECT oid, name_en, name_bn, role_type, grp_module_oid, description_en, description_bn, menu_json
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, role_type, grp_module_oid, description_en, description_bn, menu_json
FROM sec.grp_role')
AS x(oid character varying, name_en character varying, name_bn character varying, role_type character varying, grp_module_oid character varying, description_en text, description_bn text, menu_json text);
