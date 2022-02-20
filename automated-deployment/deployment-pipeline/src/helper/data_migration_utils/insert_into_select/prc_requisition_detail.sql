INSERT INTO prc.requisition_detail(oid, quantity, remarks, unit, item_oid, item_group_oid, item_category_oid, requisition_oid)
SELECT oid, quantity, remarks, unit, item_oid, item_group_oid, item_category_oid, requisition_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, quantity, remarks, unit, item_oid, item_group_oid, item_category_oid, requisition_oid
FROM prc.requisition_detail')
AS x(oid character varying, quantity numeric, remarks text, unit character varying, item_oid character varying, item_group_oid character varying, item_category_oid character varying, requisition_oid character varying);
