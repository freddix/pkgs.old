Summary:	Integrated LaTeX Environment for the GNOME Desktop
Name:		latexila
Version:	2.5.0
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/latexila/2.5/%{name}-%{version}.tar.xz
# Source0-md5:	2e92fdee0278eaed556aafd98522dae0
BuildRequires:	cmake
BuildRequires:	gtksourceview3-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	itstool
BuildRequires:	libgee-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	gtk+-update-icon-cache
Requires:	latexmk
Requires:	tetex-format-pdflatex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q

%build
rm -f src/C/*.c

install -d build
cd build
%cmake .. \
	-DBUILD_VALA=1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_desktop_database_post
%update_icon_cache hicolor
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/latexila
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.latexila.gschema.xml
%{_desktopdir}/latexila.desktop
%{_iconsdir}/hicolor/*/apps/latexila.png
%{_mandir}/man1/latexila.1*

