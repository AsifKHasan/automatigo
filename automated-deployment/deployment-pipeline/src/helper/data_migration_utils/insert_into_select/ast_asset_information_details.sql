INSERT INTO ast.asset_information_details(oid, previous_tag, serial_no, expiry_duration, asset_information_oid, remarks)
SELECT oid, previous_tag, serial_no, expiry_duration, asset_information_oid, remarks
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, previous_tag, serial_no, expiry_duration, asset_information_oid, remarks
FROM ast.asset_information_details')
AS x(oid character varying, previous_tag character varying, serial_no character varying, expiry_duration numeric, asset_information_oid character varying, remarks text);
