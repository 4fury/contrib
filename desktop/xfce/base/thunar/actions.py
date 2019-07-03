#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr \
	--enable-startup-notification \
	--enable-introspection \
	--enable-gio-unix \
	--enable-gudev \
	--enable-dbus \
	--enable-exif \
	--enable-pcre \
	--disable-gtk-doc \
	--disable-static")

	#pisitools.dosed("libtool", "^(hardcode_libdir_flag_spec=).*", '\\1""')
	#pisitools.dosed("libtool", "^(runpath_var=)LD_RUN_PATH", "\\1DIE_RPATH_DIE")
	pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.removeDir("usr/lib/systemd")
#	pisitools.removeDir("usr/share/polkit-1")

#	pisitools.dodoc("AUTHORS", \
#	"COPYING*", \
#	"FAQ", \
#	"HACKING", \
#	"NEWS", \
#	"README", \
#	"THANKS", \
#	"TODO")
