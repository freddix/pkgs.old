Summary:	Photo organizer
Name:		shotwell
Version:	0.11.6
Release:	2
License:	LGPL
Group:		X11/Applications
Source0:	http://www.yorba.org/download/shotwell/0.11/%{name}-%{version}.tar.bz2
# Source0-md5:	bbbf2843eb98b6f0ef1dfcfb934e15cf
Patch0:		%{name}-build.patch
URL:		http://www.yorba.org/shotwell/
BuildRequires:	GConf-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	libexif-devel
BuildRequires:	libgee-devel
BuildRequires:	libgexiv2-devel >= 0.3.1
BuildRequires:	libgphoto2-devel
BuildRequires:	libraw-devel
BuildRequires:	libsoup-devel
BuildRequires:	libunique-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRequires:	udev-glib-devel
BuildRequires:	vala >= 0.11.7
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	glib-gio-gsettings
Requires:	glib-networking
Requires:	libgphoto2-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Photo organizer.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{rpmcflags}"
./configure \
	--disable-desktop-update	\
	--disable-icon-update		\
	--prefix=%{_prefix}		\
	--release

%{__make} -j1 \
	CC="%{__cc}"				\
	LDFLAGS="%{rpmcflags} %{rpmldflags}"	\
	OPTFLAGS="%{rpmcflags}"			\
	USER_VALAFLAGS="-X -O2 -X -march=i686 -X -mtune=pentium4 -X -fwrapv -X -fno-strict-aliasing -X -pipe"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_iconsdir}/hicolor/scalable/apps}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome
%find_lang %{name}-extras
cat %{name}-extras.lang >> %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/shotwell
%attr(755,root,root) %{_bindir}/shotwell-video-thumbnailer

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/builtin
%attr(755,root,root) %{_libdir}/%{name}/plugins/builtin/*.so
%{_libdir}/%{name}/plugins/builtin/*.glade
%{_libdir}/%{name}/plugins/builtin/*.png

%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/shotwell.*

%{_datadir}/GConf/gsettings/shotwell.convert
%{_datadir}/glib-2.0/schemas/gschemas.compiled
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell-extras.gschema.xml
%{_datadir}/glib-2.0/schemas/org.yorba.shotwell.gschema.xml

