# The celt codec design and implementation have been merged into
# the IETF Codec Working Group's "Opus" codec. As such, this
# repository is no longer under active development.
#
# Please see https://git.xiph.org/?p=opus.git
# and https://git.xiph.org/?p=users/jm/opus-tools.git for more
# current work. Visit http://opus-codec.org/ for more information.
#
Summary:	Ultra-low delay audio codec
Name:		celt
Version:	0.11.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/celt/%{name}-%{version}.tar.gz
# Source0-md5:	5511732a426cc42bf986ca79b5cdd02f
URL:		http://celt-codec.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CELT codec is a compression algorithm for audio. Like MP3, Vorbis,
and AAC it is suitable for transmitting music with high quality.
Unlike these formats CELT imposes very little delay on the signal,
even less than is typical for speech centric formats like Speex, GSM,
or G.729.

%package devel
Summary:	Header files for CELT library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CELT library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
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
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/celtdec
%attr(755,root,root) %{_bindir}/celtenc
%attr(755,root,root) %ghost %{_libdir}/libcelt0.so.?
%attr(755,root,root) %{_libdir}/libcelt0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcelt0.so
%{_libdir}/libcelt0.la
%{_includedir}/celt
%{_pkgconfigdir}/celt.pc

