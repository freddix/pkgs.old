%include	/usr/lib/rpm/macros.perl

Summary:	An open-source memory debugger
Name:		valgrind
Version:	3.7.0
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://valgrind.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	a855fda56edf05614f099dca316d1775
Patch0:		%{name}-debuginfo.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-ld_linux_strlen.patch
URL:		http://valgrind.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	glibc-static
BuildRequires:	libgomp-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*/vgpreload.*\\.so
# ld portion broken
%undefine	with_ccache

%description
Valgrind is a GPL'd system for debugging and profiling Linux programs.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

sed -i -e 's|boost_thread-mt|boost_thread|g' configure.in

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
ac_cv_path_GDB=/usr/bin/gdb \
%configure \
	CC=gcc		\
	LDFLAGS=""	\
	--enable-tls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf _docs
mv $RPM_BUILD_ROOT%{_docdir}/valgrind _docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS FAQ.txt NEWS README README_MISSING_SYSCALL_OR_IOCTL
%doc _docs/html
%doc _docs/valgrind_manual.pdf

%dir %{_libdir}/%{name}

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*-linux
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.a
%{_libdir}/%{name}/*.supp
%{_libdir}/%{name}/*.xml

%{_includedir}/*
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/*.1*

