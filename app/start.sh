#!/bin/sh

python /app/run.py
crond -b -l 8 -L /work/cron.log
trap : TERM INT
tail -f /dev/null & wait
