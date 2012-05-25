Summary:	Little CMS - a library to transform between colour profiles
Name:		lcms2
Version:	2.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lcms/%{name}-%{version}.tar.gz
# Source0-md5:	327348d67c979c88c2dec59a23a17d85
URL:		http://www.littlecms.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Little CMS intends to be a small-footprint color management engine,
with special focus on accuracy and performance. It uses the
International Color Consortium standard (ICC), which is the modern
standard when regarding to color management.

Little CMS 2.x supports ICC profile specification v4.2 plus all
addendums.

%package devel
Summary:	Little CMS - header files and developer's documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed to compile programs with liblcms and some
documentation useful for programmers.

%package progs
Summary:	Example and demonstration programs for Little CMS
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Example and demonstration programs for Little CMS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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
%doc ChangeLog AUTHORS COPYING NEWS README.1ST
%attr(755,root,root) %ghost %{_libdir}/liblcms2.so.?
%attr(755,root,root) %{_libdir}/liblcms2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.pdf
%attr(755,root,root) %{_libdir}/liblcms2.so
%{_libdir}/liblcms2.la
%{_includedir}/lcms2*.h
%{_pkgconfigdir}/lcms2.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jpgicc
%attr(755,root,root) %{_bindir}/linkicc
%attr(755,root,root) %{_bindir}/psicc
%attr(755,root,root) %{_bindir}/tificc
%attr(755,root,root) %{_bindir}/transicc
%{_mandir}/man1/jpgicc.1*
%{_mandir}/man1/tificc.1*

