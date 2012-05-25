Summary:	Library for using OBEX
Name:		openobex
Version:	1.5
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.gz
# Source0-md5:	0d83dc86445a46a1b9750107ba7ab65c
Patch0:		%{name}-pc.patch
URL:		http://openobex.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	libtool
BuildRequires:	libusb-compat-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library tries to implement a generic OBEX Session Protocol. It
does not implement the OBEX Application FrameWork.

%package devel
Summary:	Header files for Open OBEX
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The header files are only needed for development of programs using the
Open OBEX library.

%package utils
Summary:	Open OBEX utility programs
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains utility programs made to show Open OBEX library
usage.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--enable-apps		\
	--enable-bluetooth	\
	--enable-usb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/libopenobex.so.?
%attr(755,root,root) %{_libdir}/libopenobex.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenobex.so
%{_libdir}/libopenobex.la
%{_includedir}/openobex
%{_pkgconfigdir}/*.pc

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ircp
%attr(755,root,root) %{_bindir}/irobex_palm3
%attr(755,root,root) %{_bindir}/irxfer
%attr(755,root,root) %{_bindir}/obex_tcp
%attr(755,root,root) %{_bindir}/obex_test

