INSERT INTO sec.grp_module(oid, name_en, name_bn, status, module_type, sort_order)
SELECT oid, name_en, name_bn, status, module_type, sort_order
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, module_type, sort_order
FROM sec.grp_module')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, module_type character varying, sort_order numeric);
