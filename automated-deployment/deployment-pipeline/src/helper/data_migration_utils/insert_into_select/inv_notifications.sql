INSERT INTO inv.notifications(id, content, sender, sent_on, request_id)
SELECT id, content, sender, sent_on, request_id
FROM dblink('dbname=grp_bcc_live',
'SELECT id, content, sender, sent_on, request_id
FROM inv.notifications')
AS x(id uuid, content text, sender text, sent_on timestamp without time zone, request_id uuid);
