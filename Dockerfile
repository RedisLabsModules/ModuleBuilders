FROM redis:5.0.5

ENV LIBDIR /usr/lib/redis/modules

# Set up a build environment
RUN apt-get -qq update
RUN apt-get -q install -y --no-install-recommends python python-setuptools python-pip python-dev
RUN apt-get -q install -y --no-install-recommends wget curl ca-certificates openssh-client awscli
RUN apt-get -q install -y --no-install-recommends build-essential autoconf libtool automake git
RUN set -e ;\
	curl -s -o /tmp/cmake.sh https://cmake.org/files/v3.14/cmake-3.14.5-Linux-x86_64.sh ;\
	bash /tmp/cmake.sh 

# Install python deps
RUN pip install -U git+https://github.com/RedisLabsModules/RLTest.git@master
RUN pip install -U git+https://github.com/RedisLabs/RAMP.git@master
RUN pip install mkdocs mkdocs-material mkdocs-extensions
