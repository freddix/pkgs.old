Summary:	Next Generation of POSIX capabilities library
Name:		libcap-ng
Version:	0.6.6
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (utilities)
Group:		Libraries
Source0:	http://people.redhat.com/sgrubb/libcap-ng/%{name}-%{version}.tar.gz
# Source0-md5:	eb71f967cecb44b4342baac98ef8cb0f
URL:		http://people.redhat.com/sgrubb/libcap-ng/
BuildRequires:	attr-devel
BuildRequires:	automake
BuildRequires:	linux-libc-headers
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libcap-ng library should make programming with POSIX capabilities
easier. The library has some utilities to help you analyse a system
for apps that may have too much privileges.

%package devel
Summary:	Header files for libcap-ng library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcap-ng library.

%package utils
Summary:	Utilities for analysing and setting file capabilities
License:	GPL v2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description utils
This package contains applications to analyse the POSIX capabilities
of all the program running on a system. It also lets you set the file
system based capabilities.

%package -n python-capng
Summary:	Python interface to libcap-ng library
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-capng
Python interface to libcap-ng library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/libcap-ng.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libcap-ng.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libcap-ng.so

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/_capng.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) /%{_lib}/libcap-ng.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libcap-ng.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcap-ng.so
%{_libdir}/libcap-ng.la
%{_includedir}/cap-ng.h
%{_pkgconfigdir}/libcap-ng.pc
%{_aclocaldir}/cap-ng.m4
%{_mandir}/man3/capng_*.3*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/captest
%attr(755,root,root) %{_bindir}/filecap
%attr(755,root,root) %{_bindir}/netcap
%attr(755,root,root) %{_bindir}/pscap
%{_mandir}/man8/captest.8*
%{_mandir}/man8/filecap.8*
%{_mandir}/man8/netcap.8*
%{_mandir}/man8/pscap.8*

%files -n python-capng
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_capng.so
%{py_sitedir}/capng.py[co]

