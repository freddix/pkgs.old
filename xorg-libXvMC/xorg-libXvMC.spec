Summary:	XvMC library
Name:		xorg-libXvMC
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2
# Source0-md5:	bfc7524646f890dfc30dea1d676004a3
Source1:	XvMCConfig
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXv-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XvMC library.

%package devel
Summary:	Header files for libXvMC library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
XvMC library.

This package contains the header files needed to develop programs that
use libXvMC.

%prep
%setup -qn libXvMC-%{version}

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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libXvMC.so.?
%attr(755,root,root) %ghost %{_libdir}/libXvMCW.so.?
%attr(755,root,root) %{_libdir}/libXvMC.so.*.*.*
%attr(755,root,root) %{_libdir}/libXvMCW.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/XvMCConfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMC.so
%attr(755,root,root) %{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.la
%{_libdir}/libXvMCW.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xvmc.pc

