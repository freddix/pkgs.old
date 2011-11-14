Summary:	X Toolkit library
Name:		xorg-libXt
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
# Source0-md5:	eb22c0a1f172b06b97a3f5ae89768412
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libSM-devel
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Toolkit library.

%package devel
Summary:	Header files for libXt library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Toolkit library.

This package contains the header files needed to develop programs that
use libXt.

%prep
%setup -qn libXt-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

install -d $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
install -d $RPM_BUILD_ROOT%{_datadir}/X11/{cs,da,de,es,fr,ja,ko,nl,pl,pt,pt_BR,ru,sv,zh_CN,zh_TW}/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXt.so.?
%attr(755,root,root) %{_libdir}/libXt.so.*.*.*

%dir %{_datadir}/X11/app-defaults
%lang(cs) %{_datadir}/X11/cs
%lang(da) %{_datadir}/X11/da
%lang(de) %{_datadir}/X11/de
%lang(es) %{_datadir}/X11/es
%lang(fr) %{_datadir}/X11/fr
%lang(ja) %{_datadir}/X11/ja
%lang(ko) %{_datadir}/X11/ko
%lang(nl) %{_datadir}/X11/nl
%lang(pl) %{_datadir}/X11/pl
%lang(pt) %{_datadir}/X11/pt
%lang(pt_BR) %{_datadir}/X11/pt_BR
%lang(ru) %{_datadir}/X11/ru
%lang(sv) %{_datadir}/X11/sv
%lang(zh_CN) %{_datadir}/X11/zh_CN
%lang(zh_TW) %{_datadir}/X11/zh_TW

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXt.so
%{_libdir}/libXt.la
%{_includedir}/X11/*.h
%{_pkgconfigdir}/xt.pc
%{_mandir}/man3/*.3x*

