INSERT INTO cmn.uom_conversion(oid, uom_oid_from, uom_oid_to, conversion_factor, decimal_scale, rounding_mode, created_by, created_on, updated_by, updated_on, status)
SELECT oid, uom_oid_from, uom_oid_to, conversion_factor, decimal_scale, rounding_mode, created_by, created_on, updated_by, updated_on, status
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, uom_oid_from, uom_oid_to, conversion_factor, decimal_scale, rounding_mode, created_by, created_on, updated_by, updated_on, status
FROM cmn.uom_conversion')
AS x(oid character varying, uom_oid_from character varying, uom_oid_to character varying, conversion_factor numeric, decimal_scale numeric, rounding_mode character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, status character varying);
