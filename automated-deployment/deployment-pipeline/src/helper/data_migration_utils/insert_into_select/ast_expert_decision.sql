INSERT INTO ast.expert_decision(oid, code, maintenance_cost, maintenance_vendor_name, maintenance_date, maintenance_remarks, disposal_cost, disposal_vendor_name, disposal_process, asset_oid, decision_by, decision_on, disposal_remarks, status, store_oid, office_oid, created_by, created_on, updated_by, updated_on)
SELECT oid, code, maintenance_cost, maintenance_vendor_name, maintenance_date, maintenance_remarks, disposal_cost, disposal_vendor_name, disposal_process, asset_oid, decision_by, decision_on, disposal_remarks, status, store_oid, office_oid, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, maintenance_cost, maintenance_vendor_name, maintenance_date, maintenance_remarks, disposal_cost, disposal_vendor_name, disposal_process, asset_oid, decision_by, decision_on, disposal_remarks, status, store_oid, office_oid, created_by, created_on, updated_by, updated_on
FROM ast.expert_decision')
AS x(oid character varying, code character varying, maintenance_cost character varying, maintenance_vendor_name character varying, maintenance_date date, maintenance_remarks character varying, disposal_cost character varying, disposal_vendor_name character varying, disposal_process character varying, asset_oid character varying, decision_by character varying, decision_on date, disposal_remarks character varying, status character varying, store_oid character varying, office_oid character varying, created_by character varying, created_on date, updated_by character varying, updated_on date);
