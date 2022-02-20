INSERT INTO inv.entitlement_types(id, name, bn_name, is_deleted, created_by, created_at, updated_at)
SELECT id, name, bn_name, is_deleted, created_by, created_at, updated_at
FROM dblink('dbname=grp_bcc_live',
'SELECT id, name, bn_name, is_deleted, created_by, created_at, updated_at
FROM inv.entitlement_types')
AS x(id uuid, name character varying, bn_name character varying, is_deleted boolean, created_by uuid, created_at timestamp without time zone, updated_at timestamp without time zone);
