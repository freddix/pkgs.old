%define		module	Crypto

Summary:	Python Cryptography Toolkit
Name:		python-%{module}
Version:	2.6
Release:	2
License:	Free
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
# Source0-md5:	88dad0a270d1fe83a39e0467a66a22bb
URL:		http://www.amk.ca/python/code/crypto.html
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
BuildRequires:	python
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:
- hash functions: MD2, MD4, RIPEMD
- block encryption algorithms: AES, ARC2, Blowfish, CAST, DES, Triple-DES,
  IDEA, RC5
- stream encryption algorithms: ARC4, simple XOR
- public-key algorithms: RSA, DSA, ElGamal, qNEW
- protocols: All-or-nothing transforms, chaffing/winnowing
- miscellaneous: RFC1751 module for converting 128-key keys into a set
  of English words, primality testing
- some demo programs (currently all quite old and outdated)

%prep
%setup -qn pycrypto-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/Crypto/SelfTest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS ChangeLog README TODO Doc
%attr(755,root,root) %{py_sitedir}/%{module}/*/*.so
%dir %{py_sitedir}/%{module}
%dir %{py_sitedir}/%{module}/Cipher
%dir %{py_sitedir}/%{module}/Hash
%dir %{py_sitedir}/%{module}/Protocol
%dir %{py_sitedir}/%{module}/PublicKey
%dir %{py_sitedir}/%{module}/Random
%dir %{py_sitedir}/%{module}/Random/Fortuna
%dir %{py_sitedir}/%{module}/Random/OSRNG
%dir %{py_sitedir}/%{module}/Signature
%dir %{py_sitedir}/%{module}/Util
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/*/*.py[co]
%{py_sitedir}/%{module}/*/*/*.py[co]

