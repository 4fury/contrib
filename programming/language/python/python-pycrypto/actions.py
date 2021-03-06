#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def build():
    shelltools.export("CFLAGS", "-fno-strict-aliasing -Wno-discarded-array-qualifiers -Wno-unused-const-variable -Wno-bool-compare -Wno-tautological-compare")
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -Wl,-O1 -Wl,-z,relro -Wl,--hash-style=gnu -Wl,--as-needed -Wl,--sort-common")
    pythonmodules.compile()

def install():
    pythonmodules.install()