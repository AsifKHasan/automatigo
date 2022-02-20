INSERT INTO ast.asset_allocation_details(oid, is_received, received_date, return_status, remarks, asset_oid, asset_allocation_oid)
SELECT oid, is_received, received_date, return_status, remarks, asset_oid, asset_allocation_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, is_received, received_date, return_status, remarks, asset_oid, asset_allocation_oid
FROM ast.asset_allocation_details')
AS x(oid character varying, is_received character varying, received_date timestamp without time zone, return_status character varying, remarks character varying, asset_oid character varying, asset_allocation_oid character varying);
