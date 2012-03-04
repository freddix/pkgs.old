Summary:	The GNU version of the awk text processing utility
Name:		gawk
Version:	4.0.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/gawk/%{name}-%{version}.tar.bz2
# Source0-md5:	7cdc48e99b885a4bbe0e98dcf1706b22
Patch0:		%{name}-less_verbose.patch
Patch1:		%{name}-gsub_regenarate.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
Requires:	mktemp
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# redefine _includedir to install headers in a subdir
%define         _includedir     %{_prefix}/include/awk

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%package devel
Summary:	Header files for gawk
Group:		Development/Libraries

%description devel
This is the package containing the header files for gawk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
install *.h $RPM_BUILD_ROOT%{_includedir}

rm -f $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README FUTURES LIMITATIONS NEWS PROBLEMS
%doc POSIX.STD
%attr(755,root,root) %{_bindir}/dgawk
%attr(755,root,root) %{_bindir}/gawk
%attr(755,root,root) %{_bindir}/igawk
%attr(755,root,root) %{_bindir}/pgawk*
%attr(755,root,root) %{_libdir}/awk
%{_datadir}/awk
%{_infodir}/*info*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}

