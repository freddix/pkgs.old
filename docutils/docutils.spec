Summary:	Documentation Utilities
Name:		docutils
Version:	0.8.1
Release:	1
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	2ecf8ba3ece1be1ed666150a80c838c8
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

%package -n python-%{name}
Summary:        Text documents processing modules for Python 2.x
Group:          Development/Languages/Python
%pyrequires_eq	python-libs

%description -n python-%{name}
Docutils are utilities for general- and special-purpose documentation,
including autodocumentation of Python modules. Includes
reStructuredText, the easy to read, easy to use,
what-you-see-is-what-you-get plaintext markup language.

%prep
%setup -q

%build
%{__python} setup.py config build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
    mv "${f}" "${f%.py}"
done

install extras/roman.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/rst2html
%attr(755,root,root) %{_bindir}/rst2latex
%attr(755,root,root) %{_bindir}/rst2man
%attr(755,root,root) %{_bindir}/rst2odt
%attr(755,root,root) %{_bindir}/rst2odt_prepstyles
%attr(755,root,root) %{_bindir}/rst2pseudoxml
%attr(755,root,root) %{_bindir}/rst2s5
%attr(755,root,root) %{_bindir}/rst2xetex
%attr(755,root,root) %{_bindir}/rst2xml
%attr(755,root,root) %{_bindir}/rstpep2html

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/roman.py[oc]
%{py_sitescriptdir}/docutils

