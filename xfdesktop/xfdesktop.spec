%define		xfce_version	4.10.0

Summary:	Desktop manager for the Xfce Desktop Environment
Name:		xfdesktop
Version:	4.10.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfdesktop/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	d5f6fb9fdde3ddff5804b2a251892936
URL:		http://www.xfce.org/
BuildRequires:	Thunar-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	exo-devel
BuildRequires:	garcon-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfce4-panel-devel >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	exo
Requires:	garcon
Requires:	xfconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Desktop manager for the Xfce Desktop Environment.

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
	--disable-static	\
	--enable-desktop-icons	\
	--enable-desktop-menu	\
	--enable-file-icons	\
	--enable-thunarx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	docdir="%{_datadir}/xfce4/help/%{name}"

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/{mcs-plugins,panel/plugins,modules}/*.la
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/backgrounds/xfce
%{_datadir}/backgrounds/xfce/xfce-blue.jpg
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_pixmapsdir}/*
%{_mandir}/man1/*.1*

