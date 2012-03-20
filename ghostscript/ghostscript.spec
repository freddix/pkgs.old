%bcond_with	bootstrap

Summary:	PostScript & PDF interpreter and renderer
Name:		ghostscript
Version:	8.71
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://ghostscript.com/releases/%{name}-%{version}.tar.xz
# Source0-md5:	5005d68f7395c2bfc4b05c1a60d9b6ba
Patch0:		%{name}-missquotes.patch
Patch1:		%{name}-setuid.patch
Patch2:		%{name}-time_h.patch
Patch3:		%{name}-fPIC.patch
URL:		http://www.ghostscript.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	docbook-style-dsssl
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-libX11-devel
%if ! %{with bootstrap}
BuildRequires:	glib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ghostscript is a PostScript interpreter. It can render both PostScript
and PDF compliant files to devices which include an X window, many
printer formats (including support for color printers), and popular
graphics file formats.

%package devel
Summary:	libgs header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgs - ghostscript shared library.

%package ijs-devel
Summary:	IJS development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description ijs-devel
IJS development files.

%package pstoraster
Summary:	pstoraster
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description pstoraster
pstoraster.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} -DA4"					\
	--with-fontpath="%{_datadir}/fonts:%{_datadir}/fonts/Type1"	\
	--with-ijs							\
	--without-jbig2dec						\
	--without-omni							\
	--without-x

cd ijs
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--enable-shared
cd ..

%{__make} -j1 so \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} -j1 \
	docdir=%{_docdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/ghostscript/lib,%{_libdir},%{_includedir}/{ghostscript,ps}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} soinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}-%{version}

%{__make} -C ijs install \
	DESTDIR=$RPM_BUILD_ROOT

# Headers
install psi/{iapi,ierrors}.h $RPM_BUILD_ROOT%{_includedir}/ghostscript
install base/gdevdsp.h $RPM_BUILD_ROOT%{_includedir}/ghostscript

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc \
	$RPM_BUILD_ROOT%{_bindir}/*.sh \
	$RPM_BUILD_ROOT%{_mandir}/man1/{ps2pdf1{2,3},gsbj,gsdj,gsdj500,gslj,eps2eps}.1 \
	$RPM_BUILD_ROOT%{_mandir}/de/man1/{ps2pdf1{2,3},eps2eps}.1

echo ".so gs.1"     > $RPM_BUILD_ROOT%{_mandir}/man1/ghostscript.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2pdf13.1
echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/man1/eps2eps.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsbj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gsdj500.1
echo ".so gslp.1"   > $RPM_BUILD_ROOT%{_mandir}/man1/gslj.1

echo ".so ps2ps.1"  > $RPM_BUILD_ROOT%{_mandir}/de/man1/eps2eps.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/de/man1/ps2pdf12.1
echo ".so ps2pdf.1" > $RPM_BUILD_ROOT%{_mandir}/de/man1/ps2pdf13.1

ln -sf gs $RPM_BUILD_ROOT%{_bindir}/gsc
ln -sf gs $RPM_BUILD_ROOT%{_bindir}/ghostscript

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}

%dir %{_datadir}/ghostscript
%dir %{_datadir}/ghostscript/%{version}
%dir %{_datadir}/ghostscript/%{version}/lib

%attr(755,root,root) %{_bindir}/[bdeflpsux]*
%attr(755,root,root) %{_bindir}/ghostscript
%attr(755,root,root) %{_bindir}/gs
%attr(755,root,root) %{_bindir}/gs[!x]*
%attr(755,root,root) %{_bindir}/ijs_*_example
%attr(755,root,root) %{_bindir}/wftopfa

%attr(755,root,root) %ghost %{_libdir}/libgs.so.?
%attr(755,root,root) %{_libdir}/libgs.so.*.*

%attr(755,root,root) %{_libdir}/libijs-*.so

%{_datadir}/%{name}/%{version}/lib/pphs
%{_datadir}/ghostscript/%{version}/Resource
%{_datadir}/ghostscript/%{version}/examples
%{_datadir}/ghostscript/%{version}/lib/*.*

%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgs.so
%{_includedir}/ghostscript
%{_includedir}/ps

%files ijs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ijs-config
%attr(755,root,root) %{_libdir}/libijs.so
%{_includedir}/ijs
%{_libdir}/libijs.la
%{_pkgconfigdir}/*.pc

%files pstoraster
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/cups/filter/pstoraster
%{_sysconfdir}/cups/pstoraster.convs

