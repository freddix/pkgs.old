Summary:	PNG library
Name:		libpng14
Version:	1.4.9
Release:	3
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libpng/libpng-%{version}.tar.xz
# Source0-md5:	3d6ca2f99f1f19dd746975e7fce6a45c
Patch0:		%{name}-pngminus.patch
# http://heanet.dl.sourceforge.net/project/vdubapngmod/libpng-apng-patch/%{version}/libpng-%{version}-apng.patch
Patch1:		%{name}-apng.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%package devel
Summary:	Header files for libpng
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The header files are only needed for development of programs using the
PNG library.

%package static
Summary:	Static png library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static ppng library.

%prep
%setup -qn libpng-%{version}
%patch0 -p1
%patch1 -p0

%build
%if 0
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%endif
%configure
%{__make}
%{__make} -C contrib/pngminus -f makefile.std	\
	CC="%{__cc}"				\
	LIBPATH=%{_libdir}			\
	OPT_FLAGS="%{rpmcppflags} %{rpmcflags}"

%check
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README LICENSE
%attr(755,root,root) %ghost %{_libdir}/libpng14.so.??
%attr(755,root,root) %{_libdir}/libpng14.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/libpng14-config
%attr(755,root,root) %{_libdir}/libpng14.so
%{_includedir}/libpng14
%{_pkgconfigdir}/libpng14.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpng14.a

