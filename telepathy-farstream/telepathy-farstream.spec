Summary:	Telepathy client to handle media streaming channels
Name:		telepathy-farstream
Version:	0.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-farstream/%{name}-%{version}.tar.gz
# Source0-md5:	52d110f8a9f27bce0a6c2c07e18aee56
URL:		http://telepathy.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	farstream-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-devel
BuildRequires:	python-gstreamer-devel
BuildRequires:	python-pygobject-devel
BuildRequires:	telepathy-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-farstream is a Telepathy client that uses Farsight and
GStreamer to handle media streaming channels. It's used as a
background process by other Telepathy clients, rather than presenting
any user interface of its own.

%package devel
Summary:	Header files for telepathy-farstrean library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for telepathy-farstream library.

%package apidocs
Summary:	telepathy-farstream library API documentation
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	telepathy-farsight-apidocs < 0.0.20

%description apidocs
telepathy-farstream library API documentation.

%package -n python-telepathy-farstream
Summary:	telepathy-farstream Python bindings
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-telepathy-farstream
telepathy-farstream Python bindings.

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
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-farstream.so.?
%attr(755,root,root) %{_libdir}/libtelepathy-farstream.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtelepathy-farstream.so
%{_includedir}/telepathy-1.0/telepathy-farstream
%{_pkgconfigdir}/telepathy-farstream.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-farstream

%files -n python-telepathy-farstream
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/tpfarstream.so

