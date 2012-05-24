%define		pname	gst-python

Summary:	GStreamer Python bindings
Name:		python-gstreamer
Version:	0.10.22
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.bz2
# Source0-md5:	937152fe896241f827689f4b53e79b22
URL:		http://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python bindings.

%package devel
Summary:	Development files
Group:		Development/Libraries
Requires:	pkgconfig

%description devel
Development files for GStreamer Python bindings.

%prep
%setup -qn %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/gst-*/gst/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/gst-python/0.10/examples

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELEASE TODO
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstpython.so
%attr(755,root,root) %{py_sitedir}/*.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/*.so

%dir %{py_sitedir}/gst-*
%dir %{py_sitedir}/gst-*/gst
%dir %{py_sitedir}/gst-*/gst/extend
%dir %{_datadir}/gst-python
%dir %{_datadir}/gst-python/0.10

%{py_sitedir}/gst-*/gst/*.py[co]
%{py_sitedir}/gst-*/gst/extend/*.py[co]
%{py_sitedir}/pygst.pth
%{py_sitedir}/pygst.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/gstreamer-0.10/gst/pygst.h
%{_includedir}/gstreamer-0.10/gst/pygstexception.h
%{_includedir}/gstreamer-0.10/gst/pygstminiobject.h
%{_includedir}/gstreamer-0.10/gst/pygstvalue.h

%{_pkgconfigdir}/gst-python-*.pc
%{_datadir}/gst-python/0.10/defs

