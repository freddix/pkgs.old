Summary:	VP8, a high-quality video codec
Name:		libvpx
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://webm.googlecode.com/files/%{name}-v%{version}.tar.bz2
# Source0-md5:	d987b5140412edd37d2c6b10c29ad484
URL:		http://www.webmproject.org/
BuildRequires:	doxygen
BuildRequires:	yasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VP8, a high-quality video codec.

%package devel
Summary:	Header files for libvpx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvpx library.

%prep
%setup -qn %{name}-v%{version}

%build
install -d obj
cd obj
# not autoconf configure
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
../configure \
	--as=yasm			\
	--enable-pic			\
	--enable-postproc		\
	--enable-runtime-cpu-detect	\
	--enable-shared			\
	--enable-vp8			\
	--disable-static		\
	--target=x86-linux-gcc

%{__make} verbose=true target=libs	\
	CC="%{__cc}"			\
	HAVE_GNU_STRIP=no		\
	LDFLAGS="%{rpmldflags}"

%{__make} verbose=true target=examples	\
	CC="%{__cc}"			\
	LDFLAGS="%{rpmldflags} -L."

%{__make} verbose=true target=docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/vpx,%{_libdir}}

%{__make} -C obj verbose=true install		\
	DIST_DIR=$RPM_BUILD_ROOT%{_prefix}	\
	LIBSUBDIR=%{_lib}

rm $RPM_BUILD_ROOT%{_libdir}/libvpx.so.1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE PATENTS README
%attr(755,root,root) %{_bindir}/vp8_scalable_patterns
%attr(755,root,root) %{_bindir}/vpxdec
%attr(755,root,root) %{_bindir}/vpxenc
%attr(755,root,root) %ghost %{_libdir}/libvpx.so.?
%attr(755,root,root) %{_libdir}/libvpx.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvpx.so
%{_includedir}/vpx
%{_pkgconfigdir}/vpx.pc

