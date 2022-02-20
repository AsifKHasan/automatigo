INSERT INTO inv.item_requisition_detail_feature(id, value, uom_id, item_setup_feature_id, description, name, item_requisition_details_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by)
SELECT id, value, uom_id, item_setup_feature_id, description, name, item_requisition_details_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM dblink('dbname=grp_bcc_live',
'SELECT id, value, uom_id, item_setup_feature_id, description, name, item_requisition_details_id, is_deleted, created_at, updated_at, user_id, employee_id, proxy_user_id, org_id, created_by, last_modified_by
FROM inv.item_requisition_detail_feature')
AS x(id uuid, value character varying, uom_id uuid, item_setup_feature_id uuid, description character varying, name character varying, item_requisition_details_id uuid, is_deleted boolean, created_at timestamp without time zone, updated_at timestamp without time zone, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_by uuid, last_modified_by uuid);
