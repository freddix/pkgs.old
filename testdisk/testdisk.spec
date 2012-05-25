Summary:	Tool to check and undelete partition
Name:		testdisk
Version:	6.14
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}-WIP.tar.bz2
# Source0-md5:	8acf98e25d445372ae338c31a3ebd0b9
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	ntfsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check and undelete partition. Works with the following
partitions:
- FAT12 FAT16 FAT32
- Linux Ext2, Ext3
- Linux SWAP (version 1 and 2)
- Linux Raid
- LVM and LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6
- UFS (Sun/BSD)
- XFS

%prep
%setup -qn %{name}-%{version}-WIP

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install src/testdisk $RPM_BUILD_ROOT%{_sbindir}
install src/photorec $RPM_BUILD_ROOT%{_sbindir}
install doc_src/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INFO NEWS README THANKS
%{_mandir}/man8/*.8*
%attr(755,root,root) %{_sbindir}/*

