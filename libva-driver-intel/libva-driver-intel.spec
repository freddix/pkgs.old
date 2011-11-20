%define		gitver	%{nil}

Summary:	VA driver for Intel GPUs
Name:		libva-driver-intel
Version:	1.0.15
%if "%{gitver}" != "%{nil}"
Release:        0.%{gitver}.1
Source0:        http://cgit.freedesktop.org/intel-driver/snapshot/intel-driver-%{gitver}.tar.bz2
# Source0-md5:	b38518cae4ebd3cf30f4e3f8a57c1600
%else
Release:        2
Source0:	http://cgit.freedesktop.org/intel-driver/snapshot/intel-driver-%{version}.tar.bz2
# Source0-md5:	b38518cae4ebd3cf30f4e3f8a57c1600
%endif
License:	BSD
Group:		Libraries
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	pkg-config
Requires:	Mesa-dri-driver-intel-i965
Requires:	xorg-driver-video-intel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VA driver for Intel GPUs.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn intel-driver-%{gitver}
%else
%setup -qn intel-driver-%{version}
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libva/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/libva/dri/i965_drv_video.so

