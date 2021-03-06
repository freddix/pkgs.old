Summary:	A GNU stream text editor
Name:		sed
Version:	4.2.1
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.gz
# Source0-md5:	f0fd4d7da574d4707e442285fd2d3b86
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor. Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text. The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%check
%{__make} -j1 check

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/sed.info*

