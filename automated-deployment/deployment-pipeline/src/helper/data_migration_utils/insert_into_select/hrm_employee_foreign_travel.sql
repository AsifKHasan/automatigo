INSERT INTO hrm.employee_foreign_travel(oid, employee_oid, geo_country_oid, purpose, travel_from, travel_till, created_by, created_on, updated_by, updated_on, is_deleted)
SELECT oid, employee_oid, geo_country_oid, purpose, travel_from, travel_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, geo_country_oid, purpose, travel_from, travel_till, created_by, created_on, updated_by, updated_on, is_deleted
FROM hrm.employee_foreign_travel')
AS x(oid character varying, employee_oid character varying, geo_country_oid character varying, purpose text, travel_from timestamp without time zone, travel_till timestamp without time zone, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone, is_deleted character varying);
