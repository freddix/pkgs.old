Summary:	Universally Unique Identifier library
Name:		ossp-uuid
Version:	1.6.2
Release:	3
License:	MIT
Group:		Libraries
URL:		http://www.ossp.org/pkg/lib/uuid/
Source0:	ftp://ftp.ossp.org/pkg/lib/uuid/uuid-%{version}.tar.gz
# Source0-md5:	5db0d43a9022a6ebbbc25337ae28942f
Patch0:		uuid-ossp-prefix.patch
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP uuid is a ISO-C:1999 application programming interface (API) and
corresponding command line interface (CLI) for the generation of DCE
1.1, ISO/IEC 11578:1996 and RFC 4122 compliant Universally Unique
Identifier (UUID). It supports DCE 1.1 variant UUIDs of version 1
(time and node based), version 3 (name based, MD5), version 4 (random
number based) and version 5 (name based, SHA-1). Additional API
bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs.

%package devel
Summary:	Development support for Universally Unique Identifier library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for OSSP uuid.

%package c++
Summary:	C++ support for Universally Unique Identifier library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ libraries for OSSP uuid.

%package c++-devel
Summary:	C++ development support for Universally Unique Identifier library
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
C++ development headers and libraries for OSSP uuid.

%package dce
Summary:	DCE support for Universally Unique Identifier library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description dce
DCE OSSP uuid library.

%package dce-devel
Summary:	DCE development support for Universally Unique Identifier library
Group:		Development/Libraries
Requires:	%{name}-dce = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description dce-devel
DCE development headers and libraries for OSSP uuid.

%prep
%setup -qn uuid-%{version}
%patch0 -p1

%build
%configure \
	--disable-static			\
	--includedir=%{_includedir}/oosp-uuid	\
	--with-cxx				\
	--with-dce				\
	--without-perl				\
	--without-pgsql				\
	--without-php
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libossp-uuid.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libossp-uuid.so.*.*) $RPM_BUILD_ROOT%{_libdir}/libossp-uuid.so

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%post dce -p /sbin/ldconfig
%postun dce -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HISTORY NEWS PORTING README SEEALSO THANKS TODO USERS
%attr(755,root,root) %{_bindir}/uuid
%attr(755,root,root) %ghost /%{_lib}/libossp-uuid.so.??
%attr(755,root,root) /%{_lib}/libossp-uuid.so.*.*.*
%{_mandir}/man1/uuid.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uuid-config
%dir %{_includedir}/oosp-uuid
%{_includedir}/oosp-uuid/uuid.h
%{_libdir}/libossp-uuid.so
%{_pkgconfigdir}/ossp-uuid.pc
%{_mandir}/man3/ossp-uuid.3*
%{_mandir}/man1/uuid-config.1*
%{_libdir}/libossp-uuid.la

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libossp-uuid++.so.??
%attr(755,root,root) %{_libdir}/libossp-uuid++.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%{_includedir}/oosp-uuid/uuid++.hh
%{_libdir}/libossp-uuid++.so
%{_libdir}/libossp-uuid++.la
%{_mandir}/man3/uuid++.3*

%files dce
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libossp-uuid_dce.so.??
%attr(755,root,root) %{_libdir}/libossp-uuid_dce.so.*.*.*

%files dce-devel
%defattr(644,root,root,755)
%{_includedir}/oosp-uuid/uuid_dce.h
%{_libdir}/libossp-uuid_dce.so
%{_libdir}/libossp-uuid_dce.la

