Summary:	MLT - Media Lovin' Toolkit
Name:		mlt
Version:	0.7.6
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/mlt/%{name}-%{version}.tar.gz
# Source0-md5:	105969a63339da2f8ce4ddce1652c9e7
URL:		http://www.dennedy.org/mlt/twiki/bin/view/MLT/WebHome
BuildRequires:	SDL-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	ladspa-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libdv-devel
BuildRequires:	libmad-devel
BuildRequires:	libquicktime-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	sox-devel
BuildRequires:	swig-python
BuildRequires:	which
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLT is an open source multimedia framework, designed and developed for
television broadcasting. It provides a toolkit for broadcasters, video
editors, media players, transcoders, web streamers and many more types
of applications. The functionality of the system is provided via an
assortment of ready to use tools, XML authoring components, and an
extendible plug-in based API.

%package libs
Summary:	MLT libraries
Group:		Libraries

%description libs
MLT libraries.

%package devel
Summary:	Header files for MLT
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files for MLT.

%package -n python-mlt
Summary:	MLT python module
Group:		Development/Libraries
%pyrequires_eq	python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-mlt
MLT python module.

%prep
%setup -q

sed -i 's|-Wall|-Wall %{rpmcxxflags}|g' src/mlt++/configure

%build
%configure \
	--avformat-shared=%{_prefix}	\
	--avformat-swscale	\
	--avformat-vdpau	\
	--disable-qimage	\
	--disable-sse2		\
	--disable-swfdec	\
	--enable-gpl		\
	--luma-compress		\
	--swig-languages=python

%{__make} \
	CC="%{__cc}"	\
	CXX="%{__cxx}"	\
	OPTIMISATIONS="%{rpmcflags}"

#cd src/swig/python
#./build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D src/swig/python/_mlt.so $RPM_BUILD_ROOT%{py_sitedir}/_mlt.so
install -D src/swig/python/mlt.py $RPM_BUILD_ROOT%{py_scriptdir}/mlt.py

%py_comp $RPM_BUILD_ROOT%{py_scriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/melt
%attr(755,root,root) %{_libdir}/mlt/*.so
%{_datadir}/mlt

%files libs
%defattr(644,root,root,755)
%dir %{_libdir}/mlt
%attr(755,root,root) %ghost %{_libdir}/libmlt++.so.?
%attr(755,root,root) %ghost %{_libdir}/libmlt.so.?
%attr(755,root,root) %{_libdir}/libmlt++.so.*.*.*
%attr(755,root,root) %{_libdir}/libmlt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmlt++.so
%{_libdir}/libmlt.so
%{_includedir}/mlt
%{_includedir}/mlt++
%{_pkgconfigdir}/*.pc

%files -n python-mlt
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_scriptdir}/*.py[co]

