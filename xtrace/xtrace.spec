Summary:	Strace for X11 connections
Name:		xtrace
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://alioth.debian.org/frs/download.php/3694/%{name}-%{version}_orig.tar.gz
# Source0-md5:	8f0c8f46cd3824d75be53b40c44da25a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What strace is for system calls, xtrace is for X11 connections:
you hook it between one or more X11 clients and an X server and it
prints the requests going from client to server and the replies,
events and errors going the other way.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xtrace
%{_datadir}/%{name}
%{_mandir}/man1/xtrace.1*

