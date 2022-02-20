INSERT INTO prc.consolidate_requisition_detail(oid, required_quantity, entitlement_quantity, total_quantity, approved_quantity, remarks, unit, item_category_oid, item_group_oid, consolidate_requisition_oid)
SELECT oid, required_quantity, entitlement_quantity, total_quantity, approved_quantity, remarks, unit, item_category_oid, item_group_oid, consolidate_requisition_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, required_quantity, entitlement_quantity, total_quantity, approved_quantity, remarks, unit, item_category_oid, item_group_oid, consolidate_requisition_oid
FROM prc.consolidate_requisition_detail')
AS x(oid character varying, required_quantity numeric, entitlement_quantity numeric, total_quantity numeric, approved_quantity numeric, remarks text, unit character varying, item_category_oid character varying, item_group_oid character varying, consolidate_requisition_oid character varying);
