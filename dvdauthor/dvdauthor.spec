Summary:	dvdauthor - a program that will generate a DVD movie
Name:		dvdauthor
Version:	0.7.0
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/dvdauthor/%{name}-%{version}.tar.gz
# Source0-md5:	33a447fb98ab3293ac40f869eedc17ff
Patch0:		%{name}-libpng15.patch
URL:		http://dvdauthor.sourceforge.net/
BuildRequires:	ImageMagick-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvdauthor is a program that will generate a DVD movie from a valid
MPEG-2 stream that should play when you put it in a DVD player.

%prep
%setup -qn %{name}
%patch0 -p0

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dvdauthor
%{_mandir}/man1/*.1.*

