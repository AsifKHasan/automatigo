INSERT INTO prc.component_url_notification(oid, component, url, notification_en, notification_bn, role, created_by, created_on, updated_by, updated_on)
SELECT oid, component, url, notification_en, notification_bn, role, created_by, created_on, updated_by, updated_on
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, component, url, notification_en, notification_bn, role, created_by, created_on, updated_by, updated_on
FROM prc.component_url_notification')
AS x(oid character varying, component character varying, url character varying, notification_en character varying, notification_bn character varying, role character varying, created_by character varying, created_on timestamp without time zone, updated_by character varying, updated_on timestamp without time zone);
