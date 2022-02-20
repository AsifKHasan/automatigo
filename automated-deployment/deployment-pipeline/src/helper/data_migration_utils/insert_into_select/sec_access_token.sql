INSERT INTO sec.access_token(ac_id, token_id, token, authentication_id, username, client_id, authentication, refresh_token)
SELECT ac_id, token_id, token, authentication_id, username, client_id, authentication, refresh_token
FROM dblink('dbname=grp_bcc_live',
'SELECT ac_id, token_id, token, authentication_id, username, client_id, authentication, refresh_token
FROM sec.access_token')
AS x(ac_id text, token_id text, token text, authentication_id text, username character varying, client_id character varying, authentication text, refresh_token text);
