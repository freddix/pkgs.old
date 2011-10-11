%define		module		ReportLab

Summary:	Python library for generating PDFs and graphics
Name:		python-%{module}
Version:	2.5
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.org/ftp/reportlab-%{version}.tar.gz
# Source0-md5:	cdf8b87a6cf1501de1b0a8d341a217d3
Source1:	http://www.reportlab.com/ftp/fonts/pfbfer.zip
# Source1-md5:	35d20e26490cb2a8646fab6276ac6a4c
Patch0:		%{name}-setup.patch
URL:		http://www.reportlab.org/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python
Requires:	python-PIL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library written in Python that lets you generate platform
independant PDFs and graphics.
- PDF generation: uses Python, a clean OO language, layered
  architecture
- Graphics: provides primitive shapes, reusable widgets, sample
  collections including business chart and diagrams
- PythonPoint: a utility for generating PDF slides from a simple XML
  format

%prep
%setup -qn reportlab-%{version}

%{__unzip} -qq -d src/reportlab/fonts %{SOURCE1}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/demos
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/docs
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/graphics/samples
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/test

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%attr(755,root,root) %{py_sitedir}/_renderPM.so
%attr(755,root,root) %{py_sitedir}/_rl_accel.so
%attr(755,root,root) %{py_sitedir}/pyHnj.so
%attr(755,root,root) %{py_sitedir}/sgmlop.so

%dir %{py_sitedir}/reportlab
%dir %{py_sitedir}/reportlab/fonts
%dir %{py_sitedir}/reportlab/graphics
%dir %{py_sitedir}/reportlab/graphics/barcode
%dir %{py_sitedir}/reportlab/graphics/charts
%dir %{py_sitedir}/reportlab/graphics/widgets
%dir %{py_sitedir}/reportlab/lib
%dir %{py_sitedir}/reportlab/pdfbase
%dir %{py_sitedir}/reportlab/pdfgen
%dir %{py_sitedir}/reportlab/platypus

%{py_sitedir}/reportlab-%{version}-py*.egg-info
%{py_sitedir}/reportlab/*.py[co]
%{py_sitedir}/reportlab/fonts/*.afm
%{py_sitedir}/reportlab/fonts/*.pfb
%{py_sitedir}/reportlab/fonts/*.sfd
%{py_sitedir}/reportlab/fonts/*.ttf
%{py_sitedir}/reportlab/fonts/*.txt
%{py_sitedir}/reportlab/graphics/*.py[co]
%{py_sitedir}/reportlab/graphics/barcode/*.py[co]
%{py_sitedir}/reportlab/graphics/charts/*.py[co]
%{py_sitedir}/reportlab/graphics/widgets/*.py[co]
%{py_sitedir}/reportlab/lib/*.mashed
%{py_sitedir}/reportlab/lib/*.py[co]
%{py_sitedir}/reportlab/pdfbase/*.py[co]
%{py_sitedir}/reportlab/pdfgen/*.py[co]
%{py_sitedir}/reportlab/platypus/*.py[co]

