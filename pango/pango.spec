Summary:	System for layout and rendering of internationalized text
Name:		pango
Version:	1.29.4
Release:	1
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/pango/1.29/%{name}-%{version}.tar.bz2
# Source0-md5:	a5ee785f4f31d6bdd8625a09ea3f8b4b
Patch0:		%{name}-xfonts.patch
URL:		http://www.pango.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System for layout and rendering of internationalized text.

%package devel
Summary:	System for layout and rendering of internationalized text
Group:		X11/Development/Libraries
Requires:	%{name}-gir = %{epoch}:%{version}-%{release}

%description devel
Developer files for pango.

%package modules
Summary:	System for layout and rendering of internationalized text
Group:		X11/Development/Libraries
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description modules
System for layout and rendering of internationalized text.

This package contains pango modules for: arabic, bengali, devanagari,
gujarati, gurmukhi, hangul, hebrew, indic, myanmar, tamil, thai.

%package apidocs
Summary:	Pango API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Pango API documentation.

%package gir
Summary:	GObject introspection data
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gobject-introspection-data

%description gir
GObject introspection data for Pango.


%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--enable-introspection=yes	\
	--enable-man			\
	--with-fribidi			\
	--with-html-dir=%{_gtkdocdir}	\
	--with-included-modules=basic-fc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

> $RPM_BUILD_ROOT%{_sysconfdir}/pango/pango.modules

# useless (modules loaded through libgmodule)
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/1.6.0/modules/*.la

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{be@latin,en@shaw,ps}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/pango-querymodules > %{_sysconfdir}/pango/pango.modules
exit 0

%postun -p /sbin/ldconfig

%post modules
umask 022
%{_bindir}/pango-querymodules > %{_sysconfdir}/pango/pango.modules
exit 0

%postun modules
umask 022
%{_bindir}/pango-querymodules > %{_sysconfdir}/pango/pango.modules
exit 0

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/pango-querymodules
%attr(755,root,root) %{_bindir}/pango-view
%attr(755,root,root) %ghost %{_libdir}/libpango-1.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libpangocairo-1.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libpangoft2-1.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libpangox-1.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libpangoxft-1.0.so.?
%attr(755,root,root) %{_libdir}/libpango-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangocairo-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangoft2-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangox-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libpangoxft-1.0.so.*.*.*

%dir %{_libdir}/pango
%dir %{_libdir}/pango/1.6.0
%dir %{_libdir}/pango/1.6.0/modules

%attr(755,root,root) %{_libdir}/pango/1.6.0/modules/*basic*.so
%dir %{_sysconfdir}/pango
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pango/pangox.aliases
%ghost %{_sysconfdir}/pango/pango.modules
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libpango*-1.0.so
%{_pkgconfigdir}/pango*.pc
%{_includedir}/pango-1.0
%{_datadir}/gir-1.0/*.gir

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pango/1.6.0/modules/*.so
%exclude %{_libdir}/pango/1.6.0/modules/*basic*.so

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pango

%files gir
%defattr(644,root,root,755)
%{_libdir}/girepository-1.0/*.typelib

