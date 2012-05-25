Summary:	Default GTK+ theme engines
Name:		gtk-engines
Version:	2.20.2
Release:	1
Epoch:		1
License:	GPL
Group:		Themes/GTK+
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-engines/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	5deb287bc6075dc21812130604c7dc4f
URL:		http://gtk.themes.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the graphical engines for the various GTK+ toolkit themes.

%package devel
Summary:        gtk-engines development files
Group:          Development

%description devel
This is the package containing gtk-engines development files.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-crux		\
	--disable-glide		\
	--disable-hc		\
	--disable-industrial	\
	--disable-mist		\
	--disable-redmond	\
	--disable-silent-rules	\
	--disable-thinice	\
	--enable-lua		\
	--enable-paranoia	\
	--with-system-lua
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# .la are not needed (according to spec included to package)
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/Redmond/gtk
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gdk-pixbuf-query-loaders >%{_sysconfdir}/gtk-2.0/gdk-pixbuf.loaders
exit 0

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/Clearlooks
%{_datadir}/gtk-engines/*.xml

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*

