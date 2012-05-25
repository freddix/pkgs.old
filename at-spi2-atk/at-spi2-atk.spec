Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Name:		at-spi2-atk
Version:	2.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.4/%{name}-%{version}.tar.xz
# Source0-md5:	7fd5c98aebacaeaa7ab71f95437627ae
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	at-spi2-core-devel
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
Requires(post,postun):	glib-gio-gsettings
Requires:	at-spi2-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libatk-bridge.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libatk-bridge.so
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libatk-bridge.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop
%{_datadir}/glib-2.0/schemas/org.a11y.atspi.gschema.xml

