Summary:	X Pixmap library
Name:		xorg-libXpm
Version:	3.5.10
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.bz2
# Source0-md5:	7ae7eff7a14d411e84a67bd166bcec1a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Pixmap library.

%package devel
Summary:	Header files for libXpm library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
X Pixmap library.

This package contains the header files needed to develop programs that
use libXpm.

%prep
%setup -qn libXpm-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libXpm.so.?
%attr(755,root,root) %{_libdir}/libXpm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXpm.so
%{_libdir}/libXpm.la
%{_includedir}/X11/xpm.h
%{_pkgconfigdir}/xpm.pc

