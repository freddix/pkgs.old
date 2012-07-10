Summary:	JavaScript interpreter and libraries
Name:		js
Version:	1.8.5
Release:	3
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/%{name}185-1.0.0.tar.gz
# Source0-md5:	a4574365938222adca0a6bd33329cb32
Patch0:		%{name}-install.patch
Patch1:		%{name}-bits_per_word.patch
Patch2:		%{name}-opt.patch
URL:		http://www.mozilla.org/js/
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 4.7.0
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout	-fno-strict-aliasing

%description
JavaScript Reference Implementation (codename SpiderMonkey). The
package contains JavaScript runtime (compiler, interpreter,
decompiler, garbage collector, atom manager, standard classes) and
small "shell" program that can be used interactively and with .js
files to run scripts.

%package devel
Summary:	Header files for JavaScript reference library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for JavaScript reference library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd js/src
%configure2_13 \
	--disable-static	\
	--enable-readline	\
	--enable-threadsafe	\
	--with-system-nspr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C js/src install \
	DESTDIR=$RPM_BUILD_ROOT

install js/src/shell/js js/src/jscpucfg $RPM_BUILD_ROOT%{_bindir}

# for compatibility with js
ln -sf libmozjs185.so $RPM_BUILD_ROOT%{_libdir}/libjs.so

# Create pkgconfig file
cat > $RPM_BUILD_ROOT%{_pkgconfigdir}/js.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libjs
Description: JS library
Requires: nspr >= 4.7
Version: %{version}
Libs: -L%{_libdir} -ljs
Cflags: -DXP_UNIX=1 -DJS_THREADSAFE=1 -I%{_includedir}/js
EOF

# rewrite moz185.pc file
cat > $RPM_BUILD_ROOT%{_pkgconfigdir}/mozjs185.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: libjs
Description: JS library
Requires: nspr >= 4.7
Version: %{version}
Libs: -L%{_libdir} -lmozjs185
Cflags: -DXP_UNIX=1 -DJS_THREADSAFE=1 -I%{_includedir}/js
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc js/src/README.html
%attr(755,root,root) %{_bindir}/js
%attr(755,root,root) %ghost %{_libdir}/libmozjs185.so.1.0
%attr(755,root,root) %{_libdir}/libmozjs185.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/js-config
%attr(755,root,root) %{_bindir}/jscpucfg
%attr(755,root,root) %{_libdir}/libmozjs185.so
%attr(755,root,root) %{_libdir}/libjs.so
%{_includedir}/js
%{_pkgconfigdir}/*.pc

