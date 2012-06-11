Summary:	Implementation of the MPEG-4 Systems standard (ISO/IEC 14496-1)
Name:		gpac
Version:	0.5.0
Release:	1
License:	LGPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/gpac/%{name}-%{version}.tar.gz
# Source0-md5:	19f7bb7c16913c22bdd453db1e653ca0
Patch0:		%{name}-install.patch
URL:		http://gpac.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	openjpeg-devel
BuildRequires:	xvidcore-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq   libm4systems.so

%description
GPAC is an implementation of the MPEG-4 Systems standard (ISO/IEC
14496-1) developed from scratch in ANSI C.

%package libs
Summary:	GPAC library
Group:		Libraries

%description libs
GPAC library.

%package devel
Summary:	Header files for gpac library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for gpac
library.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%configure \
	--extra-cflags="%{rpmcflags} -fPIC"	\
	--extra-ldflags="%{rpmldflags} -fPIC"	\
	--use-js=no
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-lib install \
	DESTDIR=$RPM_BUILD_ROOT

%{__ldconfig} -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS Changelog README TODO
%dir %{_libdir}/gpac
%attr(755,root,root) %{_bindir}/MP4Box
%attr(755,root,root) %{_bindir}/MP4Client
%attr(755,root,root) %{_libdir}/gpac/*.so
%{_datadir}/%{name}
%{_mandir}/man1/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgpac.so.2
%attr(755,root,root) %{_libdir}/libgpac.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gpac
%attr(755,root,root) %{_libdir}/libgpac.so

