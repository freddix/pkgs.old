Summary:	The GNU Transport Layer Security Library
Name:		gnutls
Version:	2.12.19
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.bz2
# Source0-md5:	14228b34e3d8ed176a617df40693b441
Patch0:		%{name}-link.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	guile-devel
BuildRequires:	libcfg+-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtasn1-devel
BuildRequires:	libtool
BuildRequires:	lzo-devel
BuildRequires:	nettle-devel
BuildRequires:	opencdk-devel
BuildRequires:	p11-kit-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%package devel
Summary:	Header files etc to develop gnutls applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop gnutls applications.

%package c++
Summary:	libgnutlsxx - C++ interface to gnutls library
Summary(pl.UTF-8):	libgnutlsxx - interfejs C++ do biblioteki gnutls
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
libgnutlsxx - C++ interface to gnutls library.

%package c++-devel
Summary:	Header files for libgnutlsxx, a C++ interface to gnutls library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for libgnutlsxx, a C++ interface to gnutls library.

%package guile
Summary:	Guile bindings for GnuTLS
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description guile
Guile bindings for GnuTLS.

%package guile-devel
Summary:	Guile bindings for GnuTLS - development files
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-guile = %{version}-%{release}

%description guile-devel
Guile bindings for GnuTLS - development files.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4 -I lib/gl/m4 -I libextra/gl/m4 -I lib/m4 -I libextra/m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd lib
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../libextra
%{__aclocal} -I m4 -I gl/m4 -I ../lib/m4 -I ../lib/gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%configure \
	--disable-silent-rules		\
	--disable-static		\
        --with-lzo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%find_lang libgnutls

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	guile -p /sbin/ldconfig
%postun	guile -p /sbin/ldconfig

%files -f libgnutls.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls*
%attr(755,root,root) %{_bindir}/p11tool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool

%attr(755,root,root) %ghost %{_libdir}/libgnutls-extra.so.??
%attr(755,root,root) %ghost %{_libdir}/libgnutls-openssl.so.??
%attr(755,root,root) %ghost %{_libdir}/libgnutls.so.??
%attr(755,root,root) %{_libdir}/libgnutls-extra.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*

%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*
%{_mandir}/man1/p11tool.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_infodir}/*.info*
%{_infodir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-extra.so
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%attr(755,root,root) %{_libdir}/libgnutls.so
%{_libdir}/libgnutls-extra.la
%{_libdir}/libgnutls-openssl.la
%{_libdir}/libgnutls.la
%{_includedir}/gnutls
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*gnutls*.3*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnutlsxx.so.??
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so
%{_libdir}/libgnutlsxx.la
%{_includedir}/gnutls/gnutlsxx.h

%files guile
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libguile-gnutls-extra-v-1.so.?
%attr(755,root,root) %ghost %{_libdir}/libguile-gnutls-v-1.so.?
%attr(755,root,root) %{_libdir}/libguile-gnutls-extra-v-1.so.*.*.*
%attr(755,root,root) %{_libdir}/libguile-gnutls-v-1.so.*.*.*
%{_datadir}/guile/site/gnutls.scm
%{_datadir}/guile/site/gnutls

%files guile-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguile-gnutls-extra-v-1.so
%attr(755,root,root) %{_libdir}/libguile-gnutls-v-1.so
%{_libdir}/libguile-gnutls-extra-v-1.la
%{_libdir}/libguile-gnutls-v-1.la

