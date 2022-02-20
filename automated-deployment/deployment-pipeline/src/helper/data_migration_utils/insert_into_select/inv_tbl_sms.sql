INSERT INTO inv.tbl_sms(id, notification_id, recipients)
SELECT id, notification_id, recipients
FROM dblink('dbname=grp_bcc_live',
'SELECT id, notification_id, recipients
FROM inv.tbl_sms')
AS x(id uuid, notification_id uuid, recipients text);
