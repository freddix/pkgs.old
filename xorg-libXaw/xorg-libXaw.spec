Summary:	X Athena Widgets library
Name:		xorg-libXaw
Version:	1.0.9
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
# Source0-md5:	ccc57478c41b7a75b9702241b889b1d4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ed
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXp-devel
BuildRequires:	xorg-libXpm-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Athena Widgets library.

%package devel
Summary:	Header files for libXaw library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Athena Widgets library.

This package contains the header files needed to develop programs that
use libXaw.

%prep
%setup -qn libXaw-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-specs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libXaw.so.?
%attr(755,root,root) %ghost %{_libdir}/libXaw6.so.?
%attr(755,root,root) %ghost %{_libdir}/libXaw7.so.?
%attr(755,root,root) %{_libdir}/libXaw6.so.6.*.*
%attr(755,root,root) %{_libdir}/libXaw7.so.7.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXaw6.so
%attr(755,root,root) %{_libdir}/libXaw7.so
%attr(755,root,root) %{_libdir}/libXaw.so
%{_libdir}/libXaw*.la
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*.h
%{_includedir}/X11/Xaw/Template.c
%{_pkgconfigdir}/xaw6.pc
%{_pkgconfigdir}/xaw7.pc
%{_mandir}/man3/*.3x*

