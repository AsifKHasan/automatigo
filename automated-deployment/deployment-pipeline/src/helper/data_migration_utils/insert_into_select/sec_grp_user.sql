INSERT INTO sec.grp_user(oid, username, email, password, employee_oid, status, account_expired, credentials_expired, account_locked)
SELECT oid, username, email, password, employee_oid, status, account_expired, credentials_expired, account_locked
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, username, email, password, employee_oid, status, account_expired, credentials_expired, account_locked
FROM sec.grp_user')
AS x(oid character varying, username character varying, email character varying, password character varying, employee_oid character varying, status character varying, account_expired character varying, credentials_expired character varying, account_locked character varying);
