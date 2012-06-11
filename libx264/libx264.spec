%define		snap	20120317
%define		snaph	2245
%define		rel	4
%define		api	122

Summary:	H264 encoder library
Name:		libx264
Version:	0.%{api}
Release:	1.%{snap}_%{snaph}.%{rel}
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-%{snap}-%{snaph}.tar.bz2
# Source0-md5:	a0cc528e1407bd46fc821d4baa3c4075
# get rid of gpac
# http://komisar.gin.by/x.patch/bm.patches/
Patch0:		%{name}-mp4_L-SMASH.patch
URL:		http://developers.videolan.org/x264.html
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	pkg-config
BuildRequires:	yasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-ffast-math -std=gnu99

%description
libx264 library for encoding H264 video format.

%package progs
Summary:	x264 encoder
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description progs
x264 encoder.

%package devel
Summary:	Header files for x264 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for x264 library.

%prep
%setup -qn x264-snapshot-%{snap}-%{snaph}
%patch0 -p1

sed -i -e 's|-O4 ||g' configure
sed -i -e 's| \-s||g' configure

%build
CC="%{__cc}" \
./configure \
	--bindir=%{_bindir}		\
	--enable-pic			\
	--enable-shared			\
	--exec-prefix=%{_prefix}	\
	--extra-cflags="%{rpmcflags}"	\
	--extra-ldflags="%{rpmldflags}"	\
	--includedir=%{_includedir}	\
	--libdir=%{_libdir}		\
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libx264.so.%{api}

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x264

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx264.so
%{_includedir}/*.h
%{_pkgconfigdir}/x264.pc

