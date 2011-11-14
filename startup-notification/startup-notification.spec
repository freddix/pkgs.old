Summary:	Startup Notification Library
Name:		startup-notification
Version:	0.12
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://freedesktop.org/software/startup-notification/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2cd77326d4dcaed9a5a23a1232fb38e9
URL:		http://startup-notification.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Startup Notification Library implements a mechanism allowing a
desktop environment to track application startup, to provide user
feedback and other features.

%package devel
Summary:	Startup Notification Library development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Startup Notification Library development files.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %ghost %{_libdir}/*.so.?
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*

