%define		gstname		fluendo-mpegdemux
%define		gst_major_ver   0.10

Summary:	GStreamer MPEG-2 demuxer plugin
Name:		gstreamer-%{gstname}
Version:	0.10.70
Release:	1
License:	MPL v1.1
Group:		Libraries
Source0:	http://core.fluendo.com/gstreamer/src/gst-fluendo-mpegdemux/gst-%{gstname}-%{version}.tar.bz2
# Source0-md5:	ceb9001be71e8cbc3e97f9b46c9b611e
URL:		http://gstreamer.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer-devel >= 0.10.30
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluendo GStreamer plug-in for MPEG demuxing.

%prep
%setup -qn gst-%{gstname}-%{version}

%build
%if 0
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%endif
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstflumpegdemux.so

