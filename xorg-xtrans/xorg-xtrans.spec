Summary:	xtrans library - network API translation layer
Name:		xorg-xtrans
Version:	1.2.7
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.bz2
# Source0-md5:	84c66908cf003ad8c272b0eecbdbaee3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%package devel
Summary:	xtrans library - network API translation layer
Group:		X11/Development/Libraries
Requires:	xorg-proto >= 7.6

%description devel
xtrans library provides network API translation layer to insulate X
applications and libraries from OS network vagaries.

%prep
%setup -qn xtrans-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-specs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%{_includedir}/X11/Xtrans
%{_pkgconfigdir}/xtrans.pc
%{_aclocaldir}/xtrans.m4

