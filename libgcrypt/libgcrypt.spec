Summary:	Cryptographic library based on the code from GnuPG
Name:		libgcrypt
Version:	1.4.6
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/%{name}-%{version}.tar.bz2
# Source0-md5:	dbf99425a4fe9217c84ce3a35d938634
Patch0:		%{name}-config.patch
URL:		http://www.gnu.org/directory/security/libgcrypt.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgpg-error-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a general purpose cryptographic library based on the code from
GnuPG. It provides functions for all cryptograhic building blocks:
symmetric ciphers (AES, DES, Blowfish, CAST5, Twofish, Arcfour), hash
algorithms (MD5, RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all
hash algorithms), public key algorithms (RSA, ElGamal, DSA), large
integer functions, random numbers and a lot of supporting functions.

%package devel
Summary:	Header files etc to develop libgcrypt applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop libgcrypt applications.

%package static
Summary:	Static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgcrypt library.

%prep
%setup -q
%patch0 -p1

%build
rm -f m4/libtool.m4
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libgcrypt.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo libgcrypt.so.*.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libgcrypt.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS THANKS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/dumpsexp
%attr(755,root,root) %{_bindir}/hmac256
%attr(755,root,root) %ghost /%{_lib}/libgcrypt.so.11
%attr(755,root,root) /%{_lib}/libgcrypt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgcrypt-config
%attr(755,root,root) %{_libdir}/libgcrypt.so
%{_libdir}/libgcrypt.la
%{_infodir}/*.info*
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

