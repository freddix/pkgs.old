%include	/usr/lib/rpm/macros.mono

Summary:	A fully managed implementation of libgnome-keyring
Name:		mono-gnome-keyring-sharp
Version:	1.0.2
Release:	1
License:	X11/MIT
Group:		Libraries
Source0:	http://www.go-mono.com/archive/gnome-keyring-sharp/gnome-keyring-sharp-%{version}.tar.gz
# Source0-md5:	f9a48319f3fe6123017b000d714d68b1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono-csharp
BuildRequires:	monodoc
BuildRequires:	pkg-config
BuildRequires:	rpmbuild(monoautodeps)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a fully managed implementation of
libgnome-keyring.

%package devel
Summary:	Development part of gnome-keyring-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc
Requires:	which

%description devel
Developement files and documentation for developing applications using
gnome-keyring-sharp.

%prep
%setup -qn gnome-keyring-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources

ln -s %{_pkgconfigdir}/gnome-keyring-sharp-1.0.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/gnome-keyring-sharp.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libgnome-keyring-sharp-glue.so
%{_gacdir}/Gnome.Keyring

%files devel
%defattr(644,root,root,755)
%{_monodir}/gnome-keyring-sharp-1.0
%{_pkgconfigdir}/*.pc
%{_libdir}/monodoc/sources/Gnome.Keyring.*

