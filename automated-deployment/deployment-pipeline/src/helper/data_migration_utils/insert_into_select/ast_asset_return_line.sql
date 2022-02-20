INSERT INTO ast.asset_return_line(oid, asset_return_oid, qc_pass, asset_oid, asset_allocation_line_oid)
SELECT oid, asset_return_oid, qc_pass, asset_oid, asset_allocation_line_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, asset_return_oid, qc_pass, asset_oid, asset_allocation_line_oid
FROM ast.asset_return_line')
AS x(oid character varying, asset_return_oid character varying, qc_pass character varying, asset_oid character varying, asset_allocation_line_oid character varying);
