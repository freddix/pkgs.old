%define		rnam		tap-plugins
%define		docs_snap	20040817

Summary:	Set of LADSPA plugins for digital audio processing
Name:		ladspa-plugins-tap
Version:	0.7.1
Release:	4
License:	GPL v2
Group:		Applications/Sound
Source0:	http://heanet.dl.sourceforge.net/tap-plugins/%{rnam}-%{version}.tar.gz
# Source0-md5:	87a7d378c4186ad83d98518e003c68a1
Source1:	http://heanet.dl.sourceforge.net/tap-plugins/%{rnam}-doc-%{docs_snap}.tar.gz
# Source1-md5:	9a320210a7a9417487ceb31d6e5c21be
Patch0:		%{name}-DESTDIR_OPTFLAGS.patch
URL:		http://tap-plugins.sourceforge.net/
BuildRequires:	ladspa-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LADSPA plugins for digital audio processing, intended for use
in a professional DAW environment such as Ardour.

%package doc
Summary:	TAP plugins documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description doc
TAP plugins documentation.

%prep
%setup -qn %{rnam}-%{version} -a1
%patch0 -p1

%build
sed -i -e "s|\"ladspa.h\"|<ladspa.h>|g" *.c

%{__make} \
	OPTFLAGS="-O3 -fno-strict-aliasing -fwrapv -march=i686 -mtune=pentium4 -gdwarf-2 -g2 -pipe -ffast-math -funroll-loops -Wall -fPIC -DPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_libdir}/ladspa/*.so
%{_datadir}/ladspa/rdf/*.rdf

%files doc
%defattr(644,root,root,755)
%doc %{rnam}-doc-%{docs_snap}/*

