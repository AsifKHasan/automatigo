INSERT INTO inv.item_feature(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, item_uom_id, value, bn_value, description, name, item_id, item_setup_feature_id, uom_id)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, item_uom_id, value, bn_value, description, name, item_id, item_setup_feature_id, uom_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, item_uom_id, value, bn_value, description, name, item_id, item_setup_feature_id, uom_id
FROM inv.item_feature')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, item_uom_id uuid, value character varying, bn_value character varying, description character varying, name character varying, item_id uuid, item_setup_feature_id uuid, uom_id uuid);
