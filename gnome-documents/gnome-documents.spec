Summary:	Document manager for GNOME
Name:		gnome-documents
Version:	0.4.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	465de85bf9bac48ff300b1bf6aa5851c
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	evince-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libgdata-devel
BuildRequires:	liboauth-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	tracker-devel
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires:	evince
Requires:	hicolor-icon-theme
Requires:	tracker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-documents

%description
gnome-documents is a document manager application for GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-documents/*.la

%find_lang gnome-documents

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f gnome-documents.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-documents
%attr(755,root,root) %{_libdir}/gnome-documents/libgdprivate-1.0.so
%attr(755,root,root) %{_libexecdir}/gd-tracker-gdata-miner
%attr(755,root,root) %{_libexecdir}/gnome-documents-search-provider
%dir %{_libexecdir}
%dir %{_libdir}/gnome-documents/girepository-1.0
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-documents
%{_datadir}/gnome-shell/search-providers/gnome-documents-search-provider.ini
%{_desktopdir}/gnome-documents.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_libdir}/gnome-documents/girepository-1.0/Gd-1.0.typelib

