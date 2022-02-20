INSERT INTO inv.committee(committee_id, ct_id, authorised_by, approved_by, committee_name, min_no_member, max_no_member, forming_date, purpose, comments, status, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id)
SELECT committee_id, ct_id, authorised_by, approved_by, committee_name, min_no_member, max_no_member, forming_date, purpose, comments, status, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM dblink('dbname=grp_bcc_live',
'SELECT committee_id, ct_id, authorised_by, approved_by, committee_name, min_no_member, max_no_member, forming_date, purpose, comments, status, owned_by, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM inv.committee')
AS x(committee_id uuid, ct_id uuid, authorised_by uuid, approved_by uuid, committee_name character varying, min_no_member character varying, max_no_member character varying, forming_date timestamp without time zone, purpose character varying, comments character varying, status boolean, owned_by uuid, created_date timestamp without time zone, is_deleted boolean, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid);
