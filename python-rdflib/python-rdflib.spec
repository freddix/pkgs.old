%define		module	rdflib

Summary:	Python library for working with RDF
Name:		python-%{module}
Version:	3.2.0
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://www.rdflib.net/%{module}-%{version}.tar.gz
# Source0-md5:	ab3d3a5f71ebb6fe4fd33539f5d5768e
URL:		http://www.rdflib.net/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-isodate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer, a TripleStore, an InformationStore and various
store backends. It is being developed by Daniel Krech along with the
help of a number of contributors.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{py_sitescriptdir}/rdflib

