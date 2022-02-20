INSERT INTO inv.uom_conversion(id, uom_id, uom_id_to, conversion_factor, custom_method_id, decimal_scale, rounding_mode, created_date)
SELECT id, uom_id, uom_id_to, conversion_factor, custom_method_id, decimal_scale, rounding_mode, created_date
FROM dblink('dbname=grp_bcc_live',
'SELECT id, uom_id, uom_id_to, conversion_factor, custom_method_id, decimal_scale, rounding_mode, created_date
FROM inv.uom_conversion')
AS x(id uuid, uom_id character varying, uom_id_to character varying, conversion_factor double precision, custom_method_id character varying, decimal_scale double precision, rounding_mode character varying, created_date timestamp without time zone);
