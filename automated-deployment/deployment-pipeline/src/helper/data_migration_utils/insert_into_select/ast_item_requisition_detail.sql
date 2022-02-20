INSERT INTO ast.item_requisition_detail(oid, requested_quantity, approved_quantity, revised_quantity, given_quantity, item_approval, comments, is_deleted, requisition_oid, item_group_oid, uom_oid, entitlement_oid)
SELECT oid, requested_quantity, approved_quantity, revised_quantity, given_quantity, item_approval, comments, is_deleted, requisition_oid, item_group_oid, uom_oid, entitlement_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, requested_quantity, approved_quantity, revised_quantity, given_quantity, item_approval, comments, is_deleted, requisition_oid, item_group_oid, uom_oid, entitlement_oid
FROM ast.item_requisition_detail')
AS x(oid character varying, requested_quantity numeric, approved_quantity numeric, revised_quantity numeric, given_quantity numeric, item_approval character varying, comments text, is_deleted character varying, requisition_oid character varying, item_group_oid character varying, uom_oid character varying, entitlement_oid character varying);
