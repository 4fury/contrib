#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

w = "--prefix=/usr \
     -Dlogind=none \
     -Dgsd_plugin=false \
     -Dman=true \
    "

def setup():
	shelltools.system("meson . build %s" % w)

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "TODO")

