INSERT INTO cmn.office_unit(oid, name_en, name_bn, display_order, business_order, parent_oid, office_unit_category_oid, office_oid, ministry_oid, is_deleted, created_by, created_on, updated_by, updated_on)
SELECT oid, name_en, name_bn, display_order, business_order, parent_oid, office_unit_category_oid, office_oid, ministry_oid, is_deleted, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, display_order, business_order, parent_oid, office_unit_category_oid, office_oid, ministry_oid, is_deleted, created_by, created_on, updated_by, updated_on
FROM cmn.office_unit')
AS x(oid character varying, name_en character varying, name_bn character varying, display_order numeric, business_order numeric, parent_oid character varying, office_unit_category_oid character varying, office_oid character varying, ministry_oid character varying, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
