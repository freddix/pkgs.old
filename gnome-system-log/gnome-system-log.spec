Summary:	System log viewer for GNOME
Name:		gnome-system-log
Version:	3.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-log/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	5b5958557640d0c69a6358fef3cbeda0
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to view system logs.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

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
%doc NEWS TODO
%attr(755,root,root) %{_bindir}/gnome-system-log
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/gnome-system-log
%{_datadir}/glib-2.0/schemas/*.xml
%{_desktopdir}/gnome-system-log.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_mandir}/man1/gnome-system-log.1*

