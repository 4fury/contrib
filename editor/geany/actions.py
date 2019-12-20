#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr \
	\
	--enable-vte \
	--enable-gtk3 \
	--enable-binreloc \
	\
	--disable-api-docs \
	--disable-pdf-docs \
	--disable-html-docs \
	--disable-gtkdoc-header")

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def check():
	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"ChangeLog", \
	"COPYING", \
	"HACKING", \
	"INSTALL", \
	"NEWS", \
	"README*", "THANKS", "TODO")

