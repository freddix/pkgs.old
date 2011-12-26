Summary:	A utility for getting files from remote servers (FTP, HTTP, and others)
Name:		curl
Version:	7.23.1
Release:	1
License:	MIT-like
Group:		Applications/Networking
Source0:	http://curl.haxx.se/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0296d3196b4bf82c896a869b38dbc5f2
Patch0:		%{name}-no_strip.patch
Patch1:		%{name}-ac.patch
URL:		http://curl.haxx.se/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libidn-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	openssl-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cURL is a tool for getting files with URL syntax, supporting FTP,
HTTP, HTTPS, GOPHER, TELNET, DICT, FILE and LDAP. cURL supports HTTP
POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies,
cookies, user+password authentication and a busload of other useful
tricks. The main use for curl is when you want to get or send files
automatically to or from a site using one of the supported protocols.

cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and
Dict servers, using any of the supported protocols. cURL is designed
to work without user interaction or any kind of interactivity. cURL
offers many useful capabilities, like proxy support, user
authentication, FTP upload, HTTP post, and file transfer resume.

%package libs
Summary:	curl library
Group:		Libraries

%description libs
curl library.

%package devel
Summary:	Header files and development documentation for curl library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files and development documentation for curl library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static				\
	--enable-ipv6					\
	--enable-ldaps					\
	--with-ca-bundle=/etc/certs/ca-certificates.crt	\
	--with-ssl=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README docs/{BUGS,FAQ,FEATURES,HISTORY,KNOWN_BUGS,MANUAL,SSLCERTS,THANKS,TODO,TheArtOfHttpScripting}
%attr(755,root,root) %{_bindir}/curl
%{_mandir}/man1/curl.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcurl.so.4
%attr(755,root,root) %{_libdir}/libcurl.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/{CONTRIBUTE,INTERNALS,LICENSE-MIXING,RESOURCES}
%attr(755,root,root) %{_bindir}/curl-config
%attr(755,root,root) %{_libdir}/libcurl.so
%{_libdir}/libcurl.la
%{_includedir}/curl
%{_pkgconfigdir}/libcurl.pc
%{_mandir}/man1/curl-config.1*
%{_mandir}/man3/*curl*.3*

