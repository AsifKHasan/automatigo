INSERT INTO inv.user_role_mappings(id, user_id, role_id)
SELECT id, user_id, role_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, role_id
FROM inv.user_role_mappings')
AS x(id uuid, user_id uuid, role_id uuid);
