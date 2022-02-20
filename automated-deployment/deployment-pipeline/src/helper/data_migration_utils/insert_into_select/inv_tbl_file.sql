INSERT INTO inv.tbl_file(file_id, module_name, file_original_name, file_saved_name, file_type, file_size, is_deleted, created_at, download_link)
SELECT file_id, module_name, file_original_name, file_saved_name, file_type, file_size, is_deleted, created_at, download_link
FROM dblink('dbname=grp_bcc_live',
'SELECT file_id, module_name, file_original_name, file_saved_name, file_type, file_size, is_deleted, created_at, download_link
FROM inv.tbl_file')
AS x(file_id uuid, module_name text, file_original_name character varying, file_saved_name character varying, file_type character varying, file_size bigint, is_deleted boolean, created_at timestamp without time zone, download_link text);
