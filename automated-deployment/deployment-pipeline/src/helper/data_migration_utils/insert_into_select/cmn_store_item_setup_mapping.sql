INSERT INTO cmn.store_item_setup_mapping(oid, is_deleted, created_by, created_on, updated_by, updated_on, store_oid, item_group_oid)
SELECT oid, is_deleted, created_by, created_on, updated_by, updated_on, store_oid, item_group_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, is_deleted, created_by, created_on, updated_by, updated_on, store_oid, item_group_oid
FROM cmn.store_item_setup_mapping')
AS x(oid character varying, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, store_oid character varying, item_group_oid character varying);
