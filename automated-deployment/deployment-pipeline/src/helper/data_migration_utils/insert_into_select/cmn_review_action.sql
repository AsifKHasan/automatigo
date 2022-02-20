INSERT INTO cmn.review_action(oid, request_time, review_time, return_comment, is_complete, is_rejected, is_disabled, is_deleted, source_tbl, source_row_oid, requested_by, assigned_to, review_action_type_oid, forwarded_to)
SELECT oid, request_time, review_time, return_comment, is_complete, is_rejected, is_disabled, is_deleted, source_tbl, source_row_oid, requested_by, assigned_to, review_action_type_oid, forwarded_to
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, request_time, review_time, return_comment, is_complete, is_rejected, is_disabled, is_deleted, source_tbl, source_row_oid, requested_by, assigned_to, review_action_type_oid, forwarded_to
FROM cmn.review_action')
AS x(oid character varying, request_time timestamp without time zone, review_time timestamp without time zone, return_comment text, is_complete character varying, is_rejected character varying, is_disabled character varying, is_deleted character varying, source_tbl character varying, source_row_oid character varying, requested_by character varying, assigned_to character varying, review_action_type_oid character varying, forwarded_to character varying);
