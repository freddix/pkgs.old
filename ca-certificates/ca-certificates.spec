Summary:	Common CA Certificates PEM files
Name:		ca-certificates
Version:	20120212
Release:	1
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.debian.org/debian/pool/main/c/ca-certificates/%{name}_%{version}.tar.gz
# Source0-md5:	391dea8d827db935ca0d0d1e6641bf23
Source1:	https://www.verisign.com/support/thawte-roots.zip
# Source1-md5:	21a284ebdc6e8f4178d5cc10fb9e1ef2
Source2:	http://www.certum.pl/keys/CA.pem
# Source2-md5:	35610177afc9c64e70f1ce62c1885496
Source3:	http://www.certum.pl/keys/level1.pem
# Source3-md5:	ba2d2e234ef9cfd2e6e5f810c964862e
Source4:	http://www.certum.pl/keys/level2.pem
# Source4-md5:	d06578a04e8cb23071f3870430ea0cf0
Source5:	http://www.certum.pl/keys/level3.pem
# Source5-md5:	47b67c63a52236576fc0d1150327c962
Source6:	http://www.certum.pl/keys/level4.pem
# Source6-md5:	f1f8a65d177745311a1e99f029ae5d71
Source7:	http://www.certum.pl/keys/vs.pem
# Source7-md5:	8da19ffc48c5dcc2868b1aa55f1d5983
Source8:	http://www.certum.pl/keys/na.pem
# Source8-md5:	ba571cb35e7672ff7ae95132ac1bfec4
Source9:	http://www.certum.pl/keys/tsa.pem
# Source9-md5:	1a7b3faf8ed00f4d80297de74862e102
Source10:	http://www.certum.pl/keys/class1.pem
# Source10-md5:	058436b132ea2df6972821f546104a16
Source11:	http://www.certum.pl/keys/class2.pem
# Source11-md5:	5caf7fe99b1fc6e63c40b3d081711d1b
Source12:	http://www.certum.pl/keys/class3.pem
# Source12-md5:	07bc97e21da092ba53535c7379e1b58b
Source13:	http://www.certum.pl/keys/class4.pem
# Source13-md5:	99ef61d509539af89f1c025b67245965
Source14:	http://crt.tcs.terena.org/TERENASSLCA.crt
# Source14-md5:	f62cd1546a8ef14e31ba1ce8eecd234a
Source15:	http://crt.tcs.terena.org/TERENAeScienceSSLCA.crt
# Source15-md5:	5feea35ab01a373f115219706f1f57bd
Source16:	http://crt.tcs.terena.org/TERENAPersonalCA.crt
# Source16-md5:	53eaa497c8fb0b79f14fe9f69693689a
Source17:	http://crt.tcs.terena.org/TERENAeSciencePersonalCA.crt
# Source17-md5:	e25cc655d3ebe920ca9c187e3dde9191
Source18:	http://crt.tcs.terena.org/TERENACodeSigningCA.crt
# Source18-md5:	74c9f511ab03a4e6b7462e310abfa89b
Patch0:		%{name}-undebianize.patch
Patch1:		%{name}-more-certs.patch
Patch2:		%{name}-etc-certs.patch
Patch3:		%{name}-c_rehash.sh.patch
Patch4:		%{name}-endline.patch
Patch5:		%{name}-DESTDIR.patch
Patch6:		%{name}.d.patch
URL:		http://www.cacert.org/
BuildRequires:	openssl-tools
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		certsdir	/etc/certs
%define		openssldir	/etc/openssl/certs

%description
Common CA Certificates PEM files.

%description -l pl.UTF-8
Pliki PEM popularnych certyfikatów CA.

%package update
Summary:	Script for updating CA Certificates database
Summary(pl.UTF-8):	Skrypt do odświeżania bazy certyfikatów CA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mktemp
Requires:	openssl-tools >= 0.9.8i-3

%description update
Script and data for updating CA Certificates database.

%description update -l pl.UTF-8
Skrypt i dane do odświeżania bazy certyfikatów CA.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%{__sed} -i -e 's,@openssldir@,%{openssldir},' sbin/update-ca-certificates*

%{__unzip} -qq %{SOURCE1} -d thawte

find thawte/ -name *.pem -o -name *.txt| while read f ; do
	if (file "$f" | grep -q "PEM"); then
		ff=$(echo $f | sed -e 's|[ ,]|_|g' -e 's|[()]|=|g')
		nname=$(basename "$ff" .pem)
		nname=$(basename "$nname" .txt)
		nname=$(basename "$nname" _b64)
		cp -pi "$f" "thawte/${nname}.crt"
	else
		echo "Skipping $f, doesn't look like PEM CERT"
	fi
done

install -d certum
cp -pi %{SOURCE2} certum
cp -pi %{SOURCE3} certum
cp -pi %{SOURCE4} certum
cp -pi %{SOURCE5} certum
cp -pi %{SOURCE6} certum
cp -pi %{SOURCE7} certum
cp -pi %{SOURCE8} certum
cp -pi %{SOURCE9} certum
cp -pi %{SOURCE10} certum
cp -pi %{SOURCE11} certum
cp -pi %{SOURCE12} certum
cp -pi %{SOURCE13} certum
for a in certum/*.pem; do
	mv -i "$a" "${a%.pem}.crt"
done

install -d terena
openssl x509 -inform DER -in %{SOURCE14} -outform PEM -out terena/$(basename %{SOURCE14})
openssl x509 -inform DER -in %{SOURCE15} -outform PEM -out terena/$(basename %{SOURCE15})
openssl x509 -inform DER -in %{SOURCE16} -outform PEM -out terena/$(basename %{SOURCE16})
openssl x509 -inform DER -in %{SOURCE17} -outform PEM -out terena/$(basename %{SOURCE17})
openssl x509 -inform DER -in %{SOURCE18} -outform PEM -out terena/$(basename %{SOURCE18})

%build
%{__make}

# We have those and more in specific dirs
rm mozilla/{Thawte,thawte,Certum,IGC_A,Deutsche_Telekom_Root_CA_2,Juur-SK}*.crt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_sbindir},%{certsdir},%{_sysconfdir}/ca-certificates.d}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_datadir}/ca-certificates -name '*.crt' -exec sed -i -e 's/\r$//' {} \;

(
cd $RPM_BUILD_ROOT%{_datadir}/ca-certificates
find . -name '*.crt' | sort | cut -b3-
) > $RPM_BUILD_ROOT%{_sysconfdir}/ca-certificates.conf

# build %{certsdir}/ca-certificates.crt
install -d $RPM_BUILD_ROOT%{openssldir}
./sbin/update-ca-certificates --destdir $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{openssldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post update
%{_sbindir}/update-ca-certificates --fresh || :

%files
%defattr(644,root,root,755)
%doc debian/README.Debian debian/changelog
%config(noreplace) %verify(not md5 mtime size) %{certsdir}/ca-certificates.crt

%files update
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/update-ca-certificates
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ca-certificates.conf
%dir %{_sysconfdir}/ca-certificates.d
%{_datadir}/ca-certificates

