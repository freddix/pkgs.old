%define		realname	gimp-hdrtools

Summary:	HDRtools plug-in for GIMP
Name:		gimp-plugin-hdrtools
Version:	0.1
Release:	13
License:	LGPL v2+
Group:		X11/Applications/Graphics
# seems to be down
Source0:	http://nifelheim.dyndns.org/~cocidius/files/%{realname}-%{version}.tar.bz2
# Source0-md5:	8d14fd09b8672fc13395cbe17a8e382e
URL:		http://nifelheim.dyndns.org/~cocidius/hdrtools/
BuildRequires:	gimp-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
HDR tools plug-in for GIMP.

%prep
%setup -qn %{realname}-%{version}
sed -i -e 's|-g -O2|%{rpmcflags}|' Makefile

%build
%{__make} \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D hdrtools $RPM_BUILD_ROOT%{plugindir}/hdrtools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gimp/2.0/plug-ins/*

