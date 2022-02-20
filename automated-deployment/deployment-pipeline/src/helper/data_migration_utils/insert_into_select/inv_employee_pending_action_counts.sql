INSERT INTO inv.employee_pending_action_counts(id, employee_id, source_table, source_row_id, status, count)
SELECT id, employee_id, source_table, source_row_id, status, count
FROM dblink('dbname=grp_bcc_live',
'SELECT id, employee_id, source_table, source_row_id, status, count
FROM inv.employee_pending_action_counts')
AS x(id uuid, employee_id uuid, source_table character varying, source_row_id uuid, status character varying, count integer);
