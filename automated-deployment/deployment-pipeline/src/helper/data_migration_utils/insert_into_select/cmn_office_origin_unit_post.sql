INSERT INTO cmn.office_origin_unit_post(oid, name_en, name_bn, status, level_order, sort_order, parent_oid, office_origin_unit_oid)
SELECT oid, name_en, name_bn, status, level_order, sort_order, parent_oid, office_origin_unit_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, status, level_order, sort_order, parent_oid, office_origin_unit_oid
FROM cmn.office_origin_unit_post')
AS x(oid character varying, name_en character varying, name_bn character varying, status character varying, level_order numeric, sort_order numeric, parent_oid character varying, office_origin_unit_oid character varying);
