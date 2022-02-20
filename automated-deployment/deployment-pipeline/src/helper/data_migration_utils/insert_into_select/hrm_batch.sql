INSERT INTO hrm.batch(oid, name_en, name_bn, batch_year_en, batch_year_bn, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, name_en, name_bn, batch_year_en, batch_year_bn, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, batch_year_en, batch_year_bn, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.batch')
AS x(oid character varying, name_en character varying, name_bn character varying, batch_year_en character varying, batch_year_bn character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
