INSERT INTO inv.inspection_results(id, inspected_uom_id, inspected_quantity, passed_quantity, certificate_file_id, is_deleted, created_by, created_at, updated_at)
SELECT id, inspected_uom_id, inspected_quantity, passed_quantity, certificate_file_id, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, inspected_uom_id, inspected_quantity, passed_quantity, certificate_file_id, is_deleted, created_by, created_at, updated_at
FROM inv.inspection_results')
AS x(id uuid, inspected_uom_id uuid, inspected_quantity numeric, passed_quantity numeric, certificate_file_id uuid, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
