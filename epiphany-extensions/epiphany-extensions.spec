%define		basever	3.4

Summary:	Collection of extensions for Epiphany
Name:		epiphany-extensions
Version:	3.4.0
Release:	4
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany-extensions/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	84eb15907ceb410030b00aacb6e5ff35
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	epiphany-devel >= 3.4.0
BuildRequires:	gtk3-webkit-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	opensp-devel
BuildRequires:	pcre-devel
BuildRequires:	pkg-config
Requires(post,postun):	rarian
Requires(post,postun):	glib-gio-gsettings
Requires:	epiphany
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%prep
%setup -qn %{name}-%{version}

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper		\
	--with-extensions=default
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/*/extensions/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_gsettings_cache

%postun
%scrollkeeper_update_postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/epiphany
%dir %{_libdir}/epiphany/3.*
%dir %{_libdir}/epiphany/3.*/extensions
%attr(755,root,root) %{_libdir}/epiphany/3.*/extensions/*.so
%{_libdir}/epiphany/3.*/extensions/*.ephy-extension
%{_datadir}/epiphany/icons
%{_datadir}/epiphany-extensions
%{_datadir}/glib-2.0/schemas/org.gnome.epiphanyextensions.gschema.xml

