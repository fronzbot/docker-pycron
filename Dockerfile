FROM python:3.7-slim-stretch
LABEL maintainer="Kevin Fronczak <kfronczak@gmail.com>"

VOLUME /work
VOLUME /share

RUN mkdir /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cron \
    ffmpeg \
    imagemagick \
    gifsicle \
    libav-tools \
    rsyslog \
    logrotate && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY VERSION VERSION
COPY app/ .
COPY system/rsyslog.conf /etc/rsyslog.conf

RUN python setup.py bdist_wheel && pip install dist/*.whl
RUN rm -rf build dist *egg.info

WORKDIR /work
RUN chmod +x /app/start.sh
RUN chmod +x /app/run.py

CMD ["/app/start.sh"]
