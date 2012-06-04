%define		org_name	swh-plugins

Summary:	A set of LADSPA audio plugins
Name:		ladspa-plugins-swh
Version:	0.4.15
Release:	14
License:	GPL
Group:		Applications/Sound
Source0:	http://plugin.org.uk/releases/%{version}/%{org_name}-%{version}.tar.gz
# Source0-md5:	2fbdccef2462ea553901acd429fa3573
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-shared-gsm.patch
URL:		http://plugin.org.uk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-single-devel
BuildRequires:	gettext-devel
BuildRequires:	ladspa-devel
BuildRequires:	libgsm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LADSPA audio plugins (see http://plugin.org.uk/ for more
details).

%prep
%setup -q -n %{org_name}-%{version}
%patch0 -p1
%patch1 -p1

sed -i -e 's:/lib/ladspa:/%{_lib}/ladspa:' Makefile.am

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-sse
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{_name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{_name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/swh-*.rdf

