INSERT INTO inv.direct_stock_out(id, store_id, reference_no, status, direct_stock_out_date, approved_by, issued_to, received_by, approval_date, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, store_id, reference_no, status, direct_stock_out_date, approved_by, issued_to, received_by, approval_date, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, store_id, reference_no, status, direct_stock_out_date, approved_by, issued_to, received_by, approval_date, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.direct_stock_out')
AS x(id uuid, store_id uuid, reference_no character varying, status character varying, direct_stock_out_date timestamp without time zone, approved_by uuid, issued_to uuid, received_by uuid, approval_date timestamp without time zone, comments character varying, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);