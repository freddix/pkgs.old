%include	/usr/lib/rpm/macros.gstreamer

Summary:	Audio/Video Communications Framework
Name:		farstream
Version:	0.1.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://freedesktop.org/software/farstream/releases/farstream/%{name}-%{version}.tar.gz
# Source0-md5:	5d6e561b3688d0d0c8906fec4f356df3
URL:		http://www.freedesktop.org/wiki/Software/Farstream
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	gupnp-igd-devel
BuildRequires:	libnice-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-gstreamer-devel
BuildRequires:	python-pygobject-devel
Obsoletes:	farsight2 < 0.0.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Farstream (formerly Farsight) project is an effort to create a
framework to deal with all known audio/video conferencing protocols.
On one side it offers a generic API that makes it possible to write
plugins for different streaming protocols, on the other side it offers
an API for clients to use those plugins.

The main target clients for Farstream are Instant Messaging
applications. These applications should be able to use Farstream for
all their Audio/Video conferencing needs without having to worry about
any of the lower level streaming and NAT traversal issues.

%package devel
Summary:	Header files for Farstream library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Farstream library.

%package apidocs
Summary:	Farstream API documentation
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	farsight2-apidocs < 0.0.32

%description apidocs
API documentation for Farstream library.

%package -n python-farstream
Summary:	Farstream Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-farstream
Farstream Python bindings.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--disable-silent-rules	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{farstream-0.1,gstreamer-0.10}/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libfarstream-0.1.so.0
%attr(755,root,root) %{_libdir}/libfarstream-0.1.so.*.*.*
%{_libdir}/girepository-1.0/Farstream-0.1.typelib

%dir %{_libdir}/farstream-0.1
%attr(755,root,root) %{_libdir}/farstream-0.1/libmulticast-transmitter.so
%attr(755,root,root) %{_libdir}/farstream-0.1/libnice-transmitter.so
%attr(755,root,root) %{_libdir}/farstream-0.1/librawudp-transmitter.so
%attr(755,root,root) %{_libdir}/farstream-0.1/libshm-transmitter.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsfunnel.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsmsnconference.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsrawconference.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsrtcpfilter.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsrtpconference.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libfsvideoanyrate.so
%{_datadir}/farstream

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfarstream-0.1.so
%{_datadir}/gir-1.0/Farstream-0.1.gir
%{_includedir}/farstream-0.1
%{_pkgconfigdir}/farstream-0.1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/farstream-libs-0.10
%{_gtkdocdir}/farstream-plugins-0.1

%files -n python-farstream
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/farstream.so

