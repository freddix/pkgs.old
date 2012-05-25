Summary:	Distributed SCM
Name:		mercurial
Version:	2.1.2
Release:	2
License:	GPL v2
Group:		Development/Version Control
Source0:	http://www.selenic.com/mercurial/release/%{name}-%{version}.tar.gz
# Source0-md5:	15354d739504ec46f68a0fee2ecfbf25
URL:		http://www.selenic.com/mercurial/
BuildRequires:	asciidoc
BuildRequires:	gettext-devel
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-docutils
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
BuildRequires:	xmlto
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mercurial is a fast, lightweight source control management system
designed for efficient handling of very large distributed projects.

%package gui
Summary:	GUI for mercurial
Group:		Development/Version Control
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-modules

%description gui
A tool called that allows browsing the history of a repository in a
GUI.

To enable it add to .hgrc file:
[extensions]
hgk=

%prep
%setup -q

%build
%{__python} setup.py build
%{__make} -C doc

%check
#cd tests && %{__python} run-tests.py --verbose

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install	\
	--optimize=2		\
	--root=$RPM_BUILD_ROOT

install contrib/hgk $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man{1,5}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README
%attr(755,root,root) %{_bindir}/hg
%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%dir %{py_sitedir}/%{name}
%dir %{py_sitedir}/%{name}/locale
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}/help
%{py_sitedir}/%{name}/hgweb
%{py_sitedir}/%{name}/httpclient
%{py_sitedir}/%{name}/templates
%{py_sitedir}/hgext

%lang(da) %{py_sitedir}/%{name}/locale/da
%lang(de) %{py_sitedir}/%{name}/locale/de
%lang(el) %{py_sitedir}/%{name}/locale/el
%lang(fr) %{py_sitedir}/%{name}/locale/fr
%lang(it) %{py_sitedir}/%{name}/locale/it
%lang(ja) %{py_sitedir}/%{name}/locale/ja
%lang(pt_BR) %{py_sitedir}/%{name}/locale/pt_BR
%lang(sv) %{py_sitedir}/%{name}/locale/sv
%lang(zh_CN) %{py_sitedir}/%{name}/locale/zh_CN
%lang(zh_TW) %{py_sitedir}/%{name}/locale/zh_TW
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hgk

