%include	/usr/lib/rpm/macros.perl
#
%define		ver		6.7.6
%define		pver		0
%define		QuantumDepth	16
#
Summary:	Image display, conversion, and manipulation under X
Name:		ImageMagick
Version:	%{ver}%{?pver:.%{pver}}
Release:	2
Epoch:		1
License:	Apache-like
Group:		X11/Applications/Graphics
Source0:	http://www.imagemagick.org/download/%{name}-%{ver}-%{pver}.tar.xz
# Source0-md5:	546ed0fc09435a817837b3e0fd6e307c
Patch0:		%{name}-libpath.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-ldflags.patch
Patch3:		%{name}-link.patch
URL:		http://www.imagemagick.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
BuildRequires:	graphviz-devel
BuildRequires:	jbigkit-devel
BuildRequires:	lcms-devel
BuildRequires:	libgomp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	liblqr-1-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	xorg-libXext-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# we don't want "-s" here, because it would be added to `Magick*-config --ldflags`
%define		filterout_ld	(-Wl,)?-s (-Wl,)?--strip-all
%define		modulesdir	%{_libdir}/ImageMagick-%{ver}/modules-Q%{QuantumDepth}

%description
ImageMagick is an image display, conversion, and manipulation tool. It
runs under X Window. It is very powerful in terms of it's ability to
allow the user to edit images. It can handle many different formats as
well.

%package doc
Summary:	ImageMagick documentation
Group:		Documentation

%description doc
Documentation for ImageMagick.

%package libs
Summary:	ImageMagick libraries
Group:		X11/Libraries

%description libs
ImageMagick libraries.

%package devel
Summary:	Libraries and header files for ImageMagick development
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
This is the ImageMagick development package. It includes header files
for use in developing your own applications that make use of the
ImageMagick code and/or APIs.

%package perl
Summary:	Libraries and modules for access to ImageMagick from Perl
Group:		Development/Languages/Perl
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	perl-dirs

%description perl
This is the ImageMagick Perl support package. It perl modules and
support files for access to ImageMagick library from perl without
unuseful forking or such.

%package c++
Summary:	ImageMagick Magick++ library
Group:		X11/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description c++
This package contains the Magick++ library, a C++ binding to the
ImageMagick graphics manipulation library.

Install ImageMagick-c++ if you want to use any applications that use
Magick++.

%package c++-devel
Summary:	C++ bindings for the ImageMagick library
Group:		X11/Development/Libraries
Requires:	%{name}-c++ = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
ImageMagick-c++-devel contains header files you'll need to develop
ImageMagick applications using the Magick++ C++ bindings. ImageMagick
is an image manipulation program.

If you want to create applications that will use Magick++ code or
APIs, you'll need to install ImageMagick-c++-devel, ImageMagick-devel
and ImageMagick. You don't need to install it if you just want to use
ImageMagick, or if you want to develop/compile applications using the
ImageMagick C interface, however.

%package coders
Summary:	IM coder modules
Group:		X11/Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description coders
IM coder modules.

%prep
%setup -qcTn %{name}-%{ver}-%{pver}
xz -dc %{SOURCE0} | tar xf - -C ..
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__perl} -pi -e 's,lib/graphviz,%{_lib}/graphviz,' configure.ac
find -type f -exec perl -pi -e 's=!/usr/local/bin/perl=!/usr/bin/perl='  {} \;

# avoid rebuilding (broken paths in scripts/Makefile.am)
touch www/Magick++/NEWS.html www/Magick++/ChangeLog.html

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-ltdl-install				\
	--disable-silent-rules				\
	--disable-static				\
	--enable-fast-install				\
	--enable-openmp					\
	--enable-shared					\
	--with-gs-font-dir=%{_fontsdir}/Type1		\
	--with-magick_plus_plus				\
	--with-modules					\
	--with-perl-options="INSTALLDIRS=vendor"	\
	--with-perl=%{__perl}				\
	--with-quantum-depth=%{QuantumDepth}		\
	--with-threads					\
	--with-x					\
	--without-dps					\
	--without-fpx					\
	--without-gslib					\
	--without-wmf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-perl

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdocdir=%{_docdir}/%{name}-devel-%{version}

rm -f $RPM_BUILD_ROOT%{modulesdir}/{coders,filters}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post   c++ -p /sbin/ldconfig
%postun c++ -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%dir %{_datadir}/ImageMagick-%{ver}
%dir %{_libdir}/ImageMagick-%{ver}
%dir %{_libdir}/ImageMagick-%{ver}/config
%dir %{_sysconfdir}/ImageMagick
%dir %{modulesdir}
%dir %{modulesdir}/coders
%dir %{modulesdir}/filters

%attr(755,root,root) %{_bindir}/animate
%attr(755,root,root) %{_bindir}/compare
%attr(755,root,root) %{_bindir}/composite
%attr(755,root,root) %{_bindir}/convert
%attr(755,root,root) %{_bindir}/conjure
%attr(755,root,root) %{_bindir}/display
%attr(755,root,root) %{_bindir}/identify
%attr(755,root,root) %{_bindir}/import
%attr(755,root,root) %{_bindir}/mogrify
%attr(755,root,root) %{_bindir}/montage
%attr(755,root,root) %{_bindir}/stream

%{_libdir}/ImageMagick-%{ver}/config/*.xml

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ImageMagick/*.xml
%{_sysconfdir}/ImageMagick/sRGB.icc

%{_mandir}/man1/[Iacdims]*

%files coders
%defattr(644,root,root,755)
%attr(755,root,root) %{modulesdir}/coders/*.so
%attr(755,root,root) %{modulesdir}/filters/*.so
%{modulesdir}/coders/*.la
%{modulesdir}/filters/*.la

%files doc
%defattr(644,root,root,755)
%doc www

%files libs
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%attr(755,root,root) %ghost %{_libdir}/libMagickCore.so.?
%attr(755,root,root) %ghost %{_libdir}/libMagickWand.so.?
%attr(755,root,root) %{_libdir}/libMagickCore.so.*.*.*
%attr(755,root,root) %{_libdir}/libMagickWand.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-devel-%{version}
%dir %{_includedir}/%{name}
%attr(755,root,root) %{_bindir}/Magick-config
%attr(755,root,root) %{_bindir}/MagickCore-config
%attr(755,root,root) %{_bindir}/MagickWand-config
%attr(755,root,root) %{_bindir}/Wand-config
%attr(755,root,root) %{_libdir}/libMagickCore.so
%attr(755,root,root) %{_libdir}/libMagickWand.so
%{_includedir}/%{name}/magick
%{_includedir}/%{name}/wand
%{_pkgconfigdir}/ImageMagick.pc
%{_pkgconfigdir}/MagickCore.pc
%{_pkgconfigdir}/MagickWand.pc
%{_pkgconfigdir}/Wand.pc
%{_mandir}/man1/Magick-config.1*
%{_mandir}/man1/Wand-config.1*

%files perl
%defattr(644,root,root,755)
%{perl_vendorarch}/Image/*
%dir %{perl_vendorarch}/auto/Image/Magick
%{perl_vendorarch}/auto/Image/Magick/autosplit.ix
%{perl_vendorarch}/auto/Image/Magick/Magick.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Image/Magick/Magick.so
%{_mandir}/man3/Image::Magick.*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libMagick++.so.?
%attr(755,root,root) %{_libdir}/libMagick++.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Magick++-config
%attr(755,root,root) %{_libdir}/libMagick++.so
%{_includedir}/%{name}/Magick++
%{_includedir}/%{name}/Magick++.h
%{_pkgconfigdir}/ImageMagick++.pc
%{_pkgconfigdir}/Magick++.pc
%{_mandir}/man1/Magick++-config.1*

