Summary:	Client for Cisco's AnyConnect SSL VPN
Name:		openconnect
Version:	3.17
Release:	1
License:	LGPL v2
Group:		Applications
Source0:	ftp://ftp.infradead.org/pub/openconnect/%{name}-%{version}.tar.gz
# Source0-md5:	7b42b6bc4ba7641dab9366346cdf2de4
URL:		http://www.infradead.org/openconnect.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libproxy-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	pkg-config
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenConnect is a client for Cisco's AnyConnect SSL VPN.

%package devel
Summary:        %{name} development files
Group:          Development/Libraries
Requires:       libproxy-devel

%description devel
This is the package containing %{name} development files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--with-vpnc-script=/etc/vpnc/vpnc-script
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS TODO
%{_sbindir}/openconnect
%attr(755,root,root) %ghost %{_libdir}/libopenconnect.so.?
%attr(755,root,root) %{_libdir}/libopenconnect.so.*.*.*
%{_mandir}/man8/openconnect.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenconnect.so
%{_includedir}/openconnect.h
%{_pkgconfigdir}/openconnect.pc

