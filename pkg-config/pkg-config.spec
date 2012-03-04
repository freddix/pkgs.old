Summary:	A tool for determining compilation options
Name:		pkg-config
Version:	0.26
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://pkgconfig.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	47525c26a9ba7ba14bf85e01509a7234
URL:		http://pkgconfig.freedesktop.org/wiki/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
Provides:	pkg-config(pkg-config) = %{version}
Provides:	pkgconfig = %{version}-%{release}
Provides:	pkgconfig(pkg-config) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noarchpkgconfigdir	%{_datadir}/pkgconfig

%description
pkgconfig is a tool for determining compilation options. For each
required library it reads a configuration file installed in a standard
option and ouputs the necessary compiler and linker flags.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--with-installed-popt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkgconfigdir},%{_noarchpkgconfigdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4dir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_pkgconfigdir}
%{_noarchpkgconfigdir}
%{_aclocaldir}/*
%{_mandir}/man1/*

