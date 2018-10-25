#!/bin/sh

service rsyslog start
service cron restart
python /app/run.py
crontab /etc/cron.d/pycron
trap : TERM INT
tail -f /dev/null & wait
