Summary:	GNU gzip file compression
Name:		gzip
Version:	1.4
Release:	2
License:	GPL
Group:		Applications/Archiving
Source0:	http://ftp.gnu.org/gnu/gzip/%{name}-%{version}.tar.gz
# Source0-md5:	e381b8506210c794278f5527cba0e765
Patch0:		%{name}-mktemp.patch
Patch1:		%{name}-stderr.patch
Patch2:		%{name}-zgreppipe.patch
Patch3:		%{name}-noppid.patch
Patch4:		%{name}-rsyncable.patch
Patch5:		%{name}-CVE-2006-433x.patch
URL:		http://www.gnu.org/software/gzip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
Requires:	mktemp
Provides:	gzip(rsyncable)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
This is the popular GNU file compression and decompression program,
gzip.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,%{_mandir}/pt/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/gzip $RPM_BUILD_ROOT/bin
rm -f $RPM_BUILD_ROOT%{_bindir}/gunzip $RPM_BUILD_ROOT%{_bindir}/zcat

cat > $RPM_BUILD_ROOT/bin/gunzip <<'EOF'
#!/bin/sh
exec /bin/gzip -d "$@"
EOF
cat > $RPM_BUILD_ROOT/bin/zcat <<'EOF'
#!/bin/sh
exec /bin/gzip -cd "$@"
EOF
ln -sf /bin/gzip $RPM_BUILD_ROOT%{_bindir}/gzip
ln -sf /bin/gunzip $RPM_BUILD_ROOT%{_bindir}/gunzip

# conflicts with ncompress
rm -f $RPM_BUILD_ROOT%{_bindir}/uncompress

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/gzip.info*

