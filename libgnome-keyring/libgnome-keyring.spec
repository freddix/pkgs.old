Summary:	Keep passwords and other user's secrets
Name:		libgnome-keyring
Version:	3.2.2
Release:	1
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnome-keyring/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	51b822605b45c8ea0f6df68fdc3ee611
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The library libgnome-keyring is used by applications to integrate with
the GNOME keyring system.

%package devel
Summary:	Headers for GNOME keyring library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers for GNOME keyring library.

%package apidocs
Summary:	GNOME keyring API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GNOME keyring API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgnome-keyring.so.?
%attr(755,root,root) %{_libdir}/libgnome-keyring.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-keyring.so
%{_includedir}/gnome-keyring-1
%{_pkgconfigdir}/gnome-keyring-1.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-keyring
