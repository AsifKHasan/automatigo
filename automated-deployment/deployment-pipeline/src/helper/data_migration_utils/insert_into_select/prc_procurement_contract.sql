INSERT INTO prc.procurement_contract(oid, contract_no, app_package_no, contract_signing_date, description, contract_path, status, created_by, created_on, updated_by, updated_on, vendor_oid, office_oid)
SELECT oid, contract_no, app_package_no, contract_signing_date, description, contract_path, status, created_by, created_on, updated_by, updated_on, vendor_oid, office_oid
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, contract_no, app_package_no, contract_signing_date, description, contract_path, status, created_by, created_on, updated_by, updated_on, vendor_oid, office_oid
FROM prc.procurement_contract')
AS x(oid character varying, contract_no character varying, app_package_no character varying, contract_signing_date date, description character varying, contract_path character varying, status character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, vendor_oid character varying, office_oid character varying);
