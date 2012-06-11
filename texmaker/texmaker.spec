Summary:	LaTeX development environment
Name:		texmaker
Version:	3.3.4
Release:	1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://www.xm1math.net/texmaker/%{name}-%{version}.tar.bz2
# Source0-md5:	6010c540bb3d0d3571bf523601bc1a48
Patch0:		%{name}-spelldir.patch
URL:		http://www.xm1math.net/texmaker/
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	poppler-qt4-devel
BuildRequires:	qt-build
BuildRequires:	qt-qmake
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
qmake -unix texmaker.pro	\
	CXXFLAGS="%{rpmcflags}"	\
	PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/texmaker/{*.{aff,dic},*README*}

%find_lang %{name} --with-qm --without-mo --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc utilities/AUTHORS utilities/CHANGELOG.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.css
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.js
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.svg
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

