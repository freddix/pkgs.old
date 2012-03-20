%bcond_without	gnome	# aka bootstrap
#
Summary:	GNOME Structured File library
Name:		libgsf
Version:	1.14.21
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgsf/1.14/%{name}-%{version}.tar.bz2
# Source0-md5:	2b702648b853402554c97d75405c60d3
Patch0:		%{name}-no_gconf_macros.patch
URL:		http://www.gnumeric.org/
%if %{with gnome}
BuildRequires:	GConf-devel
BuildRequires:	ORBit2-devel
BuildRequires:	libbonobo-devel
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	python-pygtk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for reading and writing structured files (e.g. MS OLE and
Zip).

%package utils
Summary:	libgsf utilities
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description utils
GSF utilities.

%package devel
Summary:	Support files necessary to compile applications with libgsf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel
Requires:	zlib-devel

%description devel
Headers, and support files necessary to compile applications using
libgsf.

%package apidocs
Summary:	libgsf API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgsf API documentation.

%package gnome
Summary:	GNOME specific extensions to libgsf
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME specific extensions to libgsf.

%package gnome-devel
Summary:	libgsf-gnome header files
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
libgsf-gnome header files.

%package -n gsf-office-thumbnailer
Summary:	Simple document thumbnailer
Group:		X11/Applications
Requires(post,preun):   GConf
Requires:	%{name}-gnome = %{version}-%{release}

%description -n gsf-office-thumbnailer
Simple document thumbnailer.

%package -n python-gsf
Summary:        Python gsf module
Group:          Libraries
%pyrequires_eq  python-libs
Requires:       %{name} = %{version}-%{release}
Requires:       python-pygtk-gtk

%description -n python-gsf
Python gsf library.

%package -n python-gsf-gnome
Summary:        Python gsf-gnome module
Group:          Libraries
%pyrequires_eq  python-libs
Requires:       python-gsf = %{version}-%{release}

%description -n python-gsf-gnome
Python gsf-gnome library.

%prep
%setup -q
%{!?with_gnome:%patch0 -p1}

%build
rm -f acinclude.m4
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
%if %{with gnome}
	--with-bonobo	\
%else
	--without-bonobo	\
	--without-gnome-vfs	\
%endif
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gsf/*.la
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/gsf/*.py
rm -rf $RPM_BUILD_ROOT%{_includedir}/%{name}-1/gsf-win32

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   gnome -p /sbin/ldconfig
%postun gnome -p /sbin/ldconfig

%post -n gsf-office-thumbnailer
%gconf_schema_install gsf-office-thumbnailer.schemas

%preun -n gsf-office-thumbnailer
%gconf_schema_uninstall gsf-office-thumbnailer.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %ghost %{_libdir}/libgsf-?.so.???
%attr(755,root,root) %{_libdir}/libgsf-?.so.*.*.*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf
%attr(755,root,root) %{_bindir}/gsf-vba-dump
%{_mandir}/man1/gsf.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsf-?.so
%dir %{_includedir}/libgsf-1
%{_includedir}/libgsf-1/gsf
%{_pkgconfigdir}/libgsf-?.pc

%files -n python-gsf
%defattr(644,root,root,755)
%dir %{py_sitedir}/gsf
%attr(755,root,root) %{py_sitedir}/gsf/_gsfmodule.so
%dir %{py_sitescriptdir}/gsf
%{py_sitescriptdir}/gsf/*.py[co]

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgsf-gnome-?.so.???
%attr(755,root,root) %{_libdir}/libgsf-gnome-?.so.*.*.*

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/libgsf-gnome-?.la
%attr(755,root,root) %{_libdir}/libgsf-gnome-?.so
%{_includedir}/libgsf-1/gsf-gnome
%{_pkgconfigdir}/libgsf-gnome-?.pc

%files -n gsf-office-thumbnailer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsf-office-thumbnailer
%{_sysconfdir}/gconf/schemas/gsf-office-thumbnailer.schemas
%{_mandir}/man1/gsf-office-thumbnailer.1*

%files -n python-gsf-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gsf/gnomemodule.so
%endif

