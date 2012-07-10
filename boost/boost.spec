# TODO: enable openmpi support

%define		fver	%(echo %{version} | tr . _)

Summary:	The Boost C++ Libraries
Name:		boost
Version:	1.50.0
Release:	1
License:	Boost Software License and others
Group:		Libraries
Source0:	http://downloads.sourceforge.net/boost/%{name}_%{fver}.tar.bz2
# Source0-md5:	52dd00be775e689f55a987baebccc462
Patch0:		%{name}-link.patch
URL:		http://www.boost.org/
BuildRequires:	bzip2-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Boost web site provides free peer-reviewed portable C++ source
libraries. The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been proposed for inclusion in the C++ Standards Committee's
upcoming C++ Standard Library Technical Report.

%package devel
Summary:	Boost C++ development headers
Group:		Development/Libraries
Requires:	%{name}-chrono-devel = %{version}-%{release}
Requires:	%{name}-date_time-devel = %{version}-%{release}
Requires:	%{name}-filesystem-devel = %{version}-%{release}
Requires:	%{name}-graph-devel = %{version}-%{release}
Requires:	%{name}-iostreams-devel = %{version}-%{release}
Requires:	%{name}-locale-devel = %{version}-%{release}
Requires:	%{name}-prg_exec_monitor-devel = %{version}-%{release}
Requires:	%{name}-program_options-devel = %{version}-%{release}
Requires:	%{name}-python-devel = %{version}-%{release}
Requires:	%{name}-random-devel = %{version}-%{release}
Requires:	%{name}-regex-devel = %{version}-%{release}
Requires:	%{name}-serialization-devel = %{version}-%{release}
Requires:	%{name}-signals-devel = %{version}-%{release}
Requires:	%{name}-system-devel = %{version}-%{release}
Requires:	%{name}-thread-devel = %{version}-%{release}
Requires:	%{name}-timer-devel = %{version}-%{release}
Requires:	%{name}-unit_test_framework-devel = %{version}-%{release}
Requires:	%{name}-wave-devel = %{version}-%{release}
Requires:	%{name}-wserialization-devel = %{version}-%{release}

%description devel
Header files for the Boost C++ libraries.

%package doc
Summary:	Boost C++ Library documentation
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description doc
Documentation for the Boost C++ Library.

###
%package chrono
Summary:	Boost C++ chrono library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description chrono
Boost C++ chrono library.

%package chrono-devel
Summary:	Boost C++ chrono headers
Group:		Development/Libraries
Requires:	%{name}-chrono = %{version}-%{release}

%description chrono-devel
Boost C++ chrono headers.

###
%package date_time
Summary:	Boost C++ date_time library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description date_time
Boost C++ date_time library.

%package date_time-devel
Summary:	Boost C++ date_time headers
Group:		Development/Libraries
Requires:	%{name}-date_time = %{version}-%{release}

%description date_time-devel
Boost C++ date_time headers.

###
%package filesystem
Summary:	Boost C++ date_time library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description filesystem
Boost C++ filesystem library.

%package filesystem-devel
Summary:	Boost C++ filesystem headers
Group:		Development/Libraries
Requires:	%{name}-filesystem = %{version}-%{release}

%description filesystem-devel
Boost C++ filesystem headers.

###
%package graph
Summary:	Boost C++ graph library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description graph
Boost C++ graph library.

%package graph-devel
Summary:	Boost C++ graph headers
Group:		Development/Libraries
Requires:	%{name}-graph = %{version}-%{release}

%description graph-devel
Boost C++ graph headers.

###
%package iostreams
Summary:	Boost C++ iostreams library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description iostreams
Boost C++ iostreams library.

%package iostreams-devel
Summary:	Boost C++ iostreams headers
Group:		Development/Libraries
Requires:	%{name}-iostreams = %{version}-%{release}

%description iostreams-devel
Boost C++ iostreams headers.

###
%package locale
Summary:	Boost C++ locale library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description locale
Boost C++ locale library.

%package locale-devel
Summary:	Boost C++ locale headers
Group:		Development/Libraries
Requires:	%{name}-locale = %{version}-%{release}

%description locale-devel
Boost C++ locale headers.


###
%package math
Summary:	Boost C++ iostreams libraries
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description math
Boost C++ math libraries.

%package math-devel
Summary:	Boost C++ iostreams headers
Group:		Development/Libraries
Requires:	%{name}-math = %{version}-%{release}

%description math-devel
Boost C++ math headers.

###
%package prg_exec_monitor
Summary:	Boost C++ prg_exec_monitor library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description prg_exec_monitor
Boost C++ prg_exec_monitor library.

%package prg_exec_monitor-devel
Summary:	Boost C++ prg_exec_monitor headers
Group:		Development/Libraries
Requires:	%{name}-prg_exec_monitor = %{version}-%{release}

%description prg_exec_monitor-devel
Boost C++ prg_exec_monitor headers.

###
%package program_options
Summary:	Boost C++ program_options library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description program_options
Boost C++ program_options library.

%package program_options-devel
Summary:	Boost C++ program_options headers
Group:		Development/Libraries
Requires:	%{name}-program_options = %{version}-%{release}

%description program_options-devel
Boost C++ program_options headers.

###
%package python
Summary:	Boost C++ python library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description python
Boost C++ python library.

%package python-devel
Summary:	Boost C++ python headers
Group:		Development/Libraries
Requires:	%{name}-python = %{version}-%{release}

%description python-devel
Boost C++ python headers.

###
%package random
Summary:	Boost C++ random library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description random
Boost C++ random library.

%package random-devel
Summary:	Boost C++ random headers
Group:		Development/Libraries
Requires:	%{name}-random = %{version}-%{release}

%description random-devel
Boost C++ random headers.

###
%package regex
Summary:	Boost C++ regex library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description regex
Boost C++ regex library.

%package regex-devel
Summary:	Boost C++ regex headers
Group:		Development/Libraries
Requires:	%{name}-regex = %{version}-%{release}

%description regex-devel
Boost C++ regex headers.

###
%package serialization
Summary:	Boost C++ serialization library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description serialization
Boost C++ serialization library.

%package serialization-devel
Summary:	Boost C++ serialization headers
Group:		Development/Libraries
Requires:	%{name}-serialization = %{version}-%{release}

%description serialization-devel
Boost C++ serialization headers.

###
%package signals
Summary:	Boost C++ signals library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description signals
Boost C++ signals library.

%package signals-devel
Summary:	Boost C++ signals headers
Group:		Development/Libraries
Requires:	%{name}-signals = %{version}-%{release}

%description signals-devel
Boost C++ signals headers.

###
%package system
Summary:	Boost C++ signals library
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description system
Boost C++ system library.

%package system-devel
Summary:	Boost C++ system headers
Group:		Development/Libraries
Requires:	%{name}-system = %{version}-%{release}

%description system-devel
Boost C++ system headers.

###
%package timer
Summary:	Boost C++ timer library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description timer
Boost C++ timer library.

%package timer-devel
Summary:	Boost C++ timer headers
Group:		Development/Libraries
Requires:	%{name}-timer = %{version}-%{release}

%description timer-devel
Boost C++ timer headers.

###
%package thread
Summary:	Boost C++ thread library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description thread
Boost C++ thread library.

%package thread-devel
Summary:	Boost C++ thread headers
Group:		Development/Libraries
Requires:	%{name}-thread = %{version}-%{release}

%description thread-devel
Boost C++ thread headers.

###
%package unit_test_framework
Summary:	Boost C++ unit_test_framework library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description unit_test_framework
Boost C++ unit_test_framework library.

%package unit_test_framework-devel
Summary:	Boost C++ unit_test_framework headers
Group:		Development/Libraries
Requires:	%{name}-unit_test_framework = %{version}-%{release}

%description unit_test_framework-devel
Boost C++ unit_test_framework headers.

###
%package wave
Summary:	Boost C++ wave library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description wave
Boost C++ wave library.

%package wave-devel
Summary:	Boost C++ wave headers
Group:		Development/Libraries
Requires:	%{name}-wave = %{version}-%{release}

%description wave-devel
Boost C++ wave headers.

###
%package wserialization
Summary:	Boost C++ wserialization library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description wserialization
Boost C++ wserialization library.

%package wserialization-devel
Summary:	Boost C++ wserialization headers
Group:		Development/Libraries
Requires:	%{name}-wserialization = %{version}-%{release}

%description wserialization-devel
Boost C++ wserialization headers.

%package tools
Summary:	Boost tools
Group:		Development/Libraries

%description tools
Boost tools.

%prep
%setup -qn %{name}_%{fver}
%patch0 -p1

sed -i "s/<optimization>speed : -O3/<optimization>speed : ${CXXFLAGS:-%rpmcxxflags} -fPIC/" tools/build/v2/tools/gcc.jam
sed -i 's/<debug-symbols>on : -g/<debug-symbols>on :/' tools/build/v2/tools/gcc.jam
sed -i 's:find-static:find-shared:' libs/graph/build/Jamfile.v2

echo "using mpi ;" >> tools/build/v2/user-config.jam

cat << EOF > tools/build/v2/user-config.jam
using gcc : %(%{__cxx} -dumpversion) : %{__cxx} ;
EOF

%build
PYTHON_ROOT=%{_prefix}
PYTHON_VERSION=2.5

mkdir -p dist/bin
cd tools/build/v2/engine
./build.sh gcc
cd ../../../../
cp tools/build/v2/engine/bin.linuxx86/bjam dist/bin

cd tools
../dist/bin/bjam release	\
	--toolset=gcc		\
	-d2			\
	cflags="%{rpmcflags}"	\
	debug-symbols=on
cd ..

./dist/bin/bjam release		\
	--layout=system		\
	--toolset=gcc		\
	-d2			\
	cflags="%{rpmcflags}"	\
	debug-symbols=on	\
	link=shared		\
	runtime-link=shared	\
	inlining=on		\
	threading=multi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/boostbook,%{_libdir},%{_includedir}}

cp -rf boost $RPM_BUILD_ROOT%{_includedir}

install -p stage/lib/lib*.so.* $RPM_BUILD_ROOT%{_libdir}
cp -a stage/lib/lib*.so $RPM_BUILD_ROOT%{_libdir}
install -p dist/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -rf dist/share/* $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	chrono -p /sbin/ldconfig
%postun	chrono -p /sbin/ldconfig

%post	date_time -p /sbin/ldconfig
%postun	date_time -p /sbin/ldconfig

%post	filesystem -p /sbin/ldconfig
%postun	filesystem -p /sbin/ldconfig

%post	graph -p /sbin/ldconfig
%postun	graph -p /sbin/ldconfig

%post	locale -p /sbin/ldconfig
%postun	locale -p /sbin/ldconfig

%post	iostreams -p /sbin/ldconfig
%postun	iostreams -p /sbin/ldconfig

%post	math -p /sbin/ldconfig
%postun	math -p /sbin/ldconfig

%post	prg_exec_monitor -p /sbin/ldconfig
%postun	prg_exec_monitor -p /sbin/ldconfig

%post	program_options -p /sbin/ldconfig
%postun	program_options -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	regex -p /sbin/ldconfig
%postun	regex -p /sbin/ldconfig

%post	serialization -p /sbin/ldconfig
%postun	serialization -p /sbin/ldconfig

%post	signals -p /sbin/ldconfig
%postun	signals -p /sbin/ldconfig

%post	system -p /sbin/ldconfig
%postun	system -p /sbin/ldconfig

%post	thread -p /sbin/ldconfig
%postun	thread -p /sbin/ldconfig

%post	timer -p /sbin/ldconfig
%postun	timer -p /sbin/ldconfig

%post	unit_test_framework -p /sbin/ldconfig
%postun	unit_test_framework -p /sbin/ldconfig

%post	wave -p /sbin/ldconfig
%postun	wave -p /sbin/ldconfig

%post	wserialization -p /sbin/ldconfig
%postun	wserialization -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE_1_0.txt

%files devel
%defattr(644,root,root,755)
%{_includedir}/boost

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}

###
%files chrono
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_chrono.so.*

%files chrono-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_chrono.so

###
%files date_time
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time.so.*

%files date_time-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time.so

###
%files filesystem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem.so.*

%files filesystem-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem.so

###
%files graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph.so.*

%files graph-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph.so

###
%files iostreams
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams.so.*

###
%files iostreams-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams.so

###
%files locale
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_locale.so.*

###
%files locale-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_locale.so

###
%files math
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_math_*.so.*

###
%files math-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_math_*.so

###
%files prg_exec_monitor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so.*

%files prg_exec_monitor-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so

###
%files program_options
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options.so.*

%files program_options-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options.so

###
%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python.so.*

%files python-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python.so

###
%files random
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_random.so.*

%files random-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_random.so

###
%files regex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex.so.*

%files regex-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex.so

###
%files signals
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals.so.*

%files signals-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals.so

###
%files system
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_system.so.*

%files system-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_system.so

###
%files timer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_timer.so.*

%files timer-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_timer.so

###
%files thread
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread.so.*

%files thread-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread.so

###
%files unit_test_framework
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so.*

%files unit_test_framework-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so

###
%files wave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave.so.*

###
%files wave-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave.so

###
%files serialization
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_serialization.so.*

###
%files serialization-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_serialization.so

###
%files wserialization
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wserialization.so.*

###
%files wserialization-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wserialization.so

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/boostbook

