Summary:	Generic spell checking library
Name:		enchant
Version:	1.6.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.abisource.com/downloads/enchant/1.6.0/%{name}-%{version}.tar.gz
# Source0-md5:	de11011aff801dc61042828041fb59c7
URL:		http://www.abisource.com/enchant/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	hunspell-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide an efficient, extensible abstraction for
dealing with different spell checking libraries. Enchant is meant to
provide a generic interface into various existing spell checking
libraries. These include, but are not limited to: Aspell/Pspell,
Ispell, Hspell, Uspell.

%package devel
Summary:	Header files for enchant library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for enchant library.

%package hunspell
Summary:	myspell provider module for Enchant
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	hunspell

%description hunspell
myspell provider module for Enchant.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-aspell	\
	--disable-ispell	\
	--disable-static	\
	--with-myspell-dir="%{_datadir}/myspell"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless - modules loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/enchant/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/enchant
%attr(755,root,root) %{_bindir}/enchant-lsmod
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/enchant
%{_datadir}/enchant
%{_mandir}/man1/enchant.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/enchant
%{_pkgconfigdir}/*.pc

%files hunspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant/libenchant_myspell.so*

