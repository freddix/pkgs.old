Summary:	PIM SyncML synchronizer
Name:		syncevolution
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.syncevolution.org/syncevolution/sources/%{name}-%{version}.tar.gz
# Source0-md5:	da75826ec8a47556a0d072f5f292c7de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRequires:	valgrind
Requires:	%{name}-libs = %{version}-%{release}
Requires:	evolution-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
SyncEvolution is a tool that synchronizes personal information
management (PIM) data like contacts, calenders, tasks, and memos
using the SyncML information synchronization standard.

%package libs
Summary:	Syncevolution libraries
Group:		Libraries

%description libs
Syncevolution libraries.

%package devel
Summary:	Header files for Syncevolution libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for Syncevolution
libraries.

%package gui
Summary:	Syncevolution GUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gui
Syncevolution GUI.

%prep
%setup -q

# fix linking
sed -i "s/-lz/-lz -ldl/g" src/synthesis/src/Makefile.am.in
# disable qt build
sed -i "s/ qt//" src/dbus/Makefile.am
# library location
sed -i "s/pkglib/lib/" src/gdbus/Makefile.am

%build
./gen-autotools.sh
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize} --automake
%{__aclocal} -I m4 -I m4-repo
%{__automake} -Wno-portability
%{__autoheader}
%{__autoconf}
cd src/synthesis/src && ./gen-makefile-am.sh && cd ..
%{__libtoolize}
%{__aclocal} -I m4 -I m4-repo
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../..
%configure \
	--disable-static	\
	--enable-bluetooth	\
	--enable-dbus-service	\
	--enable-gui		\
	--enable-libcurl	\
	--enable-libsoup	\
	--enable-qtcontacts=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_libexecdir}/{,backends}/*.la
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README test/README*
%dir %{_libexecdir}
%dir %{_libexecdir}/backends
%attr(755,root,root) %{_bindir}/synccompare
%attr(755,root,root) %{_bindir}/syncevo*
%attr(755,root,root) %{_libexecdir}/syncevo-dbus-server
%attr(755,root,root) %{_libexecdir}/syncevo-dbus-server-startup.sh
%attr(755,root,root) %{_libexecdir}/backends/*.so
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.syncevolution.service
%{_mandir}/man1/syncevolution.1*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sync-ui
%{_desktopdir}/sync.desktop
%{_iconsdir}/hicolor/*/apps/sync.png
%{_sysconfdir}/xdg/autostart/syncevo-dbus-server.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libsynthesissdk.a
%{_libdir}/libsynthesisstubs.a
%{_includedir}/syncevo
%{_includedir}/syncevo-dbus
%{_includedir}/synthesis
%{_pkgconfigdir}/*.pc

