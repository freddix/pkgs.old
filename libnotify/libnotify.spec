Summary:	Desktop notifications library
Name:		libnotify
Version:	0.7.4
Release:	1
License:	LGPL v2.1+ (library), GPL v2+ (tools)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libnotify/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	1ec80af539a176d0e5a430534e98e956
Patch0:		%{name}-no_gtk.patch
URL:		http://developer.gnome.org/notification-spec/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	glib-gio-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
A library that sends desktop notifications to a notification daemon,
as defined in the Desktop Notifications spec. These notifications can
be used to inform the user about an event or display some form of
information without getting in the user's way.

%package devel
Summary:	libnotify header files
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnotify-based programs development.

%package apidocs
Summary:	libnotify API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libnotify  API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libnotify.so.?
%attr(755,root,root) %{_libdir}/libnotify.so.*.*.*
%{_datadir}/gir-1.0/Notify-0.7.gir

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libnotify
%{_pkgconfigdir}/*.pc
%{_libdir}/girepository-1.0/*.typelib

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
