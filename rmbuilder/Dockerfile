# BUILD redisfab/rmbuilder:${REDIS_VER}-${ARCH}-${OSNICK}

ARG REDIS_VER=6.2.3

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

ADD rmbuilder/* /build/
ADD deps/ /build/deps

RUN ./deps/readies/bin/getpy2
RUN ./deps/readies/bin/getpy3
RUN python2 ./system-setup.py
RUN python3 ./system-setup.py

RUN python2 ./gears/system-setup.py
RUN python3 ./graph/system-setup.py
RUN python2 ./search/system-setup.py
RUN python2 ./rscoordinator/system-setup.py
RUN python3 ./timeseries/system-setup.py
RUN python3 ./ai/system-setup.py
RUN python3 ./redisjson/system-setup.py

RUN ./system-setup-docs.py
