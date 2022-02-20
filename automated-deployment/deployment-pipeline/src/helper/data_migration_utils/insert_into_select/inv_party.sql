INSERT INTO inv.party(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, name, remark, party_type_id, party_business_type_id, party_bank_detail_id, party_person_id)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, name, remark, party_type_id, party_business_type_id, party_bank_detail_id, party_person_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, name, remark, party_type_id, party_business_type_id, party_bank_detail_id, party_person_id
FROM inv.party')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, name text, remark text, party_type_id uuid, party_business_type_id uuid, party_bank_detail_id uuid, party_person_id uuid);
