Summary:	Notification Daemon
Name:		notification-daemon
Version:	0.7.4
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/notification-daemon/0.7/%{name}-%{version}.tar.xz
# Source0-md5:	5efbb577cf92cb7ee3972d567c21f7b3
URL:		http://www.galago-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkg-config
Requires:	dbus
Obsoletes:	xdg-desktop-notification-daemon
Provides:	xdg-desktop-notification-daemon
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
A daemon that displays passive pop-up notifications as per the Desktop
Notifications spec.

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
%{__intltoolize}
%{__aclocal} -I macros
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/notification-daemon
%{_desktopdir}/notification-daemon.desktop

