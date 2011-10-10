#
%define		_fver	%(echo %{version} | tr . _)
#
Summary:	The Boost C++ Libraries
Name:		boost
Version:	1.44.0
Release:	2
License:	Boost Software License and others
Group:		Libraries
Source0:	http://downloads.sourceforge.net/boost/%{name}_%{_fver}.tar.bz2
# Source0-md5:	f02578f5218f217a9f20e9c30e119c6a
Patch0:		%{name}-link.patch
URL:		http://www.boost.org/
BuildRequires:	boost-jam >= 3.1.3
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	python-devel >= 2.5
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
Requires:	%{name}-date_time-devel = %{version}-%{release}
Requires:	%{name}-filesystem-devel = %{version}-%{release}
Requires:	%{name}-graph-devel = %{version}-%{release}
Requires:	%{name}-iostreams-devel = %{version}-%{release}
Requires:	%{name}-prg_exec_monitor-devel = %{version}-%{release}
Requires:	%{name}-program_options-devel = %{version}-%{release}
Requires:	%{name}-python-devel = %{version}-%{release}
Requires:	%{name}-random-devel = %{version}-%{release}
Requires:	%{name}-regex-devel = %{version}-%{release}
Requires:	%{name}-serialization-devel = %{version}-%{release}
Requires:	%{name}-signals-devel = %{version}-%{release}
Requires:	%{name}-system-devel = %{version}-%{release}
Requires:	%{name}-thread-devel = %{version}-%{release}
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

%prep
%setup -q -n %{name}_%{_fver}
%patch0 -p1

sed -i "s/<optimization>speed : -O3/<optimization>speed : ${CXXFLAGS:-%rpmcxxflags} -fPIC/" tools/build/v2/tools/gcc.jam
sed -i 's/<debug-symbols>on : -g/<debug-symbols>on :/' tools/build/v2/tools/gcc.jam
sed -i 's:find-static:find-shared:' libs/graph/build/Jamfile.v2

%build
PYTHON_ROOT=%{_prefix}
PYTHON_VERSION=2.5
bjam \
	--toolset=gcc		\
	-d2			\
	debug-symbols=on	\
	inlining=on		\
	threading=multi		\
	variant=release

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -rf boost $RPM_BUILD_ROOT%{_includedir}

install bin.v2/libs/*/build/gcc-*/release/debug-symbols-on/inlining-on/threading-multi/lib*.so.*.*.* \
	$RPM_BUILD_ROOT%{_libdir}

# create symlinks without -gccXX-mt-* things in names
for f in $RPM_BUILD_ROOT%{_libdir}/*.so.*.*.*; do
	[ -f "$f" ] || continue
	f=$(basename "$f")
	soname=$(basename "$f" | sed -e 's#-gcc..-mt-.*#.so#g')
	[ ! -f "$RPM_BUILD_ROOT%{_libdir}/$soname" ] && ln -s "$f" "$RPM_BUILD_ROOT%{_libdir}/$soname"
	rawsoname=$(basename "$f" | sed -e 's#\.so.*#.so#g')
	[ ! -f "$RPM_BUILD_ROOT%{_libdir}/$rawsoname" ] && ln -s "$f" "$RPM_BUILD_ROOT%{_libdir}/$rawsoname"
done

# documentation
install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}

%if 0
# as the documentation doesn't completely reside in a directory of its
# own, we need to find out ourselves... this looks for HTML files and
# then collects everything linked from those.  this is certainly quite
# unoptimized wrt mkdir calls, but does it really matter?
installdocs() {
for i in $(find -type f -name '*.htm*'); do
	# bjam docu is included in the boost-jam RPM
	if test "`echo $i | sed 's,jam_src,,'`" = "$i"; then
		install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/${i%/*}
		for LINKED in `%{__perl} - $i $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/$i <<'EOT'
			sub rewrite_link
			{
				my $link = shift;
				# rewrite links from boost/* to %{_includedir}/boost/* and
				# ignore external links as well as document-internal ones.
				# HTML files are also ignored as they get installed anyway.
				if (!($link =~ s,^(?:../)*boost/,%{_includedir}/boost/,) && !($link =~ m,(?:^[^/]+:|^\#|\.html?(?:$|\#)),))
				{
					(my $file = $link) =~ s/\#.*//;
					print "$file\n";
				}
				$link;
			}
			open IN, @ARGV[0];
			open OUT, ">@ARGV[1]";
			my $in_link;
			while (<IN>)
			{
				$in_link and s/^\s*"([^"> ]*)"/'"' . rewrite_link($1) . '"'/e;
				s/(href|src)="([^"> ]*)"/"$1=\"" . rewrite_link($2) . '"'/eig;
				print OUT;
				$in_link = /href|src=\s*$/;
			}
EOT`; do
			TARGET=${i%/*}/$LINKED
			# ignore non-existant linked files
			if test -f $TARGET; then
				install -D -m 644 $TARGET $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/$TARGET
			fi
		done
	fi
done
}; installdocs
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	date_time -p /sbin/ldconfig
%postun	date_time -p /sbin/ldconfig

%post	filesystem -p /sbin/ldconfig
%postun	filesystem -p /sbin/ldconfig

%post	graph -p /sbin/ldconfig
%postun	graph -p /sbin/ldconfig

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

