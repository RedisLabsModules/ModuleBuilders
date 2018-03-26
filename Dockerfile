FROM redis:4.0.7

ENV LIBDIR /usr/lib/redis/modules
ENV DEPS "python python-setuptools python-pip build-essential wget autoconf libtool automake git openssh-client python-dev"
# Set up a build environment
RUN set -ex;\
    deps="$DEPS";\
    apt-get update; \
    apt-get install -y --no-install-recommends $deps;
# Instal python deps
RUN set -ex; \
    pip install -U rmtest ramp-packer awscli mkdocs mkdocs-material mkdocs-extensions;

