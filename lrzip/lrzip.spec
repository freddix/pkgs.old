Summary:	Long Range ZIP or Lzma RZIP
Name:		lrzip
Version:	0.608
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
# Source0-md5:	c8c6d5a7b2587684eb51f175ac23fb54
URL:		http://ck.kolivas.org/apps/lrzip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lzo-devel
BuildRequires:	nasm
BuildRequires:	perl-tools-pod
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a compression program optimised for large files. The larger
the file and the more memory you have, the better the compression
advantage this will provide, especially once the files are larger than
100MB. The advantage can be chosen to be either size (much smaller
than bzip2) or speed (much faster than bzip2). Decompression is much
always faster than bzip2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--enable-asm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	LN_S=/bin/true

ln -sf %{_bindir}/lrzip $RPM_BUILD_ROOT%{_bindir}/lrunzip
ln -sf %{_bindir}/lrztar $RPM_BUILD_ROOT%{_bindir}/lrzuntar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README README-NOT-BACKWARD-COMPATIBLE TODO WHATS-NEW
%doc doc/README* doc/lrzip.conf.example doc/magic.header.txt
%attr(755,root,root) %{_bindir}/lrunzip
%attr(755,root,root) %{_bindir}/lrzip
%attr(755,root,root) %{_bindir}/lrztar
%attr(755,root,root) %{_bindir}/lrzuntar
%{_mandir}/man1/lrunzip.1*
%{_mandir}/man1/lrzcat.1*
%{_mandir}/man1/lrzip.1*
%{_mandir}/man1/lrztar.1*
%{_mandir}/man1/lrzuntar.1*
%{_mandir}/man5/lrzip.conf.5*

