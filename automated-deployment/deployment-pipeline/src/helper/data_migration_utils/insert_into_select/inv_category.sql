INSERT INTO inv.category(category_id, parent_category_id, cat_name, bn_cat_name, cat_description, status, owned_by, created_date, is_deleted, is_trackable, accounts_category, user_id, employee_id, proxy_user_id, org_id)
SELECT category_id, parent_category_id, cat_name, bn_cat_name, cat_description, status, owned_by, created_date, is_deleted, is_trackable, accounts_category, user_id, employee_id, proxy_user_id, org_id
FROM dblink('dbname=grp_bcc_live',
'SELECT category_id, parent_category_id, cat_name, bn_cat_name, cat_description, status, owned_by, created_date, is_deleted, is_trackable, accounts_category, user_id, employee_id, proxy_user_id, org_id
FROM inv.category')
AS x(category_id uuid, parent_category_id uuid, cat_name character varying, bn_cat_name character varying, cat_description character varying, status boolean, owned_by uuid, created_date timestamp without time zone, is_deleted boolean, is_trackable boolean, accounts_category character varying, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid);
