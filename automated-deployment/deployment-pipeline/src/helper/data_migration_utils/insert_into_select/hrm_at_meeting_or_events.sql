INSERT INTO hrm.at_meeting_or_events(oid, employee_oid, meeting_or_event_venue, meeting_time, attendance_id)
SELECT oid, employee_oid, meeting_or_event_venue, meeting_time, attendance_id
FROM dblink('dbname=grp_bcc_live',
'SELECT oid, employee_oid, meeting_or_event_venue, meeting_time, attendance_id
FROM hrm.at_meeting_or_events')
AS x(oid character varying, employee_oid character varying, meeting_or_event_venue character varying, meeting_time timestamp without time zone, attendance_id character varying);
