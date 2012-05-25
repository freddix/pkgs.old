Summary:	Color targets from vendors for color calibration
Name:		shared-color-targets
Version:	0.1.1
Release:	1
License:	CC-BY-SA v3.0
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	0354664fc0d5c0efbe3a14089956e461
URL:		http://github.com/hughsie/shared-color-targets
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains target files for popular scanner calibration
targets.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_datadir}/color/targets/test.it8
%{_datadir}/color/targets/wolf_faust
%{_datadir}/shared-color-targets

