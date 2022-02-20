INSERT INTO hrm.address_info(oid, village_house_no_road_no, police_station, post_office, postal_code, district_oid, division_oid, country_oid, phone_no, is_deleted, created_by, created_on, updated_by, updated_on)
SELECT oid, village_house_no_road_no, police_station, post_office, postal_code, district_oid, division_oid, country_oid, phone_no, is_deleted, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, village_house_no_road_no, police_station, post_office, postal_code, district_oid, division_oid, country_oid, phone_no, is_deleted, created_by, created_on, updated_by, updated_on
FROM hrm.address_info')
AS x(oid character varying, village_house_no_road_no character varying, police_station character varying, post_office character varying, postal_code character varying, district_oid character varying, division_oid character varying, country_oid character varying, phone_no character varying, is_deleted character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
