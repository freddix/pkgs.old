%define		module	numpy
#
Summary:	Python numerical facilities
Name:		python-%{module}
Version:	1.5.1
Release:	2
Epoch:		1
License:	BSD
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/numpy/%{module}-%{version}.tar.gz
# Source0-md5:	376ef150df41b5353944ab742145352d
URL:		http://sourceforge.net/projects/numpy/
BuildRequires:	lapack-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NumPy is a collection of extension modules to provide high-performance
multidimensional numeric arrays to the Python programming language.

%package devel
Summary:	C header files for numerical modules
Group:		Development/Languages/Python
%pyrequires_eq	python-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
C header files for numerical modules.

%package numarray
Summary:	Array manipulation and computations for python
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description numarray
Numarray provides array manipulation and computational capabilities
similar to those found in IDL, Matlab, or Octave. Using numarray, it
is possible to write many efficient numerical data processing
applications directly in Python without using any C, C++ or Fortran
code (as well as doing such analysis interactively within Python or
PyRAF). For algorithms that are not well suited for efficient
computation using array facilities it is possible to write C functions
(and eventually Fortran) that can read and write numarray arrays that
can be called from Python.

Numarray is a re-implementation of an older Python array module called
Numeric. In general its interface is very similar. It is mostly
backward compatible and will be becoming more so in future releases.

%package numarray-devel
Summary:	Header files for python-numarray
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-numarray = %{epoch}:%{version}-%{release}

%description numarray-devel
Header files for python-numarray.

%package oldnumeric
Summary:	Old numeric packages
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description oldnumeric
Old numeric packages.

%package -n f2py
Summary:	Fortran to Python interface generator
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n f2py
Fortran to Python interface generator.

%prep
%setup -qn %{module}-%{version}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

mv $RPM_BUILD_ROOT%{py_sitedir}/%{module}/site.cfg{.example,}

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/{*.txt,COMPATIBILITY,scipy_compatibility,doc}
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*/{tests,docs}
# already in f2py package
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/f2py/f2py.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/%{module}/core/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/fft/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/lib/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/linalg/*.so
%attr(755,root,root) %{py_sitedir}/%{module}/random/*.so
%dir %{py_sitedir}/%{module}
%dir %{py_sitedir}/%{module}/compat
%dir %{py_sitedir}/%{module}/core
%dir %{py_sitedir}/%{module}/distutils
%dir %{py_sitedir}/%{module}/distutils/command
%dir %{py_sitedir}/%{module}/distutils/fcompiler
%dir %{py_sitedir}/%{module}/fft
%dir %{py_sitedir}/%{module}/lib
%dir %{py_sitedir}/%{module}/lib/benchmarks
%dir %{py_sitedir}/%{module}/linalg
%dir %{py_sitedir}/%{module}/matrixlib
%dir %{py_sitedir}/%{module}/polynomial
%dir %{py_sitedir}/%{module}/random
%dir %{py_sitedir}/%{module}/testing
%dir %{py_sitedir}/%{module}/tools
%dir %{py_sitedir}/numpy/ma
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/compat/*.py[co]
%{py_sitedir}/%{module}/core/*.py[co]
%{py_sitedir}/%{module}/distutils/*.py[co]
%{py_sitedir}/%{module}/distutils/command/*.py[co]
%{py_sitedir}/%{module}/distutils/fcompiler/*.py[co]
%{py_sitedir}/%{module}/fft/*.py[co]
%{py_sitedir}/%{module}/lib/*.py[co]
%{py_sitedir}/%{module}/lib/benchmarks/*.py[co]
%{py_sitedir}/%{module}/linalg/*.py[co]
%{py_sitedir}/%{module}/matrixlib/*.py[co]
%{py_sitedir}/%{module}/polynomial/*.py[co]
%{py_sitedir}/%{module}/random/*.py[co]
%{py_sitedir}/%{module}/testing/*.py[co]
%{py_sitedir}/%{module}/tests
%{py_sitedir}/%{module}/tools/py3tool.py[co]
%{py_sitedir}/numpy/ma/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/core/include
%{py_sitedir}/%{module}/core/lib
%{py_sitedir}/%{module}/random/*.h
%{py_sitedir}/%{module}/site.cfg

%files numarray
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/numarray
%attr(755,root,root) %{py_sitedir}/%{module}/numarray/*.so
%{py_sitedir}/%{module}/numarray/*.py[co]

%files numarray-devel
%defattr(644,root,root,755)
%{py_sitedir}/%{module}/numarray/include

%files oldnumeric
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}/oldnumeric
%{py_sitedir}/%{module}/oldnumeric/*

%files -n f2py
%defattr(644,root,root,755)
%attr(744,root,root) %{_bindir}/f2py
%dir %{py_sitedir}/%{module}/f2py
%{py_sitedir}/%{module}/f2py/*.py[co]
%{py_sitedir}/%{module}/f2py/src

