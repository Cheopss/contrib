#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make()

def install():
    perlmodules.install()

    for d in ["contrib"]:
        pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), d)

    pisitools.dodoc("Changes", "LICENSE", "PATENTS", "README")
