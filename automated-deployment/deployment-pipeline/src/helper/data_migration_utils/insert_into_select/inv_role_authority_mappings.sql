INSERT INTO inv.role_authority_mappings(id, role_id, authority_id)
SELECT id, role_id, authority_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, role_id, authority_id
FROM inv.role_authority_mappings')
AS x(id uuid, role_id uuid, authority_id integer);
