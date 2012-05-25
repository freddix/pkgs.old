%define		module	setuptools

Summary:	A collection of enhancements to the Python distutils
Name:		python-setuptools
Version:	0.6c11
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
# Source0-md5:	7df2a529a074f613b509fb44feefe74e
URL:		http://peak.telecommunity.com/DevCenter/setuptools
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setuptools is a collection of enhancements to the Python distutils
(for Python 2.3.5 and up on most platforms; 64-bit platforms require a
minimum of Python 2.4) that allow you to more easily build and
distribute Python packages, especially ones that have dependencies on
other packages.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--single-version-externally-managed	\
	--optimize 2				\
	--root=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*/*.exe

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
install site.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}*
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/site.py

