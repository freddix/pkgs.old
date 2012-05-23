Summary:	GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.4.1
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://yorba.org/download/gexiv2/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	055effe708652f0c7440a3def06047da
BuildRequires:	exiv2-devel
BuildRequires:	glib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library.
It makes the basic features of Exiv2 available to GNOME applications.

%package devel
Summary:	Header files for gexiv2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for gexiv2 library.

%prep
%setup -q

# use rpmcflags
sed -i -e 's|-O2 -g|%{rpmcflags}|g' Makefile

%build
./configure \
	--prefix=%{_prefix}	\
	--release

%{__make} \
	CFLAGS="%{rpmcxxflags} -pipe -fPIC -nostdlib"	\
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX="%{_prefix}"	\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgexiv2.so.?
%attr(755,root,root) %{_libdir}/libgexiv2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgexiv2.so
%{_libdir}/libgexiv2.la
%{_includedir}/gexiv2
%{_pkgconfigdir}/gexiv2.pc
%{_datadir}/vala/vapi/gexiv2.vapi

