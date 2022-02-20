INSERT INTO ast.asset_information(oid, code, description, status, in_type, tagged_by, tagged_on, temporary_item_oid, item_oid, office_oid, store_oid, created_by, created_on, updated_by, updated_on)
SELECT oid, code, description, status, in_type, tagged_by, tagged_on, temporary_item_oid, item_oid, office_oid, store_oid, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, description, status, in_type, tagged_by, tagged_on, temporary_item_oid, item_oid, office_oid, store_oid, created_by, created_on, updated_by, updated_on
FROM ast.asset_information')
AS x(oid character varying, code character varying, description text, status character varying, in_type character varying, tagged_by character varying, tagged_on timestamp without time zone, temporary_item_oid character varying, item_oid character varying, office_oid character varying, store_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
