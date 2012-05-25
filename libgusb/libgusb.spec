Summary:	GObject wrapper for libusb1 library
Name:		libgusb
Version:	0.1.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	9cf5d2ef121f857c565189f82e9e7233
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop. This makes it easy to
integrate low level USB transfers with your high-level application or
system daemon.

%package devel
Summary:	Header files for GUsb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GUsb library.

%package apidocs
Summary:	GUsb API documentation
Group:		Documentation

%description apidocs
API and internal documentation for GUsb library.

%prep
%setup -q

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
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libgusb.so.?
%attr(755,root,root) %{_libdir}/libgusb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgusb.so
%{_libdir}/libgusb.la
%{_includedir}/gusb-1
%{_pkgconfigdir}/gusb.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gusb

