Summary:	GNOME session manager
Name:		gnome-session
Version:	3.4.1
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-session/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	993ade4c005ec47d7992ab971177bad9
Source1:	%{name}-gnome.desktop
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	systemd-devel
BuildRequires:	upower-devel
Requires(post,preun):	glib-gio-gsettings
Requires:	upower
Provides:	xsession
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
GNOME session manager and several other session management
related utilities.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-systemd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/{autostart,default-session,shutdown}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/gnome.desktop

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,crh,en@shaw,ha,ig,tk,ps}

%find_lang %{name} --with-gnome --all-name

%clean
rm -fr $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS *ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-session
%attr(755,root,root) %{_bindir}/gnome-session-properties
%attr(755,root,root) %{_bindir}/gnome-session-quit
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnome-session-check-accelerated
%attr(755,root,root) %{_libexecdir}/gnome-session-check-accelerated-helper
%dir %{_datadir}/gnome/autostart
%dir %{_datadir}/gnome/default-session
%dir %{_datadir}/gnome/shutdown
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_datadir}/gnome-session/gsm-inhibit-dialog.ui
%{_datadir}/gnome-session/hardware-compatibility
%{_datadir}/gnome-session/session-properties.ui
%{_datadir}/gnome-session/sessions/gnome-fallback.session
%{_datadir}/gnome-session/sessions/gnome.session
%{_datadir}/xsessions/gnome.desktop
%{_datadir}/GConf/gsettings/gnome-session.convert
%{_datadir}/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%{_desktopdir}/session-properties.desktop
%{_iconsdir}/hicolor/*/*/session-properties.*
%{_mandir}/man[15]/*

