%define		gitver	4a27dd287cdb85d80ceaf6b54e7de0c17e01c00d

%bcond_without	sna	# enable SNA acceleration architecture

Summary:	X.org video driver for Intel integrated graphics chipsets
Name:		xorg-driver-video-intel
Version:	2.17.0
%if "%{gitver}" != "%{nil}"
Release:	1.%{gitver}.1
%else
Release:	1
%endif
License:	MIT
Group:		X11/Applications
%if "%{gitver}" != "%{nil}"
Source0:	http://cgit.freedesktop.org/xorg/driver/xf86-video-intel/snapshot/xf86-video-intel-%{gitver}.tar.gz
# Source0-md5:	bb72b84dd421d60028e17f351a547cf5
%else
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-intel-%{version}.tar.bz2
# Source0-md5:	bb72b84dd421d60028e17f351a547cf5
%endif
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pixman-devel
BuildRequires:	pkg-config
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-libXvMC-devel
BuildRequires:	xorg-proto
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xserver-server-devel
Provides:	xorg-driver-video
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Intel integrated graphics chipsets.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn xf86-video-intel-%{gitver}
%else
%setup -qn xf86-video-intel-%{version}
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_sna:--enable-sna}	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,so}
rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%{_mandir}/man4/intel.4*

