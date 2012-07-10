%include	/usr/lib/rpm/macros.mono
%include	/usr/lib/rpm/macros.perl

Summary:	Mono language bindings for GNOME
Name:		mono-gnome-desktop-sharp
Version:	2.26.0
Release:	17
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-desktop-sharp/2.26/gnome-desktop-sharp-%{version}.tar.bz2
# Source0-md5:	4bc990900bb318b2ba0b0e7998bb47d1
Patch0:		%{name}-ungnome.patch
URL:		http://www.mono-project.com/GtkSharp
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	librsvg-devel
BuildRequires:	libwnck2-devel
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp
BuildRequires:	monodoc
BuildRequires:	pkg-config
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	vte2-devel
# not detected
Requires:	gnome-desktop2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for Mono to GNOME libraries.

%package devel
Summary:	Development part of GNOME#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mono-rsvg2-sharp = %{version}-%{release}
Requires:	mono-vte-sharp = %{version}-%{release}
Requires:	mono-wnck-sharp = %{version}-%{release}
Requires:	gnome-desktop2-devel
Requires:	librsvg-devel
Requires:	libwnck-devel
Requires:	monodoc
Requires:	vte-devel
Requires:	which

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GNOME#.

%package -n mono-rsvg2-sharp
Summary:	Mono bindings for rsvg library
Group:		Libraries
Requires:	librsvg

%description -n mono-rsvg2-sharp
Mono bindings for rsvg library

%package -n mono-vte-sharp
Summary:	Mono bindings for vte library
Group:		Libraries
Requires:	vte

%description -n mono-vte-sharp
Mono bindings for vte library.

%package -n mono-wnck-sharp
Summary:	Mono bindings for wnck library
Group:		Libraries
Requires:	libwnck

%description -n mono-wnck-sharp
Mono bindings for wnck library.

%prep
%setup -qn gnome-desktop-sharp-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n mono-vte-sharp -p /sbin/ldconfig
%postun	-n mono-vte-sharp -p /sbin/ldconfig
%post	-n mono-wnck-sharp -p /sbin/ldconfig
%postun	-n mono-wnck-sharp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_gacdir}/gnomedesktop-sharp

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_datadir}/gnomedesktop-sharp
%{_datadir}/rsvg2-sharp
%{_datadir}/vte-sharp
%{_datadir}/wnck-sharp
%{_monodir}/gnomedesktop-sharp-2.20
%{_monodir}/rsvg2-sharp-2.0
%{_monodir}/vte-sharp-0.16
%{_monodir}/wnck-sharp-2.20
%{_pkgconfigdir}/gnome-desktop-sharp-2.0.pc
%{_pkgconfigdir}/rsvg2-sharp-2.0.pc
%{_pkgconfigdir}/vte-sharp-0.16.pc
%{_pkgconfigdir}/wnck-sharp-1.0.pc

%files -n mono-rsvg2-sharp
%defattr(644,root,root,755)
%{_gacdir}/rsvg2-sharp

%files -n mono-vte-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtesharpglue-2.so
%{_gacdir}/vte-sharp

%files -n mono-wnck-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwncksharpglue-2.so
%{_gacdir}/wnck-sharp

