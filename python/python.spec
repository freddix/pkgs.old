# tests which will not work on 64-bit platforms
%define		no64bit_tests	test_audioop test_rgbimg test_imageop
# tests which may fail because of builder environment limitations (no /proc or /dev/pts)
%define		nobuilder_tests test_resource test_openpty test_socket test_nis test_posix test_locale test_pty test_urllib2 test_zlib
# tests which fail because of some unknown/unresolved reason (this list should be empty)
%define		broken_tests test_anydbm test_bsddb test_re test_shelve test_whichdb test_zipimport test_distutils test_pydoc

%define		py_dyndir	%{py_libdir}/lib-dynload
%define		py_incdir	%{_includedir}/python%{py_ver}
%define		py_libdir	%{py_prefix}/%{_lib}/python%{py_ver}
%define		py_prefix	%{_prefix}
%define		py_sitedir	%{py_libdir}/site-packages
%define		py_ver		2.6

Summary:	Very high level scripting language with X interface
Name:		python
Version:	%{py_ver}.7
Release:	1
Epoch:		1
License:	PSF
Group:		Applications
Source0:	http://www.python.org/ftp/python/%{version}/Python-%{version}.tar.bz2
# Source0-md5:	d40ef58ed88438a870bbeb0ac5d4217b
Source1:	http://www.python.org/ftp/python/doc/%{version}/%{name}-%{version}-docs-html.tar.bz2
# Source1-md5:	a2fc12049840d5c66262c546cdf241fd
Patch0:		%{name}-pythonpath.patch
Patch1:		%{name}-no_ndbm.patch
Patch2:		%{name}-ac_fixes.patch
Patch3:		%{name}-lib64.patch
Patch4:		%{name}-noarch_to_datadir.patch
URL:		http://www.python.org/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	file
BuildRequires:	gdbm-devel
BuildRequires:	gmp-devel
BuildRequires:	libffi-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		test_flags	-l -x
%define		test_list	%{nobuilder_tests} %{broken_tests}

%description
Python is an interpreted, interactive, object-oriented programming
language. It incorporates modules, exceptions, dynamic typing, very
high level dynamic data types, and classes. Python combines remarkable
power with very clear syntax. It has interfaces to many system calls
and libraries, as well as to various window systems, and is extensible
in C or C++. It is also usable as an extension language for
applications that need a programmable interface.

%package libs
Summary:	Python library
Group:		Libraries/Python
# broken detection in rpm/pythondeps.sh
Provides:	python(abi) = %{py_ver}
Provides:	python(bytecode) = %{py_ver}

%description libs
Python shared library and very essental modules for Python binary.

%package modules
Summary:	Python modules
Group:		Libraries/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description modules
Python officially distributed modules.

%package modules-sqlite
Summary:	Python SQLite module
Group:		Libraries/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description modules-sqlite
Python SQLite module.

%package -n pydoc
Summary:	Python interactive module documentation access support
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Obsoletes:	python-pydoc

%description -n pydoc
Python interactive module documentation access support.

%package devel
Summary:	Libraries and header files for building python code
Group:		Development/Languages/Python
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
The Python interpreter is relatively easy to extend with dynamically
loaded extensions and to embed in other programs. This package
contains the header files and libraries which are needed to do both of
these tasks.

%package devel-src
Summary:	Python module sources
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-src
Python module sources.

%package devel-tools
Summary:	Python development tools
Group:		Development/Languages/Python
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description devel-tools
Python development tools such as profilers and debugger.

%package doc
Summary:	Documentation on Python
Group:		Documentation
Obsoletes:	python-docs

%description doc
This package contains documentation on the Python language and
interpretor as a mix of plain ASCII files and LaTeX sources.

%package doc-info
Summary:	Documentation on Python in texinfo format
Group:		Documentation

%description doc-info
Documentation on Python in texinfo format.

%prep
%setup -qn Python-%{version} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
sed -i -e 's#-ltermcap#-ltinfo#g' configure*
%{__autoconf}
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure \
	--enable-shared				\
	--enable-unicode=ucs4			\
	--with-system-ffi			\
	--with-threads				\
	BLDSHARED='$(CC) $(CFLAGS) -shared'	\
	LDSHARED='$(CC) $(CFLAGS) -shared'	\
	LINKCC='$(PURIFY) $(CXX)'		\
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%{__make} \
	OPT="%{rpmcflags}" 2>&1 | awk '
BEGIN { fail = 0; logmsg = ""; }
{
		if ($0 ~ /\*\*\* WARNING:/) {
				fail = 1;
				logmsg = logmsg $0;
		}
		print $0;
}
END { if (fail) { print "\nPROBLEMS FOUND:"; print logmsg; exit(1); } }'

LC_ALL=C
export LC_ALL

%check
%{__make} -j1 test \
        TESTOPTS="%{test_flags} %{test_list}" \
	TESTPYTHON="LD_LIBRARY_PATH=`pwd` PYTHONHOME=`pwd` PYTHONPATH=`pwd`/Lib:`pwd`/Lib/lib-tk:`pwd`/build/lib.linux-`uname -m`-%{py_ver} ./python -tt"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}} \
	$RPM_BUILD_ROOT{%{py_sitedir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT%{_infodir} \
	$RPM_BUILD_ROOT/etc/shrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install Makefile.pre.in $RPM_BUILD_ROOT%{py_libdir}/config

ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython.so
ln -sf libpython%{py_ver}.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libpython%{py_ver}.so

rm -f $RPM_BUILD_ROOT%{_bindir}/python%{py_ver}

#
# create several useful aliases, such as timeit.py, profile.py, pdb.py, smtpd.py
#

# for python devel tools
for script in timeit profile pdb pstats; do
    echo alias $script.py=\"python -m ${script}\"
done > $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh

sed 's/=/ /' \
	< $RPM_BUILD_ROOT/etc/shrc.d/python-devel.sh \
	> $RPM_BUILD_ROOT/etc/shrc.d/python-devel.csh

# for python modules
for script in smtpd webbrowser; do
    echo alias $script.py=\"python -m ${script}\"
done > $RPM_BUILD_ROOT/etc/shrc.d/python-modules.sh

sed 's/=/ /' \
	< $RPM_BUILD_ROOT/etc/shrc.d/python-modules.sh \
	> $RPM_BUILD_ROOT/etc/shrc.d/python-modules.csh

sed -i 's|/usr/bin/python2.6|/usr/bin/python|' $RPM_BUILD_ROOT%{_bindir}/{2to3,pydoc}

# just to cut the noise, as they are not packaged (now)
# first tests
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/test
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/bsddb/test
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/ctypes/test
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/distutils/tests
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/email/test
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/sqlite3/test
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/json/tests
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/lib2to3/tests

# other files
rm -r $RPM_BUILD_ROOT%{py_scriptdir}/plat-*/regen
rm -rf $RPM_BUILD_ROOT%{_bindir}/idle
rm -rf $RPM_BUILD_ROOT%{_datadir}/*/{lib-tk,idlelib,lib-old}
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/ctypes/macholib/fetch_macholib
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/distutils/command/command_template
rm -rf $RPM_BUILD_ROOT%{py_scriptdir}/plat-*/regen

find $RPM_BUILD_ROOT%{py_scriptdir} -name \*.egg-info -exec rm {} \;
find $RPM_BUILD_ROOT%{py_scriptdir} -name \*.bat -exec rm {} \;
find $RPM_BUILD_ROOT%{py_scriptdir} -name \*.txt -exec rm {} \;
find $RPM_BUILD_ROOT%{py_scriptdir} -name README\* -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/python
%{_mandir}/man1/python.1*

%files modules
%defattr(644,root,root,755)
/etc/shrc.d/python-modules*
%exclude %{py_scriptdir}/UserDict.py[co]
%exclude %{py_scriptdir}/codecs.py[co]
%exclude %{py_scriptdir}/copy_reg.py[co]
%exclude %{py_scriptdir}/locale.py[co]
%exclude %{py_scriptdir}/posixpath.py[co]
%exclude %{py_scriptdir}/pdb.py[co]
%exclude %{py_scriptdir}/profile.py[co]
%exclude %{py_scriptdir}/pstats.py[co]
%exclude %{py_scriptdir}/pydoc.py[co]
%exclude %{py_scriptdir}/site.py[co]
%exclude %{py_scriptdir}/stat.py[co]
%exclude %{py_scriptdir}/timeit.py[co]
%exclude %{py_scriptdir}/os.py[co]
%exclude %{py_scriptdir}/encodings/*.py[co]
%exclude %{py_scriptdir}/types.py[co]

%{py_scriptdir}/*.py[co]
%{py_dyndir}/*.egg-info

#
# list .so modules to be sure that all of them are built
#
%attr(755,root,root) %{py_dyndir}/_bisect.so
%attr(755,root,root) %{py_dyndir}/_bsddb.so
%attr(755,root,root) %{py_dyndir}/_bytesio.so
%attr(755,root,root) %{py_dyndir}/_codecs_cn.so
%attr(755,root,root) %{py_dyndir}/_codecs_hk.so
%attr(755,root,root) %{py_dyndir}/_codecs_iso2022.so
%attr(755,root,root) %{py_dyndir}/_codecs_jp.so
%attr(755,root,root) %{py_dyndir}/_codecs_kr.so
%attr(755,root,root) %{py_dyndir}/_codecs_tw.so
%attr(755,root,root) %{py_dyndir}/_collections.so
%attr(755,root,root) %{py_dyndir}/_csv.so
%attr(755,root,root) %{py_dyndir}/_ctypes*.so
%attr(755,root,root) %{py_dyndir}/_curses.so
%attr(755,root,root) %{py_dyndir}/_curses_panel.so
%attr(755,root,root) %{py_dyndir}/_elementtree.so
%attr(755,root,root) %{py_dyndir}/_fileio.so
%attr(755,root,root) %{py_dyndir}/_functools.so
%attr(755,root,root) %{py_dyndir}/_hashlib.so
%attr(755,root,root) %{py_dyndir}/_heapq.so
%attr(755,root,root) %{py_dyndir}/_json.so
%attr(755,root,root) %{py_dyndir}/_locale.so
%attr(755,root,root) %{py_dyndir}/_lsprof.so
%attr(755,root,root) %{py_dyndir}/_multibytecodec.so
%attr(755,root,root) %{py_dyndir}/_multiprocessing.so
%attr(755,root,root) %{py_dyndir}/_random.so
%attr(755,root,root) %{py_dyndir}/_socket.so
%attr(755,root,root) %{py_dyndir}/_ssl.so
%attr(755,root,root) %{py_dyndir}/_testcapi.so
%attr(755,root,root) %{py_dyndir}/_weakref.so
%attr(755,root,root) %{py_dyndir}/array.so
%attr(755,root,root) %{py_dyndir}/audioop.so
%attr(755,root,root) %{py_dyndir}/binascii.so
%attr(755,root,root) %{py_dyndir}/bz2.so
%attr(755,root,root) %{py_dyndir}/cPickle.so
%attr(755,root,root) %{py_dyndir}/cStringIO.so
%attr(755,root,root) %{py_dyndir}/cmath.so
%attr(755,root,root) %{py_dyndir}/crypt.so
%attr(755,root,root) %{py_dyndir}/datetime.so
%attr(755,root,root) %{py_dyndir}/dbm.so
%attr(755,root,root) %{py_dyndir}/dl.so
%attr(755,root,root) %{py_dyndir}/fcntl.so
%attr(755,root,root) %{py_dyndir}/future_builtins.so
%attr(755,root,root) %{py_dyndir}/gdbm.so
%attr(755,root,root) %{py_dyndir}/grp.so
%attr(755,root,root) %{py_dyndir}/imageop.so
%attr(755,root,root) %{py_dyndir}/itertools.so
%attr(755,root,root) %{py_dyndir}/math.so
%attr(755,root,root) %{py_dyndir}/mmap.so
%attr(755,root,root) %{py_dyndir}/nis.so
%attr(755,root,root) %{py_dyndir}/operator.so
%attr(755,root,root) %{py_dyndir}/parser.so
%attr(755,root,root) %{py_dyndir}/pyexpat.so
%attr(755,root,root) %{py_dyndir}/readline.so
%attr(755,root,root) %{py_dyndir}/resource.so
%attr(755,root,root) %{py_dyndir}/select.so
%attr(755,root,root) %{py_dyndir}/spwd.so
%attr(755,root,root) %{py_dyndir}/strop.so
%attr(755,root,root) %{py_dyndir}/syslog.so
%attr(755,root,root) %{py_dyndir}/termios.so
%attr(755,root,root) %{py_dyndir}/time.so
%attr(755,root,root) %{py_dyndir}/unicodedata.so
%attr(755,root,root) %{py_dyndir}/zlib.so

%dir %{py_scriptdir}/bsddb
%dir %{py_scriptdir}/compiler
%dir %{py_scriptdir}/ctypes
%dir %{py_scriptdir}/ctypes/macholib
%dir %{py_scriptdir}/curses
%dir %{py_scriptdir}/distutils
%dir %{py_scriptdir}/distutils/command
%dir %{py_scriptdir}/email
%dir %{py_scriptdir}/email/mime
%dir %{py_scriptdir}/json
%dir %{py_scriptdir}/logging
%dir %{py_scriptdir}/multiprocessing
%dir %{py_scriptdir}/multiprocessing/dummy
%dir %{py_scriptdir}/plat-*
%dir %{py_scriptdir}/wsgiref
%dir %{py_scriptdir}/xml
%dir %{py_scriptdir}/xml/dom
%dir %{py_scriptdir}/xml/etree
%dir %{py_scriptdir}/xml/parsers
%dir %{py_scriptdir}/xml/sax

%{py_scriptdir}/bsddb/*.py[co]
%{py_scriptdir}/compiler/*.py[co]
%{py_scriptdir}/ctypes/*.py[co]
%{py_scriptdir}/ctypes/macholib/*.py[co]
%{py_scriptdir}/curses/*.py[co]
%{py_scriptdir}/distutils/*.py[co]
%{py_scriptdir}/distutils/command/*.py[co]
%{py_scriptdir}/email/*.py[co]
%{py_scriptdir}/email/mime/*.py[co]
%{py_scriptdir}/json/*.py[co]
%{py_scriptdir}/logging/*.py[co]
%{py_scriptdir}/multiprocessing/*.py[co]
%{py_scriptdir}/multiprocessing/dummy/*.py[co]
%{py_scriptdir}/plat-*/*.py[co]
%{py_scriptdir}/wsgiref/*.py[co]
%{py_scriptdir}/xml/*.py[co]
%{py_scriptdir}/xml/dom/*.py[co]
%{py_scriptdir}/xml/etree/*.py[co]
%{py_scriptdir}/xml/parsers/*.py[co]
%{py_scriptdir}/xml/sax/*.py[co]

%files modules-sqlite
%defattr(644,root,root,755)
%dir %{py_scriptdir}/sqlite3
%attr(755,root,root) %{py_dyndir}/_sqlite3.so
%{py_scriptdir}/sqlite3/*.py[co]

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpython*.so.*

%dir %{py_dyndir}
%dir %{py_scriptdir}
%dir %{py_libdir}
%dir %{py_sitescriptdir}
%dir %{py_sitedir}

# shared modules required by python library
%attr(755,root,root) %{py_dyndir}/_struct.so

# modules required by python library
%{py_scriptdir}/UserDict.py[co]
%{py_scriptdir}/codecs.py[co]
%{py_scriptdir}/copy_reg.py[co]
%{py_scriptdir}/locale.py[co]
%{py_scriptdir}/posixpath.py[co]
%{py_scriptdir}/site.py[co]
%{py_scriptdir}/stat.py[co]
%{py_scriptdir}/os.py[co]
# needed by the dynamic sys.lib patch
%{py_scriptdir}/types.py[co]

# encodings required by python library
%dir %{py_scriptdir}/encodings
%{py_scriptdir}/encodings/*.py[co]

%files -n pydoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydoc
%{py_scriptdir}/pydoc.py[co]

%files devel
%defattr(644,root,root,755)
%doc Misc/{ACKS,NEWS,README,README.valgrind,valgrind-python.supp}
%attr(755,root,root) %{_bindir}/python-config
%attr(755,root,root) %{_bindir}/python%{py_ver}-config
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{py_incdir}
%{py_incdir}/*.h

%dir %{py_libdir}/config
%attr(755,root,root) %{py_libdir}/config/makesetup
%attr(755,root,root) %{py_libdir}/config/install-sh
%{py_libdir}/config/Makefile
%{py_libdir}/config/Makefile.pre.in
%{py_libdir}/config/Setup
%{py_libdir}/config/Setup.config
%{py_libdir}/config/Setup.local
%{py_libdir}/config/config.c
%{py_libdir}/config/config.c.in
%{py_libdir}/config/python.o

%files devel-src
%defattr(644,root,root,755)
%attr(-,root,root) %{py_scriptdir}/*.py
%{py_scriptdir}/bsddb/*.py
%{py_scriptdir}/compiler/*.py
%{py_scriptdir}/ctypes/*.py
%{py_scriptdir}/ctypes/macholib/*.py
%{py_scriptdir}/curses/*.py
%{py_scriptdir}/distutils/*.py
%{py_scriptdir}/distutils/command/*.py
%{py_scriptdir}/email/*.py
%{py_scriptdir}/email/mime/*.py
%{py_scriptdir}/encodings/*.py
%{py_scriptdir}/hotshot/*.py
%{py_scriptdir}/json/*.py
%{py_scriptdir}/lib2to3/*.py
%{py_scriptdir}/lib2to3/fixes/*.py
%{py_scriptdir}/lib2to3/pgen2/*.py
%{py_scriptdir}/logging/*.py
%{py_scriptdir}/multiprocessing/*.py
%{py_scriptdir}/multiprocessing/dummy/*.py
%{py_scriptdir}/plat-*/*.py
%{py_scriptdir}/sqlite3/*.py
%{py_scriptdir}/wsgiref/*.py
%{py_scriptdir}/xml/*.py
%{py_scriptdir}/xml/dom/*.py
%{py_scriptdir}/xml/etree/*.py
%{py_scriptdir}/xml/parsers/*.py
%{py_scriptdir}/xml/sax/*.py

%files devel-tools
%defattr(644,root,root,755)
%doc Lib/pdb.doc
/etc/shrc.d/python-devel*
%attr(755,root,root) %{_bindir}/2to3
%attr(755,root,root) %{py_dyndir}/_hotshot.so

%dir %{py_scriptdir}/hotshot
%dir %{py_scriptdir}/lib2to3
%dir %{py_scriptdir}/lib2to3/fixes
%dir %{py_scriptdir}/lib2to3/pgen2

%{py_scriptdir}/hotshot/*.py[co]
%{py_scriptdir}/lib2to3/*.pickle
%{py_scriptdir}/lib2to3/*.py[co]
%{py_scriptdir}/lib2to3/fixes/*.py[co]
%{py_scriptdir}/lib2to3/pgen2/*.py[co]
%{py_scriptdir}/pdb.py[co]
%{py_scriptdir}/profile.py[co]
%{py_scriptdir}/pstats.py[co]
%{py_scriptdir}/timeit.py[co]

%files doc
%defattr(644,root,root,755)
%doc python-%{version}-docs-html/*

