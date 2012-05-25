%define		ruby_ridir	%{_datadir}/ri/%{ruby_ver}/system
#
%define		ruby_ver	1.9.1
%define		patchlevel	136
%define		basever		1.9.2
%define		rel		2
#
Summary:	Ruby - interpreted scripting language
Name:		ruby
Version:	%{basever}
Release:	p%{patchlevel}.%{rel}
License:	The Ruby License
Group:		Development/Languages
Source0:	ftp://ftp.ruby-lang.org/pub/ruby/%{name}-%{basever}-p%{patchlevel}.tar.bz2
# Source0-md5:	52958d35d1b437f5d9d225690de94c13
URL:		http://www.ruby-lang.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	doxygen
BuildRequires:	gdbm-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	ruby
BuildRequires:	sed
BuildRequires:	tk-devel
BuildRequires:	unzip
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Provides:	ruby(ver) = %{ruby_ver}
Provides:	ruby-modules(ver) = %{ruby_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in Perl). It is simple,
straight-forward, extensible, and portable.

%package libs
Summary:	Ruby libraries
Group:		Libraries

%description libs
Ruby libraries.

%package tk
Summary:	Ruby/Tk bindings
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tk
This pachage contains Ruby/Tk bindings.

%package devel
Summary:	Ruby development libraries
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Ruby development libraries.

%package doc-ri
Summary:	Ruby ri documentation
Group:		Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description doc-ri
Ruby ri documentation.

%prep
%setup -qn %{name}-%{basever}-p%{patchlevel}

find -type f \( -name '*.rb' -o -name '*.cgi' -o -name '*.test' -o -name 'ruby.1' \
	-o -name 'ruby.info*' -o -name '*.html' -o -name '*.tcl' -o -name '*.texi' \) \
	| xargs %{__sed} -i 's,/usr/local/bin/,%{_bindir}/,'

sed -i -e 's|LIBRUBYARG_STATIC|LIBRUBYARG_SHARED|g' lib/mkmf.rb

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--enable-shared	\
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.EXT ChangeLog ToDo
%attr(755,root,root) %{_bindir}/erb
%attr(755,root,root) %{_bindir}/gem
%attr(755,root,root) %{_bindir}/irb
%attr(755,root,root) %{_bindir}/rake
%attr(755,root,root) %{_bindir}/rdoc
%attr(755,root,root) %{_bindir}/ri
%attr(755,root,root) %{_bindir}/ruby
%attr(755,root,root) %{_bindir}/testrb

%dir %{_datadir}/ri
%dir %{_datadir}/ri/%{ruby_ver}
%dir %{_datadir}/ri/%{ruby_ver}/system

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{ruby_ver}
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/digest
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/dl
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/enc
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/enc/trans
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/io
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/json
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/json/ext
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/mathn
%dir %{_libdir}/%{name}/%{ruby_ver}/*-linux*/racc

%dir %{_libdir}/%{name}/site_ruby
%dir %{_libdir}/%{name}/site_ruby/%{ruby_ver}
%dir %{_libdir}/%{name}/site_ruby/%{ruby_ver}/*-linux*
%dir %{_libdir}/%{name}/vendor_ruby
%dir %{_libdir}/%{name}/vendor_ruby/%{ruby_ver}
%dir %{_libdir}/%{name}/vendor_ruby/%{ruby_ver}/*-linux*

%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/[a-s]*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/[u-z]*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/digest/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/dl/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/enc/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/enc/trans/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/io/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/json/ext/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/mathn/*.so
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/racc/*.so

%dir %{_libdir}/%{name}/gems
%dir %{_libdir}/%{name}/gems/%{ruby_ver}
%dir %{_libdir}/%{name}/gems/%{ruby_ver}/specifications
%{_libdir}/%{name}/gems/%{ruby_ver}/specifications/*.gemspec

%{_libdir}/%{name}/%{ruby_ver}/*-linux*/rbconfig.rb
%{_libdir}/%{name}/%{ruby_ver}/*.rb
%{_libdir}/%{name}/%{ruby_ver}/bigdecimal
%{_libdir}/%{name}/%{ruby_ver}/cgi
%{_libdir}/%{name}/%{ruby_ver}/date
%{_libdir}/%{name}/%{ruby_ver}/digest
%{_libdir}/%{name}/%{ruby_ver}/dl
%{_libdir}/%{name}/%{ruby_ver}/drb
%{_libdir}/%{name}/%{ruby_ver}/fiddle
%{_libdir}/%{name}/%{ruby_ver}/irb
%{_libdir}/%{name}/%{ruby_ver}/json
%{_libdir}/%{name}/%{ruby_ver}/minitest
%{_libdir}/%{name}/%{ruby_ver}/net
%{_libdir}/%{name}/%{ruby_ver}/openssl
%{_libdir}/%{name}/%{ruby_ver}/optparse
%{_libdir}/%{name}/%{ruby_ver}/racc
%{_libdir}/%{name}/%{ruby_ver}/rake
%{_libdir}/%{name}/%{ruby_ver}/rbconfig
%{_libdir}/%{name}/%{ruby_ver}/rdoc
%{_libdir}/%{name}/%{ruby_ver}/rexml
%{_libdir}/%{name}/%{ruby_ver}/rinda
%{_libdir}/%{name}/%{ruby_ver}/ripper
%{_libdir}/%{name}/%{ruby_ver}/rss
%{_libdir}/%{name}/%{ruby_ver}/rubygems
%{_libdir}/%{name}/%{ruby_ver}/shell
%{_libdir}/%{name}/%{ruby_ver}/syck
%{_libdir}/%{name}/%{ruby_ver}/test
%{_libdir}/%{name}/%{ruby_ver}/uri
%{_libdir}/%{name}/%{ruby_ver}/webrick
%{_libdir}/%{name}/%{ruby_ver}/xmlrpc
%{_libdir}/%{name}/%{ruby_ver}/yaml

%{_mandir}/man1/erb.1*
%{_mandir}/man1/irb.1*
%{_mandir}/man1/rake.1*
%{_mandir}/man1/ri.1*
%{_mandir}/man1/ruby.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libruby.so.?.?
%attr(755,root,root) %{_libdir}/libruby.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libruby.so
%{_includedir}/%{name}-%{ruby_ver}

%files tk
%defattr(644,root,root,755)
%{_libdir}/%{name}/%{ruby_ver}/tcltk.rb
%{_libdir}/%{name}/%{ruby_ver}/tk*.rb
%{_libdir}/%{name}/%{ruby_ver}/tk
%{_libdir}/%{name}/%{ruby_ver}/tkextlib
%attr(755,root,root) %{_libdir}/%{name}/%{ruby_ver}/*-linux*/t*.so

%files doc-ri
%defattr(644,root,root,755)
%{_datadir}/ri/%{ruby_ver}/system/*

