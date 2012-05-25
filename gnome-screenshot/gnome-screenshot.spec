Summary:	Screenshot utility
Name:		gnome-screenshot
Version:	3.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-screenshot/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	765d74d798f9c23ffd8bae379449d3a9
URL:		http://live.gnome.org/GnomeUtils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows to make a desktop screenshot.

%prep
%setup -q

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-screenshot
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-screenshot
%{_desktopdir}/gnome-screenshot.desktop
%{_mandir}/man1/gnome-screenshot.1*

