Summary:	Instant messaging program
Name:		pidgin
Version:	2.10.0
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.bz2
# Source0-md5:	e1453c9093c4f32beec19abd14069a3f
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-dbus-dir.patch
Patch3:		%{name}-gnome-keyring.patch
Patch4:		%{name}-missing-linking.patch
URL:		http://www.pidgin.im/
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-glib-devel
BuildRequires:	dbus-glib-devel
#BuildRequires:	evolution-data-server-devel
BuildRequires:	farsight2-devel
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	graphviz
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtkspell-devel
BuildRequires:	libgadu-devel
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-libXScrnSaver-devel
Requires(post,preun):	GConf
Requires(post,postun):	hicolor-icon-theme
Requires:	libpurple = %{epoch}:%{version}-%{release}
Requires:	%{name}-protocols = %{epoch}:%{version}-%{release}
Requires:	gnome-keyring
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libjabber.so.0 libymsg.so.0 liboscar.so.0

%description
Pidgin allows you to talk to anyone using AOL's Instant Messenger
service (you can sign up at http://www.aim.aol.com). It uses the TOC
version of the AOL protocol, so your buddy list is stored on AOL's
servers and can be retrieved from anywhere. It contains many of the
same features as AOL's IM client while at the same time incorporating
many new features. Pidgin also contains a multiple connection feature
which consists of protocol plugins. These plugins allow you to use
Pidgin to connect to other chat services such as Yahoo!, ICQ, MSN,
Jabber, Napster, Zephyr, IRC and Gadu-Gadu.

%package -n finch
Summary:	Pidgin console UI
Group:		Applications/Communications
Epoch:		1
Requires:	finch-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-protocols = %{epoch}:%{version}-%{release}

%description -n finch
Pidgin console UI.

%package protocols
Summary:	Pidgin protocols
Group:		Applications/Communications
Epoch:		1

%description protocols
Pidgin protocols.

%package -n libpurple
Summary:	Pidgin client library
Group:		Libraries
Epoch:		1

%description -n libpurple
Pidgin client library.

%package -n finch-libs
Summary:	Pidgin console client library
Group:		Libraries
Epoch:		1

%description -n finch-libs
Pidgin console client library.

%package -n libpurple-devel
Summary:	Development files for Pidgin client library
Group:		Development/Libraries
Epoch:		1
Requires:	libpurple = %{epoch}:%{version}-%{release}

%description -n libpurple-devel
Development files for Pidgin.

%package -n finch-devel
Summary:	Development files for Pidgin client library
Group:		Development/Libraries
Epoch:		1
Requires:	libpurple-devel = %{epoch}:%{version}-%{release}
Requires:	finch-libs = %{epoch}:%{version}-%{release}
Requires:	ncurses-devel

%description -n finch-devel
Development files for Pidgin.

%package plugin-evolution
Summary:	Plugin for Ximian Evolution integration
Group:		Libraries
Epoch:		1
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-evolution
Provides integration with Evolution.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
#%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-gevolution	\
	--disable-meanwhile	\
	--disable-perl		\
	--disable-silent-rules	\
	--disable-tk		\
	--enable-dbus		\
	--enable-gnome-keyring	\
	--enable-nss=no

%{__make} -C libpurple/ciphers libpurple-ciphers.la
%{__make} -C libpurple libpurple.la
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# trash removal
rm $RPM_BUILD_ROOT{%{_bindir}/purple-client-example,%{_libdir}/purple-2/dbus-example.*}
rm -f $RPM_BUILD_ROOT%{_libdir}/{finch,gnt,pidgin,purple-2}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca_ES@valencian,ca@valencia,mhr,my_MM,ms_MY,ps,sr@latin}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install purple.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall purple.schemas

%postun
%update_icon_cache hicolor

%post	-n libpurple -p /sbin/ldconfig
%postun	-n libpurple -p /sbin/ldconfig

%post	-n finch-libs -p /sbin/ldconfig
%postun	-n finch-libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* HACKING
%dir %{_libdir}/pidgin
%attr(755,root,root) %{_bindir}/pidgin
%attr(755,root,root) %{_bindir}/purple-remote
%attr(755,root,root) %{_bindir}/purple-send
%attr(755,root,root) %{_bindir}/purple-send-async
%attr(755,root,root) %{_bindir}/purple-url-handler
%attr(755,root,root) %{_libdir}/pidgin/*.so*
#%%exclude %{_libdir}/pidgin/gevolution.so
%{_datadir}/sounds/purple
%{_desktopdir}/pidgin.desktop
%{_pixmapsdir}/pidgin
%{_iconsdir}/hicolor/*/apps/pidgin.*
%{_mandir}/man?/*
%{_sysconfdir}/gconf/schemas/purple.schemas

%files -n finch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/finch
%attr(755,root,root) %{_libdir}/finch/*.so
%attr(755,root,root) %{_libdir}/gnt/*.so
%dir %{_libdir}/finch
%dir %{_libdir}/gnt

%files protocols
%defattr(644,root,root,755)
%dir %{_libdir}/purple-2
%attr(755,root,root) %{_libdir}/purple-2/*.so*

%files -n libpurple
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpurple-client.so.0
%attr(755,root,root) %ghost %{_libdir}/libpurple.so.0
%attr(755,root,root) %{_libdir}/libpurple-client.so.*.*.*
%attr(755,root,root) %{_libdir}/libpurple.so.*.*.*

%files -n finch-libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnt.so.0
%attr(755,root,root) %{_libdir}/libgnt.so.*.*.*

%files -n libpurple-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpurple-client.so
%attr(755,root,root) %{_libdir}/libpurple.so
%{_aclocaldir}/purple.m4
%{_includedir}/pidgin
%{_includedir}/libpurple
%{_libdir}/libpurple-client.la
%{_libdir}/libpurple.la
%{_pkgconfigdir}/pidgin.pc
%{_pkgconfigdir}/purple.pc

%files -n finch-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnt.so
%{_includedir}/finch
%{_includedir}/gnt
%{_libdir}/libgnt.la
%{_pkgconfigdir}/finch.pc
%{_pkgconfigdir}/gnt.pc

%if 0
%files plugin-evolution
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pidgin/gevolution.so

%files doc
%defattr(644,root,root,755)
%doc doc/html/*.{html,png,css}
%endif

