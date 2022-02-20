INSERT INTO inv.party_organization(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, name, party_id, office_type_id)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, name, party_id, office_type_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, name, party_id, office_type_id
FROM inv.party_organization')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, name text, party_id uuid, office_type_id uuid);
