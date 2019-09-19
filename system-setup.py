#!/usr/bin/env python2

import sys
import os
from subprocess import Popen, PIPE
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "deps/readies"))
import paella

#----------------------------------------------------------------------------------------------

class RedisModuleBuilderSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    #------------------------------------------------------------------------------------------
    def common_first(self):
        self.install_downloaders()
        self.setup_pip()
        self.pip_install("wheel")
        self.pip_install("setuptools --upgrade")

        self.install("git cmake patchelf awscli jq zip unzip")
        self.install("coreutils") # for realpath

    #------------------------------------------------------------------------------------------
    def debian_compat(self):
        self.install("build-essential")
        self.install("autotools-dev autoconf libtool")

        # python 2
        self.install("python-psutil python-regex")
        self.install("python-gevent") # pip cannot build gevent on ARM
        self.pip_install("virtualenv")

        # python 3
        self.install("python3 python3-venv python3-psutil")
        self.install("python3-networkx python3-numpy python3-skimage")

        self.install("sudo")
        self.install("zlib1g-dev libssl-dev libreadline-dev libffi-dev")
        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def redhat_compat(self):
        self.group_install("'Development Tools'")
        self.install("redhat-lsb-core")

        self.install("epel-release")
        self.install("python36 python36-pip")
        self.install("python36-psutil")

        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def fedora(self):
        self.group_install("'Development Tools'")
        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def macosx(self):
        p = Popen('xcode-select -p', stdout=PIPE, close_fds=True, shell=True)
        out, _ = p.communicate()
        if out.splitlines() == []:
            fatal("Xcode tools are not installed. Please run xcode-select --install.")

        self.install("libtool autoconf automake llvm")
        self.install("zlib openssl readline")
        self.install("redis")
        self.install("binutils") # into /usr/local/opt/binutils

        self.pip_install("pipenv")
        self.pip_install("gevent")

        self.install("git-lfs")

    #------------------------------------------------------------------------------------------

    def common_last(self):
        # RLTest before RAMP due to redis<->redis-py-cluster version dependency
        # if not self.has_command("RLTest"):
        #     self.pip_install("git+https://github.com/RedisLabsModules/RLTest.git@master")
        # if not self.has_command("ramp"):
        #     self.pip_install("git+https://github.com/RedisLabs/RAMP@master")
        # self.pip_install("redis-py-cluster")

        self.pip_install("mkdocs mkdocs-material mkdocs-extensions")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisModuleBuilderSetup(nop = args.nop).setup()
