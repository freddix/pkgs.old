Summary:	GNU fast lexical analyzer generator
Name:		flex
Version:	2.5.35
Release:	2
License:	BSD-like
Group:		Development/Tools
Source0:	http://heanet.dl.sourceforge.net/flex/%{name}-%{version}.tar.bz2
# Source0-md5:	10714e50cea54dc7a227e3eddcd44d57
Patch0:		%{name}-locale.patch
URL:		http://flex.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
# m4-quotes* patches require rebuilding *.c from scan.l
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	texinfo
BuildRequires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fPIC

%description
This is the GNU fast lexical analyzer generator. It generates lexical
tokenizing code based on a lexical (regular expression based)
description of the input. It is designed to work with both yacc and
bison, and is used by many programs as part of their build process.

%prep
%setup -q
%patch0 -p1

# force regeneration
rm -f skel.c

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf flex $RPM_BUILD_ROOT%{_bindir}/lex
ln -sf flex $RPM_BUILD_ROOT%{_bindir}/flex++

echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/flex++.1
echo .so flex.1 > $RPM_BUILD_ROOT%{_mandir}/man1/lex.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/flex*
%{_libdir}/*.a
%{_includedir}/*.h

