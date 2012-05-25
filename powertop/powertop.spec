Summary:	Tool that helps to optimze power usage
Name:		powertop
Version:	2.0
Release:	3
License:	GPL v2
Group:		Applications
Source0:	https://01.org/powertop/sites/default/files/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	8f27e2b0bf1c68b1f5a9a98294238bb2
URL:		http://www.lesswatts.org/projects/powertop/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool that helps to optimze power usage.

%prep
%setup -q

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/cache/powertop

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

:> $RPM_BUILD_ROOT/var/cache/powertop/saved_parameters.powertop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_sbindir}/powertop
%dir /var/cache/powertop
%ghost /var/cache/powertop/saved_parameters.powertop

