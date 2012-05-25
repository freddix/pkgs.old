Summary:	Telepathy client for GNOME
Name:		empathy
Version:	3.4.1
Release:	2
License:	GPL
Group:		X11/Applications/Communications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/empathy/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	f8d63575926a21cb0aa98375b35968ef
Patch0:		%{name}-configure.patch
URL:		http://live.gnome.org/Empathy
BuildRequires:	cheese-devel
BuildRequires:	clutter-gst-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	enchant-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	gcr-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk3-webkit-devel
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libchamplain-gtk-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel
#BuildRequires:	nautilus-sendto-devel
BuildRequires:	telepathy-farstream-devel
BuildRequires:	telepathy-logger-devel
BuildRequires:	telepathy-mission-control-devel
BuildRequires:	yelp-tools
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	folks
Requires:	gnome-online-accounts
Requires:	gsettings-desktop-schemas
Requires:	telepathy-logger
Requires:	telepathy-mission-control
Requires:	telepathy-service
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Empathy consists of a rich set of reusable instant messaging widgets
and a GNOME client using those widgets. It uses Telepathy and Nokia's
Mission Control, and reuses Gossip's UI. The main goal is to permit
desktop integration by providing libempathy and libempathy-gtk
libraries.

%package -n nautilus-sendto-empathy
Summary:	nautilus-sendto Empathy plugin
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus-sendto

%description -n nautilus-sendto-empathy
A nautilus-sendto plugin for sending files via Empathy.

%prep
%setup -q
%patch0 -p1

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-geocode		\
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-static		\
	--enable-goa			\
	--enable-gudev			\
	--enable-location		\
	--enable-map			\
	--enable-spell			\
	--with-cheese			\
	--with-connectivity=nm		\
	--with-eds
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/empathy
%attr(755,root,root) %{_bindir}/empathy-accounts
%attr(755,root,root) %{_bindir}/empathy-debugger
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/empathy-auth-client
%attr(755,root,root) %{_libexecdir}/empathy-call
%attr(755,root,root) %{_libexecdir}/empathy-chat
%attr(755,root,root) %{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so

%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Call.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Chat.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.FileTransfer.service

%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml

%{_datadir}/telepathy/clients/Empathy.Auth.client
%{_datadir}/telepathy/clients/Empathy.Call.client
%{_datadir}/telepathy/clients/Empathy.Chat.client
%{_datadir}/telepathy/clients/Empathy.FileTransfer.client

%{_iconsdir}/hicolor/*/apps/*
%{_desktopdir}/*.desktop

%{_mandir}/man1/empathy*.1*

%if 0
%files -n nautilus-sendto-empathy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus-sendto/plugins/libnstempathy.so
%endif

