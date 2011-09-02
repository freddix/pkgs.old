Summary:	GTK+ based media player
Name:		xnoise
Version:	0.1.27
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://xnoise.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	13da25d364b9e7c5b16dd204775ca4e1
URL:		http://www.xnoise-media-player.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRequires:	taglib-devel
BuildRequires:	vala-devel >= 0.11.5
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gstreamer-plugins-ugly
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XNOISE is a media player for Gtk+ with a slick GUI, great
speed and lots of features.

%package libs
Summary:	Xnoise libraries
Group:		Libraries

%description libs
Xnoise libraries.

%package devel
Summary:	Development files for xnoise
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the development files for xnoise.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make} \
	libxnoisedir="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT		\
	libxnoisedir="%{_libdir}"	\
	vapidir="%{_datadir}/vala-0.10/vapi"

rm -f $RPM_BUILD_ROOT%{_libdir}/xnoise/*.la

# FIX ME!
# partially wrong locale names
#%find_lang %{name}

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xnoise
%dir %{_libdir}/xnoise
%attr(755,root,root) %{_libdir}/xnoise/lib*.so
%exclude %{_libdir}/xnoise/*test*.so
%{_libdir}/xnoise/*.xnplugin

%{_datadir}/%{name}
%{_desktopdir}/xnoise.desktop
%{_iconsdir}/hicolor/*/apps/xnoise*.*
%{_iconsdir}/hicolor/*/status/xn-*.*
%{_mandir}/man1/xnoise.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xnoise
%{_pkgconfigdir}/*.pc
%{_datadir}/vala-0.10/vapi/*.deps
%{_datadir}/vala-0.10/vapi/*.vapi

