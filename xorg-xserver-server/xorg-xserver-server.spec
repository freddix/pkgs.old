%define         gitver	%{nil}

Summary:	X.org server
Name:		xorg-xserver-server
Version:	1.12.2
%if "%{gitver}" != "%{nil}"
Release:	0.%{gitver}.1
Source0:	http://cgit.freedesktop.org/xorg/xserver/snapshot/xserver-%{gitver}.tar.bz2
# Source0-md5:	791f0323b886abb7954de7f042bb7dc6
%else
Release:	1
Source0:	http://xorg.freedesktop.org/releases/individual/xserver/xorg-server-%{version}.tar.bz2
# Source0-md5:	791f0323b886abb7954de7f042bb7dc6
%endif
License:	MIT
Group:		X11/Servers
Patch0:		%{name}-less-acpi-brokenness.patch
Patch1:		%{name}-fdo27497.patch
Patch2:		%{name}-cache-indirect-opcode.patch
Patch3:		%{name}-DamageSetReportAfterOp.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	dbus-devel
BuildRequires:	libdrm-devel
BuildRequires:	libpciaccess-devel >= 0.13
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	pixman-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXau-devel
BuildRequires:	xorg-libXaw-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXdmcp-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfont-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-libXres-devel
BuildRequires:	xorg-libXt-devel
BuildRequires:	xorg-libXtst-devel
BuildRequires:	xorg-libXv-devel
BuildRequires:	xorg-libXxf86dga-devel
BuildRequires:	xorg-libXxf86misc-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	xorg-libfontenc-devel
BuildRequires:	xorg-libxkbfile-devel
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xtrans-devel
Requires:	Mesa-dri-driver-swrast
Requires:	xkeyboard-config
Requires:	xorg-app-rgb
Requires:	xorg-app-xkbcomp
Requires:	xorg-driver-input-evdev
Requires:	xorg-font-alias
Requires:	xorg-font-cursor-misc
Requires:	xorg-font-misc-base
Requires:	xorg-libXt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	libscanpci.so libxf1bpp.so

%description
Xorg server is a generally used X server which uses display hardware.
It requires proper driver for your display hardware.

%package devel
Summary:	Header files for X.org server
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto

%description devel
Header files for X.org server.

%package -n xorg-xserver-Xnest
Summary:	Nested X server
Group:		X11/Servers

%description -n xorg-xserver-Xnest
Xnest X server.

%package -n xorg-xserver-Xephyr
Summary:	Xephyr X server
Group:		X11/Servers

%description -n xorg-xserver-Xephyr
Xephyr X server.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn xserver-%{gitver}
%else
%setup -qn xorg-server-%{version}
%endif

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1 -R

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-config-hal			\
	--disable-dmx				\
	--disable-silent-rules			\
	--disable-xfake				\
	--disable-xfbdev			\
	--disable-xvfb				\
	--enable-config-udev			\
	--enable-glx-tls			\
	--enable-kdrive				\
	--enable-xephyr				\
	--enable-xnest				\
	--with-fontrootdir="%{_fontsdir}"	\
	--with-dri-driver-path=%{_libdir}/xorg/modules/dri	\
	--with-os-name="Freddix"		\
	--with-xkb-output=/var/lib/xkb		\
	--with-xkb-path=/usr/share/X11/xkb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/xorg.conf.d
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{dri,drivers,input}

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{*,*/*}.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if "%{gitver}" != "%{nil}"
%doc COPYING
%else
%doc COPYING ChangeLog
%endif
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/dri
%dir %{_libdir}/xorg/modules/drivers
%dir %{_libdir}/xorg/modules/extensions
%dir %{_libdir}/xorg/modules/input
%dir %{_libdir}/xorg/modules/multimedia

%dir %{_datadir}/X11/xorg.conf.d
%dir /etc/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/*.conf

%attr(755,root,root) %{_bindir}/X
%attr(755,root,root) %{_bindir}/Xorg
%attr(755,root,root) %{_bindir}/cvt
%attr(755,root,root) %{_bindir}/gtf

%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libdbe.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libdri.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libdri2.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libextmod.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/librecord.so
%attr(755,root,root) %{_libdir}/xorg/modules/lib*.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/*.so

%{_libdir}/xorg/protocol.txt

%dir /var/lib/xkb
/var/lib/xkb/README.compiled

%{_mandir}/man1/Xorg.1x*
%{_mandir}/man1/Xserver.1x*
%{_mandir}/man1/cvt.1*
%{_mandir}/man1/gtf.1x*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man5/xorg.conf.5x*
%{_mandir}/man5/xorg.conf.d.5x*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg
%{_aclocaldir}/xorg-server.m4
%{_pkgconfigdir}/xorg-server.pc

%files -n xorg-xserver-Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1x*

%files -n xorg-xserver-Xephyr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1x*

