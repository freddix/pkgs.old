Summary:	Protocol definitions and daemon for D-Bus at-spi
Name:		at-spi2-core
Version:	2.4.2
Release:	1
License:	LGPL v2+
Group:		Daemons
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-core/2.4/%{name}-%{version}.tar.xz
# Source0-md5:	bc940d3f80180b669d8b31b6717dbe97
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXevie-devel
BuildRequires:	xorg-libXevie-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXtst-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/at-spi2

%description
at-spi allows assistive technologies to access GTK-based applications.
Essentially it exposes the internals of applications for automation,
so tools such as screen readers, magnifiers, or even scripting
interfaces can query and interact with GUI controls.

%package libs
Summary:	at-spi2 core library
Group:		Libraries

%description libs
at-spi2 core library.

%package devel
Summary:	Header files for at-spi2 library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for at-spi2 library.

%package apidocs
Summary:	at-spi2 library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
at-spi2 library API documentation.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static			\
	--with-dbus-daemondir=%{_bindir}	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/at-spi-bus-launcher
%attr(755,root,root) %{_libexecdir}/at-spi2-registryd
%dir %{_sysconfdir}/at-spi2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/at-spi2/accessibility.conf
%{_datadir}/dbus-1/services/org.a11y.Bus.service
%{_datadir}/dbus-1/services/org.a11y.atspi.Registry.service
%{_sysconfdir}/xdg/autostart/at-spi-dbus-bus.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libatspi.so.?
%attr(755,root,root) %{_libdir}/libatspi.so.*.*.*
%{_libdir}/girepository-1.0/Atspi-2.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatspi.so
%{_libdir}/libatspi.la
%{_includedir}/at-spi-2.0
%{_datadir}/gir-1.0/Atspi-2.0.gir
%{_pkgconfigdir}/atspi-2.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libatspi

