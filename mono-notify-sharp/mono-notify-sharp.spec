%include	/usr/lib/rpm/macros.mono

Summary:	C# Desktop Notifications implementation
Name:		mono-notify-sharp
Version:	0.4.0
Release:	3
License:	X11/MIT
Source0:	notify-sharp-%{version}.tar.bz2
# Source0-md5:	6a40b072125f109f3f38db993511e3d2
Patch0:		%{name}-monodir.patch
Patch1:		%{name}-fix-app-name-derivation.patch
Patch2:		%{name}-reverse-cap-check.patch
Patch3:		%{name}-use-dbus-sharp.patch
Group:		Development/Libraries
URL:		http://trac.galago-project.org/wiki/DesktopNotifications
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	mono-dbus-sharp-devel
BuildRequires:	mono-gtk-sharp-devel
BuildRequires:	monodoc
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

%package devel
Summary:	Files required for compilation using notify-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files required for compilation using notify-sharp.

%prep
%setup -qn notify-sharp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-docs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%{_gacdir}/notify-sharp

%files devel
%defattr(644,root,root,755)
%{_monodir}/notify-sharp
%{_pkgconfigdir}/notify-sharp.pc

