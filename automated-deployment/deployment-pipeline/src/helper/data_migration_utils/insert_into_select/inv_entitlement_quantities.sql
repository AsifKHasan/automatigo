INSERT INTO inv.entitlement_quantities(id, entitlement_id, uom_id, amount, is_deleted, created_by, created_at, updated_at)
SELECT id, entitlement_id, uom_id, amount, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, entitlement_id, uom_id, amount, is_deleted, created_by, created_at, updated_at
FROM inv.entitlement_quantities')
AS x(id uuid, entitlement_id uuid, uom_id uuid, amount double precision, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
