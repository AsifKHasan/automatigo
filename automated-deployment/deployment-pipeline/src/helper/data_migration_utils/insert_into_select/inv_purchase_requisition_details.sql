INSERT INTO inv.purchase_requisition_details(id, requisition_id, item_id, uom_id, required_qty, approved_qty, revised_qty, committee_approved_qty, item_approval, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, requisition_id, item_id, uom_id, required_qty, approved_qty, revised_qty, committee_approved_qty, item_approval, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, requisition_id, item_id, uom_id, required_qty, approved_qty, revised_qty, committee_approved_qty, item_approval, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.purchase_requisition_details')
AS x(id uuid, requisition_id uuid, item_id uuid, uom_id uuid, required_qty integer, approved_qty integer, revised_qty integer, committee_approved_qty integer, item_approval boolean, comments character varying, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);
