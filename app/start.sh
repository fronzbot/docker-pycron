#!/bin/sh
service rsyslog start
service cron restart
crontab -r

# Install user-generated requirements files
if [ -e /work/my_requirements.txt ]
then
    pip install -r /work/my_requirements.txt
fi

# If config.yaml doesn't exist, use the example version
if [ ! -e /work/config.yaml ]
then
    cp /app/config.yaml.example /work/config.yaml
    cp /app/example.py /work/example.py
fi

python /app/run.py
crontab /etc/cron.d/pycron

trap : TERM INT
tail -f /var/log/syslog & wait
