INSERT INTO inv.uom_category(uom_type_id)
SELECT uom_type_id
FROM dblink('dbname=grp_bcc_live',
'SELECT uom_type_id
FROM inv.uom_category')
AS x(uom_type_id character varying);
