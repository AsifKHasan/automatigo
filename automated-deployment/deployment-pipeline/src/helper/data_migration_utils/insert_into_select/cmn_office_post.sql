INSERT INTO cmn.office_post(oid, created_by, created_on, updated_by, updated_on, is_deleted, office_oid, post_oid)
SELECT oid, created_by, created_on, updated_by, updated_on, is_deleted, office_oid, post_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, is_deleted, office_oid, post_oid
FROM cmn.office_post')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying, office_oid character varying, post_oid character varying);
