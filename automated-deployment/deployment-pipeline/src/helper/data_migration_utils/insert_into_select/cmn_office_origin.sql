INSERT INTO cmn.office_origin(oid, name_en, name_bn, status, level_order, sort_order, parent_oid, office_layer_oid, ministry_oid)
SELECT oid, name_en, name_bn, status, level_order, sort_order, parent_oid, office_layer_oid, ministry_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, level_order, sort_order, parent_oid, office_layer_oid, ministry_oid
FROM cmn.office_origin')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, level_order numeric, sort_order numeric, parent_oid character varying, office_layer_oid character varying, ministry_oid character varying);
