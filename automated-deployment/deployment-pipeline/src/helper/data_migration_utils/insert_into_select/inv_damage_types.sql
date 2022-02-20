INSERT INTO inv.damage_types(id, name, is_deleted, created_by, created_at, updated_at)
SELECT id, name, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, name, is_deleted, created_by, created_at, updated_at
FROM inv.damage_types')
AS x(id uuid, name character varying, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
