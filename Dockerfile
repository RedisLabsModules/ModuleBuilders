# BUILD redisfab/rmbuilder:${REDIS_VER}-${ARCH}-${OSNICK}

ARG REDIS_VER=6.0.1

# OSNICK=bionic|stretch|buster
ARG OSNICK=buster

# OS=debian:buster-slim|debian:stretch-slim|ubuntu:bionic
ARG OS=debian:buster-slim

# ARCH=x64|arm64v8|arm32v7
ARG ARCH=x64

#----------------------------------------------------------------------------------------------
FROM redisfab/redis:${REDIS_VER}-${ARCH}-${OSNICK} AS redis
FROM ${OS}

WORKDIR /build
COPY --from=redis /usr/local/ /usr/local/

ADD ./ /build
WORKDIR /build

RUN ./deps/readies/bin/getpy2
RUN ./system-setup.py

RUN ./modules/gears/system-setup.py
RUN ./modules/graph/system-setup.py
RUN ./modules/search/system-setup.py
RUN ./modules/timeseries/system-setup.py

RUN ./deps/readies/bin/getpy3
RUN ./system-setup-docs.py

RUN ./modules/ai/system-setup.py
