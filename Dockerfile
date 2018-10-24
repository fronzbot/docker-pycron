FROM python:3.7-alpine

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

WORKDIR /app
ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD VERSION /app

VOLUME /work /share
