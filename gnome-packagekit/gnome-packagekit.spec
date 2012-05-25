Summary:	GNOME PackageKit Client
Name:		gnome-packagekit
Version:	3.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-packagekit/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	0ed5e9ada5088ea26e62686b686b90eb
URL:		http://www.packagekit.org/
BuildRequires:	PackageKit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libcanberra-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:  systemd-devel
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	PackageKit
Requires:	polkit-gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages.

%package -n python-gnome-packagekit
Summary:	Widgets to use PackageKit in GTK+ applications
Group:		Libraries/Python
Requires:	gnome-packagekit = %{version}-%{release}
Requires:	python-packagekit
Requires:	python-pygtk-gtk

%description -n python-gnome-packagekit
This module provides widgets to use PackageKit in GTK+ applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-scrollkeeper		\
	--disable-silent-rules		\
	--enable-systemd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README
%attr(755,root,root) %{_bindir}/gpk-*
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%{_datadir}/gnome-packagekit
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*

%files -n python-gnome-packagekit
%defattr(644,root,root,755)
%{py_sitescriptdir}/packagekit/*.py[co]

