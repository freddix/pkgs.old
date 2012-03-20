Summary:	A utility for determining file types
Name:		file
Version:	5.11
Release:	2
License:	distributable
Group:		Applications/File
Source0:	ftp://ftp.astron.com/pub/file/%{name}-%{version}.tar.gz
# Source0-md5:	16a407bd66d6c7a832f3a5c0d609c27b
Source2:	%{name}-zisofs.magic
Source3:	%{name}-mscompress.magic
Source4:	%{name}-magic.mime-gen.awk
Patch0:		%{name}-search_path.patch
Patch1:		%{name}-am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	libmagic = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is useful for finding out what type of file you are
looking at on your system. For example, if an fsck results in a file
being stored in lost+found, you can run file on it to find out if it's
safe to 'more' it or if it's a binary. It recognizes many file types,
including ELF binaries, system libraries, RPM packages, and many
different graphics formats.

%package -n libmagic
Summary:	libmagic library
Group:		Libraries

%description -n libmagic
Library of functions which operate on magic database file.

%package -n libmagic-devel
Summary:	Header files for libmagic library
Group:		Development/Libraries
Requires:	libmagic = %{version}-%{release}

%description -n libmagic-devel
Library of functions which operate on magic database file.

This package contains the header files needed to develop programs that
use these libmagic.

%package -n python-magic
Summary:	Python bindings for libmagic
Group:		Libraries/Python
Requires:	libmagic = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-magic
Python bindings for libmagic.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cp -p %{SOURCE2} magic/Magdir/zisofs
cp -p %{SOURCE3} magic/Magdir/mscompress

rm -f magic/Magdir/{*.orig,*~}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-fsect-man5 \
	--enable-static=no
%{__make}

cd python
%{__python} setup.py build
cd ..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_libdir}/libmagic.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libmagic.so.*.*.*) \
        $RPM_BUILD_ROOT%{_libdir}/libmagic.so

cd python
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
%py_postclean
cd ..

awk -f %{SOURCE4} < $RPM_BUILD_ROOT%{_datadir}/misc/magic > $RPM_BUILD_ROOT%{_datadir}/misc/magic.mime
ln -s misc $RPM_BUILD_ROOT%{_datadir}/file

rm -f $RPM_BUILD_ROOT%{_mandir}/file-magic4.diff

%check
%{__make} -j1 check

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libmagic -p /sbin/ldconfig
%postun	-n libmagic -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/file
%{_datadir}/file
%{_datadir}/misc/magic
%{_datadir}/misc/magic.mgc
%{_datadir}/misc/magic.mime
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/magic
%{_mandir}/man1/file.1*
%{_mandir}/man5/magic.5*

%files -n libmagic
%defattr(644,root,root,755)
%attr(755,root,root) %ghost /%{_lib}/libmagic.so.?
%attr(755,root,root) /%{_lib}/libmagic.so.*.*.*

%files -n libmagic-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmagic.so
%{_libdir}/libmagic.la
%{_includedir}/magic.h
%{_mandir}/man3/libmagic.3*

%files -n python-magic
%defattr(644,root,root,755)
%{py_sitescriptdir}/magic.py[co]

