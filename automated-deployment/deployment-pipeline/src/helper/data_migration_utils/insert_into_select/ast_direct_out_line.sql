INSERT INTO ast.direct_out_line(oid, direct_out_oid, remarks, asset_oid)
SELECT oid, direct_out_oid, remarks, asset_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, direct_out_oid, remarks, asset_oid
FROM ast.direct_out_line')
AS x(oid character varying, direct_out_oid character varying, remarks text, asset_oid character varying);
