INSERT INTO cmn.review_action_type(oid, name_en, name_bn, priority, is_deleted, created_by, created_on, updated_by, updated_on)
SELECT oid, name_en, name_bn, priority, is_deleted, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, priority, is_deleted, created_by, created_on, updated_by, updated_on
FROM cmn.review_action_type')
AS x(oid character varying, name_en character varying, name_bn character varying, priority numeric, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
