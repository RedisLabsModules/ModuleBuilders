FROM redis:latest

ENV LIBDIR /usr/lib/redis/modules
ENV DEPS "python python-setuptools python-pip build-essential wget autoconf libtool automake git openssh-client"
# Set up a build environment
RUN set -ex;\
    deps="$DEPS";\
    apt-get update; \
    apt-get install -y --no-install-recommends $deps;
# Instal python deps
RUN set -ex; \
    pip install rmtest ramp-packer awscli;

