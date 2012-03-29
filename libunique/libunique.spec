Summary:	Library to make sure only one instance of a program is running
Name:		libunique
Version:	1.1.6
Release:	4
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libunique/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	7955769ef31f1bc4f83446dbb3625e6d
Patch0:		%{name}-gchar.patch
URL:		http://live.gnome.org/LibUnique
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unique is a library for writing single instance application. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%package devel
Summary:	Header files for unique library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel

%description devel
Header files for unique library.

%package apidocs
Summary:	unique library API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
unique library API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-introspection	\
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
%doc AUTHORS README
%attr(755,root,root) %ghost %{_libdir}/libunique-1.0.so.?
%attr(755,root,root) %{_libdir}/libunique-1.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunique-1.0.so
%{_includedir}/unique-1.0
%{_pkgconfigdir}/unique-1.0.pc
%{_datadir}/gir-1.0/Unique-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/unique

