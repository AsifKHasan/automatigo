INSERT INTO inv.roles(id, created_on, created_by, updated_on, description, name, updated_by, organisation_id)
SELECT id, created_on, created_by, updated_on, description, name, updated_by, organisation_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, created_on, created_by, updated_on, description, name, updated_by, organisation_id
FROM inv.roles')
AS x(id uuid, created_on timestamp without time zone, created_by uuid, updated_on timestamp without time zone, description text, name character varying, updated_by uuid, organisation_id uuid);
