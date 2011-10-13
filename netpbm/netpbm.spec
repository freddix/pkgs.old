Summary:	A library for handling different graphics file formats
Name:		netpbm
Version:	10.35.82
Release:	1
License:	Freeware
Group:		Libraries
Source0:	http://downloads.sourceforge.net/netpbm/%{name}-%{version}.tgz
# Source0-md5:	fcae2fc7928ad7d31b0540ec0c3e710b
Patch0:		%{name}-make.patch
Patch1:		%{name}-build.patch
URL:		http://netpbm.sourceforge.net/
BuildRequires:	flex
BuildRequires:	jasper-devel
BuildRequires:	jbigkit-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel
BuildRequires:	perl-base
BuildRequires:	perl-modules
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The netpbm package contains a library of functions which support
programs for handling various graphics file formats, including .pbm
(portable bitmaps), .pgm (portable graymaps), .pnm (portable anymaps),
.ppm (portable pixmaps) and others.

%package devel
Summary:	Development tools for programs which will use the netpbm libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The netpbm-devel package contains the header files and programmer's
documentation for developing programs which can handle the various
graphics file formats supported by the netpbm libraries.

%package progs
Summary:	Tools for manipulating graphics files in netpbm supported formats
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
The netpbm-progs package contains a group of scripts for manipulating
the graphics files in formats which are supported by the netpbm
libraries. For example, netpbm-progs includes the rasttopnm script,
which will convert a Sun rasterfile into a portable anymap.
Netpbm-progs contains many other scripts for converting from one
graphics file format to another.

%package progs-pstopnm
Summary:	pstopnm - tool to convert PostScript files to PNM images
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	fonts-Type1-urw
Requires:	ghostscript
Obsoletes:	libgr-progs
Conflicts:	ghostscript-esp

%description progs-pstopnm
This package contains pstopnm tool to convert PostScript files to PNM
images.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure << EOF



















EOF

# it appends defines to pm_config.h twice if -j > 1
%{__make} -j1 \
	CC="%{__cc}"					\
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fPIC"	\
	JASPERDEPLIBS="-ljasper"			\
	JASPERHDR_DIR="%{_includedir}/jasper"		\
	JASPERLIB=""					\
	JPEGINC_DIR=%{_includedir}			\
	JPEGLIB_DIR=%{_libdir}				\
	LDFLAGS="%{rpmldflags}"				\
	LINUXSVGALIB="NONE"				\
	NETPBM_DOCURL="%{_docdir}/%{name}-%{version}/netpbm.sourceforge.net/doc/"
	PNGINC_DIR=%{_includedir}			\
	PNGLIB_DIR=%{_libdir}				\
	TIFFINC_DIR=%{_includedir}			\
	TIFFLIB_DIR=%{_libdir}				\
	X11LIB=%{_libdir}/libX11.so			\
	XML2LIBS="$(%{_bindir}/xml2-config --libs)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir},%{_mandir}/man{1,3,5}}

rm -rf PKG
%{__make} -j1 package \
	pkgdir=$(pwd)/PKG \
	LINUXSVGALIB="NONE"

%{__rm} PKG/bin/doc.url
cp -df PKG/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -df PKG/lib/* $RPM_BUILD_ROOT%{_libdir}
install PKG/link/*.a $RPM_BUILD_ROOT%{_libdir}
install PKG/include/*.h $RPM_BUILD_ROOT%{_includedir}
install PKG/man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install PKG/man/man3/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install PKG/man/man5/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

# Install the static-only librle.a
install urt/{rle,rle_config}.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{COPYRIGHT.PATENT,HISTORY,USERDOC}
%attr(755,root,root) %ghost %{_libdir}/libnetpbm.so.??
%attr(755,root,root) %{_libdir}/libnetpbm.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetpbm.so
%{_includedir}/bitio.h
%{_includedir}/colorname.h
%{_includedir}/mallocvar.h
%{_includedir}/nstring.h
%{_includedir}/pam*.h
%{_includedir}/pbm*.h
%{_includedir}/pgm.h
%{_includedir}/pm*.h
%{_includedir}/pnm.h
%{_includedir}/ppm*.h
%{_includedir}/rle*.h
%{_includedir}/shhopt.h
%{_mandir}/man3/libnetpbm.3*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%exclude %{_bindir}/pstopnm
%exclude %{_mandir}/man1/pstopnm.1*

%files progs-pstopnm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pstopnm
%{_mandir}/man1/pstopnm.1*

