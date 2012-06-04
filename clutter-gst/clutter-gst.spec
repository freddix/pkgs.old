Summary:	Library integrating clutter with GStreamer
Name:		clutter-gst
Version:	1.5.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://source.clutter-project.org/sources/clutter-gst/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	9615d8617450a0778e8c5d28fc316163
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	cogl-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer-plugins-bad-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library integrating clutter with GStreamer.

%package devel
Summary:	Header files for clutter-gst library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for clutter-gst library.

%package apidocs
Summary:	clutter-gst API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
clutter-gst API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libclutter-gst-1.0.so.?
%attr(755,root,root) %{_libdir}/libclutter-gst-1.0.so.*.*.*
%{_libdir}/girepository-1.0/ClutterGst-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclutter-gst-1.0.so
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstclutter.so
%{_includedir}/clutter-1.0/clutter-gst
%{_datadir}/gir-1.0/ClutterGst-1.0.gir
%{_pkgconfigdir}/clutter-gst-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

