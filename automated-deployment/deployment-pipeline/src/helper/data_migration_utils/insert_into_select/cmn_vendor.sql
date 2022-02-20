INSERT INTO cmn.vendor(oid, code, name_en, name_bn, contact_address, contact_no, email, billing_address, description, status, created_by, created_on, updated_by, updated_on)
SELECT oid, code, name_en, name_bn, contact_address, contact_no, email, billing_address, description, status, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, code, name_en, name_bn, contact_address, contact_no, email, billing_address, description, status, created_by, created_on, updated_by, updated_on
FROM cmn.vendor')
AS x(oid character varying, code character varying, name_en character varying, name_bn character varying, contact_address character varying, contact_no character varying, email character varying, billing_address character varying, description text, status character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
