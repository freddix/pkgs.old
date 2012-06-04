Summary:	Backup program
Name:		obnam
Version:	1.0
Release:	3
License:	GPL v3
Group:		Applications
Source0:	http://code.liw.fi/debian/pool/main/o/obnam/%{name}_%{version}.orig.tar.gz
# Source0-md5:	4fdfc23ac8636d045502c99a12ffdbed
URL:		http://liw.fi/obnam
BuildRequires:	python-cliapp
BuildRequires:	python-devel
BuildRequires:	python-larch
BuildRequires:	python-paramiko
BuildRequires:	python-tracing
BuildRequires:	python-ttystatus
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-cliapp
Requires:	python-larch
Requires:	python-paramiko
Requires:	python-tracing
Requires:	python-ttystatus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A backup tool.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/obnam
%attr(755,root,root) %{_bindir}/obnam-benchmark
%attr(755,root,root) %{_bindir}/obnam-viewprof
%attr(755,root,root) %{py_sitedir}/obnamlib/_obnam.so
%dir %{py_sitedir}/obnamlib
%dir %{py_sitedir}/obnamlib/plugins
%{py_sitedir}/obnamlib/*.py*
%{py_sitedir}/obnamlib/plugins/*.py*
%{_mandir}/man1/obnam.1*
%{_mandir}/man1/obnam-benchmark.1*

