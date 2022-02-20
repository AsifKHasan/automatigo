INSERT INTO cmn.entitlement(oid, quantity, started_from, is_deleted, created_by, created_on, updated_by, updated_on, entitlement_type_oid, office_oid, post_oid, item_group_oid, uom_oid)
SELECT oid, quantity, started_from, is_deleted, created_by, created_on, updated_by, updated_on, entitlement_type_oid, office_oid, post_oid, item_group_oid, uom_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, quantity, started_from, is_deleted, created_by, created_on, updated_by, updated_on, entitlement_type_oid, office_oid, post_oid, item_group_oid, uom_oid
FROM cmn.entitlement')
AS x(oid character varying, quantity numeric, started_from character varying, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, entitlement_type_oid character varying, office_oid character varying, post_oid character varying, item_group_oid character varying, uom_oid character varying);
