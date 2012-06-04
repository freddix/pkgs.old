%define		upstream_ver	3071201

Summary:	SQLite library
Name:		sqlite3
Version:	3.7.12.1
Release:	1
License:	LGPL
Group:		Libraries
# Source0Download: http://sqlite.org/download.html
Source0:	http://www.sqlite.org/sqlite-src-%{upstream_ver}.zip
# Source0-md5:	f9455b25017ffadc38d11f3dea5b43ae
URL:		http://sqlite.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRequires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _ulibdir        /usr/lib

%description
SQLite is a C library that implements an SQL database engine. A large
subset of SQL92 is supported. A complete database is stored in a
single disk file. The API is designed for convenience and ease of use.
Applications that link against SQLite can enjoy the power and
flexiblity of an SQL database without the administrative hassles of
supporting a separate database server. Because it omits the
client-server interaction overhead and writes directly to disk, SQLite
is also faster than the big database servers for most operations. In
addition to the C library, the SQLite distribution includes a
command-line tool for interacting with SQLite databases and SQLite
bindings for Tcl/Tk.

%package devel
Summary:	Header files for SQLite development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these SQLite.

%prep
%setup -qn sqlite-src-%{upstream_ver}

sed -i 's/mkdir doc/#mkdir doc/' Makefile*

%build
%{__libtoolize}
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	--disable-tcl		\
	--enable-load-extension	\
	--enable-static=no	\
	--enable-threadsafe

%{__make} \
	OPT_FEATURE_FLAGS="\
	-DSQLITE_DISABLE_DIRSYNC=1 \
	-DSQLITE_ENABLE_COLUMN_METADATA=1 \
	-DSQLITE_ENABLE_COLUMN_METADATA=1 \
	-DSQLITE_ENABLE_FTS3=3 \
	-DSQLITE_ENABLE_RTREE=1 \
	-DSQLITE_ENABLE_UNLOCK_NOTIFY=1 \
	-DSQLITE_OMIT_LOAD_EXTENSION=1 \
	-DSQLITE_SECURE_DELETE=1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install sqlite3.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/sqlite3
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/sqlite3.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

