%include	/usr/lib/rpm/macros.mono

Summary:	.NET language bindings for GIO
Name:		mono-gio-sharp
Version:	2.22.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://download.mono-project.com/sources/gio-sharp/gio-sharp-%{version}.tar.bz2
# Source0-md5:	3d0716b050b3f14820a34b7208559a92
URL:		http://github.com/mono/gio-sharp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-gio-devel
BuildRequires:	mono-csharp
BuildRequires:	mono-gtk-sharp-devel
BuildRequires:	pkg-config
Requires:	glib-gio
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GIO library.

%package devel
Summary:	GIO# development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mono-gtk-sharp-devel
Requires:	glib-gio-devel

%description devel
GIO# development files.

%prep
%setup -qn gio-sharp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/gio-sharp

%files devel
%defattr(644,root,root,755)
%{_datadir}/gapi-2.0/gio-api.xml
%{_pkgconfigdir}/gio-sharp-2.0.pc

