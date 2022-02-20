INSERT INTO sec.grp_subfeature(oid, name_en, name_bn, status, sort_order, feature_oid)
SELECT oid, name_en, name_bn, status, sort_order, feature_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, sort_order, feature_oid
FROM sec.grp_subfeature')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, sort_order numeric, feature_oid character varying);
