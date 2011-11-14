Summary:	Metacity window manager
Name:		metacity
Version:	2.30.3
Release:	3
Epoch:		3
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/gnome/sources/metacity/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	553784f376d96b902e19ff437cd5b339
Patch0:		%{name}-freddix.patch
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
Requires(post,preun):	GConf
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	metacity-theme-shiki-colors
Provides:	window-manager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metacity is a simple window manager that integrates nicely with
GNOME.

%package libs
Summary:	Metacity - libraries
Group:		X11/Libraries

%description libs
This package contains libraries for Metacity window manager.

%package devel
Summary:	Metacity - header files
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This package contains header files for Metacity window manager.

%package themes
Summary:	Basic Metacity themes
Group:		Themes/GTK+
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description themes
Basic Metacity themes.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	ZENITY=%{_bindir}/zenity	\
	--disable-static		\
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xml/metacity

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/metacity-theme.dtd $RPM_BUILD_ROOT%{_datadir}/xml/metacity

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,ha,ig,la}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install metacity.schemas

%preun
%gconf_schema_uninstall metacity.schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README rationales.txt doc/theme-format.txt
%attr(755,root,root) %{_bindir}/metacity
%attr(755,root,root) %{_bindir}/metacity-message
%attr(755,root,root) %{_bindir}/metacity-theme-viewer
%attr(755,root,root) %{_bindir}/metacity-window-demo

%{_datadir}/%{name}
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/xml/metacity
%{_mandir}/man1/metacity*.1*
%{_sysconfdir}/gconf/schemas/metacity.schemas

%{_datadir}/gnome/wm-properties/metacity-wm.desktop
%{_desktopdir}/metacity.desktop

%files themes
%defattr(644,root,root,755)
%{_datadir}/themes/AgingGorilla
%{_datadir}/themes/Atlanta
%{_datadir}/themes/Bright
%{_datadir}/themes/Crux
%{_datadir}/themes/Esco
%{_datadir}/themes/Metabox
%{_datadir}/themes/Simple

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libmetacity-private.so.?
%attr(755,root,root) %{_libdir}/libmetacity-private.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog HACKING doc/dialogs.txt
%attr(755,root,root) %{_libdir}/libmetacity-private.so
%{_libdir}/libmetacity-private.la
%{_includedir}/metacity-1
%{_pkgconfigdir}/libmetacity-private.pc

