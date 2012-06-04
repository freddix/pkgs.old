Summary:	LADSPA REV plugin
Name:		ladspa-plugins-rev
Version:	0.3.1
Release:	2
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/REV-plugins-%{version}.tar.bz2
# Source0-md5:	bca920c2cbf5e33989e7cafab6fbaee4
Patch0:		%{name}-make.patch
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This reverb is based on gverb by Juhana Sadeharju, but the code
(now C++) is entirely original.

%prep
%setup -qn REV-plugins-%{version}
%patch0 -p1

%build
%{__make} \
	CXX=%{__cxx}		\
	LDFLAGS="%{rpmldflags}"	\
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

install *.so $RPM_BUILD_ROOT%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/*.so

