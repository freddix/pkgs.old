%define		pre	%{nil}

Summary:	Small and fast window manger for the X Window
Name:		openbox
Version:	3.5.0
Release:	13
Epoch:		1
License:	GPL
Group:		X11/Window Managers
Source0:	http://icculus.org/openbox/releases/%{name}-%{version}.tar.gz
# Source0-md5:	00441b53cf14c03566c8e82643544ff9
Source1:	%{name}.desktop
Source2:	%{name}-autostart.sh
Source3:	%{name}-default-menu.xml
Source4:	%{name}-xdg-menu
Source5:	%{name}-drives-menu
Patch0:		%{name}-freddix.patch
Patch1:		%{name}-libs.patch
URL:		http://openbox.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-autopoint
BuildRequires:	imlib2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pango-devel
BuildRequires:	pkg-config
BuildRequires:	rpm-pythonprov
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-libSM-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	openbox-theme-colors
Requires:	python-pygobject
Requires:	python-pyxdg
Requires:	udisks
Requires:	xdg-menus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_apiver		3.5
%define		_libexecdir	%{_datadir}/%{name}

%description
Openbox3 is a completely new window manager, and is not based upon any
previous window manager code-base. Its primary goals are standards
support/compliance, and intelligent window management.

%package libs
Summary:	openbox libraries
Group:		Libraries

%description libs
openbox libraries.

%package devel
Summary:	Header files for openbox
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Development header files for writing applications based on openbox.

%package xsession
Summary:	Simple, but usable X session
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xsession
Requires:	gmrun
Requires:	nitrogen
Requires:	obconf
Requires:	urxvt

%description xsession
Simple, but usable X session based on Openbox WM.
Includes:
- gmrun, providing "run program" window
- nitrogen for background setting
- obconf, an Openbox GUI configurator
- urxvt, as a X terminal

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make} \
	theme="Clearlooks-ob3"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 	\
	secretbindir=%{_datadir}/openbox

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/openbox/autostart.sh
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/openbox/menu.xml

install %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/openbox-xdg-menu
install %{SOURCE5} $RPM_BUILD_ROOT%{_libexecdir}/openbox-drives-menu

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{no,ua}
rm -rf $RPM_BUILD_ROOT%{_docdir}/openbox

mv -f $RPM_BUILD_ROOT%{_datadir}/themes/Clearlooks{,-ob3}
mv -f $RPM_BUILD_ROOT%{_datadir}/themes/Clearlooks-Olive{,-ob3}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG COMPLIANCE README
%attr(755,root,root) %{_bindir}/obxprop
%attr(755,root,root) %{_bindir}/openbox
%attr(755,root,root) %{_bindir}/openbox-session

# scripts
%attr(755,root,root) %{_libexecdir}/openbox-autostart
%attr(755,root,root) %{_libexecdir}/openbox-drives-menu
%attr(755,root,root) %{_libexecdir}/openbox-xdg-autostart
%attr(755,root,root) %{_libexecdir}/openbox-xdg-menu

%dir %{_sysconfdir}/xdg/openbox
%attr(755,root,root) %{_sysconfdir}/xdg/openbox/autostart
%attr(755,root,root) %{_sysconfdir}/xdg/openbox/autostart.sh
%attr(755,root,root) %{_sysconfdir}/xdg/openbox/environment

# dirs
%dir %{_datadir}/%{name}
%dir %{_datadir}/themes/Artwiz-boxed
%dir %{_datadir}/themes/Artwiz-boxed/openbox-3
%dir %{_datadir}/themes/Bear2
%dir %{_datadir}/themes/Bear2/openbox-3
%dir %{_datadir}/themes/Clearlooks-3.4
%dir %{_datadir}/themes/Clearlooks-3.4/openbox-3
%dir %{_datadir}/themes/Clearlooks-Olive-ob3
%dir %{_datadir}/themes/Clearlooks-Olive-ob3/openbox-3
%dir %{_datadir}/themes/Clearlooks-ob3
%dir %{_datadir}/themes/Clearlooks-ob3/openbox-3
%dir %{_datadir}/themes/Mikachu
%dir %{_datadir}/themes/Mikachu/openbox-3
%dir %{_datadir}/themes/Natura
%dir %{_datadir}/themes/Natura/openbox-3
%dir %{_datadir}/themes/Onyx
%dir %{_datadir}/themes/Onyx-Citrus
%dir %{_datadir}/themes/Onyx-Citrus/openbox-3
%dir %{_datadir}/themes/Onyx/openbox-3
%dir %{_datadir}/themes/Orang
%dir %{_datadir}/themes/Orang/openbox-3
%dir %{_datadir}/themes/Syscrash
%dir %{_datadir}/themes/Syscrash/openbox-3
%dir %{_libexecdir}

%{_datadir}/xsessions/openbox.desktop
%{_desktopdir}/openbox.desktop
%{_pixmapsdir}/openbox.png
%{_sysconfdir}/xdg/openbox/*.xml

# themes
%{_datadir}/themes/Artwiz-boxed/openbox-3/*
%{_datadir}/themes/Bear2/openbox-3/*
%{_datadir}/themes/Clearlooks-3.4/openbox-3/*
%{_datadir}/themes/Clearlooks-Olive-ob3/openbox-3/*
%{_datadir}/themes/Clearlooks-ob3/openbox-3/*
%{_datadir}/themes/Mikachu/openbox-3/*
%{_datadir}/themes/Natura/openbox-3/*
%{_datadir}/themes/Onyx-Citrus/openbox-3/*
%{_datadir}/themes/Onyx/openbox-3/*
%{_datadir}/themes/Orang/openbox-3/*
%{_datadir}/themes/Syscrash/openbox-3/*

%{_mandir}/man1/obxprop.1*
%{_mandir}/man1/openbox.1*
%{_mandir}/man1/openbox-session.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %ghost %{_libdir}/lib*.so.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/openbox
%dir %{_includedir}/openbox/%{_apiver}
%{_includedir}/openbox/%{_apiver}/obrender
%{_includedir}/openbox/%{_apiver}/obt
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files xsession
%defattr(644,root,root,755)

