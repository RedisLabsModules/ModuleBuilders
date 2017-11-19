# ModuleBuildDocker
Docker file for creating the base image for module build environments

# Docker Hub Repo

[https://hub.docker.com/r/redislabsmodules/rmbuilder/](https://hub.docker.com/r/redislabsmodules/rmbuilder/)

# Example Dockerfile using this image:

```docker
FROM redislabsmodules/rmbuilder:latest

# Build the source
ADD ./src /src
WORKDIR /src

CMD make distclean && make -j 4 && make package
```
