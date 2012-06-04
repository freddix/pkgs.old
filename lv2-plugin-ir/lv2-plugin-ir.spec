%define		rname	ir.lv2

Summary:	LV2 audio processing plugin
Name:		lv2-plugin-ir
Version:	1.3.1
Release:	2
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://factorial.hu/system/files/%{rname}-%{version}.tar.gz
# Source0-md5:	2c7767db934a1ca4d55d220e7ebad912
Patch0:		%{name}-build.patch
Patch1:		%{name}-zita_conv3.patch
BuildRequires:	gtk+-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRequires:	zita-convolver-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IR is a zero-latency, realtime, high performance signal convolver
especially for creating reverb effects. Supports impulse responses
with 1, 2 or 4 channels, in any soundfile format supported by
libsndfile.

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}"			\
	CC="%{__cc}"			\
	LDFLAGS="%{rpmldflags}"		\
	OPTCXXFLAGS="%{rpmcxxflags}"	\
	OPTCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LIBDIR="%{_libdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/lv2/%{rname}
%attr(755,root,root) %{_libdir}/lv2/%{rname}/*.so
%{_libdir}/lv2/%{rname}/*.ttl

