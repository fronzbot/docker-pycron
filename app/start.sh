#!/bin/sh
service rsyslog start
service cron restart
crontab -r

echo "module(load='imudp')" >> /etc/rsyslog.conf
echo "input(type='imudp' port='514')" >> /etc/rsyslog.conf
service rsyslog restart

if [ -e /work/my_requirements.txt ]
then
    pip install -r /work/my_requirements.txt
fi

python /app/run.py
crontab /etc/cron.d/pycron

trap : TERM INT
tail -f /var/log/syslog & wait
