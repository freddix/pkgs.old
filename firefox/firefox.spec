Summary:	Web browser
Name:		firefox
Version:	12.0
Release:	0.3
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications
Source0:	http://releases.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/source/%{name}-%{version}.source.tar.bz2
# Source0-md5:	80c3e5927274de7f181fb5f931ac5fd4
Source1:	http://releases.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/linux-i686/xpi/de.xpi
# Source1-md5:	3837059d8fd355e83a9e29fc5c34b4b1
Source2:	http://releases.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/linux-i686/xpi/pl.xpi
# Source2-md5:	4a9d0533bf8942083af3a058f4ef9be1
Source100:	vendor.js
Patch0:		%{name}-config.patch
Patch1:		%{name}-pc.patch
Patch2:		%{name}-hunspell.patch
Patch3:		%{name}-system_cairo.patch
URL:		http://www.mozilla.org/projects/firefox/
BuildRequires:	GConf-devel
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10.2-2
BuildRequires:	gtk+-devel
BuildRequires:	hunspell-devel
BuildRequires:	libIDL-devel
BuildRequires:	libevent-devel
BuildRequires:	libffi-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvpx-devel
BuildRequires:	nspr-devel >= 1:4.9
BuildRequires:	nss-devel >= 1:3.13.3
BuildRequires:	pango-devel
BuildRequires:	perl-modules
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRequires:	sqlite3-devel >= 3.7.10
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web browser.

%prep
%setup -qc

cd mozilla-release
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# use system headers
rm -f extensions/spellcheck/hunspell/src/*.hxx

echo 'LOCAL_INCLUDES += $(MOZ_HUNSPELL_CFLAGS)' >> extensions/spellcheck/src/Makefile.in

%build
cd mozilla-release
cp -f %{_datadir}/automake/config.* build/autoconf

cat << 'EOF' > .mozconfig
. $topsrcdir/browser/config/mozconfig

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-%{_target_cpu}
#
ac_add_options --host=%{_host}
ac_add_options --build=%{_host}
#
ac_add_options --libdir=%{_libdir}
ac_add_options --prefix=%{_prefix}
#
ac_add_options --disable-crashreporter
ac_add_options --disable-installer
ac_add_options --disable-javaxpcom
ac_add_options --disable-logging
ac_add_options --disable-mochitest
ac_add_options --disable-tests
ac_add_options --disable-updater
#
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier
#
ac_add_options --disable-debug
ac_add_options --disable-pedantic
ac_add_options --disable-strip
ac_add_options --disable-strip-install
ac_add_options --enable-optimize
#
ac_add_options --disable-gnomeui
ac_add_options --disable-gnomevfs
ac_add_options --enable-gio
ac_add_options --enable-startup-notification
#
ac_add_options --enable-system-cairo
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-lcms
ac_add_options --enable-system-sqlite
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman
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
ac_add_options --enable-official-branding
#
export BUILD_OFFICIAL=1
export MOZILLA_OFFICIAL=1
export MOZ_UA_BUILDID=20100101
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1

EOF

export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags} -Wl,-rpath,%{_libdir}/firefox"

%{__make} -f client.mk build		\
	CC="%{__cc}"			\
	CXX="%{__cxx}"			\
	STRIP="/bin/true"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}	\
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22,24x24,32x32,48x48,256x256}/apps

cd mozilla-release

cp -p %{SOURCE100} obj-%{_target_cpu}/dist/bin/defaults/pref/all-freddix.js

%{__make} -f client.mk install		\
	DESTDIR=$RPM_BUILD_ROOT		\
	STRIP="/bin/true"

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/langpack-de@firefox.mozilla.org.xpi
install %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/langpack-pl@firefox.mozilla.org.xpi

install %{SOURCE100} $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults/preferences

%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/dictionaries
ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}/hyphenation

ln -s %{_libdir}/browser-plugins $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

for i in 16 22 24 32 48 256; do
    install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
    cp browser/branding/official/default${i}.png \
    	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/firefox.png
done

cat > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop <<EOF
[Desktop Entry]
Name=Firefox
GenericName=Web Browser
Comment=Mozilla.org web browser
Exec=%{name} %u
Icon=%{name}
StartupNotify=true
Terminal=false
Type=Application
Categories=GTK;Network;WebBrowser;
MimeType=text/html;text/xml;application/xhtml+xml;x-scheme-handler/http;x-scheme-handler/https;
EOF

rm -rf $RPM_BUILD_ROOT{%{_datadir}/idl,%{_includedir},%{_libdir}/firefox-devel}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/defaults/pref
%dir %{_libdir}/%{name}/dictionaries
%dir %{_libdir}/%{name}/extensions
%dir %{_libdir}/%{name}/hyphenation
%dir %{_libdir}/%{name}/plugins

%attr(755,root,root) %{_bindir}/firefox
%attr(755,root,root) %{_libdir}/%{name}/components/libbrowsercomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdbusservice.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozgnome.so
%attr(755,root,root) %{_libdir}/%{name}/firefox
%attr(755,root,root) %{_libdir}/%{name}/libmozalloc.so
%attr(755,root,root) %{_libdir}/%{name}/libxpcom.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%attr(755,root,root) %{_libdir}/%{name}/mozilla-xremote-client
%attr(755,root,root) %{_libdir}/%{name}/plugin-container

%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/blocklist.xml
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/chrome.manifest
%{_libdir}/%{name}/components/binary.manifest
%{_libdir}/%{name}/defaults/preferences
%{_libdir}/%{name}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}
%{_libdir}/%{name}/icons
%{_libdir}/%{name}/omni.ja
%{_libdir}/%{name}/searchplugins
%{_libdir}/%{name}/platform.ini
%{_libdir}/%{name}/update-settings.ini
%{_libdir}/%{name}/defaults/pref/channel-prefs.js
%{_libdir}/%{name}/dependentlibs.list

%lang(de) %{_libdir}/%{name}/extensions/langpack-de@firefox.mozilla.org.xpi
%lang(pl) %{_libdir}/%{name}/extensions/langpack-pl@firefox.mozilla.org.xpi

%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png

