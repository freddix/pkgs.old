Summary:	Tool suite for mobile phones
Name:		gammu
Version:	1.30.0
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://dl.cihar.com/gammu/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	5bb061f1299e7ae8d38ecac1b8b11465
URL:		http://www.gammu.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gammu (formerly known as MyGnokii2) is cellular manager for various
mobile phones and modems.

%package libs
Summary:	Gammu library
Group:		Libraries

%description libs
Gammu tool suite library.

%package devel
Summary:	Header files for Gammu tool suite for mobile phones
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files for Gammu tool suite for mobile phones.

%package -n python-gammu
Summary:	Python bingings for Gammu library
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
%pyrequires_eq	python-modules

%description -n python-gammu
Python bingings for Gammu library.

%prep
%setup -q

%build
mkdir -p build
cd build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -D docs/config/gammurc $RPM_BUILD_ROOT%{_sysconfdir}/gammurc

%find_lang %{name}
%find_lang libgammu

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gammurc
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/gammu-detect
%attr(755,root,root) %{_bindir}/gammu-smsd
%attr(755,root,root) %{_bindir}/gammu-smsd-inject
%attr(755,root,root) %{_bindir}/gammu-smsd-monitor
%attr(755,root,root) %{_bindir}/jadmaker
%{_datadir}/%{name}
%{_mandir}/man[157]/*

%files libs -f libgammu.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libGammu.so.?
%attr(755,root,root) %ghost %{_libdir}/libgsmsd.so.?
%attr(755,root,root) %{_libdir}/libGammu.so.*.*
%attr(755,root,root) %{_libdir}/libgsmsd.so.*.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/libGammu.so
%attr(755,root,root) %{_libdir}/libgsmsd.so
%{_includedir}/gammu
%{_pkgconfigdir}/gammu.pc
%{_pkgconfigdir}/gammu-smsd.pc

%files -n python-gammu
%defattr(644,root,root,755)
%doc README.Python
%dir %{py_sitedir}/gammu
%attr(755,root,root) %{py_sitedir}/gammu/*.so
%{py_sitedir}/gammu/*.py[co]

