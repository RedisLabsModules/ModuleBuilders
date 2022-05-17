# docker run -it --user 1000:1000 IMAGE bash

ARG USERID=1000
ARG GROUPID=1000

FROM ubuntu:focal

ARG USERID
ARG GROUPID

RUN apt-get -qq update
RUN apt install -y sudo

RUN echo "CREATE_HOME yes" >> /etc/login.defs
RUN echo "user    ALL=(ALL:ALL) ALL" >> /etc/sudoers

RUN groupadd -g ${USERID} user
RUN useradd -d /home/user -g ${GROUPID} -u ${USERID} user
RUN bash -c 'echo -e "user\nuser" | passwd user'

WORKDIR /home/user
USER user
