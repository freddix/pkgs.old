Summary:	Autoconf macros for xorg
Name:		xorg-util-macros
Version:	1.15.0
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
# Source0-md5:	357efdfa69f3e092de3b7000b90f6f4a
Patch0:		%{name}-x.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define debug_package %{nil}

%description
Autoconf macros for xorg.

%prep
%setup -qn util-macros-%{version}
%patch0 -R -p1

%build
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
%doc COPYING ChangeLog
%{_aclocaldir}/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc

