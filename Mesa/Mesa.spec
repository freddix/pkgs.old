%define		gitver	%{nil}

Summary:	Free OpenGL implementation
Name:		Mesa
Version:	7.11.1
%if "%{gitver}" != "%{nil}"
Release:	6.%{gitver}.1
Source:		http://cgit.freedesktop.org/mesa/mesa/snapshot/mesa-%{gitver}.tar.bz2
%else
Release:	1
Source0:	ftp://ftp.freedesktop.org/pub/mesa/%{version}/MesaLib-%{version}.tar.gz
# Source0-md5:	ac0181a4076770fb657c1169af43aa09
%endif
License:	MIT (core), SGI (GLU) and others - see COPYRIGHT file
Group:		X11/Libraries
Patch0:		%{name}-hush-vblank-warning.patch
URL:		http://www.mesa3d.org/
BuildRequires:	expat-devel
BuildRequires:	libdrm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
BuildRequires:	talloc-devel
BuildRequires:	xorg-libXdamage-devel
BuildRequires:	xorg-libXt-devel
BuildRequires:	xorg-libXxf86vm-devel
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-makedepend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dridir		%{_libdir}/xorg/modules/dri

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL(R). To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc. However, the author does not possess an OpenGL
license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI.

%package libGL
Summary:	Free Mesa3D implementation of libGL OpenGL library
License:	MIT
Group:		X11/Libraries
Provides:	OpenGL = 2.1
# reports version 1.3, but supports glXGetProcAddress() from 1.4
Provides:	OpenGL-GLX = 1.4

%description libGL
This package contains libGL which implements OpenGL 1.5 and GLX 1.4
specifications. It uses DRI for rendering.

%package libGL-devel
Summary:	Header files for Mesa3D libGL library
License:	MIT
Group:		X11/Development/Libraries
# loose dependency on libGL to use with other libGL binaries
Requires:	OpenGL >= 1.5
Requires:	xorg-libX11-devel
Provides:	OpenGL-devel = 2.1
Provides:	OpenGL-GLX-devel = 1.4

%description libGL-devel
Header files for Mesa3D libGL library.

%package libGLU
Summary:	SGI implementation of libGLU OpenGL library
License:	SGI Free Software License B v1.1
Group:		Libraries
# loose dependency on libGL.so.1 to use with other libGL binaries
Requires:	OpenGL >= 1.2
Provides:	OpenGL-GLU = 1.3

%description libGLU
SGI implementation of libGLU OpenGL library. It implements OpenGL GLU
1.3 specifications.

%package libGLU-devel
Summary:	Header files for SGI libGLU library
License:	SGI Free Software License B v1.1
Group:		Development/Libraries
Requires:	%{name}-libGLU = %{version}-%{release}
Requires:	OpenGL-devel >= 1.2
Requires:	libstdc++-devel
Provides:	OpenGL-GLU-devel = 1.3

%description libGLU-devel
Header files for SGI libGLU library.

%package dri-driver-ati-radeon-R200
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server

%description dri-driver-ati-radeon-R200
X.org DRI drivers for ATI R200 card family (Radeon 8500-92xx)

%package dri-driver-ati-radeon-R300
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server

%description dri-driver-ati-radeon-R300
X.org DRI drivers for ATI R300 card family.

%package dri-driver-ati-radeon-R600
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	firmware-radeon
Requires:	xorg-driver-video-ati
Requires:	xorg-xserver-server

%description dri-driver-ati-radeon-R600
X.org DRI drivers for ATI R600 card family.

%package dri-driver-intel-i915
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-server

%description dri-driver-intel-i915
X.org DRI drivers for Intel i915 card family.

%package dri-driver-intel-i965
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-driver-video-intel
Requires:	xorg-xserver-server

%description dri-driver-intel-i965
X.org DRI drivers for Intel i965 card family.

%package dri-driver-swrast
Summary:	X.org DRI drivers
Group:		X11/Libraries
Requires:	xorg-xserver-server

%description dri-driver-swrast
X.org DRI software rasterizer driver.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn mesa-%{gitver}
%else
%setup -q
%endif

%patch0 -p1

# remove header - not free software
rm -f include/GL/uglglutshapes.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-asm			\
	--disable-egl			\
	--disable-gl-osmesa		\
	--disable-glut			\
	--disable-glw			\
	--enable-gallium-llvm		\
	--enable-glx-tls		\
	--enable-texture-float		\
	--with-dri-driverdir=%{dridir}	\
	--with-dri-drivers="i915,i965,r200,swrast"	\
	--with-driver=dri		\
	--with-gallium-drivers="r300,r600,swrast"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_includedir}/GL/{[a-fh-np-wyz],gg,glf,glut}*.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	libGL -p /sbin/ldconfig
%postun	libGL -p /sbin/ldconfig

%post	libGLU -p /sbin/ldconfig
%postun	libGLU -p /sbin/ldconfig

%files libGL
%defattr(644,root,root,755)
%doc docs/{*.html,README.{3DFX,GGI,MITS,QUAKE,THREADS},RELNOTES*}
%attr(755,root,root) %ghost %{_libdir}/libGL.so.1
%attr(755,root,root) %{_libdir}/libGL.so.*.*
# symlink for binary apps which fail to conform Linux OpenGL ABI
# (and dlopen libGL.so instead of libGL.so.1)
%attr(755,root,root) %{_libdir}/libGL.so

%files libGL-devel
%defattr(644,root,root,755)
%doc docs/*.spec
%dir %{_includedir}/GL
%dir %{_includedir}/GL/internal
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/internal/dri_interface.h
%{_pkgconfigdir}/dri.pc
%{_pkgconfigdir}/gl.pc

%files libGLU
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libGLU.so.1
%attr(755,root,root) %{_libdir}/libGLU.so.*.*

%files libGLU-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_pkgconfigdir}/glu.pc

%files dri-driver-ati-radeon-R200
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/r200_dri.so

%files dri-driver-ati-radeon-R300
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/r300_dri.so

%files dri-driver-ati-radeon-R600
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/r600_dri.so

%files dri-driver-intel-i915
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/i915_dri.so

%files dri-driver-intel-i965
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/i965_dri.so

%files dri-driver-swrast
%defattr(644,root,root,755)
%attr(755,root,root) %{dridir}/swrast_dri.so
%attr(755,root,root) %{dridir}/swrastg_dri.so

