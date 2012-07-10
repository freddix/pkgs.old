Summary:	The Gimp Toolkit
Name:		gtk+
Version:	2.24.10
Release:	7
Epoch:		2
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-%{version}.tar.xz
# Source0-md5:	7fdcb407dd174010a695b555bf9b65e2
URL:		http://www.gtk.org/
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	cups-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	jasper-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-progs
BuildRequires:	pango-devel
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	shared-mime-info
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXcursor-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXft-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-libXrender-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abivers		2.10.0

%description
GTK+, which stands for the Gimp ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach.

%package libs
Summary:	GTK+ libraries
Group:		X11/Libraries

%description libs
GTK+ libraries.

%package devel
Summary:	GTK+ header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for the GTK+ libraries.

%package apidocs
Summary:	GTK+ API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GTK+ API documentation.

%package update-icon-cache
Summary:	Utility to update icon cache used by GTK+ library
Group:		Applications/System

%description update-icon-cache
Utility to update icon cache used by GTK+ library.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal} -I m4macros
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static		\
	--enable-introspection=yes	\
	--enable-man			\
	--enable-shm			\
	--with-gdktarget=x11		\
	--with-html-dir=%{_gtkdocdir}	\
	--with-xinput=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_sysconfdir}/gtk-2.0} \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/%{abivers}/filesystems

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gtk.immodules

# shut up check-files (static modules and *.la for modules)
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/*/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.la

rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-*/demo

# remove unsupported locale scheme
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/{az_IR,ca@valencia,crh,io,my,ps}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
exit 0

%postun
if [ "$1" != "0" ]; then
	umask 022
	%{_bindir}/gtk-query-immodules-2.0 >%{_sysconfdir}/gtk-2.0/gtk.immodules
fi
exit 0

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gtk-builder-convert
%attr(755,root,root) %{_bindir}/gtk-query*

%dir %{_libdir}/gtk-2.0/modules
%dir %{_libdir}/gtk-2.0/%{abivers}
%dir %{_libdir}/gtk-2.0/%{abivers}/engines
%dir %{_libdir}/gtk-2.0/%{abivers}/filesystems
%dir %{_libdir}/gtk-2.0/%{abivers}/immodules
%dir %{_libdir}/gtk-2.0/%{abivers}/printbackends
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libferret.so
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libgail.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/engines/libpixmap.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/immodules/*.so
%attr(755,root,root) %{_libdir}/gtk-2.0/%{abivers}/printbackends/*.so

%dir %{_datadir}/gtk-2.0
%dir %{_datadir}/themes/Default/gtk-*
%dir %{_datadir}/themes/Emacs
%dir %{_datadir}/themes/Emacs/gtk-*
%dir %{_datadir}/themes/Raleigh
%dir %{_datadir}/themes/Raleigh/gtk-*
%dir %{_sysconfdir}/gtk-2.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk-2.0/im-multipress.conf
%ghost %{_sysconfdir}/gtk-2.0/gtk.immodules
%{_datadir}/themes/Default/gtk-*/gtkrc
%{_datadir}/themes/Emacs/gtk-*/gtkrc
%{_datadir}/themes/Raleigh/gtk-*/gtkrc

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/gtk-2.0
%attr(755,root,root) %ghost %{_libdir}/libgailutil.so.??
%attr(755,root,root) %ghost %{_libdir}/libg*-x11-2.0.so.?
%attr(755,root,root) %{_libdir}/libgailutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libg*-x11-2.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gail-*
%{_includedir}/gtk-*
%{_aclocaldir}/*.m4
%{_libdir}/gtk-*/include
%{_pkgconfigdir}/*.pc

%{_datadir}/gir-1.0/Gtk-2.0.gir
%{_datadir}/gir-1.0/Gdk-2.0.gir
%{_datadir}/gir-1.0/GdkX11-2.0.gir

%{_mandir}/man1/*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gail-libgail-util
%{_gtkdocdir}/gdk
%{_gtkdocdir}/gtk

%files update-icon-cache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-update-icon-cache

