Summary:	Keep passwords and other user's secrets
Name:		gnome-keyring
Version:	3.4.1
Release:	1
License:	LGPL v2+/GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-keyring/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	607b334b43300465d18676dbc4d97de9
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gcr-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	libtool
BuildRequires:	p11-kit-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires:	gcr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
GNOME Keyring is a program that keeps password and other secrets for
users. It is run as a daemon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.

The library libgnome-keyring is used by applications to integrate with
the GNOME keyring system.

%prep
%setup -q

sed -i "s|LXDE|OPENBOX|g" daemon/*.desktop.in.in

%build
rm -f daemon/*.desktop.in
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile		\
	--disable-silent-rules			\
	--disable-static			\
	--with-html-dir=%{_gtkdocdir}		\
	--with-pam-dir=/%{_lib}/security	\
	--with-ca-certificates=%{_sysconfdir}/certs/ca-certificates.crt	\
	--with-root-certs=/etc/certs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-pam	\
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_lib}/security/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-keyring/*/*.la
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-keyring
%attr(755,root,root) %{_bindir}/gnome-keyring-3
%attr(755,root,root) %{_bindir}/gnome-keyring-daemon

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/devel
%dir %{_libdir}/pkcs11
%attr(755,root,root) %{_libdir}/pkcs11/*.so
%attr(755,root,root) %{_libexecdir}/devel/*.so

%attr(755,root,root) /%{_lib}/security/pam_gnome_keyring.so

%{_datadir}/dbus-1/services/org.freedesktop.secrets.service
%{_datadir}/dbus-1/services/org.gnome.keyring.service

%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml

%{_sysconfdir}/xdg/autostart/gnome-keyring-gpg.desktop
%{_sysconfdir}/xdg/autostart/gnome-keyring-pkcs11.desktop
%{_sysconfdir}/xdg/autostart/gnome-keyring-secrets.desktop
%{_sysconfdir}/xdg/autostart/gnome-keyring-ssh.desktop
%{_sysconfdir}/pkcs11/modules/gnome-keyring-module

