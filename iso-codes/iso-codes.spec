Summary:	List of country and language names
Name:		iso-codes
Version:	3.25.1
Release:	2
License:	LGPL
Group:		Applications/Text
Source0:	ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/%{name}-%{version}.tar.bz2
# Source0-md5:	4e5620cc9e64b64ebcce0a00e22a22f7
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	python-PyXML
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noarchpkgconfigdir	%{_datadir}/pkgconfig

%description
This package aims to provide the list of the country and language (and
currency) names in one place, rather than repeated in many programs.

%prep
%setup -q

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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{crh,dv,haw,kok,no,pa_IN,ps,syr,wo}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{_datadir}/xml/iso-codes
%{_noarchpkgconfigdir}/iso-codes.pc

