Summary:	fontenc library
Name:		xorg-libfontenc
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libfontenc-%{version}.tar.bz2
# Source0-md5:	11d3c292f05a90f6f67840a9e9c3d9b8
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fontenc library.

%package devel
Summary:	Header files for libfontenc library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
# just for dirs
Requires:	xorg-proto

%description devel
fontenc library.

This package contains the header files needed to develop programs that
use libfontenc.

%prep
%setup -qn libfontenc-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-encodingsdir=%{_fontsdir}/encodings
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libfontenc.so.?
%attr(755,root,root) %{_libdir}/libfontenc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfontenc.so
%{_libdir}/libfontenc.la
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/fontenc.pc

