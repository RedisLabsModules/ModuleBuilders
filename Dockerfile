FROM redis:5.0.4

ENV LIBDIR /usr/lib/redis/modules
ENV DEPS "python python-setuptools python-pip build-essential wget autoconf libtool automake git openssh-client python-dev cmake"
ENV PYDEPS "rmtest ramp-packer awscli mkdocs mkdocs-material mkdocs-extensions"

# Set up a build environment
RUN set -ex;\
    deps="$DEPS";\
    apt-get update; \
    apt-get install -y --no-install-recommends $deps;

# Install python deps
RUN set -ex; \
    pip install -U $PYDEPS;
