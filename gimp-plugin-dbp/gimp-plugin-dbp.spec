%define		plugin_name	dbp

Summary:	Simple batch processing plug-in for the GIMP
Name:		gimp-plugin-%{plugin_name}
Version:	1.1.9
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.ozemail.com.au/~hodsond/dbpSrc-1-1-9.tgz
# Source0-md5:	1106625707798ab8ea1317ac6bece1c5
URL:		http://members.ozemail.com.au/~hodsond/dbp.html
BuildRequires:	gimp-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool --gimpplugindir)/plug-ins

%description
Simple batch processing plug-in for the GIMP.

%prep
%setup -qn %{plugin_name}-%{version}

sed -i -e 's|-O2 ||' \
       -e 's|g++|$(CPP)|' Makefile

%build
%{__make}			\
	CPP="%{__cxx}"		\
	CPPFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D dbp $RPM_BUILD_ROOT%{plugindir}/%{plugin_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/%{plugin_name}

