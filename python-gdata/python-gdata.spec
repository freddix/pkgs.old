%define		module	gdata
#
Summary:	Google Data API for Python
Name:		python-%{module}
Version:	1.2.4
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	http://gdata-python-client.googlecode.com/files/%{module}.py-%{version}.tar.gz
# Source0-md5:	521f33a377d64f8a6505ba119415b787
URL:		http://code.google.com/p/gdata-python-client/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Google Data Python Client Library provides a library and source
code that make it easy to access data through Google Data APIs.

%prep
%setup -q -n %{module}.py-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE_NOTES.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/atom
%{py_sitescriptdir}/gdata.py-*.egg-info

