%define		rname	vicious

Summary:	Modular widget library for the Awesome WM
Name:		awesome-plugin-%{rname}
Version:	2.0.3
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://git.sysphere.org/vicious/snapshot/vicious-%{version}.tar.gz
# Source0-md5:	dd457309354eadad61f5ef8c79fb25cc
URL:		http://awesome.naquadah.org/wiki/Vicious
Requires:	awesome
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vicious is a modular widget library for the "awesome" window manager,
derived from the "Wicked" widget library. Vicious widget types are a
framework for creating your own widgets.

%prep
%setup -qn %{rname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{rname}/widgets
install *.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{rname}
install widgets/*.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib/%{rname}/widgets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_datadir}/awesome/lib/%{rname}

