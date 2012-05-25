Summary:	SPICE protocol headers
Name:		spice-protocol
Version:	0.10.1
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://www.spice-space.org/download/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	7147ef0d9295dbe44510870f8d047e9c
URL:		http://www.spice-space.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header files defining the SPICE protocol.

The Spice project aims to provide a complete open source solution for
interaction with virtualized desktop devices.

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
%doc COPYING NEWS
%{_includedir}/spice-1
%{_npkgconfigdir}/spice-protocol.pc

