Summary:	The GLib ICE implementation
Name:		libnice
Version:	0.1.2
Release:	1
License:	LGPL v2 and MPL v1.1
Group:		Libraries
Source0:	http://nice.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	1914dd98380dd68632d3d448cc23f1e8
URL:		http://nice.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gnutls-devel
BuildRequires:	gssdp-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-igd-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE). It provides GLib-based
library and GStreamer elements.

ICE is useful for applications that want to establish peer-to-peer UDP
data streams. It automates the process of traversing NATs and provides
security against some attacks.

Existing standards that use ICE include the Session Initiation
Protocol (SIP) and Jingle, XMPP extension for audio/video calls.

%package devel
Summary:	Header files for libnice library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnice library.

%package apidocs
Summary:	libnice library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnice library API documentation.

%package -n gstreamer-nice
Summary:	Nice plguin for gstreamer
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n gstreamer-nice
Nice plugin fofr gstreamer.

%prep
%setup -q

%build
mkdir m4
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/stunbdc
%attr(755,root,root) %{_bindir}/stund
%attr(755,root,root) %ghost %{_libdir}/libnice.so.??
%attr(755,root,root) %{_libdir}/libnice.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnice.so
%{_libdir}/libnice.la
%{_includedir}/nice
%{_includedir}/stun
%{_pkgconfigdir}/nice.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libnice

%files -n gstreamer-nice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstnice.so

