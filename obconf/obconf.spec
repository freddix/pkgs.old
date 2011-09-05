%define		git_ver	cc7a18807663313ef111d86a75844ded0416a889

Summary:	Tool for configuring the Openbox window manager
Name:		obconf
Version:	2.0.4
Release:	0.%{git_ver}.1
License:	GPL v2
Group:		X11/Applications
#Source0:	http://icculus.org/openbox/obconf/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{git_ver}.tar.xz
# Source0-md5:	b22e273721851dedad72acbc77eefb68
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-revert_9cffa6a9ddfc4074f3de8d0302404d70c2818d8f.patch
URL:		http://openbox.org/obconf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	openbox-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ObConf allows you to configure Openbox in real-time. You can change
options such as the theme, desktop names, and focus settings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -R

sed -i -e 's|no|nb|' po/LINGUAS
mv -f po/{no,nb}.po
rm -f po/stamp-po

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_mime_database

%postun
%update_desktop_database_postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/obconf.glade
%{_datadir}/%{name}/*.png
%{_datadir}/mime/packages/obconf.xml
%{_desktopdir}/obconf.desktop
%{_pixmapsdir}/obconf.png

