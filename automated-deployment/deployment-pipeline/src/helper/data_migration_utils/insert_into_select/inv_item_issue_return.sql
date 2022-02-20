INSERT INTO inv.item_issue_return(store_id, item_id, item_requisition_issue_id, uom_id, returned_by, returned_qty, comments, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by)
SELECT store_id, item_id, item_requisition_issue_id, uom_id, returned_by, returned_qty, comments, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT store_id, item_id, item_requisition_issue_id, uom_id, returned_by, returned_qty, comments, id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by
FROM inv.item_issue_return')
AS x(store_id uuid, item_id uuid, item_requisition_issue_id uuid, uom_id uuid, returned_by uuid, returned_qty numeric, comments character varying, id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid);
