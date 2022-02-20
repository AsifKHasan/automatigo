INSERT INTO ast.direct_out(oid, code, remarks, status, requested_by, requested_on, decision_by, decision_on, store_oid, office_oid, user_oid, office_unit_oid, office_unit_post_oid, purpose_oid, asset_alloc_oid, allocation_date, created_by, created_on, updated_by, updated_on)
SELECT oid, code, remarks, status, requested_by, requested_on, decision_by, decision_on, store_oid, office_oid, user_oid, office_unit_oid, office_unit_post_oid, purpose_oid, asset_alloc_oid, allocation_date, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, remarks, status, requested_by, requested_on, decision_by, decision_on, store_oid, office_oid, user_oid, office_unit_oid, office_unit_post_oid, purpose_oid, asset_alloc_oid, allocation_date, created_by, created_on, updated_by, updated_on
FROM ast.direct_out')
AS x(oid character varying, code character varying, remarks character varying, status character varying, requested_by character varying, requested_on date, decision_by character varying, decision_on date, store_oid character varying, office_oid character varying, user_oid character varying, office_unit_oid character varying, office_unit_post_oid character varying, purpose_oid character varying, asset_alloc_oid character varying, allocation_date date, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
