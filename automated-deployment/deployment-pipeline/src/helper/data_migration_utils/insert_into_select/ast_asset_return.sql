INSERT INTO ast.asset_return(oid, code, requester_oid, filepath, requested_date, decided_by, decision_date, status, qc_by, qc_on, store_oid, office_oid, asset_allocation_oid, created_by, created_on, updated_by, updated_on)
SELECT oid, code, requester_oid, filepath, requested_date, decided_by, decision_date, status, qc_by, qc_on, store_oid, office_oid, asset_allocation_oid, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, requester_oid, filepath, requested_date, decided_by, decision_date, status, qc_by, qc_on, store_oid, office_oid, asset_allocation_oid, created_by, created_on, updated_by, updated_on
FROM ast.asset_return')
AS x(oid character varying, code character varying, requester_oid character varying, filepath character varying, requested_date date, decided_by character varying, decision_date date, status character varying, qc_by character varying, qc_on date, store_oid character varying, office_oid character varying, asset_allocation_oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
