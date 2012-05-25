Summary:	GPS multiplexing daemon
Name:		gypsy
Version:	0.8
Release:	1
License:	LGPL v2+ (library), GPL v2+ (daemon)
Group:		Daemons
Source0:	http://gypsy.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	32b8db24db86d2dac87b391dd255f4bf
Patch0:		%{name}-link.patch
URL:		http://gypsy.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to
access GPS data from multiple GPS sources concurrently.

%package libs
Summary:	Gypsy library
Group:		Libraries

%description libs
Gypsy GPS multiplexing library.

%package devel
Summary:	Development package for gypsy
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for development with gypsy.

%package apidocs
Summary:	Gypsy API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
This package contains developer documentation for gypsy.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gypsy-daemon
/etc/dbus-1/system.d/Gypsy.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Gypsy.service

%files libs
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS TODO
%attr(755,root,root) %ghost %{_libdir}/libgypsy.so.?
%attr(755,root,root) %{_libdir}/libgypsy.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgypsy.so
%{_includedir}/gypsy
%{_pkgconfigdir}/gypsy.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gypsy

