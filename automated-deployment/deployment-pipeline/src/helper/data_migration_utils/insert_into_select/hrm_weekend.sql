INSERT INTO hrm.weekend(oid, announce_date, week_day, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, announce_date, week_day, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, announce_date, week_day, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.weekend')
AS x(oid character varying, announce_date timestamp without time zone, week_day character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
