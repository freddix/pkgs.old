Summary:	Fast, easy and lightweight image viewer
Name:		viewnior
Version:	1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://cloud.github.com/downloads/xsisqox/Viewnior/%{name}-%{version}.tar.gz
# Source0-md5:	273c379933ae3e74ad414fde00198695
BuildRequires:	gtk+-devel
BuildRequires:	pkg-config
BuildRequires:	shared-mime-info-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viewnior is an image viewer program. Created to be simple,
fast and elegant. It's minimalistic interface provides more
screenspace for images.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
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
%update_icon_cache hicolor
%update_desktop_database_post

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/viewnior.*
%{_mandir}/man1/viewnior.1*

