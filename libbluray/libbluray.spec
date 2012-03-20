Summary:	Library to access Blu-Ray disks for video playback
Name:		libbluray
Version:	0.2.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.videolan.org/pub/videolan/libbluray/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d4cfcf3f110e9d2afe01d29feb8c842b
URL:		http://www.videolan.org/developers/libbluray.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is aiming to provide a full portable free open source
bluray library, which can be plugged into popular media players to
allow full bluray navigation and playback on Linux. It will eventually
be compatible with all current titles, and will be easily portable and
embeddable in standard players such as mplayer and vlc.

%package devel
Summary:	Header files for libbluray library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libbluray library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
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
%doc README.txt
%attr(755,root,root) %ghost %{_libdir}/libbluray.so.?
%attr(755,root,root) %{_libdir}/libbluray.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbluray.so
%{_libdir}/libbluray.la
%{_includedir}/libbluray
%{_pkgconfigdir}/libbluray.pc

