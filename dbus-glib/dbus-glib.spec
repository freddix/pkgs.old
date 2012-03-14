Summary:	GLib-based library for using D-BUS
Name:		dbus-glib
Version:	0.98
Release:	2
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://dbus.freedesktop.org/releases/dbus-glib/%{name}-%{version}.tar.gz
# Source0-md5:	3f7f117dc7c8d899d9acfdcbf9253fb8
Patch0:		%{name}-makefile.patch
URL:		http://www.freedesktop.org/Software/dbus
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	expat-devel
BuildRequires:	glib-gio-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-BUS add-on library to integrate the standard D-BUS library with the
GLib thread abstraction and main loop.

%package devel
Summary:	Header files for GLib-based library for using D-BUS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GLib-based library for using D-BUS.

%package apidocs
Summary:	dbus-glib API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
dbus-glib API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libdbus-glib-1.so.?
%attr(755,root,root) %{_libdir}/libdbus-glib-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbus-binding-tool
%attr(755,root,root) %{_libdir}/libdbus-glib-1.so
%{_includedir}/dbus-1.0/dbus/dbus-glib*.h
%{_includedir}/dbus-1.0/dbus/dbus-gtype-specialized.h
%{_includedir}/dbus-1.0/dbus/dbus-gvalue-parse-variant.h
%{_pkgconfigdir}/dbus-glib-1.pc
%{_mandir}/man1/dbus-binding-tool.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

