Summary:	A GNU file archiving program
Name:		tar
Version:	1.26
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Archiving
Source0:	ftp://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.xz
# Source0-md5:	0ced6f20b9fa1bea588005b5ad4b52c1
Patch0:		%{name}-zero-block.patch
URL:		http://www.gnu.org/software/tar/tar.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	sed
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/
%define		_bindir		/bin
%define		_libexecdir	/sbin

%description
The GNU tar program saves many files together into one archive and can
restore individual files (or all of the files) from the archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive.

Tar includes multivolume support, automatic archive compression/
decompression, the ability to perform remote archives and the ability
to perform incremental and full backups.

If you want to use Tar for remote backups, you'll also need to install
the rmt package.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/bin,%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_bindir}/tar $RPM_BUILD_ROOT/usr/bin/gtar

help2man ./src/tar -o tar.1
install tar.1 $RPM_BUILD_ROOT%{_mandir}/man1

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/bin/*
%{_infodir}/tar.info*
%{_mandir}/man1/*

