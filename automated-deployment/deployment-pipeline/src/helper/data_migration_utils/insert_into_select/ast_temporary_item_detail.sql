INSERT INTO ast.temporary_item_detail(oid, received_quantity, qualified_quantity, disqualified_quantity, extra_quantity, remarks, item_oid, work_order_detail_oid, temporary_item_oid)
SELECT oid, received_quantity, qualified_quantity, disqualified_quantity, extra_quantity, remarks, item_oid, work_order_detail_oid, temporary_item_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, received_quantity, qualified_quantity, disqualified_quantity, extra_quantity, remarks, item_oid, work_order_detail_oid, temporary_item_oid
FROM ast.temporary_item_detail')
AS x(oid character varying, received_quantity numeric, qualified_quantity numeric, disqualified_quantity numeric, extra_quantity numeric, remarks character varying, item_oid character varying, work_order_detail_oid character varying, temporary_item_oid character varying);
