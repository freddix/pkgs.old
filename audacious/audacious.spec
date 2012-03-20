Summary:	Media player based on BMP
Name:		audacious
Version:	2.5.4
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.gz
# Source0-md5:	e4329571a1887fadfe4aac6f2b302871
URL:		http://audacious-media-player.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	libmowgli-devel >= 0.9
BuildRequires:	libsamplerate-devel
BuildRequires:	libmcs-devel
BuildRequires:	pkgconfig
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	audacious-plugins
Requires:	mcs-backend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audacious is a media player based on BMP. Since the development of the
former project had been terminated, this fork was created.

%package libs
Summary:	Audacious media player library
Group:		X11/Applications/Sound

%description libs
Audacious media player library.

%package devel
Summary:	Header files for Audacious media player
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files required for compiling Audacious media player plugins.

%prep
%setup -qn %{name}-%{version}

sed -i -e 's|pt_PT|pt|' po/Makefile
mv po/{pt_PT,pt}.po

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/audacious/{Container,Effect,General,Input,Output,Transport,Visualization}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/%{name}.png \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/audacious.png
install pixmaps/%{name}.svg \
	$RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/audacious.svg

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audacious
%attr(755,root,root) %{_bindir}/audtool

%dir %{_datadir}/audacious
%dir %{_datadir}/audacious/images
%dir %{_libdir}/audacious/Container
%dir %{_libdir}/audacious/Effect
%dir %{_libdir}/audacious/General
%dir %{_libdir}/audacious/Input
%dir %{_libdir}/audacious/Output
%dir %{_libdir}/audacious/Transport
%dir %{_libdir}/audacious/Visualization

%{_datadir}/audacious/images/*

%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*

%{_mandir}/man*/*

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/audacious
%attr(755,root,root) %ghost %{_libdir}/libaudclient.so.?
%attr(755,root,root) %ghost %{_libdir}/libaudcore.so.?
%attr(755,root,root) %ghost %{_libdir}/libaudgui.so.?
%attr(755,root,root) %ghost %{_libdir}/libaudtag.so.?
%attr(755,root,root) %{_libdir}/libaudclient.so.*.*.*
%attr(755,root,root) %{_libdir}/libaudcore.so.*.*.*
%attr(755,root,root) %{_libdir}/libaudtag.so.*.*.*
%attr(755,root,root) %{_libdir}/libaudgui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaudclient.so
%attr(755,root,root) %{_libdir}/libaudcore.so
%attr(755,root,root) %{_libdir}/libaudgui.so
%attr(755,root,root) %{_libdir}/libaudtag.so
%{_includedir}/audacious
%{_includedir}/libaudcore
%{_includedir}/libaudgui
%{_pkgconfigdir}/audacious.pc
%{_pkgconfigdir}/audclient.pc

