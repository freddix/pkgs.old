%include	/usr/lib/rpm/macros.mono

Summary:	.NET library for using D-BUS message bus
Name:		mono-dbus-glib-sharp
Version:	0.5.0
Release:	3
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	https://github.com/downloads/mono/dbus-sharp/dbus-sharp-glib-%{version}.tar.gz
# Source0-md5:	2284293316eb3a89f0f78798b8a24418
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-dbus-sharp-devel
BuildRequires:	pkg-config
Requires:	dbus-glib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS.

%package devel
Summary:	Development .NET library for using D-BUS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel
Requires:	mono-dbus-sharp-devel

%description devel
Development .NET library for using D-BUS.

%prep
%setup -qn dbus-sharp-glib-%{version}

%build
%{__libtoolize}
%{__aclocal}
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

%files
%defattr(644,root,root,755)
%{_gacdir}/dbus-sharp-glib

%files devel
%defattr(644,root,root,755)
%{_monodir}/dbus-sharp-glib-1.0
%{_pkgconfigdir}/dbus-sharp-glib-1.0.pc

