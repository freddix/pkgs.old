Summary:	Matroska video utilities
Name:		mkvtoolnix
Version:	5.0.1
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://www.bunkus.org/videotools/mkvtoolnix/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	93fbbe946de6013eca699c0c2a93a4e9
Patch0:		%{name}-configure.patch
URL:		http://www.bunkus.org/videotools/mkvtoolnix/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	flac-devel
BuildRequires:	libebml-devel
BuildRequires:	libmatroska-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	lzo-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	ruby
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matroska video utilities.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I ac
%{__autoheader}
%{__autoconf}
%{__automake} ||
%configure \
	--with-boost-filesystem=boost_filesystem	\
	--with-boost-regex=boost_regex			\
	--with-boost-system=boost_system

# rakefile, rake can be used, but it supports only one thread
./drake -j2

%install
rm -rf $RPM_BUILD_ROOT

./drake install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*

