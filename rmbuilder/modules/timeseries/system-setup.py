#!/usr/bin/env python2

import sys
import os
import argparse

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
READIES = os.path.join(ROOT, "deps/readies")
sys.path.insert(0, READIES)
import paella

#----------------------------------------------------------------------------------------------

class RedisTimeSeriesSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        self.pip_install("wheel")
        self.pip_install("setuptools --upgrade")

        self.install("git jq curl")

    def debian_compat(self):
        self.run("%s/bin/getgcc" % READIES)

    def redhat_compat(self):
        self.run("%s/bin/getgcc" % READIES)
        self.install("redhat-lsb-core")
        self.run("%s/bin/getepel" % READIES)
        if self.dist == "amzn":
            self.run("amazon-linux-extras install epel")
            self.install("python3-devel")
        else:
            self.install("python3-devel libaec-devel")

    def fedora(self):
        self.run("%s/bin/getgcc" % READIES)
        self.install("python3-networkx")

    def archlinux(self):
        self.install("lcov-git", aur=True)

    def macos(self):
        self.install_gnu_utils()
        self.install("redis")

    def freebsd(self):
        self.install_gnu_utils()

    def common_last(self):
        if not self.has_command("lcov"):
            self.install("lcov")
        self.run("python3 %s/bin/getrmpytools" % READIES)
        self.pip_install("-r tests/flow/requirements.txt")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisTimeSeriesSetup(nop = args.nop).setup()
