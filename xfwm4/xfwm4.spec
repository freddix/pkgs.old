%define		xfce_version	4.10.0

Summary:	Window manager for Xfce
Name:		xfwm4
Version:	4.10.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfwm4/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	333e5e25a85411c304e9b4474bf00537
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libwnck2-devel
BuildRequires:	libxfce4kbd-devel >= %{xfce_version}
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRequires:	xorg-libXcomposite-devel
BuildRequires:	xorg-libXpm-devel
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfwm4 is a EWMH standard compliant window manager.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/themes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO example.gtkrc-2.0
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/xfce4/xfwm4
%attr(755,root,root) %{_libdir}/xfce4/xfwm4/helper-dialog

%{_desktopdir}/*.desktop

%dir %{_datadir}/xfwm4
%{_datadir}/xfwm4/defaults
%{_datadir}/themes/*
%{_iconsdir}/hicolor/*/*/*

