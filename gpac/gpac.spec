Summary:	Implementation of the MPEG-4 Systems standard (ISO/IEC 14496-1)
Name:		gpac
Version:	0.4.5
Release:	8
License:	LGPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/gpac/%{name}-%{version}.tar.gz
# Source0-md5:	755e8c438a48ebdb13525dd491f5b0d1
Patch0:		%{name}-install.patch
Patch1:		%{name}-libpng14.patch
URL:		http://gpac.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	freetype-devel
BuildRequires:	js-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	openjpeg-devel
BuildRequires:	xvidcore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq   libm4systems.so

%description
GPAC is an implementation of the MPEG-4 Systems standard (ISO/IEC
14496-1) developed from scratch in ANSI C.

%package devel
Summary:	Header files for gpac library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for gpac
library.

%package utils
Summary:	GPAC utilities
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
GPAC utilities.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p0

%build
chmod a+x configure
%configure \
	--extra-cflags="%{rpmcflags} -fPIC"	\
	--extra-ldflags="%{rpmldflags} -fPIC"

%{__make} -j1 \
	DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-lib \
	bindir=$RPM_BUILD_ROOT%{_bindir}	\
	libdir=$RPM_BUILD_ROOT%{_libdir}	\
	mandir=$RPM_BUILD_ROOT%{_mandir}	\
	plugdir=$RPM_BUILD_ROOT%{_libdir}/gpac	\
	prefix=$RPM_BUILD_ROOT%{_prefix}	\
	real_plugdir=%{_libdir}/gpac

%{__ldconfig} -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS Changelog README TODO
%attr(755,root,root) %{_libdir}/libgpac-%{version}.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/gpac
%attr(755,root,root) %{_libdir}/libgpac.so

%files utils
%defattr(644,root,root,755)
%dir %{_libdir}/gpac
%attr(755,root,root) %{_bindir}/MP4Box
%attr(755,root,root) %{_bindir}/MP4Client
%attr(755,root,root) %{_libdir}/gpac/*.so
%{_datadir}/%{name}
%{_mandir}/man1/*

