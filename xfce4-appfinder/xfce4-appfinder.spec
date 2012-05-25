%define		xfce_version	4.10.0

Summary:	Application finder for Xfce
Name:		xfce4-appfinder
Version:	4.10.0
Release:	1
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce4-appfinder/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	799f70a9ad67b450da67810a5107e623
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	garcon-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
Requires:	garcon
Requires:	xfconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application finder for the Xfce Desktop Environment.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir="%{_datadir}/xfce4/help/%{name}"

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop

