Summary:	The BeeCrypt Cryptography Library
Name:		beecrypt
Version:	4.2.1
Release:	2
Epoch:		2
License:	LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/beecrypt/%{name}-%{version}.tar.gz
# Source0-md5:	8441c014170823f2dff97e33df55af1e
URL:		http://sourceforge.net/projects/beecrypt/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-mmmx -msse -msse2

%description
BeeCrypt is an open source cryptography library that contains highly
optimized C and assembler implementations of many well-known
algorithms including Blowfish, MD5, SHA-1, Diffie-Hellman, and
ElGamal.

%package devel
Summary:	The BeeCrypt Cryptography Library - development files
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The BeeCrypt Cryptography Library - development files.

%prep
%setup -q

# --with-cplusplus or building (even empty) *.cxx into libbeecrypt
# makes it (and thus rpm) depending on libstdc++ which is unacceptable
sed -i -e 's/ cppglue\.cxx$//' Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-openmp		\
	--enable-static=no		\
	--without-cplusplus		\
	--without-python		\
	--without-java
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/libbeecrypt.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib} ; echo libbeecrypt.so.*.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libbeecrypt.so

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BENCHMARKS BUGS CONTRIBUTORS NEWS README
%attr(755,root,root) %ghost /%{_lib}/libbeecrypt.so.?
%attr(755,root,root) /%{_lib}/libbeecrypt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbeecrypt.so
%{_libdir}/libbeecrypt.la
%{_includedir}/beecrypt

