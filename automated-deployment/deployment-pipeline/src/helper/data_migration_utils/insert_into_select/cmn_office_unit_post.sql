INSERT INTO cmn.office_unit_post(oid, post_oid, display_order, business_order, parent_oid, office_unit_oid, phone_no, is_deleted, created_by, created_on, updated_by, updated_on)
SELECT oid, post_oid, display_order, business_order, parent_oid, office_unit_oid, phone_no, is_deleted, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, post_oid, display_order, business_order, parent_oid, office_unit_oid, phone_no, is_deleted, created_by, created_on, updated_by, updated_on
FROM cmn.office_unit_post')
AS x(oid character varying, post_oid character varying, display_order numeric, business_order numeric, parent_oid character varying, office_unit_oid character varying, phone_no character varying, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
