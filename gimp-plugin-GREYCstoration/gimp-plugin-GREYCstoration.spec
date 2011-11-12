%define		rname	GREYCstoration
#
Summary:	GREYCstoration plug-in for GIMP
Name:		gimp-plugin-%{rname}
Version:	2.9
Release:	13
License:	LGPL v2+
Group:		X11/Applications/Graphics
Source0:	http://heanet.dl.sourceforge.net/cimg/%{rname}-%{version}.zip
# Source0-md5:	67b6bfcadd485ee4669069da52a1e8f5
URL:		http://cimg.sourceforge.net/greycstoration/
BuildRequires:	gimp-devel
BuildRequires:	pkg-config
Requires:	gimp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%(gimptool --gimpplugindir)/plug-ins
%define		specflags	-O3

%description
GREYCstoration is a GIMP plug-in using the algorithm written by David
Tschumperle from GREYC laboratory (at Caen in France). Current version
of the plugin only supports the restoration functionality, but the
algorithm can also do great picture resize or good inpainting.

%prep
%setup -qn %{rname}-%{version}

%build
%{__make} -j1 -C src greycstoration4gimp		\
	CC="%{__cxx}"				\
	GREYCSTORATION_OPT_FLAGS="-fno-tree-pre %{rpmcflags} %{rpmldflags}"	\
	STRIP_EXE=

%install
rm -rf $RPM_BUILD_ROOT

install -D src/greycstoration4gimp $RPM_BUILD_ROOT%{plugindir}/greycstoration

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt Licence_CeCILL_V2-en.txt
%attr(755,root,root) %{plugindir}/greycstoration

