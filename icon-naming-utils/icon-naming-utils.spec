%include	/usr/lib/rpm/macros.perl

Summary:	Icon naming utility
Name:		icon-naming-utils
Version:	0.8.90
Release:	4
License:	GPL
Group:		Applications
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2c5c7a418e5eb3268f65e21993277fba
Patch0:		%{name}-paths.patch
URL:		http://tango.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-XML-Simple
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility maps the icon names used by the GNOME and KDE desktops to
the icon names proposed in the Icon Naming Specification.

%prep
%setup -q
%patch0 -p1

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_npkgconfigdir}/*.pc

