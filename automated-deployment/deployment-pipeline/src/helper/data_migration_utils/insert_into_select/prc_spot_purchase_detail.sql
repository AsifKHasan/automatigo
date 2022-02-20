INSERT INTO prc.spot_purchase_detail(oid, quantity, unit_rate, remarks, status, receive_date, discount_amount, gross_amount, total_amount, unit, item_oid, item_group_oid, item_category_oid, package_oid, economic_code_oid, spot_purchase_oid)
SELECT oid, quantity, unit_rate, remarks, status, receive_date, discount_amount, gross_amount, total_amount, unit, item_oid, item_group_oid, item_category_oid, package_oid, economic_code_oid, spot_purchase_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, quantity, unit_rate, remarks, status, receive_date, discount_amount, gross_amount, total_amount, unit, item_oid, item_group_oid, item_category_oid, package_oid, economic_code_oid, spot_purchase_oid
FROM prc.spot_purchase_detail')
AS x(oid character varying, quantity numeric, unit_rate numeric, remarks text, status character varying, receive_date date, discount_amount numeric, gross_amount numeric, total_amount numeric, unit character varying, item_oid character varying, item_group_oid character varying, item_category_oid character varying, package_oid character varying, economic_code_oid character varying, spot_purchase_oid character varying);
