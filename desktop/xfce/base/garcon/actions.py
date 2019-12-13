#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr \
	--libexecdir=/usr/lib \
	--localstatedir=/var \
	--sysconfdir=/etc \
	\
	--disable-gtk-doc \
	--disable-static \
	\
	--enable-libxfce4ui \
	--enable-gtk2")

	#pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
	#pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
	pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", \
	"ChangeLog", \
	"COPYING", \
	"HACKING", \
	"NEWS", \
	"README", \
	"STATUS", \
	"THANKS", \
	"TODO")

