INSERT INTO cmn.review_action_detail(oid, audited_qty, status, remarks, is_deleted, created_by, created_on, updated_by, updated_on, review_action_oid, review_action_type_oid, item_requisition_detail_oid)
SELECT oid, audited_qty, status, remarks, is_deleted, created_by, created_on, updated_by, updated_on, review_action_oid, review_action_type_oid, item_requisition_detail_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, audited_qty, status, remarks, is_deleted, created_by, created_on, updated_by, updated_on, review_action_oid, review_action_type_oid, item_requisition_detail_oid
FROM cmn.review_action_detail')
AS x(oid character varying, audited_qty numeric, status character varying, remarks text, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, review_action_oid character varying, review_action_type_oid character varying, item_requisition_detail_oid character varying);
