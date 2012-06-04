%include	/usr/lib/rpm/macros.perl

Summary:	OpenSSL Toolkit libraries for the "Secure Sockets Layer" (SSL v2/v3)
Name:		openssl
Version:	0.9.8x
Release:	1
License:	Apache-like
Group:		Libraries
Source0:	ftp://ftp.openssl.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	ee17e9bc805c8cc7d0afac3b0ef78eda
Patch0:		%{name}-include.patch
Patch1:		%{name}-ca-certificates.patch
Patch2:		%{name}-ldflags.patch
Patch3:		%{name}-asflag.patch
Patch4:		%{name}-fips_install.patch
URL:		http://www.openssl.org/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	sed
Requires:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, full-featured, and Open Source toolkit implementing
the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS
v1) protocols with full-strength cryptography world-wide. The project
is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its
related documentation.

OpenSSL is based on the excellent SSLeay library developed by Eric A.
Young and Tim J. Hudson. The OpenSSL toolkit is licensed under an
Apache-style licence, which basically means that you are free to get
and use it for commercial and non-commercial purposes subject to some
simple license conditions.

This package contains shared libraries only, install openssl-tools if
you want to use openssl cmdline tool.

%package tools
Summary:	OpenSSL command line tool and utilities
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description tools
The OpenSSL Toolkit cmdline tool openssl and utility scripts.

%package tools-perl
Summary:	OpenSSL utilities written in Perl
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description tools-perl
OpenSSL Toolkit tools written in Perl.

%package devel
Summary:	Development part of OpenSSL Toolkit libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development part of OpenSSL library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__perl} -pi -e 's#%{_prefix}/local/bin/perl#%{__perl}#g' \
	`grep -l -r "%{_prefix}/local/bin/perl" *`

sed -i -e 's|$prefix/lib/engines|%{_libdir}/engines|g' Configure

%build
touch Makefile.*
%{__perl} util/perlpath.pl %{__perl}

./Configure		\
	--openssldir=%{_sysconfdir}/%{name}	\
	--libdir=%{_lib}			\
	enable-md2 shared zlib threads		\
%ifarch %{ix86}
	linux-elf	\
%endif
%ifarch %{x8664}
	linux-x86_64	\
%endif
	%{rpmcflags} %{rpmldflags} -DOPENSSL_NO_TLS1_2_CLIENT

%{__make} -j1 all rehash	\
	CC="%{__cc}"		\
	INSTALLTOP=%{_prefix}

# Rename POD sources of man pages. "openssl_" prefix is added to each
# manpage to avoid potential conflicts with other packages.

for dir in doc/{apps,ssl,crypto}; do
	cd $dir || exit 1;
	%{__perl} -pi -e 's/(\W)((?<!openssl_)\w+)(\(\d\))/$1openssl_$2$3/g; s/openssl_openssl/openssl/g;' *.pod;

	for pod in !(openssl*).pod; do
		mv -f $pod openssl_$pod;
	done
	cd ../..
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_libdir}/%{name}} \
	$RPM_BUILD_ROOT{%{_mandir}/{pl/man1,man{1,3,5,7}},%{_datadir}/ssl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} -j1 install \
	INSTALLTOP=%{_prefix} \
	INSTALL_PREFIX=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

install lib*.so.*.* $RPM_BUILD_ROOT%{_libdir}
ln -sf libcrypto.so.*.* $RPM_BUILD_ROOT%{_libdir}/libcrypto.so
ln -sf libssl.so.*.* $RPM_BUILD_ROOT%{_libdir}/libssl.so

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/misc/* $RPM_BUILD_ROOT%{_libdir}/%{name}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/misc

# not installed as individual utilities (see openssl dgst instead)
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{md2,md4,md5,mdc2,ripemd160,sha,sha1}.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CHANGES.SSLeay LICENSE NEWS README doc/*.txt
%doc doc/openssl_button.gif doc/openssl_button.html
%attr(755,root,root) %{_libdir}/libcrypto.so.*.*.*
%attr(755,root,root) %{_libdir}/libssl.so.*.*.*
%dir %{_libdir}/engines
%attr(755,root,root) %{_libdir}/engines/*.so
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/certs
%dir %{_sysconfdir}/%{name}/private
%dir %{_datadir}/ssl

%files tools
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/openssl.cnf
%attr(755,root,root) %{_bindir}/%{name}

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/CA.sh
%attr(755,root,root) %{_libdir}/%{name}/c_hash
%attr(755,root,root) %{_libdir}/%{name}/c_info
%attr(755,root,root) %{_libdir}/%{name}/c_issuer
%attr(755,root,root) %{_libdir}/%{name}/c_name

%{_mandir}/man1/openssl.1*
%{_mandir}/man1/openssl_asn1parse.1*
%{_mandir}/man1/openssl_ca.1*
%{_mandir}/man1/openssl_ciphers.1*
%{_mandir}/man1/openssl_crl.1*
%{_mandir}/man1/openssl_crl2pkcs7.1*
%{_mandir}/man1/openssl_dgst.1*
%{_mandir}/man1/openssl_dhparam.1*
%{_mandir}/man1/openssl_dsa.1*
%{_mandir}/man1/openssl_dsaparam.1*
%{_mandir}/man1/openssl_ec.1*
%{_mandir}/man1/openssl_ecparam.1*
%{_mandir}/man1/openssl_enc.1*
%{_mandir}/man1/openssl_errstr.1*
%{_mandir}/man1/openssl_gendsa.1*
%{_mandir}/man1/openssl_genrsa.1*
%{_mandir}/man1/openssl_nseq.1*
%{_mandir}/man1/openssl_ocsp.1*
%{_mandir}/man1/openssl_passwd.1*
%{_mandir}/man1/openssl_pkcs12.1*
%{_mandir}/man1/openssl_pkcs7.1*
%{_mandir}/man1/openssl_pkcs8.1*
%{_mandir}/man1/openssl_rand.1*
%{_mandir}/man1/openssl_req.1*
%{_mandir}/man1/openssl_rsa.1*
%{_mandir}/man1/openssl_rsautl.1*
%{_mandir}/man1/openssl_s_client.1*
%{_mandir}/man1/openssl_s_server.1*
%{_mandir}/man1/openssl_s_time.1*
%{_mandir}/man1/openssl_sess_id.1*
%{_mandir}/man1/openssl_smime.1*
%{_mandir}/man1/openssl_speed.1*
%{_mandir}/man1/openssl_spkac.1*
%{_mandir}/man1/openssl_verify.1*
%{_mandir}/man1/openssl_version.1*
%{_mandir}/man1/openssl_x509.1*
%{_mandir}/man5/openssl_config.5*
%{_mandir}/man5/openssl_x509v3_config.5*

%files tools-perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/c_rehash
%attr(755,root,root) %{_libdir}/%{name}/CA.pl
%{_mandir}/man1/openssl_CA.pl.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcrypto.so
%attr(755,root,root) %{_libdir}/libssl.so
%{_includedir}/%{name}
%{_pkgconfigdir}/libcrypto.pc
%{_pkgconfigdir}/libssl.pc
%{_pkgconfigdir}/openssl.pc
%{_mandir}/man3/openssl*.3*
%{_mandir}/man7/openssl_des_modes.7*

