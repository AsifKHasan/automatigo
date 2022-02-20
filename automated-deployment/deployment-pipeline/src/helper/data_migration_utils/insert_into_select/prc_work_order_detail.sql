INSERT INTO prc.work_order_detail(oid, quantity, previous_received_quantity, remarks, status, delivery_date, unit, unit_rate, total_amount, item_oid, item_group_oid, package_oid, economic_code_oid, item_category_oid, work_order_oid)
SELECT oid, quantity, previous_received_quantity, remarks, status, delivery_date, unit, unit_rate, total_amount, item_oid, item_group_oid, package_oid, economic_code_oid, item_category_oid, work_order_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, quantity, previous_received_quantity, remarks, status, delivery_date, unit, unit_rate, total_amount, item_oid, item_group_oid, package_oid, economic_code_oid, item_category_oid, work_order_oid
FROM prc.work_order_detail')
AS x(oid character varying, quantity numeric, previous_received_quantity numeric, remarks text, status character varying, delivery_date date, unit character varying, unit_rate numeric, total_amount numeric, item_oid character varying, item_group_oid character varying, package_oid character varying, economic_code_oid character varying, item_category_oid character varying, work_order_oid character varying);
