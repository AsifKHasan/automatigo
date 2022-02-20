INSERT INTO hrm.grade(oid, name_en, name_bn, sort_order, cadre_oid, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, name_en, name_bn, sort_order, cadre_oid, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, sort_order, cadre_oid, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.grade')
AS x(oid character varying, name_en character varying, name_bn character varying, sort_order numeric, cadre_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
