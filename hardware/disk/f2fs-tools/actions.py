#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
	#shelltools.system("sed -i '16,17d' tools/Makefile.am")

	shelltools.system("./autogen.sh")
	autotools.configure("--without-selinux")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("COPYING", "README")
