Summary:	Telepathy Glib bindings
Name:		telepathy-glib
Version:	0.18.1
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz
# Source0-md5:	461732739e3fbf8467991bbe661fb29a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	glib-gio-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy Glib bindings.

%package devel
Summary:	Header files for telepathy-glib library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for telepathy
library.

%package apidocs
Summary:	telepathy-glib API documentation
Group:		Development/Libraries
Requires:	gtk-doc-common

%description apidocs
telepathy-glib API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-static=no	\
	--enable-vala-bindings	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/telepathy

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%dir %{_libdir}/telepathy
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-glib.so.?
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%{_includedir}/telepathy-*
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so
%{_pkgconfigdir}/telepathy-glib.pc
%{_datadir}/gir-1.0/TelepathyGLib-0.12.gir
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-glib

