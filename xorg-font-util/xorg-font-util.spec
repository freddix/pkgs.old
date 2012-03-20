Summary:	Font utilities
Name:		xorg-font-util
Version:	1.3.0
Release:	2
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
# Source0-md5:	ddfc8a89d597651408369d940d03d06b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font utilities.

%prep
%setup -qn font-util-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--with-mapdir=%{_fontsdir}/util
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/bdftruncate
%attr(755,root,root) %{_bindir}/ucs2any
%{_fontsdir}/util
%{_mandir}/man1/bdftruncate.1x*
%{_mandir}/man1/ucs2any.1x*
%{_aclocaldir}/fontutil.m4
%{_pkgconfigdir}/fontutil.pc

