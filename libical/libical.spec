Summary:	libical library
Name:		libical
Version:	0.47
Release:	1
License:	MPL 1.1 or LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/freeassociation/%{name}-%{version}.tar.gz
# Source0-md5:	21f7f8a21e3d857c9476be732e52dc32
Patch0:		%{name}-as_needed.patch
Patch1:		%{name}-cxx.patch
URL:		http://freeassociation.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package devel
Summary:	libical header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libical header files.

%package c++
Summary:	C++ bindings for libical libraries
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ bindings for libical libraries.

%package c++-devel
Summary:	Header files for libical C++ bindings
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
libical c++ header files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--enable-cxx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libical.so.?
%attr(755,root,root) %ghost %{_libdir}/libicalss.so.?
%attr(755,root,root) %ghost %{_libdir}/libicalvcal.so.?
%attr(755,root,root) %{_libdir}/libical.so.*.*.*
%attr(755,root,root) %{_libdir}/libicalss.so.*.*.*
%attr(755,root,root) %{_libdir}/libicalvcal.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/UsingLibical*
%attr(755,root,root) %{_libdir}/libical.so
%attr(755,root,root) %{_libdir}/libicalss.so
%attr(755,root,root) %{_libdir}/libicalvcal.so
%{_pkgconfigdir}/libical.pc
%{_includedir}/ical.h
%{_includedir}/libical
%exclude %{_includedir}/libical/icalparameter_cxx.h
%exclude %{_includedir}/libical/icalproperty_cxx.h
%exclude %{_includedir}/libical/icalvalue_cxx.h
%exclude %{_includedir}/libical/icptrholder.h
%exclude %{_includedir}/libical/vcomponent.h

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libical_cxx.so.?
%attr(755,root,root) %ghost %{_libdir}/libicalss_cxx.so.?
%attr(755,root,root) %{_libdir}/libical_cxx.so.*.*.*
%attr(755,root,root) %{_libdir}/libicalss_cxx.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libical_cxx.so
%attr(755,root,root) %{_libdir}/libicalss_cxx.so
%{_includedir}/libical/icalparameter_cxx.h
%{_includedir}/libical/icalproperty_cxx.h
%{_includedir}/libical/icalvalue_cxx.h
%{_includedir}/libical/icptrholder.h
%{_includedir}/libical/vcomponent.h

