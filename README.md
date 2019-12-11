[![GitHub issues](https://img.shields.io/github/release/RedisLabsModules/ModuleBuildDocker.svg?kill_cache=1)](https://github.com/RedisLabsModules/ModuleBuildDocker/releases/latest)
[![CircleCI](https://circleci.com/gh/RedisLabsModules/ModuleBuildDocker/tree/master.svg?style=svg)](https://circleci.com/gh/RedisLabsModules/ModuleBuildDocker/tree/master)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/redislabsmodules/rmbuilder.svg)](https://hub.docker.com/r/redislabsmodules/rmbuilder/builds/)

# ModuleBuildDocker
Docker file for creating the base image for module build environments

# Example Dockerfile using this image:

```docker
FROM redislabsmodules/rmbuilder:latest

# Build the source
ADD ./src /src
WORKDIR /src

CMD make distclean && make -j 4 && make package
```

# Another example Dockerfile:

```docker
FROM redisfab/rmbuilder:x64-buster

# Build the source
ADD ./src /src
WORKDIR /src

CMD make distclean && make -j 4 && make package
```
