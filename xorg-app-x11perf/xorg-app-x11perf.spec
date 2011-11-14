Summary:	Simple X server performance benchmarker
Name:		xorg-app-x11perf
Version:	1.5.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/x11perf-%{version}.tar.bz2
# Source0-md5:	5c3c7431a38775caaea6051312a49bc9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXft-devel
# just xmuu
BuildRequires:	xorg-libXmu-devel
BuildRequires:	xorg-libXrender-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple X server performance benchmarker.

%prep
%setup -qn x11perf-%{version}

%build
%{__aclocal}
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%dir %{_libdir}/X11/x11perfcomp
%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*
%{_mandir}/man1/Xmark.1x*
%{_mandir}/man1/x11perf.1x*
%{_mandir}/man1/x11perfcomp.1x*

