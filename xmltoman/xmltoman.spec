%include	/usr/lib/rpm/macros.perl
#
Summary:	XML to man format converter
Name:		xmltoman
Version:	0.4
Release:	4
License:	GPL
Group:		Applications
Source0:	http://heanet.dl.sourceforge.net/xmltoman/%{name}-%{version}.tar.gz
# Source0-md5:	99be944b9fce40b3fe397049bf14a097
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML to man format converter.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install		\
	DESTDIR=$RPM_BUILD_ROOT	\
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/xmlmantohtml
%attr(755,root,root) %{_bindir}/xmltoman
%{_datadir}/%{name}

