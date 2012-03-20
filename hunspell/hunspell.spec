Summary:	Hunspell - a spell checker and morphological analyzer library
Name:		hunspell
Version:	1.3.2
Release:	3
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
# Source0-md5:	3121aaf3e13e5d88dfff13fb4a5f1ab8
URL:		http://hunspell.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
OpenOffice.org UNO module.

%package libs
Summary:	hunspell library
Group:		Libraries

%description libs
hunspell library.

%package devel
Summary:	Files for developing with hunspell
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Includes and definitions for developing with hunspell.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--disable-static	\
	--with-readline		\
	--with-ui
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/myspell

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_bindir}/example

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.myspell AUTHORS AUTHORS.myspell COPYING THANKS license.hunspell license.myspell
%dir %{_datadir}/myspell
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_mandir}/man4/*.4*
%lang(hu) %{_mandir}/hu/man1/*.1*
%lang(hu) %{_mandir}/hu/man4/*.4*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libhunspell-*.*.so.?
%attr(755,root,root) %{_libdir}/libhunspell-*.*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhunspell-*.*.so
%{_libdir}/libhunspell-*.*.la
%{_libdir}/libparsers.a
%{_includedir}/%{name}
%{_pkgconfigdir}/hunspell.pc

