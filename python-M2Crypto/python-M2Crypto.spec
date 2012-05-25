Summary:	Python interface to OpenSSL
Name:		python-M2Crypto
Version:	0.21.1
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-%{version}.tar.gz
# Source0-md5:	f93d8462ff7646397a9f77a2fe602d17
Patch0:		%{name}-swig_sources.patch
Patch1:		%{name}-store2ssl.patch
Patch2:		%{name}-swig.patch
URL:		http://wiki.osafoundation.org/bin/view/Projects/MeTooCrypto
BuildRequires:	openssl-devel
BuildRequires:	python-devel
BuildRequires:	swig-python
BuildRequires:	unzip
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M2Crypto makes accessible to the Python programmer the following:
- DH, RSA, DSA, symmetric ciphers, message digests, HMACs.
- SSL functionality to implement clients and servers.
- S/MIME v2.

%prep
%setup -qn M2Crypto-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

find demo -type d -name CVS | xargs rm -rf

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENCE README doc/*.html
%attr(755,root,root) %{py_sitedir}/M2Crypto/*.so
%dir %{py_sitedir}/M2Crypto
%dir %{py_sitedir}/M2Crypto/PGP
%dir %{py_sitedir}/M2Crypto/SSL
%{py_sitedir}/M2Crypto-*.egg-info
%{py_sitedir}/M2Crypto/*.py[oc]
%{py_sitedir}/M2Crypto/PGP/*.py[oc]
%{py_sitedir}/M2Crypto/SSL/*.py[oc]

