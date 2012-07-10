%include	/usr/lib/rpm/macros.mono

Summary:	.NET library for using D-BUS message bus
Name:		mono-dbus-sharp
Version:	0.7.0
Release:	3
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	https://github.com/downloads/mono/dbus-sharp/dbus-sharp-%{version}.tar.gz
# Source0-md5:	1964fc341dcbaeda859c53cee295d042
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkg-config
Requires:	dbus-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS.

%package devel
Summary:	Development .NET library for using D-BUS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel

%description devel
Development .NET library for using D-BUS.

%prep
%setup -qn dbus-sharp-%{version}

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
%{_gacdir}/dbus-sharp

%files devel
%defattr(644,root,root,755)
%{_monodir}/dbus-sharp-1.0
%{_pkgconfigdir}/dbus-sharp-1.0.pc

