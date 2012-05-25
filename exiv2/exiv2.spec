Summary:	Exif and Iptc metadata manipulation tools
Name:		exiv2
Version:	0.21.1
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://www.exiv2.org/%{name}-%{version}.tar.gz
# Source0-md5:	5c99bbcaa998f6b200b92f2bf0ac4f9e
Source1:	ax_cxx_check_flag.m4
Patch0:		%{name}-mkinstalldirs.patch
URL:		http://www.exiv2.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exif and Iptc metadata manipulation tools.

%package libs
Summary:	Exif and Iptc metadata manipulation library
Group:		Libraries

%description libs
Exif and Iptc metadata manipulation library.

%package devel
Summary:	Exif and Iptc metadata manipulation library development files
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Exif and Iptc metadata manipulation library development files.

%prep
%setup -q
%patch0 -p0

install %{SOURCE1} config
ln -s config/configure.ac .

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
# don't touch autoheader, config.h.in has been manually modified
%configure \
	--disable-static
%{__make} \
	CFLAGS="%{rpmcflags} -Wall"	\
	CXXFLAGS="%{rpmcxxflags} -Wall"	\
	DESTDIR=$RPM_BUILD_ROOT		\
	bindir=%{_bindir}		\
	incdir=%{_includedir}/exiv2	\
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	CFLAGS="%{rpmcflags} -Wall"	\
	CXXFLAGS="%{rpmcxxflags} -Wall"	\
	DESTDIR=$RPM_BUILD_ROOT		\
	bindir=%{_bindir}		\
	incdir=%{_includedir}/exiv2	\
	libdir=%{_libdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/exiv2.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libexiv2.so.??
%attr(755,root,root) %{_libdir}/libexiv2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexiv2.so
%{_libdir}/libexiv2.la
%{_includedir}/%{name}
%{_pkgconfigdir}/exiv2.pc

