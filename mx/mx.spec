Summary:	Mx Toolkit
Name:		mx
Version:	1.4.5
Release:	1
License:	LGPL v2.1
Group:		X11/Libraries
Source0:	http://source.clutter-project.org/sources/mx/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	fda6be1b5818e5b04150ef4fde3b4762
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mx is a widget toolkit using Clutter that provides a set of standard
interface elements, including buttons, progress bars, scroll bars and
others. It also implements some standard managers. One other
interesting feature is the possibility setting style properties from a
CSS format file.

%package devel
Summary:	Header files for mx libraries
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for mx libraries.

%package apidocs
Summary:	mx libraries API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for mx libraries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mx-create-image-cache
%attr(755,root,root) %ghost %{_libdir}/libmx-1.0.so.?
%attr(755,root,root) %ghost %{_libdir}/libmx-gtk-1.0.so.?
%attr(755,root,root) %{_libdir}/libmx-1.0.so.*.*.*
%attr(755,root,root) %{_libdir}/libmx-gtk-1.0.so.*.*.*
%{_libdir}/girepository-1.0/Mx-1.0.typelib
%{_libdir}/girepository-1.0/MxGtk-1.0.typelib
%{_datadir}/mx

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmx-1.0.so
%attr(755,root,root) %{_libdir}/libmx-gtk-1.0.so
%{_libdir}/libmx-1.0.la
%{_libdir}/libmx-gtk-1.0.la
%{_datadir}/gir-1.0/Mx-1.0.gir
%{_datadir}/gir-1.0/MxGtk-1.0.gir
%{_includedir}/mx-1.0
%{_pkgconfigdir}/mx-1.0.pc
%{_pkgconfigdir}/mx-gtk-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/mx-gtk
%{_gtkdocdir}/mx

