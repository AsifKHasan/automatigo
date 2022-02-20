INSERT INTO ast.direct_in_line(oid, item_oid, direct_in_oid, user_oid, office_unit_oid, serial_no, previous_tag, expiry_duration, remarks, asset_oid, asset_alloc_oid, allocation_date, purpose_oid)
SELECT oid, item_oid, direct_in_oid, user_oid, office_unit_oid, serial_no, previous_tag, expiry_duration, remarks, asset_oid, asset_alloc_oid, allocation_date, purpose_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, item_oid, direct_in_oid, user_oid, office_unit_oid, serial_no, previous_tag, expiry_duration, remarks, asset_oid, asset_alloc_oid, allocation_date, purpose_oid
FROM ast.direct_in_line')
AS x(oid character varying, item_oid character varying, direct_in_oid character varying, user_oid character varying, office_unit_oid character varying, serial_no character varying, previous_tag character varying, expiry_duration numeric, remarks text, asset_oid character varying, asset_alloc_oid character varying, allocation_date date, purpose_oid character varying);
