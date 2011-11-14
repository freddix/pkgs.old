Summary:	X Cursor library
Name:		xorg-libXcursor
Version:	1.1.12
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXcursor-%{version}.tar.bz2
# Source0-md5:	a93b5a6f5b05976d2c0d3f8a07f6ac6a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXfixes-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Cursor - client-side cursor loading library.

%package devel
Summary:	Header files for libXcursor library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Cursor - client-side cursor loading library.

This package contains the header files needed to develop programs that
use libXcursor.

%prep
%setup -qn libXcursor-%{version}

%build
%{__libtoolize}
%{__aclocal}
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXcursor.so.?
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcursor.so
%{_libdir}/libXcursor.la
%dir %{_includedir}/X11/Xcursor
%{_includedir}/X11/Xcursor/*.h
%{_pkgconfigdir}/xcursor.pc
%{_mandir}/man3/*.3x*

