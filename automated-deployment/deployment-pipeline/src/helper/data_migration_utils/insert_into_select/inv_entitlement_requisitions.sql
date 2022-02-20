INSERT INTO inv.entitlement_requisitions(id, entitlement_id, requisition_detail_id, employee_id, amount, uom_id, is_retrieved, is_deleted, created_by, created_at, updated_at)
SELECT id, entitlement_id, requisition_detail_id, employee_id, amount, uom_id, is_retrieved, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, entitlement_id, requisition_detail_id, employee_id, amount, uom_id, is_retrieved, is_deleted, created_by, created_at, updated_at
FROM inv.entitlement_requisitions')
AS x(id uuid, entitlement_id uuid, requisition_detail_id uuid, employee_id uuid, amount double precision, uom_id uuid, is_retrieved boolean, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
