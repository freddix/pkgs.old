Summary:	GIF-manipulation library
Name:		giflib
Version:	4.1.6
Release:	4
License:	X Consortium-like
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/giflib/%{name}-%{version}.tar.bz2
# Source0-md5:	7125644155ae6ad33dbc9fc15a14735f
Patch0:		%{name}-link.patch
Patch1:		%{name}-segfault.patch
URL:		http://sourceforge.net/projects/giflib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIF loading and saving shared library. This version uses LZW
compression (warning: patent/license issues in some countries).

%package devel
Summary:	GIF-manipulation library header files and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries and headers needed for developing programs that use libgif
to load and save GIF image files.

%package progs
Summary:	Programs for converting and transforming GIF images
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
This package contains various programs for manipulating GIF image
files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libgif.so.?
%attr(755,root,root) %{_libdir}/libgif.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.{txt,png} doc/{gif_lib,index,liberror}.html
%attr(755,root,root) %{_libdir}/libgif.so
%{_libdir}/libgif.la
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%doc doc/gif2* doc/gif[a-z]* doc/*2gif*
%attr(755,root,root) %{_bindir}/*

