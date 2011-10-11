%define		dict_version	2.00

Summary:	Tesseract Open Source OCR Engine
Name:		tesseract
Version:	3.00
Release:	2
License:	Apache Software License v2
Group:		Applications/Graphics
Source0:	http://tesseract-ocr.googlecode.com/files//%{name}-%{version}.tar.gz
# Source0-md5:	cc812a261088ea0c3d2da735be35d09f
#
Source1:	http://tesseract-ocr.googlecode.com/files/deu.traineddata.gz
# Source1-md5:	be81a761f61800f6d39393a31435fff3
Source2:	http://tesseract-ocr.googlecode.com/files/deu-frak.traineddata.gz
# Source2-md5:	e3117394f775a720117efadda202af50
Source3:	http://tesseract-ocr.googlecode.com/files/eng.traineddata.gz
# Source3-md5:	d91041ad156cf2db36664e91ef799451
Source4:	http://tesseract-ocr.googlecode.com/files/pol.traineddata.gz
# Source4-md5:	c3d6447245663138f1d3aa4567c72192
#
Patch0:		%{name}-missing.patch
Patch1:		%{name}-link.patch
URL:		http://code.google.com/p/tesseract-ocr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	leptonica-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	'.+(libtesseract).+\.so.+'

%description
A commercial quality OCR engine originally developed at HP between
1985 and 1995. In 1995, this engine was among the top 3 evaluated by
UNLV. It was open-sourced by HP and UNLV in 2005.

%package libs
Summary:	Tesseract libraries
Group:		Development/Libraries

%description libs
Tesseract libraries.

%package devel
Summary:	Header files for Tesseract libraries
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the development header files necessary to
develop applications using Tesseract API.

%package trainer
Summary:	Tesseract trainer for new languages
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description trainer
Tesseract trainer for new languages.

%package lang-de
Summary:	Tesseract german language support
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description lang-de
Tesseract german language support.

%package lang-pl
Summary:	Tesseract polish language support
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description lang-pl
Tesseract polish language support.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/tessdata

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for l in deu deu-frak eng pol; do
	gzip -dc $RPM_SOURCE_DIR/${l}.traineddata.gz > $RPM_BUILD_ROOT%{_datadir}/tessdata/${l}.traineddata
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/tesseract

%dir %{_datadir}/tessdata
%{_datadir}/tessdata/configs
%{_datadir}/tessdata/tessconfigs
%{_datadir}/tessdata/eng.*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtesseract_*.so.?
%attr(755,root,root) %{_libdir}/libtesseract_*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtesseract_*.so
%{_libdir}/libtesseract_*.la
%{_includedir}/%{name}

%files trainer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cntraining
%attr(755,root,root) %{_bindir}/combine_tessdata
%attr(755,root,root) %{_bindir}/mftraining
%attr(755,root,root) %{_bindir}/unicharset_extractor
%attr(755,root,root) %{_bindir}/wordlist2dawg

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/tessdata/deu-frak.*
%{_datadir}/tessdata/deu.*

%files lang-pl
%defattr(644,root,root,755)
%{_datadir}/tessdata/pol.*

