%define 	pre	rc4
#
Summary:	RPM packages management helper tool
Name:		poldek
Version:	0.30
Release:	0.%{pre}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://carme.pld-linux.org/~cactus/snaps/poldek/%{name}-%{version}%{pre}.tar.xz
# Source0-md5:	1903db3137c297f42405ba2ac3fa17db
Source1:	%{name}.conf
Source2:	%{name}-aliases.conf
Patch0:		%{name}-config.patch
URL:		http://poldek.pld-linux.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	check
BuildRequires:	db-devel
BuildRequires:	gettext-autopoint
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-tools-pod
BuildRequires:	popt-devel
BuildRequires:	python-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-devel
BuildRequires:	xmlto
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rpm
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
poldek is an RPM package management tool which allows you to easily
perform package verification, installation (including system
installation from scratch), upgrading, and removal.

%package libs
Summary:	poldek libraries
Group:		Libraries

%description libs
poldek libraries.

%package devel
Summary:	Header files for poldek libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for poldek libraries.

%package -n python-poldek
Summary:	Python modules for poldek
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-poldek
Python modules for poldek.

%prep
%setup -q
%patch0 -p1

%build
%{__autopoint}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
cd tndb
%{__libtoolize}
autoreconf -i
cd ../trurlib
%{__libtoolize}
autoreconf -i
cd ..

CPPFLAGS="-std=gnu99"
%configure \
	--disable-static	\
	--enable-nls		\
	--with-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/cache/%{name}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -j1 -C python install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{py_sitedir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/repos.d/freddix-source.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aliases.conf

# get rid of unneeded sources
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{rh,fedora,centos,pld}-source.conf
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/repos.d/pld*

# include them in %doc
rm -rf configs
cp -a conf configs
rm -f configs/Makefile*

%py_postclean
rm -f $RPM_BUILD_ROOT%{py_sitedir}/_poldekmod.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README* NEWS TODO configs/

%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/repos.d

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/repos.d/*.conf

%dir /var/cache/%{name}

%{_infodir}/poldek.info*
%{_mandir}/man1/%{name}*
%lang(pl) %{_mandir}/pl/man1/%{name}*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpoclidek.so.?
%attr(755,root,root) %ghost %{_libdir}/libpoldek.so.?
%attr(755,root,root) %ghost %{_libdir}/libtndb.so.?
%attr(755,root,root) %ghost %{_libdir}/libtrurl.so.?
%attr(755,root,root) %ghost %{_libdir}/libvfile.so.?
%attr(755,root,root) %{_libdir}/libpoclidek.so.*.*.*
%attr(755,root,root) %{_libdir}/libpoldek.so.*.*.*
%attr(755,root,root) %{_libdir}/libtndb.so.*.*.*
%attr(755,root,root) %{_libdir}/libtrurl.so.*.*.*
%attr(755,root,root) %{_libdir}/libvfile.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoclidek.so
%attr(755,root,root) %{_libdir}/libpoldek.so
%attr(755,root,root) %{_libdir}/libtndb.so
%attr(755,root,root) %{_libdir}/libtrurl.so
%attr(755,root,root) %{_libdir}/libvfile.so
%{_libdir}/libpoclidek.la
%{_libdir}/libpoldek.la
%{_libdir}/libtndb.la
%{_libdir}/libtrurl.la
%{_libdir}/libvfile.la
%{_includedir}/*

%files -n python-poldek
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_poldekmod.so
%{py_sitescriptdir}/poldek.py[co]
%{py_sitescriptdir}/poldekmod.py[co]

