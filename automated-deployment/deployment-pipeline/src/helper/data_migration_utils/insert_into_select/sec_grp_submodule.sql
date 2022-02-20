INSERT INTO sec.grp_submodule(oid, name_en, name_bn, status, sort_order, module_oid)
SELECT oid, name_en, name_bn, status, sort_order, module_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, sort_order, module_oid
FROM sec.grp_submodule')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, sort_order numeric, module_oid character varying);
