FROM ubuntu:22.04
RUN apt-get update && apt-get install -y \
    build-essential \
    libhidapi-dev \
    libc6-dev
WORKDIR /app
COPY libspectr.c libspectr.h hid.c hidapi.h .