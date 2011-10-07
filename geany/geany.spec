Summary:	Fast and lightweight IDE using GTK+
Name:		geany
Version:	0.21
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://download.geany.org/%{name}-%{version}.tar.bz2
# Source0-md5:	117d78ae5275c8c517686b6db9d71ef1
URL:		http://www.geany.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	vte-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	vte
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages. Another goal was to be as
independent as possible from a special Desktop Environment like KDE or
GNOME.

%package devel
Summary:	Geany Development files
Group:		Development/Libraries
Requires:	gtk+-devel

%description devel
Geany Development files.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/geany/*.la
rm -f $RPM_BUILD_ROOT%{_docdir}/geany/{AUTHORS,COPYING,ChangeLog,NEWS,README,THANKS,TODO,ScintillaLicense.txt}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{lb,pt_PT}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO scintilla/License.txt
%dir %{_docdir}/geany
%dir %{_libdir}/geany

%attr(755,root,root) %{_bindir}/geany
%attr(755,root,root) %{_libdir}/geany/*.so

%{_datadir}/%{name}
%{_desktopdir}/geany.desktop
%{_iconsdir}/hicolor/*/apps/*

%{_docdir}/geany/html
%{_docdir}/geany/manual.txt
%{_mandir}/man1/geany.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/geany
%{_pkgconfigdir}/*.pc

