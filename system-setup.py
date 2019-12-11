#!/usr/bin/env python2

import sys
import os
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

        self.install("git")
        self.install("coreutils") # for realpath

    #------------------------------------------------------------------------------------------
    def debian_compat(self):
        self.install("build-essential")

        self.install("python-regex")

        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def redhat_compat(self):
        self.group_install("'Development Tools'")
        self.install("redhat-lsb-core")

        self.install("epel-release")
        self.install("python2-regex")

        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def fedora(self):
        self.group_install("'Development Tools'")
        self.install("python2-regex")
        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def macosx(self):
        p = Popen('xcode-select -p', stdout=PIPE, close_fds=True, shell=True)
        out, _ = p.communicate()
        if out.splitlines() == []:
            fatal("Xcode tools are not installed. Please run xcode-select --install.")

        self.install("redis")
        self.install("binutils") # into /usr/local/opt/binutils

        self.install("git-lfs")

    #------------------------------------------------------------------------------------------

    def common_last(self):
        self.install("valgrind")

        self.pip_install("mkdocs mkdocs-material mkdocs-extensions")
        self.pip_install("pytest redis redis-py-cluster rmtest")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisModuleBuilderSetup(nop = args.nop).setup()
