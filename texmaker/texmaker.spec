Summary:	LaTeX development environment
Name:		texmaker
Version:	3.1
Release:	1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://www.xm1math.net/texmaker/%{name}-%{version}.tar.bz2
# Source0-md5:	10a14c75abbb7234d4e5e58a7c85b110
Patch0:		%{name}-spelldir.patch
URL:		http://www.xm1math.net/texmaker/
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	poppler-qt4-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-phonon-devel
BuildRequires:	qt4-qmake
Requires(post,postun):	desktop-file-utils
Requires:	tetex-format-pdflatex
Suggests:	hunspell-dictionaries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Texmaker is a free LaTeX editor, that integrates many tools needed to
develop documents with LaTeX, in just one application.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 -unix texmaker.pro	\
	CXXFLAGS="%{rpmcflags}"	\
	PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/texmaker/{*.{aff,dic},*README*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc utilities/AUTHORS utilities/CHANGELOG.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}

%lang(ca) %{_datadir}/%{name}/texmaker_ca.qm
%lang(cs) %{_datadir}/%{name}/texmaker_cs.qm
%lang(cs) %{_datadir}/%{name}/texmaker_cs.qm
%lang(de) %{_datadir}/%{name}/texmaker_de.qm
%lang(de) %{_datadir}/%{name}/texmaker_de.qm
%lang(es) %{_datadir}/%{name}/texmaker_es.qm
%lang(fa) %{_datadir}/%{name}/texmaker_fa.qm
%lang(fr) %{_datadir}/%{name}/texmaker_fr.qm
%lang(fr) %{_datadir}/%{name}/texmaker_fr.qm
%lang(gl) %{_datadir}/%{name}/texmaker_gl.qm
%lang(hu) %{_datadir}/%{name}/texmaker_hu.qm
%lang(it) %{_datadir}/%{name}/texmaker_it.qm
%lang(nl) %{_datadir}/%{name}/texmaker_nl.qm
%lang(pl) %{_datadir}/%{name}/texmaker_pl.qm
%lang(pt) %{_datadir}/%{name}/texmaker_pt_BR.qm
%lang(ru) %{_datadir}/%{name}/texmaker_ru.qm
%lang(zh_CN) %{_datadir}/%{name}/texmaker_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/texmaker_zh_TW.qm

%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.svg
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

