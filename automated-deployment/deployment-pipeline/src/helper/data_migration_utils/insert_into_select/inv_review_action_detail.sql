INSERT INTO inv.review_action_detail(id, review_action_id, detail_id, audited_qty, status, remark, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, review_action_id, detail_id, audited_qty, status, remark, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, review_action_id, detail_id, audited_qty, status, remark, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.review_action_detail')
AS x(id uuid, review_action_id uuid, detail_id uuid, audited_qty numeric, status boolean, remark character varying, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);
