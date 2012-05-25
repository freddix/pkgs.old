Summary:	Color profile manager for the GNOME desktop
Name:		gnome-color-manager
Version:	3.4.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/gnome-color-manager/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	dc8e97c93a29a7623f8e248ed784b77f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	colord-devel
BuildRequires:	exiv2-devel
BuildRequires:	intltool
BuildRequires:	lcms2-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libtool
BuildRequires:	udev-glib-devel
BuildRequires:	vte-devel
BuildRequires:	xorg-libXxf86vm-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	colord
Suggests:	argyllcms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Color profile manager for the GNOME desktop.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__gnome_doc_prepare}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gcm-calibrate-helper
%attr(755,root,root) %{_libexecdir}/gcm-helper-exiv

%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/gcm-*.1*

