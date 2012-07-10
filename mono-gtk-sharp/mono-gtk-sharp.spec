%include	/usr/lib/rpm/macros.mono

Summary:	Mono bindings for GTK+
Name:		mono-gtk-sharp
Version:	2.12.11
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.mono-project.com/sources/gtk-sharp212/gtk-sharp-%{version}.tar.bz2
# Source0-md5:	c278da6a472c6c13b698af012f543c64
Patch0:		%{name}-destdir.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mono-csharp
BuildRequires:	monodoc
BuildRequires:	ncurses-devel
BuildRequires:	pkg-config
Requires:	mono-atk-sharp = %{version}-%{release}
Requires:	mono-pango-sharp = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for Mono to GTK+ libraries.

%package devel
Summary:	Development part of GTK#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mono-glade-sharp = %{version}-%{release}
Requires:	monodoc
Requires:	which

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GTK#.

%package -n mono-atk-sharp
Summary:	Mono bindings for atk library
Group:		Libraries
Requires:	mono-glib-sharp = %{version}-%{release}

%description -n mono-atk-sharp
Mono bindings for atk library.

%package -n mono-glade-sharp
Summary:	Mono bindings for Glade
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description -n mono-glade-sharp
Mono bindings for Glade library.

%package -n mono-glib-sharp
Summary:	Mono bindings for Glib
Group:		Libraries

%description -n mono-glib-sharp
Mono bindings for Glib library.

%package -n mono-pango-sharp
Summary:	Mono bindings for Pango
Group:		Libraries
Requires:	mono-glib-sharp = %{version}-%{release}

%description -n mono-pango-sharp
Mono bindings for Pango library.

%prep
%setup -qn gtk-sharp-%{version}
%patch0 -p1

# fix build with new glib
sed -i -e "s|/gthread.h|.h|" glib/glue/thread.c

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

rm -f $RPM_BUILD_ROOT%{_prefix}/lib/lib*glue-2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n mono-atk-sharp -p /sbin/ldconfig
%postun	-n mono-atk-sharp -p /sbin/ldconfig

%post	-n mono-glade-sharp -p /sbin/ldconfig
%postun	-n mono-glade-sharp -p /sbin/ldconfig

%post	-n mono-glib-sharp -p /sbin/ldconfig
%postun	-n mono-glib-sharp -p /sbin/ldconfig

%post	-n mono-pango-sharp -p /sbin/ldconfig
%postun	-n mono-pango-sharp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%dir %{_monodir}/gtk-sharp-2.0
%attr(755,root,root) %{_libdir}/libgdksharpglue-2.so
%attr(755,root,root) %{_libdir}/libgtksharpglue-2.so
%{_gacdir}/gdk-sharp
%{_gacdir}/gtk-dotnet
%{_gacdir}/gtk-sharp
%{_gacdir}/policy.2.*.gdk-sharp
%{_gacdir}/policy.2.*.gtk-dotnet
%{_gacdir}/policy.2.*.gtk-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.10.gdk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.10.gtk-dotnet.dll
%{_monodir}/gtk-sharp-2.0/policy.2.10.gtk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.gdk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.gtk-dotnet.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.gtk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.gdk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.gtk-dotnet.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.gtk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.gdk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.gtk-dotnet.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.gtk-sharp.dll

%files devel
%defattr(644,root,root,755)
%doc README.generator ChangeLog
%attr(755,root,root) %{_bindir}/gapi*

%dir %{_prefix}/lib/gtk-sharp-2.0
%attr(755,root,root) %{_prefix}/lib/gtk-sharp-2.0/gapi*

# dlls
%{_monodir}/gtk-sharp-2.0/atk-sharp.dll
%{_monodir}/gtk-sharp-2.0/gdk-sharp.dll
%{_monodir}/gtk-sharp-2.0/glade-sharp.dll
%{_monodir}/gtk-sharp-2.0/glib-sharp.dll
%{_monodir}/gtk-sharp-2.0/gtk-dotnet.dll
%{_monodir}/gtk-sharp-2.0/gtk-sharp.dll
%{_monodir}/gtk-sharp-2.0/pango-sharp.dll

# mododoc
%{_libdir}/monodoc/sources/*

# APIs
%dir %{_datadir}/gapi-2.0
%{_datadir}/gapi-2.0/atk-api.xml
%{_datadir}/gapi-2.0/gdk-api.xml
%{_datadir}/gapi-2.0/glade-api.xml
%{_datadir}/gapi-2.0/glib-api.xml
%{_datadir}/gapi-2.0/gtk-api.xml
%{_datadir}/gapi-2.0/pango-api.xml

# pkg-config files
%{_pkgconfigdir}/gapi-2.0.pc
%{_pkgconfigdir}/glade-sharp-2.0.pc
%{_pkgconfigdir}/glib-sharp-2.0.pc
%{_pkgconfigdir}/gtk-dotnet-2.0.pc
%{_pkgconfigdir}/gtk-sharp-2.0.pc

%files -n mono-atk-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatksharpglue-2.so
%{_gacdir}/atk-sharp
%{_gacdir}/policy.2.*.atk-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.8.atk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.atk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.10.atk-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.atk-sharp.dll

%files -n mono-glade-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgladesharpglue-2.so
%{_gacdir}/glade-sharp
%{_gacdir}/policy.2.*.glade-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.10.glade-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.glade-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.glade-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.glade-sharp.dll

%files -n mono-glib-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglibsharpglue-2.so
%{_gacdir}/glib-sharp
%{_gacdir}/policy.2.*.glib-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.10.glib-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.glib-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.glib-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.glib-sharp.dll

%files -n mono-pango-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangosharpglue-2.so
%{_gacdir}/pango-sharp
%{_gacdir}/policy.2.*.pango-sharp
%{_monodir}/gtk-sharp-2.0/policy.2.10.pango-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.4.pango-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.6.pango-sharp.dll
%{_monodir}/gtk-sharp-2.0/policy.2.8.pango-sharp.dll

