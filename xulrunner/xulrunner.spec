Summary:	Mozilla Runtime Environment for XUL+XPCOM applications
Name:		xulrunner
Version:	9.0.1
Release:	2
Epoch:		1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/source/firefox-%{version}.source.tar.bz2
# Source0-md5:	7cf2bd379792a9b232267c6a79680566
Source1:	%{name}-freddix-prefs.js
Patch0:		%{name}-config.patch
Patch1:		%{name}-pc.patch
Patch2:		%{name}-hunspell.patch
URL:		http://developer.mozilla.org/en/docs/XULRunner
BuildRequires:	GConf-devel
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10.2-2
BuildRequires:	gtk+-devel
BuildRequires:	hunspell-devel
BuildRequires:	libIDL-devel
BuildRequires:	libevent-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvpx-devel
BuildRequires:	nspr-devel >= 1:4.8.9
BuildRequires:	nss-devel >= 1:3.13.1
BuildRequires:	pango-devel
BuildRequires:	perl-modules
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRequires:	sqlite3-devel >= 3.7.9
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XULRunner is a Mozilla runtime package that can be used to bootstrap
XUL+XPCOM applications that are as rich as Firefox and Thunderbird. It
will provide mechanisms for installing, upgrading, and uninstalling
these applications. XULRunner will also provide libxul, a solution
which allows the embedding of Mozilla technologies in other projects
and products.

%package devel
Summary:	Headers for developing programs that will use XULRunner
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	nspr-devel
Requires:	nss-devel

%description devel
XULRunner development package.

%package gnome
Summary:	GNOME support package for XULRunner
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnome
GNOME support package for XULRunner.

%prep
%setup -qc

cd mozilla-release
%patch0 -p1
%patch1 -p1
%patch2 -p1

# use system headers
rm -f extensions/spellcheck/hunspell/src/*.hxx

echo 'LOCAL_INCLUDES += $(MOZ_HUNSPELL_CFLAGS)' >> extensions/spellcheck/src/Makefile.in

%build
cd mozilla-release
cp -f %{_datadir}/automake/config.* build/autoconf

cat << 'EOF' > .mozconfig
. $topsrcdir/xulrunner/config/mozconfig

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-%{_target_cpu}
#
ac_add_options --host=%{_host}
ac_add_options --build=%{_host}
#
ac_add_options --bindir=%{_bindir}
ac_add_options --datadir=%{_datadir}
ac_add_options --exec-prefix=%{_exec_prefix}
ac_add_options --includedir=%{_includedir}
ac_add_options --infodir=%{_infodir}
ac_add_options --libdir=%{_libdir}
ac_add_options --libexecdir=%{_libexecdir}
ac_add_options --localstatedir=%{_localstatedir}
ac_add_options --mandir=%{_mandir}
ac_add_options --prefix=%{_prefix}
ac_add_options --sbindir=%{_sbindir}
ac_add_options --sharedstatedir=%{_sharedstatedir}
ac_add_options --sysconfdir=%{_sysconfdir}
#
ac_add_options --disable-crashreporter
ac_add_options --disable-installer
ac_add_options --disable-javaxpcom
ac_add_options --disable-logging
ac_add_options --disable-mochitest
ac_add_options --disable-safe-browsing
ac_add_options --disable-tests
ac_add_options --disable-updater
ac_add_options --disable-url-classifier
#
ac_add_options --disable-debug
ac_add_options --disable-pedantic
ac_add_options --disable-strip
ac_add_options --disable-strip-install
ac_add_options --enable-optimize
ac_add_options --with-default-mozilla-five-home=%{_libdir}/%{name}
#
ac_add_options --disable-gnomeui
ac_add_options --disable-gnomevfs
ac_add_options --enable-canvas
ac_add_options --enable-canvas3d
ac_add_options --enable-default-toolkit=cairo-gtk2
ac_add_options --enable-gio
ac_add_options --enable-pango
ac_add_options --enable-places
ac_add_options --enable-shared-js
ac_add_options --enable-smil
ac_add_options --enable-startup-notification
ac_add_options --enable-svg
#
ac_add_options --enable-system-cairo
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-lcms
ac_add_options --enable-system-sqlite
ac_add_options --with-pthreads
ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
#
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-extensions=default
ac_add_options --with-distribution-id=org.freddix
#
export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1

EOF

export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"

%{__make} -f client.mk build	\
	CC="%{__cc}"		\
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
cd mozilla-release

cp -p %{SOURCE1} obj-%{_target_cpu}/dist/bin/defaults/pref/all-freddix.js

%{__make} -j1 -f client.mk install \
	DESTDIR=$RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}-devel/sdk/lib/*.so
ln -s %{_libdir}/%{name}/libmozalloc.so $RPM_BUILD_ROOT%{_libdir}/%{name}-devel/sdk/lib/libmozalloc.so
ln -s %{_libdir}/%{name}/libmozjs.so $RPM_BUILD_ROOT%{_libdir}/%{name}-devel/sdk/lib/libmozjs.so
ln -s %{_libdir}/%{name}/libxpcom.so $RPM_BUILD_ROOT%{_libdir}/%{name}-devel/sdk/lib/libxpcom.so
ln -s %{_libdir}/%{name}/libxul.so $RPM_BUILD_ROOT%{_libdir}/%{name}-devel/sdk/lib/libxul.so

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/xpcshell $RPM_BUILD_ROOT%{_bindir}/xpcshell
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/xulrunner $RPM_BUILD_ROOT%{_bindir}/xulrunner
mv $RPM_BUILD_ROOT%{_libdir}/%{name}/xulrunner-bin $RPM_BUILD_ROOT%{_bindir}/xulrunner-bin
ln -s %{_bindir}/xpcshell $RPM_BUILD_ROOT%{_libdir}/%{name}/xpcshell
ln -s %{_bindir}/xulrunner-bin $RPM_BUILD_ROOT%{_libdir}/%{name}/xulrunner-bin
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/xulrunner

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/hyphenation
ln -s %{_datadir}/hyphenation $RPM_BUILD_ROOT%{_libdir}/%{name}/hyphenation

cat << 'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%{_libdir}/xulrunner
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xulrunner
%attr(755,root,root) %{_bindir}/xulrunner-bin

%attr(755,root,root) %{_libdir}/xulrunner/*.sh
%attr(755,root,root) %{_libdir}/xulrunner/libmozalloc.so
%attr(755,root,root) %{_libdir}/xulrunner/libmozjs.so
%attr(755,root,root) %{_libdir}/xulrunner/libxpcom.so
%attr(755,root,root) %{_libdir}/xulrunner/libxul.so
%attr(755,root,root) %{_libdir}/xulrunner/mozilla-xremote-client
%attr(755,root,root) %{_libdir}/xulrunner/plugin-container
%attr(755,root,root) %{_libdir}/xulrunner/xulrunner-bin

%attr(755,root,root) %{_libdir}/xulrunner/components/libdbusservice.so

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/dictionaries
%dir %{_libdir}/%{name}/hyphenation
%dir %{_libdir}/%{name}/plugins

%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/chrome.manifest
%{_libdir}/%{name}/components/binary.manifest
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/omni.jar
%{_libdir}/%{name}/platform.ini
%{_sysconfdir}/ld.so.conf.d/%{name}.conf

%files devel
%defattr(644,root,root,755)

%dir %{_libdir}/%{name}-devel
%dir %{_libdir}/%{name}-devel/bin
%dir %{_libdir}/%{name}-devel/idl
%dir %{_libdir}/%{name}-devel/include
%dir %{_libdir}/%{name}-devel/lib
%dir %{_libdir}/%{name}-devel/sdk
%dir %{_libdir}/%{name}-devel/sdk/bin
%dir %{_libdir}/%{name}-devel/sdk/lib

%attr(755,root,root) %{_bindir}/xpcshell
%attr(755,root,root) %{_libdir}/%{name}-devel/sdk/bin/*
%attr(755,root,root) %{_libdir}/%{name}-devel/sdk/lib/*.so
%{_libdir}/%{name}-devel/sdk/lib/*.desc
%attr(755,root,root) %{_libdir}/%{name}/xulrunner-stub
%attr(755,root,root) %{_libdir}/xulrunner/xpcshell

%{_datadir}/idl/%{name}
%{_includedir}/%{name}
%{_libdir}/%{name}-devel/sdk/lib/*.a
%{_libdir}/%{name}-devel/xpcom-config.h
%{_pkgconfigdir}/*.pc

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xulrunner/components/libmozgnome.so

