Summary:	Web browser
Name:		firefox
Version:	11.0
Release:	2
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		X11/Applications
Source0:	http://releases.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/source/%{name}-%{version}.source.tar.bz2
# Source0-md5:	4b07acf47857aff72776d805409cdd1b
Source1:	http://releases.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/linux-i686/xpi/de.xpi
# Source1-md5:	02321790ce5cb8edbf97c6272fa5ea3c
Source2:	http://releases.mozilla.org/pub/mozilla.org/%{name}/releases/%{version}/linux-i686/xpi/pl.xpi
# Source2-md5:	e7487c9657d9c555d35527630e7c15a9
Source100:	vendor.js
Patch0:		%{name}-version.patch
URL:		http://developer.mozilla.org/en/docs/XULRunner
BuildRequires:	GConf-devel
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	gtk+-devel
BuildRequires:	hunspell-devel
BuildRequires:	libIDL-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	pango-devel
BuildRequires:	perl-modules
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xulrunner-devel >= 11.0
BuildRequires:	zip
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	xulrunner
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		app_version	4.0

%description
Web browser.

%prep
%setup -qc

cd mozilla-release
%patch0 -p1

# ugly, but better than to install autoconf2_13
sed -i 's#VPX_CODEC_USE_INPUT_PARTITION#VPX_CODEC_USE_INPUT_FRAGMENTS#' configure

%build
cd mozilla-release

cat << 'EOF' > .mozconfig
. $topsrcdir/browser/config/mozconfig

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build

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
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier
#
ac_add_options --disable-debug
ac_add_options --disable-pedantic
ac_add_options --disable-strip
ac_add_options --disable-strip-install
ac_add_options --enable-libxul
ac_add_options --enable-optimize
ac_add_options --with-libxul-sdk=$(pkg-config --variable=sdkdir libxul)
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
ac_add_options --with-pthreads
ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-libxul
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-png
ac_add_options --with-system-zlib
#
ac_add_options --enable-official-branding
#
MOZILLA_OFFICIAL=1
BUILD_OFFICIAL=1
export BUILD_OFFICIAL
export MOZILLA_OFFICIAL

EOF

export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"

%{__make} -f client.mk build		\
	CC="%{__cc}"			\
	CXX="%{__cxx}"			\
	STRIP="/bin/true"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}	\
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22,24x24,32x32,48x48,256x256}/apps

cd mozilla-release

%{__make} -f client.mk install		\
	DESTDIR=$RPM_BUILD_ROOT		\
	STRIP="/bin/true"

install %{SOURCE1} $RPM_BUILD_ROOT%{_libdir}/%{name}-%{app_version}/extensions/langpack-de@firefox.mozilla.org.xpi
install %{SOURCE2} $RPM_BUILD_ROOT%{_libdir}/%{name}-%{app_version}/extensions/langpack-pl@firefox.mozilla.org.xpi

install %{SOURCE100} $RPM_BUILD_ROOT%{_libdir}/%{name}-%{app_version}/defaults/preferences

ln -s %{_datadir}/myspell $RPM_BUILD_ROOT%{_libdir}/%{name}-%{app_version}/dictionaries
ln -s %{_libdir}/browser-plugins $RPM_BUILD_ROOT%{_libdir}/%{name}-%{app_version}/plugins

for i in 16 22 24 32 48 256; do
    install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps
    cp browser/branding/official/default${i}.png \
    	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x${i}/apps/firefox.png
done

ln -s ../xulrunner $RPM_BUILD_ROOT%{_libdir}/%{name}-%{app_version}/xulrunner

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

rm -rf $RPM_BUILD_ROOT%{_bindir}/firefox
cat > $RPM_BUILD_ROOT%{_bindir}/firefox <<EOF
#!/bin/sh
exec /usr/lib/xulrunner/run-mozilla.sh /usr/lib/firefox-4.0/firefox "\$@"
EOF

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
%attr(755,root,root) %{_bindir}/firefox
%attr(755,root,root) %{_libdir}/%{name}-%{app_version}/components/libbrowsercomps.so
%attr(755,root,root) %{_libdir}/%{name}-%{app_version}/firefox

%dir %{_libdir}/%{name}-%{app_version}
%dir %{_libdir}/%{name}-%{app_version}/components
%dir %{_libdir}/%{name}-%{app_version}/dictionaries
%dir %{_libdir}/%{name}-%{app_version}/extensions
%dir %{_libdir}/%{name}-%{app_version}/plugins
%dir %{_libdir}/%{name}-%{app_version}/defaults

%{_libdir}/%{name}-%{app_version}/application.ini
%{_libdir}/%{name}-%{app_version}/blocklist.xml
%{_libdir}/%{name}-%{app_version}/chrome
%{_libdir}/%{name}-%{app_version}/chrome.manifest
%{_libdir}/%{name}-%{app_version}/components/binary.manifest
%{_libdir}/%{name}-%{app_version}/defaults/preferences
%{_libdir}/%{name}-%{app_version}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}
%{_libdir}/%{name}-%{app_version}/icons
%{_libdir}/%{name}-%{app_version}/omni.ja
%{_libdir}/%{name}-%{app_version}/searchplugins
%{_libdir}/%{name}-%{app_version}/xulrunner

%lang(de) %{_libdir}/%{name}-%{app_version}/extensions/langpack-de@firefox.mozilla.org.xpi
%lang(pl) %{_libdir}/%{name}-%{app_version}/extensions/langpack-pl@firefox.mozilla.org.xpi

%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png

