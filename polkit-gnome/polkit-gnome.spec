Summary:	GNOME dialogs for polkit
Name:		polkit-gnome
Version:	0.105
Release:	1
License:	LGPL v2+ (polkit-gnome library), GPL v2+ (D-Bus service)
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/polkit-gnome/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	50ecad37c8342fb4a52f590db7530621
URL:		http://people.freedesktop.org/~david/polkit-spec.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	polkit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/polkit

%description
polkit-gnome provides a D-BUS session bus service that is used to
bring up authentication dialogs used for obtaining privileges.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-examples	\
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f polkit-gnome-1.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS TODO
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/polkit-gnome-authentication-agent-1

