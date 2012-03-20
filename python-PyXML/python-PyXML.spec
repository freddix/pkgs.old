%define	module	PyXML

Summary:	Python/XML package
Name:		python-%{module}
Version:	0.8.4
Release:	13
License:	BeOpen Python Open Source License
Vendor:		XML-SIG <xml-sig@python.org>
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyxml/%{module}-%{version}.tar.gz
# Source0-md5:	1f7655050cebbb664db976405fdba209
Patch0:		%{name}-python26.patch
URL:		http://pyxml.sourceforge.net/
BuildRequires:	expat-devel
BuildRequires:	python
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyXML package is a collection of libraries to process XML with
Python.

%prep
%setup -qn %{module}-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build \
	--with-libexpat=%{_prefix} \
	--ldflags=-lexpat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc ANNOUNCE CREDITS LICENCE README* TODO
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/_xmlplus

