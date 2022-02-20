INSERT INTO inv.authority_authority_mappings(id, parent_id, child_id)
SELECT id, parent_id, child_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, parent_id, child_id
FROM inv.authority_authority_mappings')
AS x(id integer, parent_id integer, child_id integer);
