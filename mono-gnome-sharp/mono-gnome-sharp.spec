%include	/usr/lib/rpm/macros.mono
%include	/usr/lib/rpm/macros.perl

Summary:	Mono language bindings for GNOME
Name:		mono-gnome-sharp
Version:	2.24.2
Release:	11
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-sharp/2.24/gnome-sharp-%{version}.tar.bz2
# Source0-md5:	3b38f53960c736d4afb8f04204efe98b
Patch0:		%{name}-destdir.patch
URL:		http://www.mono-project.com/GtkSharp
BuildRequires:	GConf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp
BuildRequires:	mono-gtk-sharp-devel
BuildRequires:	monodoc
BuildRequires:	ncurses-devel
BuildRequires:	pkg-config
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for Mono to GNOME libraries.

%package -n mono-art-lgpl-sharp
Summary:	art_gpl bindings for GNOME#
Group:		Libraries
Requires:	libart_lgpl

%description -n mono-art-lgpl-sharp
art_gpl bindings for GNOME#.

%package -n mono-gconf-sharp
Summary:	GConf bindings for GNOME#
Group:		Libraries
Requires:	GConf-libs

%description -n mono-gconf-sharp
GConf bindings for GNOME#.

%package -n mono-gnomevfs-sharp
Summary:	GNOME VFS bindings for GNOME#
Group:		Libraries
Requires:	gnome-vfs-libs

%description -n mono-gnomevfs-sharp
GConf bindings for GNOME#.

%package devel
Summary:	Development part of GNOME#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mono-art-lgpl-sharp = %{version}-%{release}
Requires:	mono-gconf-sharp = %{version}-%{release}
Requires:	mono-gnomevfs-sharp = %{version}-%{release}
Requires:	monodoc
Requires:	which

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GNOME#.

%prep
%setup -qn gnome-sharp-%{version}
%patch0 -p1

# no samples
sed -i -e 's| sample||' Makefile.am

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomesharpglue-2.so
%{_gacdir}/gnome-sharp

%{_gacdir}/gconf-sharp-peditors
%{_gacdir}/policy.2.*.gconf-sharp-peditors
%{_monodir}/gtk-sharp-2.0/policy.2.16.gconf-sharp-peditors.dll
%{_monodir}/gtk-sharp-2.0/policy.2.20.gconf-sharp-peditors.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.gconf-sharp-peditors.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.gconf-sharp-peditors.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.gconf-sharp-peditors.dll

%files -n mono-art-lgpl-sharp
%defattr(644,root,root,755)
%{_gacdir}/art-sharp
%{_gacdir}/policy.2.*.art-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.16.art-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.20.art-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.art-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.art-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.art-sharp.dll

%files -n mono-gconf-sharp
%defattr(644,root,root,755)
%{_gacdir}/gconf-sharp
%{_gacdir}/policy.2.*.gconf-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.16.gconf-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.20.gconf-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.gconf-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.gconf-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.gconf-sharp.dll

%files -n mono-gnomevfs-sharp
%defattr(644,root,root,755)
%{_gacdir}/gnome-vfs-sharp
%{_gacdir}/policy.2.*.gnome-vfs-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.16.gnome-vfs-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.20.gnome-vfs-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.gnome-vfs-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.gnome-vfs-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.gnome-vfs-sharp.dll

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gconfsharp2-schemagen
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%{_libdir}/libgnomesharpglue-2.la

%{_monodir}/gtk-sharp-2.0/art-sharp.dll
%{_monodir}/gtk-sharp-2.0/gconf-sharp.dll
%{_monodir}/gtk-sharp-2.0/gconf-sharp-peditors.dll
%{_monodir}/gtk-sharp-2.0/gnome-sharp.dll
%{_monodir}/gtk-sharp-2.0/gnome-vfs-sharp.dll

%{_datadir}/gapi-2.0/art-api.xml
%{_datadir}/gapi-2.0/gnome-api.xml
%{_datadir}/gapi-2.0/gnome-vfs-api.xml

%{_pkgconfigdir}/art-sharp-2.0.pc
%{_pkgconfigdir}/gconf-sharp-2.0.pc
%{_pkgconfigdir}/gconf-sharp-peditors-2.0.pc
%{_pkgconfigdir}/gnome-sharp-2.0.pc
%{_pkgconfigdir}/gnome-vfs-sharp-2.0.pc

