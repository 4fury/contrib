#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr --disable-static --with-x")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.removeDir("usr/share/gnome-control-center")

	pisitools.dodoc("AUTHORS", \
	"COPYING", \
	"HACKING", \
	"NEWS", \
	"README", \
	"THANKS", \
	"TODO")
