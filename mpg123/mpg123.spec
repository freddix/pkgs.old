Summary:	MPEG 3 audio player
Name:		mpg123
Version:	1.13.8
Release:	1
License:	LGPL, GPL (mpglib)
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/mpg123/%{name}-%{version}.tar.bz2
# Source0-md5:	e82b09c5533c414d670339a717faebab
URL:		http://www.mpg123.de/
Patch1:		%{name}-am.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mpg123 is a fast, free (for non-commercial use) and portable MPEG
audio player for Unix. It supports MPEG 1.0/2.0 layers 1, 2 and 3
(those famous "MP3" files). For full CD quality playback (44 kHz, 16
bit, stereo) a Pentium, SPARCstation10, DEC Alpha or similar CPU is
required. Mono and/or reduced quality playback (22 kHz or 11 kHz) is
even possible on i486 CPUs.

%package libs
Summary:	An optimized MPEG Audio decoder library
Group:		Libraries

%description libs
An optimized MPEG Audio decoder library.

%package libs-devel
Summary:	Header file for mpg123 library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header file for mpg123 library.

%prep
%setup -q
%patch1 -p1

rm -rf libltdl

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ltdl-install=no	\
	--with-audio=alsa,pulse		\
	--with-cpu=x86			\
	--with-default-audio=alsa	\
	--with-module-suffix=.so	\
	--with-optimization=0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{_libdir}/mpg123/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/BENCHMARKING doc/BUGS ChangeLog README doc/README.remote doc/TODO doc/README.3DNOW
%dir %{_libdir}/mpg123
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/mpg123/output_alsa.*
%attr(755,root,root) %{_libdir}/mpg123/output_dummy.*
%attr(755,root,root) %{_libdir}/mpg123/output_pulse.*
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%doc NEWS.libmpg123
%attr(755,root,root) %{_libdir}/libmpg123.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpg123.so.0

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpg123.so
%{_libdir}/libmpg123.la
%{_includedir}/mpg123.h
%{_pkgconfigdir}/libmpg123.pc

