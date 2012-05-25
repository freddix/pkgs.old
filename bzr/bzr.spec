Summary:	Version control system
Name:		bzr
Version:	2.5.0
Release:	2
License:	GPL v2
Group:		Development/Version Control
Source0:	https://launchpad.net/bzr/2.5/2.5.0/+download/%{name}-%{version}.tar.gz
# Source0-md5:	44eb47b77995098a28f017e2daa606b6
Patch0:		%{name}-locale-path.patch
URL:		http://bazaar-vcs.org/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bazaar is a version control system that helps you track project
history over time and to collaborate easily with others.
Whether you're a single developer, a co-located team or a community
of developers scattered across the world, Bazaar scales and adapts
to meet your needs.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--install-data %{_datadir} \
	--root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/bzrlib/tests
rm -rf $RPM_BUILD_ROOT%{_localedir}/sco

%find_lang %{name}
%py_postclean


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*.txt NEWS README TODO
%attr(755,root,root) %{_bindir}/bzr
%dir %{py_sitedir}/bzrlib
%{py_sitedir}/bzrlib/*.py[co]
%attr(755,root,root) %{py_sitedir}/bzrlib/_*.so
%{py_sitedir}/bzrlib/bundle
%{py_sitedir}/bzrlib/doc
%{py_sitedir}/bzrlib/doc_generate
%{py_sitedir}/bzrlib/export
%{py_sitedir}/bzrlib/filters
%{py_sitedir}/bzrlib/help_topics
%{py_sitedir}/bzrlib/plugins
%{py_sitedir}/bzrlib/repofmt
%{py_sitedir}/bzrlib/smart
%{py_sitedir}/bzrlib/store
%{py_sitedir}/bzrlib/transport
%{py_sitedir}/bzrlib/ui
%{py_sitedir}/bzrlib/util
%{py_sitedir}/bzrlib/version_info_formats
%{_mandir}/man1/bzr.1*

