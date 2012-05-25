%define 	module	isodate

Summary:	An ISO 8601 date/time/duration parser and formater
Name:		python-%{module}
Version:	0.4.7
Release:	1
License:	GPL v3
Group:		Development/Languages
URL:		http://pypi.python.org/pypi/isodate/
Source0:	http://pypi.python.org/packages/source/i/isodate/isodate-%{version}.tar.gz
# Source0-md5:	4ab330655445387b449de381f6ca864c
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ISO 8601 date/time parser.

This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is
not mentioned there, then it is treated as non existent, and not as an
allowed option.

%prep
%setup -qn isodate-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt TODO.txt
%dir %{py_sitescriptdir}/isodate
%{py_sitescriptdir}/isodate/*.py*

