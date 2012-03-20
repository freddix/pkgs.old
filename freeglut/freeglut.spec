Summary:	A freely licensed alternative to the GLUT library
Name:		freeglut
Version:	2.6.0
Release:	3
License:	MIT
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/freeglut/%{name}-%{version}.tar.gz
# Source0-md5:	39f0f2de89f399529d2b981188082218
URL:		http://freeglut.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXxf86vm-devel
Provides:	OpenGL-glut = 3.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freeglut, the Free OpenGL Utility Toolkit, is meant to be a free
alternative to Mark Kilgard's GLUT library. It is distributed under an
X-Consortium style license (see COPYING for details), to offer you a
chance to use and/or modify the source.

It makes use of OpenGL, GLU, and pthread libraries. The library does
not make use of any GLUT code and is not 100% compatible. Code
recompilation and/or slight modifications might be required for your
applications to work with freeglut.

%package devel
Summary:	Header files for freeglut library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-libXext-devel
Requires:	xorg-libXxf86vm-devel
Provides:	OpenGL-glut-devel = 3.7

%description devel
Header files for freeglut library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
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
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/{freeglut.html,index.html,progress.html,*.png}
%lang(fr) %doc LISEZ_MOI
%attr(755,root,root) %ghost %{_libdir}/libglut.so.?
%attr(755,root,root) %{_libdir}/libglut.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{freeglut_user_interface.html,structure.html}
%attr(755,root,root) %{_libdir}/libglut.so
%{_libdir}/libglut.la
%{_includedir}/GL/freeglut*.h
%{_includedir}/GL/glut.h

