Summary:	Unpacks .zip files such as those made by pkzip under DOS
Name:		unzip
Version:	6.0
Release:	1
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://ftp.info-zip.org/pub/infozip/src/%{name}60.tgz
# Source0-md5:	62b490407489521db863b523a7f86375
Patch0:		%{name}-opt.patch
URL:		http://www.info-zip.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-DASM_CRC -DLARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT -DUNICODE_WCHAR -DUNICODE_SUPPORT -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DHAVE_DIRENT_H -DHAVE_TERMIOS_H -D_MBCS

%description
unzip will list, test, or extract files from a ZIP archive, commonly
found on MS-DOS systems. A companion program, zip, creates ZIP
archives; both programs are compatible with archives created by
PKWARE's PKZIP and PKUNZIP for MS-DOS, but in many cases the program
options or default behaviors differ.

%prep
%setup -qn %{name}60
%patch0 -p1

ln -sf unix/Makefile Makefile

%build
%{__make} unzips			\
	AF="-Di386 %{rpmldflags}"	\
	AS="%{__cc}"			\
	CC="%{__cc}"			\
	CF="%{rpmcflags} -I. -Wall"	\
	CRCA_O="crc_gcc.o"		\
	LD="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COPYING.OLD History.600 LICENSE README ToDo WHERE file_id.diz *.txt proginfo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*

