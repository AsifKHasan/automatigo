INSERT INTO cmn.stakeholder(oid, created_by, created_on, updated_by, updated_on, is_deleted, name_en, name_bn, gateway_address, stackholder_id)
SELECT oid, created_by, created_on, updated_by, updated_on, is_deleted, name_en, name_bn, gateway_address, stackholder_id
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, created_by, created_on, updated_by, updated_on, is_deleted, name_en, name_bn, gateway_address, stackholder_id
FROM cmn.stakeholder')
AS x(oid character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying, name_en character varying, name_bn character varying, gateway_address character varying, stackholder_id character varying);
