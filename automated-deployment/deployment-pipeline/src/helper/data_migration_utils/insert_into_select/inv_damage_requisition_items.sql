INSERT INTO inv.damage_requisition_items(id, item_in_out_id, uom_id, quantity, type_id, requisition_id, justification, is_deleted, created_by, created_at, updated_at)
SELECT id, item_in_out_id, uom_id, quantity, type_id, requisition_id, justification, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, item_in_out_id, uom_id, quantity, type_id, requisition_id, justification, is_deleted, created_by, created_at, updated_at
FROM inv.damage_requisition_items')
AS x(id uuid, item_in_out_id uuid, uom_id uuid, quantity double precision, type_id uuid, requisition_id uuid, justification character varying, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
