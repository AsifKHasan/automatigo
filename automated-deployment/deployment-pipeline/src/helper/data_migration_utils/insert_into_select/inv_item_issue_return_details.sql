INSERT INTO inv.item_issue_return_details(item_issue_return_details_id, item_issue_return_id, item_id, unit_id, approved_qty, issued_qty, return_qty, comments, owned_by, created_date, is_deleted)
SELECT item_issue_return_details_id, item_issue_return_id, item_id, unit_id, approved_qty, issued_qty, return_qty, comments, owned_by, created_date, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT item_issue_return_details_id, item_issue_return_id, item_id, unit_id, approved_qty, issued_qty, return_qty, comments, owned_by, created_date, is_deleted
FROM inv.item_issue_return_details')
AS x(item_issue_return_details_id uuid, item_issue_return_id uuid, item_id uuid, unit_id uuid, approved_qty numeric, issued_qty numeric, return_qty numeric, comments character varying, owned_by uuid, created_date timestamp without time zone, is_deleted boolean);
