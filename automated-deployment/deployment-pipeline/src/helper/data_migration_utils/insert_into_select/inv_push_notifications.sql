INSERT INTO inv.push_notifications(id, notification_id, is_viewed, is_clicked, type, recipient)
SELECT id, notification_id, is_viewed, is_clicked, type, recipient
FROM dblink('dbname=grp_bcc_live',
'SELECT id, notification_id, is_viewed, is_clicked, type, recipient
FROM inv.push_notifications')
AS x(id uuid, notification_id uuid, is_viewed boolean, is_clicked boolean, type character varying, recipient uuid);
