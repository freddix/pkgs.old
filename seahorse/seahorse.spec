Summary:	GNOME application for managing encryption keys
Name:		seahorse
Version:	3.4.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	0d5215a1b6d5747afe0909f4d91f53b9
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gcr-devel
BuildRequires:	gedit-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnupg
BuildRequires:	gobject-introspection-devel
BuildRequires:	gpgme-devel
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	openldap-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gcr
Requires:	gnome-keyring
Requires:	gnupg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/seahorse

%description
Seahorse is a GNOME application for managing encryption keys
and passwords in the GnomeKeyring

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	SSH_KEYGEN_PATH=%{_bindir}/ssh-keygen	\
	SSH_PATH=%{_bindir}/ssh			\
	--disable-schemas-compile 		\
	--disable-silent-rules			\
	--disable-static			\
	--enable-pgp
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/seahorse
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/seahorse-ssh-askpass
%attr(755,root,root) %{_libexecdir}/xloadimage
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/org.gnome.seahorse.convert
%{_datadir}/GConf/gsettings/org.gnome.seahorse.manager.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.window.gschema.xml
%{_desktopdir}/seahorse.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/seahorse.1*

