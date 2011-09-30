Summary:	Networking support for GLib
Name:		glib-networking
Version:	2.30.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib-networking/2.30/%{name}-%{version}.tar.xz
# Source0-md5:	a147c0d5aced1ba0fcc1feea53873a52
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gnutls-devel
#BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	intltool
BuildRequires:	libproxy-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio
Requires:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains a libproxy-based GProxyResolver
implementation and a gnutls-based GTlsConnection implementation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-ca-certificates=/etc/certs/ca-certificates.crt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules || :

%postun
umask 022
%{_bindir}/gio-querymodules %{_libdir}/gio/modules || :

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/glib-pacrunner
%attr(755,root,root) %{_libdir}/gio/modules/libgiognutls.so
%attr(755,root,root) %{_libdir}/gio/modules/libgiolibproxy.so
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service

