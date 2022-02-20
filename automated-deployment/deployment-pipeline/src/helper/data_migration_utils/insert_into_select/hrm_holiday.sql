INSERT INTO hrm.holiday(oid, name_en, name_bn, holiday_date, depends_on_moon, is_multi_dated, from_date, to_date, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, name_en, name_bn, holiday_date, depends_on_moon, is_multi_dated, from_date, to_date, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, name_en, name_bn, holiday_date, depends_on_moon, is_multi_dated, from_date, to_date, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.holiday')
AS x(oid character varying, name_en character varying, name_bn character varying, holiday_date timestamp without time zone, depends_on_moon character varying, is_multi_dated character varying, from_date timestamp without time zone, to_date timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
