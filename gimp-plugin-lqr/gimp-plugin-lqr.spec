Summary:	Liquid Rescale GIMP plug-in
Name:		gimp-plugin-lqr
Version:	0.7.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://liquidrescale.wikidot.com/local--files/en:download-page-sources/gimp-lqr-plugin-%{version}.tar.bz2
# Source0-md5:	d7ee28b16bdbd9f46bc9f21cf5deb487
URL:		http://liquidrescale.wikidot.com/
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	liblqr-1-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimp_datadir	%(gimptool --gimpdatadir)
%define		gimp_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
This plug-in aims at resizing pictures non uniformly while preserving
their features, i.e. avoiding distortion of the important parts.
It supports manual feature selection, and can also be used to
remove portions of the picture in a consistent way.

%prep
%setup -qn gimp-lqr-plugin-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{es_ES,eu_ES,nb_NO,ro_RO}

%find_lang gimp20-lqr-plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gimp20-lqr-plugin.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog BUGS README TODO
%attr(755,root,root) %{gimp_plugindir}/gimp-lqr-plugin
%attr(755,root,root) %{gimp_plugindir}/plug_in_lqr_iter
%{_datadir}/gimp-lqr-plugin
%{gimp_datadir}/scripts/batch-gimp-lqr.scm

