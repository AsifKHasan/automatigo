INSERT INTO inv.item_requisition_details(id, requisition_id, item_id, uom_id, required_qty, approved_qty, revised_qty, committee_approved_qty, item_approval, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, entitlement_id, last_modified_by, entitlement_item_id)
SELECT id, requisition_id, item_id, uom_id, required_qty, approved_qty, revised_qty, committee_approved_qty, item_approval, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, entitlement_id, last_modified_by, entitlement_item_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, requisition_id, item_id, uom_id, required_qty, approved_qty, revised_qty, committee_approved_qty, item_approval, comments, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, entitlement_id, last_modified_by, entitlement_item_id
FROM inv.item_requisition_details')
AS x(id uuid, requisition_id uuid, item_id uuid, uom_id uuid, required_qty numeric, approved_qty numeric, revised_qty numeric, committee_approved_qty numeric, item_approval boolean, comments character varying, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, entitlement_id uuid, last_modified_by uuid, entitlement_item_id uuid);
