Summary:	Font configuration and customization tools
Name:		fontconfig
Version:	2.8.0
Release:	4
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	http://fontconfig.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	77e15a92006ddc2adbb06f840d591c0e
Source1:	%{name}-lcd-filter.conf
Patch0:		%{name}-blacklist.patch
URL:		http://fontconfig.org/
BuildRequires:	autoconf
BuildRequires:	automake
# not really needed, makes bootstrap easier
#BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.
This package contains tools and documentation.

%package libs
Summary:	Font configuration and customization library
Group:		Development/Libraries

%description libs
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.

%package devel
Summary:	Font configuration and customization library - development files
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these fontconfig.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-docs \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man{1,3,5},/var/cache/fontconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/10-lcd-filter.conf

install doc/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install doc/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

cp -f conf.d/README README.confd

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
HOME=/tmp %{_bindir}/fc-cache -r -s 2>/dev/null || :

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README README.confd
%attr(755,root,root) %{_bindir}/fc-*

%dir %{_sysconfdir}/fonts
%dir %{_sysconfdir}/fonts/conf.avail
%dir %{_sysconfdir}/fonts/conf.d

%config(noreplace) %verify(not link md5 mtime size) %{_sysconfdir}/fonts/conf.d/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fonts/fonts.conf
%{_sysconfdir}/fonts/conf.d/README
%{_sysconfdir}/fonts/conf.avail/*.conf
%{_sysconfdir}/fonts/fonts.dtd
/var/cache/fontconfig

%{_mandir}/man5/*.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libfontconfig.so.?
%attr(755,root,root) %{_libdir}/libfontconfig.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/fontconfig-devel/*.html
%attr(755,root,root) %{_libdir}/libfontconfig.so
%{_libdir}/libfontconfig.la
%{_includedir}/fontconfig
%{_pkgconfigdir}/fontconfig.pc
%{_mandir}/man3/*.3*

