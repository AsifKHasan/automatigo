INSERT INTO inv.gate_pass_file(id, file_name, file_id, upload_date, gate_pass_id, is_deleted)
SELECT id, file_name, file_id, upload_date, gate_pass_id, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT id, file_name, file_id, upload_date, gate_pass_id, is_deleted
FROM inv.gate_pass_file')
AS x(id uuid, file_name character varying, file_id character varying, upload_date date, gate_pass_id uuid, is_deleted boolean);
