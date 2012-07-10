%include	/usr/lib/rpm/macros.mono

Summary:	Mono.Addins - framework for creating extensible applications and libraries
Name:		mono-addins
Version:	0.6.2
Release:	1
License:	GPL/MIT
Group:		Development/Tools
Source0:	http://download.mono-project.com/sources/mono-addins/%{name}-%{version}.tar.bz2
# Source0-md5:	afbbe5e9fdf9b03911bc8e6b94feb60b
Patch0:		%{name}-automake.patch
URL:		http://www.mono-project.com/Mono.Addins
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-gtk-sharp-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mono.Addins has been designed to be easy to use and useful for a wide
range of applications: from simple applications with small
extensibility needs, to complex applications which need support for
large add-in structures. This new framework intends to set an standard
for building extensible applications and add-ins in Mono.

%package devel
Summary:	Mono.Addins development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Mono.Addins development files.

%prep
%setup -q
%patch0 -p1

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_monodir}/gac/Mono.Addins/*/*.mdb
rm -rf $RPM_BUILD_ROOT%{_gacdir}/Mono.Addins.MSBuild
rm -rf $RPM_BUILD_ROOT%{_gacdir}/policy.0.?.Mono.Addins.MSBuild
rm -rf $RPM_BUILD_ROOT%{_monodir}/xbuild

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mautil
%{_gacdir}/Mono.Addins
%{_gacdir}/Mono.Addins.CecilReflector
%{_gacdir}/Mono.Addins.Gui
%{_gacdir}/Mono.Addins.Setup
%{_gacdir}/policy.0.?.Mono.Addins
%{_gacdir}/policy.0.?.Mono.Addins.CecilReflector
%{_gacdir}/policy.0.?.Mono.Addins.Gui
%{_gacdir}/policy.0.?.Mono.Addins.Setup
%{_mandir}/man1/mautil.1*

%files devel
%defattr(644,root,root,755)
%{_monodir}/mono-addins
%{_pkgconfigdir}/*

