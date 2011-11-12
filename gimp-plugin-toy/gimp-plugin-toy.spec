Summary:	Toy effect GIMP plug-in
Name:		gimp-plugin-toy
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://registry.gimp.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	21c6b2f66ab348291d620ba06b8bd7dd
URL:		http://registry.gimp.org/node/25803
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimp_datadir	%(gimptool --gimpdatadir)
%define		gimp_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
This plug-in creates a toy effect or tilt-shift miniature faking on
a selected layer.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gimp20-toy

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gimp20-toy.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog BUGS README TODO
%attr(755,root,root) %{gimp_plugindir}/gimp-plugin-toy
%{_datadir}/toy

