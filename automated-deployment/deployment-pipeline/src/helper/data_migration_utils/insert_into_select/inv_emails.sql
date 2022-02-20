INSERT INTO inv.emails(id, notification_id, cc, bcc, recipients, subject, attachments)
SELECT id, notification_id, cc, bcc, recipients, subject, attachments
FROM dblink('dbname=grp_bcc_live',
'SELECT id, notification_id, cc, bcc, recipients, subject, attachments
FROM inv.emails')
AS x(id uuid, notification_id uuid, cc text, bcc text, recipients text, subject character varying, attachments character varying);
