Summary:	mkfontdir application
Name:		xorg-app-mkfontdir
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkfontdir-%{version}.tar.bz2
# Source0-md5:	18c429148c96c2079edda922a2b67632
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-util-macros
Requires:	xorg-app-mkfontscale
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkfontdir application.

%prep
%setup -qn mkfontdir-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
%attr(755,root,root) %{_bindir}/mkfontdir
%{_mandir}/man1/mkfontdir.1x*

