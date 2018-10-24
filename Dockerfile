FROM python:3.7-alpine
LABEL maintainer="Kevin Fronczak <kfronczak@gmail.com>"

VOLUME /work
VOLUME /share

RUN mkdir /app
WORKDIR /app

RUN apk update && \
    apk add libxml2-dev \
            libxslt-dev \
            libffi-dev \
            libgcc \
            gcc \
            g++ \
            musl-dev \
            musl \
            openssl-dev \
            curl \
            bash \
            dcron \
            sdl2 \
            ffmpeg \
            ffmpeg-libs \
            jpeg-dev \
            openjpeg-dev \
            tiff-dev \
            zlib-dev \
            freetype-dev \
            lcms2-dev \
            tk-dev \
            tcl-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY VERSION VERSION
COPY app/ .
COPY app/config.yaml.example /work

WORKDIR /work

RUN ["chmod", "+x", "/app/start.sh"]
RUN ["chmod", "+x", "/app/run.py"]

CMD ["/app/start.sh"]
