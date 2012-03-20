%define		major	8.5
%define		minor	11
#
Summary:	Tk GUI toolkit for Tcl, with shared libraries
Name:		tk
Version:	%{major}.%{minor}
Release:	2
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://downloads.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
# Source0-md5:	b61b72f0aad230091b100746f078b8f1
Patch0:		%{name}-ieee.patch
Patch1:		%{name}-manlnk.patch
Patch2:		%{name}-pil.patch
Patch3:		%{name}-opt_flags_pass_fix.patch
Patch4:		%{name}-soname_fix.patch
Patch5:		%{name}-norpath.patch
# http://www.tclsource.org/?page=tk
Patch6:		%{name}-aa-cairo.patch
Patch7:		%{name}-unix-scrollbars.patch
Patch8:		%{name}-unix-3d-borders.patch
Patch9:		%{name}-lib64.patch
Patch10:	%{name}-x.patch
Patch11:	%{name}-no_tcl_stub.patch
Patch12:	%{name}-link.patch
URL:		http://www.tcl.tk/
BuildRequires:	autoconf
BuildRequires:	tcl-devel >= %{version}
BuildRequires:	xorg-libXScrnSaver-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXft-devel
Requires:	tcl >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	/usr/lib

%description
Tk is a X Window widget set designed to work closely with the Tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%package devel
Summary:	Tk GUI toolkit for Tcl header files and development documentation
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}
Requires:	tcl-devel >= %{version}

%description devel
Tk GUI toolkit for Tcl header files and development documentation.

%package demo
Summary:	Tk GUI toolkit for Tcl - demo programs
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description demo
Tk GUI toolkit for Tcl - demo programs.

%prep
%setup -qn %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
cd unix
%{__autoconf}
TCL_BIN_DIR=%{_libdir}
%configure \
	--disable-symbols	\
	--disable-threads	\
	--enable-64bit		\
	--enable-shared		\
	--enable-xft
%{__make}

sed -i -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}/%{name}-private#" tkConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_ulibdir}}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT%{_includedir}/%{name}-private/'{}' ';'
for h in $RPM_BUILD_ROOT%{_includedir}/*.h; do
	rh=$(basename "$h")
	if [ -f "$RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic/$rh" ]; then
		ln -sf "../../$rh" $RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic
	fi
done

ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk.so
ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk%{major}.so
ln -sf libtk%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtk%{major}.so.0
mv -f $RPM_BUILD_ROOT%{_bindir}/wish%{major} $RPM_BUILD_ROOT%{_bindir}/wish

if [ "%{_libdir}" != "%{_ulibdir}" ] ; then
	mv $RPM_BUILD_ROOT%{_libdir}/tk* $RPM_BUILD_ROOT%{_ulibdir}
fi

install generic/tkInt.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%dir %{_ulibdir}/tk%{major}
%dir %{_ulibdir}/tk%{major}/msgs
%{_ulibdir}/tk%{major}/*.tcl
%{_ulibdir}/tk%{major}/images
%{_ulibdir}/tk%{major}/msgs/en.msg
%{_ulibdir}/tk%{major}/tclIndex
%{_ulibdir}/tk%{major}/tkAppInit.c
%{_ulibdir}/tk%{major}/ttk

%lang(cs) %{_ulibdir}/tk%{major}/msgs/cs.msg
%lang(da) %{_ulibdir}/tk%{major}/msgs/da.msg
%lang(de) %{_ulibdir}/tk%{major}/msgs/de.msg
%lang(el) %{_ulibdir}/tk%{major}/msgs/el.msg
%lang(en_GB) %{_ulibdir}/tk%{major}/msgs/en_gb.msg
%lang(eo) %{_ulibdir}/tk%{major}/msgs/eo.msg
%lang(es) %{_ulibdir}/tk%{major}/msgs/es.msg
%lang(fr) %{_ulibdir}/tk%{major}/msgs/fr.msg
%lang(hu) %{_ulibdir}/tk%{major}/msgs/hu.msg
%lang(it) %{_ulibdir}/tk%{major}/msgs/it.msg
%lang(nl) %{_ulibdir}/tk%{major}/msgs/nl.msg
%lang(pl) %{_ulibdir}/tk%{major}/msgs/pl.msg
%lang(pt) %{_ulibdir}/tk%{major}/msgs/pt.msg
%lang(ru) %{_ulibdir}/tk%{major}/msgs/ru.msg
%lang(sv) %{_ulibdir}/tk%{major}/msgs/sv.msg
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/tkConfig.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libtkstub%{major}.a
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/mann/*

%files demo
%defattr(644,root,root,755)
%{_ulibdir}/tk%{major}/demos

