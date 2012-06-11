Summary:	Simple screen locker
Name:		i3lock
Version:	2.4.1
Release:	2
License:	BSD
Group:		X11/Applications
Source0:	http://i3wm.org/i3lock/%{name}-%{version}.tar.bz2
# Source0-md5:	fbc954133a6335be89e394d9ec85fcfd
Source1:	%{name}.pamd
BuildRequires:	cairo-devel
BuildRequires:	libev-devel
BuildRequires:	pam-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
Requires:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
i3lock is a simple screen locker like slock. After starting it,
you will see a white screen (you can configure the color/an image).
You can return to your screen by entering your password.

%prep
%setup -q

%build
%{__make} \
	EXTRA_CFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/i3lock
install -D i3lock.1 $RPM_BUILD_ROOT%{_mandir}/man1/i3lock.1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/i3lock
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/i3lock
%{_mandir}/man1/i3lock.1*

