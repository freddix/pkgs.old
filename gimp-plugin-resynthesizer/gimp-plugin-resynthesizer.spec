%define		plugin	resynthesizer

Summary:	Gimp plug-in for texture synthesis
Name:		gimp-plugin-%{plugin}
Version:	0.16
Release:	4
License:	CeCILL FREE SOFTWARE LICENSE
Group:		X11/Applications/Graphics
Source0:	http://www.logarithmic.net/pfh-files/resynthesizer/%{plugin}-%{version}.tar.gz
# Source0-md5:	097b3a21803fe02e47b8b8649af48144
URL:		http://www.logarithmic.net/pfh/resynthesizer
BuildRequires:	gimp-devel
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool --gimpplugindir)/plug-ins
%define		scriptdir	%(gimptool --gimpdatadir)/scripts
%define		specflags	-fomit-frame-pointer

%description
G'MIC interpreter embedded in a GIMP plugin.

%prep
%setup -qn %{plugin}-%{version}

sed -i -e 's|^CFLAGS.*|CFLAGS=$(GIMP_CFLAGS) $(OPTFLAGS)|' Makefile

%build
%{__make}		\
	CC="%{__cxx}"	\
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{scriptdir}}

install resynth $RPM_BUILD_ROOT%{plugindir}
install smart-enlarge.scm smart-remove.scm $RPM_BUILD_ROOT%{scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{plugindir}/resynth
%{scriptdir}/*.scm

