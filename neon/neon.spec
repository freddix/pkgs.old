Summary:	An HTTP and WebDAV client library
Name:		neon
Version:	0.29.6
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://www.webdav.org/neon/%{name}-%{version}.tar.gz
# Source0-md5:	591e0c82e6979e7e615211b386b8f6bc
URL:		http://www.webdav.org/neon/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neon is an HTTP and WebDAV client library, with a C interface.
Featuring:
 - High-level interface to HTTP and WebDAV methods (PUT, GET, HEAD etc).
 - Low-level interface to HTTP request handling, to allow implementing
   new methods easily.
 - HTTP/1.1 and HTTP/1.0 persistent connections.
 - RFC2617 basic and digest authentication (including auth-int,
   md5-sess).
 - Proxy support (including basic/digest authentication).
 - Generic WebDAV 207 XML response handling mechanism.
 - XML parsing using the expat or libxml parsers.
 - Easy generation of error messages from 207 error responses.
 - WebDAV resource manipulation: MOVE, COPY, DELETE, MKCOL.
 - WebDAV metadata support: set and remove properties, query any set of
   properties (PROPPATCH/PROPFIND).

%package devel
Summary:	Header files for neon
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
C header files for the neon library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%configure \
	--enable-shared		\
	--enable-static=no	\
	--with-libxml2		\
	--with-ssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO doc/*.txt doc/html/*
%attr(755,root,root) %ghost %{_libdir}/libneon.so.??
%attr(755,root,root) %{_libdir}/libneon.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/neon-config
%attr(755,root,root) %{_libdir}/libneon.so
%{_libdir}/libneon.la
%{_includedir}/neon
%{_pkgconfigdir}/neon.pc

