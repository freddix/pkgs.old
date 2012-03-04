Summary:	Tools needed to create Texinfo format documentation files
Name:		texinfo
Version:	4.13a
Release:	2
License:	GPL
Group:		Applications/Publishing
Source0:	ftp://ftp.gnu.org/gnu/texinfo/%{name}-%{version}.tar.lzma
# Source0-md5:	20b37e49464bd72df4c6cfba33340f87
Patch0:		%{name}-as_needed-fix.patch
Patch1:		%{name}-segv.patch
URL:		http://texinfo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	sed
BuildRequires:	zlib-devel
Requires:	info = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Texinfo is a documentation system that can produce both online
information and printed output from a single source file. Normally,
you'd have to write two separate documents: one for online help or
other online information and the other for a typeset manual or other
printed work. Using Texinfo, you only need to write one source
document. Then when the work needs revision, you only have to revise
one source document. The GNU Project uses the Texinfo file format for
most of its documentation.

%package -n info
Summary:	A stand-alone TTY-based reader for GNU texinfo documentation
Group:		Applications/System
Requires:	fix-info-dir
Obsoletes:	info-install

%description -n info
The GNU project uses the texinfo file format for much of its
documentation. This package includes a standalone browser program to
view these files.

%package texi2dvi
Summary:	Texinfo to dvi conversion tool
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}
Requires:	texlive
Requires:	texlive-fonts-latex
Requires:	texlive-plain

%description texi2dvi
Texinfo to dvi conversion tool.

%prep
%setup -qn %{name}-4.13
%patch0 -p1
%patch1 -p1

%build
%{__autopoint}
%{__aclocal} -I gnulib/m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_sbindir},/sbin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/install-info $RPM_BUILD_ROOT%{_sbindir}
ln -sf %{_sbindir}/install-info $RPM_BUILD_ROOT/sbin/install-info

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post -n info
/usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INTRODUCTION NEWS README TODO
%attr(755,root,root) %{_bindir}/makeinfo
%attr(755,root,root) %{_bindir}/texindex
%{_datadir}/texinfo

%{_infodir}/texinfo*
%{_mandir}/man1/makeinfo.1*
%{_mandir}/man1/texindex.1*
%{_mandir}/man5/texinfo.5*

%files -n info -f texinfo.lang
%defattr(644,root,root,755)
%doc info/README
%attr(755,root,root) %{_bindir}/info
%attr(755,root,root) %{_bindir}/infokey
%attr(755,root,root) /sbin/install-info
%attr(755,root,root) %{_sbindir}/install-info

%{_infodir}/info.info*
%{_infodir}/info-stnd.info*

%{_mandir}/man1/info.1*
%{_mandir}/man1/infokey.1*
%{_mandir}/man1/install-info.1*
%{_mandir}/man5/info.5*

%files texi2dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdftexi2dvi
%attr(755,root,root) %{_bindir}/texi2dvi
%attr(755,root,root) %{_bindir}/texi2pdf
%{_mandir}/man1/pdftexi2dvi.1*
%{_mandir}/man1/texi2dvi.1*
%{_mandir}/man1/texi2pdf.1*

