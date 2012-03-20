%define		module	Pyrex
#
Summary:	Language for writing Python Extension Modules
Name:		python-%{module}
Version:	0.9.8.5
Release:	2
License:	free
Group:		Libraries/Python
Source0:	http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/%{module}-%{version}.tar.gz
# Source0-md5:	3b3d8397c2c9a58fc59a90e2b49c651a
URL:		http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
%pyrequires_eq	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Pyrex lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python.

%prep
%setup -qn %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install			\
	--root=$RPM_BUILD_ROOT			\
	--install-purelib=%{py_sitescriptdir}	\
	-O2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*

