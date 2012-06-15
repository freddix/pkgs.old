Summary:	A tool to rip video DVDs from the command line
Name:		dvdbackup
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/dvdbackup/%{name}-%{version}.tar.bz2
# Source0-md5:	e4b35ba716852361f35cecafff44f37c
Patch0:		%{name}-include.patch
URL:		http://dvdbackup.sourceforge.net/
BuildRequires:	libdvdread-devel >= 4.2.0
Suggests:	libdvdcss
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvdbackup is a tool to rip video DVDs from the command line. It has
the advantages of being small, fast, and easy to use.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/dvdbackup
%{_mandir}/man1/dvdbackup.1*

