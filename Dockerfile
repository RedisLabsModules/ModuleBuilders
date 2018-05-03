FROM redis:latest

ENV LIBDIR /usr/lib/redis/modules
ENV DEPS "python python-setuptools python-pip build-essential wget autoconf libtool automake git openssh-client python-dev"

# Set up a build environment
RUN set -ex;\
    deps="$DEPS";\
    apt-get update; \
    apt-get install -y --no-install-recommends $deps;

# Install python deps
RUN set -ex; \
    pip install -U rmtest ramp-packer awscli mkdocs mkdocs-material mkdocs-extensions;

# Install docker cli
RUN set -ex; \
    VER="18.03.1-ce"; \
    wget -O /tmp/docker-$VER.tgz https://download.docker.com/linux/static/stable/x86_64/docker-$VER.tgz; \
    tar -xz -C /tmp -f /tmp/docker-$VER.tgz; \
    mv /tmp/docker/* /usr/bin;

