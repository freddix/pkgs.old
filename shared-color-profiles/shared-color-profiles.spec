Summary:	Shared color profiles to be used in color management aware applications
Name:		shared-color-profiles
Version:	0.1.5
Release:	1
License:	Free (Public Domain, CC-BY-SA, CC-BY-ND, zlib, MIT - depending on profile)
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.gz
# Source0-md5:	65501b1376825b350b3deca97bbbf652
URL:		http://github.com/hughsie/shared-color-profiles
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains various profiles which are useful for programs
that are color management aware.

%prep
%setup -q

%build
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
%doc AUTHORS NEWS README
%{_datadir}/color/icc/*.ic[cm]
%{_datadir}/color/icc/Argyll
%{_datadir}/color/icc/Oysonar
%{_datadir}/color/icc/Yamma
%{_datadir}/shared-color-profiles

