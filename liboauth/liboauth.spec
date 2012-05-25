Summary:	OAuth library functions
Name:		liboauth
Version:	0.9.6
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://liboauth.sourceforge.net/pool/%{name}-%{version}.tar.gz
# Source0-md5:	508aa0df1e3065b2d7566d85013b2aca
URL:		http://liboauth.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	nss-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboauth is a collection of POSIX-C functions implementing the OAuth
Core RFC 5849 standard. liboauth provides functions to escape and
encode parameters according to OAuth specification and offers
high-level functionality to sign requests or verify OAuth signatures
as well as perform HTTP requests.

%package devel
Summary:	Development files for liboauth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	nss-devel

%description devel
This package contains the header files for developing applications
that use liboauth.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static	\
	--enable-nss
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.MIT ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/liboauth.so.?
%attr(755,root,root) %{_libdir}/liboauth.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboauth.so
%{_includedir}/oauth.h
%{_pkgconfigdir}/oauth.pc
%{_mandir}/man3/oauth.3*

