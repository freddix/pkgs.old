Summary:	C library for reading and writing files containing sampled sound
Name:		libsndfile
Version:	1.0.25
Release:	3
License:	LGPL v2.1+
Group:		Development/Libraries
Source0:	http://www.mega-nerd.com/libsndfile/files/%{name}-%{version}.tar.gz
# Source0-md5:	e2b7bb637e01022c7d20f95f9c3990a2
URL:		http://www.mega-nerd.com/libsndfile/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%package devel
Summary:	libsndfile header files and development documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-lib-devel
Requires:	flac-devel
Requires:	libogg-devel
Requires:	libvorbis-devel

%description devel
Header files and development documentation for libsndfile.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I M4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libsndfile1-dev
rm -rf $RPM_BUILD_ROOT%{_datadir}/octave/site/m

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sndfile-*
%attr(755,root,root) %ghost %{_libdir}/libsndfile.so.?
%attr(755,root,root) %{_libdir}/libsndfile.so.*.*.*
%{_mandir}/man1/sndfile-*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/new_file_type.HOWTO
%attr(755,root,root) %{_libdir}/libsndfile.so
%{_libdir}/libsndfile.la
%{_includedir}/sndfile.h*
%{_pkgconfigdir}/sndfile.pc

