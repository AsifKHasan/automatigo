INSERT INTO inv.uom(id, uom_id, bn_uom_id, uom_type_id, abbreviation, description, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id)
SELECT id, uom_id, bn_uom_id, uom_type_id, abbreviation, description, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, uom_id, bn_uom_id, uom_type_id, abbreviation, description, created_date, is_deleted, user_id, employee_id, proxy_user_id, org_id
FROM inv.uom')
AS x(id uuid, uom_id character varying, bn_uom_id character varying, uom_type_id character varying, abbreviation character varying, description character varying, created_date timestamp without time zone, is_deleted boolean, user_id uuid, employee_id uuid, proxy_user_id uuid, org_id uuid);
