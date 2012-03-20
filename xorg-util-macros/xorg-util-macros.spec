Summary:	Autoconf macros for xorg
Name:		xorg-util-macros
Version:	1.17
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
# Source0-md5:	4f41667e1bf4938bb2b24fa09d517f77
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

