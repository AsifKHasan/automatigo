INSERT INTO inv.inspections(id, facility_id, in_out_id, process_type, result_id, is_deleted, created_by, created_at, updated_at)
SELECT id, facility_id, in_out_id, process_type, result_id, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, facility_id, in_out_id, process_type, result_id, is_deleted, created_by, created_at, updated_at
FROM inv.inspections')
AS x(id uuid, facility_id uuid, in_out_id uuid, process_type character varying, result_id uuid, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
