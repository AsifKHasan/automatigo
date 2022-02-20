INSERT INTO inv.item_setup_feature(id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, item_uom_id, name, bn_name, item_setup_id, item_feature_category_id, uom_id, is_mandatory, is_unique)
SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, item_uom_id, name, bn_name, item_setup_id, item_feature_category_id, uom_id, is_mandatory, is_unique
FROM dblink('dbname=grp_bcc_live',
'SELECT id, user_id, employee_id, proxy_user_id, org_id, created_at, updated_at, is_deleted, created_by, last_modified_by, item_uom_id, name, bn_name, item_setup_id, item_feature_category_id, uom_id, is_mandatory, is_unique
FROM inv.item_setup_feature')
AS x(id uuid, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid, created_at timestamp without time zone, updated_at timestamp without time zone, is_deleted boolean, created_by uuid, last_modified_by uuid, item_uom_id uuid, name character varying, bn_name character varying, item_setup_id uuid, item_feature_category_id uuid, uom_id uuid, is_mandatory boolean, is_unique boolean);
