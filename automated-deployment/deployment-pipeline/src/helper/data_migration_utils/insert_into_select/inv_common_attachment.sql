INSERT INTO inv.common_attachment(id, file_title, file_id, source_tbl, source_row_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, file_title, file_id, source_tbl, source_row_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, file_title, file_id, source_tbl, source_row_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.common_attachment')
AS x(id uuid, file_title character varying, file_id uuid, source_tbl character varying, source_row_id uuid, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);
