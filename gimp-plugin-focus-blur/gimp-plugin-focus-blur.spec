Summary:	Focus blur GIMP plug-in
Name:		gimp-plugin-focus-blur
Version:	3.2.6
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://registry.gimp.org/files/focusblur-%{version}.tar.bz2
# Source0-md5:	6196c88aeee8733bacc3c6e9ac3c6cf8
URL:		http://registry.gimp.org/node/1444
BuildRequires:	fftw3-devel
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimp_datadir	%(gimptool --gimpdatadir)
%define		gimp_plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Blurring (DoF) effect for GIMP.

%prep
%setup -qn focusblur-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gimp20-focusblur

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gimp20-focusblur.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{gimp_plugindir}/focusblur

