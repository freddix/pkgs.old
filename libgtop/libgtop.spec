Summary:	LibGTop library
Name:		libgtop
Version:	2.28.4
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgtop/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	058ad506a5b90a43ee478bb0580e8ee4
Patch0:		%{name}-configure.patch
URL:		http://www.home-of-linux.org/gnome/libgtop/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkg-config
BuildRequires:	popt-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library that fetches information about the running system such as
cpu and memory usage, active processes etc. On Linux systems, these
information are taken directly from the /proc filesystem while on
other systems a server is used to read those information from
/dev/kmem or whatever.

%package devel
Summary:	Header files and etc for develop LibGTop applications
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and etc for develop LibGTop applications.

%package apidocs
Summary:	libgtop API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgtop API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}	\
	--with-libgtop-smp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw,es_ES,la,ps}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgtop-2.0.so.?
%attr(755,root,root) %{_libdir}/libgtop-2.0.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtop-2.0.so
%{_libdir}/libgtop-2.0.la
%{_includedir}/libgtop-2.0
%{_datadir}/gir-1.0/GTop-2.0.gir
%{_infodir}/*info*
%{_pkgconfigdir}/libgtop-2.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

