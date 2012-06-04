Summary:	Plugin standard for audio systems
Name:		lv2
Version:	1.0.0
Release:	3
License:	LGPL v2.1 or later and BSD-like
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	af98a50d8dfa8318a69800ea48b421f6
BuildRequires:	gtk+-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 is a plugin standard for audio systems. It defines a minimal yet
extensible C API for plugin code and a format for plugin "bundles".

%package devel
Summary:	LV2 development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
LV2 development files.

%package examples
Summary:	Example LV2 plugins
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+

%description examples
Example LV2 plugins.

%prep
%setup -q

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
./waf -v configure --nocache --prefix=%{_prefix}
./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/lv2core.lv2
%{_libdir}/lv2/lv2core.lv2/lv2core.doap.ttl
%{_libdir}/lv2/lv2core.lv2/lv2core.ttl
%{_libdir}/lv2/lv2core.lv2/manifest.ttl

%files examples
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/eg-amp.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-amp.lv2/amp.so
%{_libdir}/lv2/eg-amp.lv2/amp.ttl
%{_libdir}/lv2/eg-amp.lv2/manifest.ttl

%dir %{_libdir}/lv2/eg-sampler.lv2
%attr(755,root,root) %{_libdir}/lv2/eg-sampler.lv2/sampler.so
%{_libdir}/lv2/eg-sampler.lv2/click.wav
%{_libdir}/lv2/eg-sampler.lv2/manifest.ttl
%{_libdir}/lv2/eg-sampler.lv2/sampler.ttl
%{_libdir}/lv2/eg-sampler.lv2/sampler_ui.so

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lv2
%dir %{_includedir}/lv2/lv2plug.in
%dir %{_includedir}/lv2/lv2plug.in/ns
%dir %{_includedir}/lv2/lv2plug.in/ns/ext
%dir %{_includedir}/lv2/lv2plug.in/ns/extensions
%dir %{_includedir}/lv2/lv2plug.in/ns/lv2core
%{_includedir}/lv2.h
%{_includedir}/lv2/lv2plug.in/ns/ext/atom
%{_includedir}/lv2/lv2plug.in/ns/ext/data-access
%{_includedir}/lv2/lv2plug.in/ns/ext/dynmanifest
%{_includedir}/lv2/lv2plug.in/ns/ext/event
%{_includedir}/lv2/lv2plug.in/ns/ext/instance-access
%{_includedir}/lv2/lv2plug.in/ns/ext/log
%{_includedir}/lv2/lv2plug.in/ns/ext/midi
%{_includedir}/lv2/lv2plug.in/ns/ext/patch
%{_includedir}/lv2/lv2plug.in/ns/ext/port-groups
%{_includedir}/lv2/lv2plug.in/ns/ext/port-props
%{_includedir}/lv2/lv2plug.in/ns/ext/presets
%{_includedir}/lv2/lv2plug.in/ns/ext/resize-port
%{_includedir}/lv2/lv2plug.in/ns/ext/state
%{_includedir}/lv2/lv2plug.in/ns/ext/time
%{_includedir}/lv2/lv2plug.in/ns/ext/uri-map
%{_includedir}/lv2/lv2plug.in/ns/ext/urid
%{_includedir}/lv2/lv2plug.in/ns/ext/worker
%{_includedir}/lv2/lv2plug.in/ns/extensions/ui
%{_includedir}/lv2/lv2plug.in/ns/extensions/units

%dir %{_libdir}/lv2/atom.lv2
%dir %{_libdir}/lv2/data-access.lv2
%dir %{_libdir}/lv2/dynmanifest.lv2
%dir %{_libdir}/lv2/event.lv2
%dir %{_libdir}/lv2/instance-access.lv2
%dir %{_libdir}/lv2/log.lv2
%dir %{_libdir}/lv2/meta.lv2
%dir %{_libdir}/lv2/midi.lv2
%dir %{_libdir}/lv2/parameters.lv2
%dir %{_libdir}/lv2/patch.lv2
%dir %{_libdir}/lv2/port-groups.lv2
%dir %{_libdir}/lv2/port-props.lv2
%dir %{_libdir}/lv2/presets.lv2
%dir %{_libdir}/lv2/resize-port.lv2
%dir %{_libdir}/lv2/state.lv2
%dir %{_libdir}/lv2/time.lv2
%dir %{_libdir}/lv2/ui.lv2
%dir %{_libdir}/lv2/units.lv2
%dir %{_libdir}/lv2/uri-map.lv2
%dir %{_libdir}/lv2/urid.lv2
%dir %{_libdir}/lv2/worker.lv2

%{_libdir}/lv2/atom.lv2/atom.h
%{_libdir}/lv2/atom.lv2/atom.ttl
%{_libdir}/lv2/atom.lv2/forge.h
%{_libdir}/lv2/atom.lv2/manifest.ttl
%{_libdir}/lv2/atom.lv2/util.h
%{_libdir}/lv2/data-access.lv2/data-access.h
%{_libdir}/lv2/data-access.lv2/data-access.ttl
%{_libdir}/lv2/data-access.lv2/manifest.ttl
%{_libdir}/lv2/dynmanifest.lv2/dynmanifest.h
%{_libdir}/lv2/dynmanifest.lv2/dynmanifest.ttl
%{_libdir}/lv2/dynmanifest.lv2/lv2-dynmanifest.doap.ttl
%{_libdir}/lv2/dynmanifest.lv2/manifest.ttl
%{_libdir}/lv2/event.lv2/event-helpers.h
%{_libdir}/lv2/event.lv2/event.h
%{_libdir}/lv2/event.lv2/event.ttl
%{_libdir}/lv2/event.lv2/manifest.ttl
%{_libdir}/lv2/instance-access.lv2/instance-access.h
%{_libdir}/lv2/instance-access.lv2/instance-access.ttl
%{_libdir}/lv2/instance-access.lv2/manifest.ttl
%{_libdir}/lv2/log.lv2/log.h
%{_libdir}/lv2/log.lv2/log.ttl
%{_libdir}/lv2/log.lv2/manifest.ttl
%{_libdir}/lv2/lv2core.lv2/lv2.h
%{_libdir}/lv2/meta.lv2/manifest.ttl
%{_libdir}/lv2/meta.lv2/meta.ttl
%{_libdir}/lv2/midi.lv2/manifest.ttl
%{_libdir}/lv2/midi.lv2/midi.h
%{_libdir}/lv2/midi.lv2/midi.ttl
%{_libdir}/lv2/parameters.lv2/manifest.ttl
%{_libdir}/lv2/parameters.lv2/parameters.ttl
%{_libdir}/lv2/patch.lv2/manifest.ttl
%{_libdir}/lv2/patch.lv2/patch.h
%{_libdir}/lv2/patch.lv2/patch.ttl
%{_libdir}/lv2/port-groups.lv2/manifest.ttl
%{_libdir}/lv2/port-groups.lv2/port-groups.h
%{_libdir}/lv2/port-groups.lv2/port-groups.ttl
%{_libdir}/lv2/port-props.lv2/manifest.ttl
%{_libdir}/lv2/port-props.lv2/port-props.h
%{_libdir}/lv2/port-props.lv2/port-props.ttl
%{_libdir}/lv2/presets.lv2/manifest.ttl
%{_libdir}/lv2/presets.lv2/presets.h
%{_libdir}/lv2/presets.lv2/presets.ttl
%{_libdir}/lv2/resize-port.lv2/manifest.ttl
%{_libdir}/lv2/resize-port.lv2/resize-port.h
%{_libdir}/lv2/resize-port.lv2/resize-port.ttl
%{_libdir}/lv2/state.lv2/manifest.ttl
%{_libdir}/lv2/state.lv2/state.h
%{_libdir}/lv2/state.lv2/state.ttl
%{_libdir}/lv2/time.lv2/manifest.ttl
%{_libdir}/lv2/time.lv2/time.h
%{_libdir}/lv2/time.lv2/time.ttl
%{_libdir}/lv2/ui.lv2/lv2-ui.doap.ttl
%{_libdir}/lv2/ui.lv2/manifest.ttl
%{_libdir}/lv2/ui.lv2/ui.h
%{_libdir}/lv2/ui.lv2/ui.ttl
%{_libdir}/lv2/units.lv2/lv2-units.doap.ttl
%{_libdir}/lv2/units.lv2/manifest.ttl
%{_libdir}/lv2/units.lv2/units.h
%{_libdir}/lv2/units.lv2/units.ttl
%{_libdir}/lv2/uri-map.lv2/manifest.ttl
%{_libdir}/lv2/uri-map.lv2/uri-map.h
%{_libdir}/lv2/uri-map.lv2/uri-map.ttl
%{_libdir}/lv2/urid.lv2/manifest.ttl
%{_libdir}/lv2/urid.lv2/urid.h
%{_libdir}/lv2/urid.lv2/urid.ttl
%{_libdir}/lv2/worker.lv2/manifest.ttl
%{_libdir}/lv2/worker.lv2/worker.h
%{_libdir}/lv2/worker.lv2/worker.ttl
%{_pkgconfigdir}/*.pc
