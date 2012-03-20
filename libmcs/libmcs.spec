Summary:	mcs library and userland tools
Name:		libmcs
Version:	0.7.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tgz
# Source0-md5:	c47fc81f3efacaa0a5a0b8fd14f9d48e
BuildRequires:	libmowgli-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mcs is a library and set of userland tools which abstract
the storage of configuration settings away from userland
applications.

%package tools
Summary:	mcs library userland tools
group:		Applications
requires:	%{name} = %{version}-%{release}

%description tools
mcs library userland tools.

%package backend-keyconf
Summary:	mcs keyconf backend
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Provides:	mcs-backend

%description backend-keyconf
mcs keyconf backend.

%package backend-gconf
Summary:	mcs gconf backend
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Provides:	mcs-backend

%description backend-gconf
mcs gconf backend.

%package devel
Summary:	Header files for mcs library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for mcs library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%configure
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
%doc AUTHORS README TODO
%attr(755,root,root) %ghost %{_libdir}/libmcs.so.1
%attr(755,root,root) %{_libdir}/libmcs.so.*.*.*
%dir %{_libdir}/mcs

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files backend-keyconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mcs/keyfile.so

%files backend-gconf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mcs/gconf.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmcs.so
%{_includedir}/libmcs
%{_pkgconfigdir}/*.pc

