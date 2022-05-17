
FROM debian:bullseye

ENV HUGO_VER=0.88.1

RUN apt-get update -qq
RUN apt-get install -y ca-certificates wget curl rsync

RUN apt-get install -y python3-pip python3-yaml
RUN python3 -m pip install --upgrade pip

RUN apt-get install -y nodejs npm
RUN npm install -g npm

RUN wget -q -O /tmp/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VER}/hugo_extended_${HUGO_VER}_Linux-64bit.deb
RUN dpkg -i /tmp/hugo.deb
