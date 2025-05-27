Name:           noson
Version:        2.12.10
Release:        0
Summary:        C++ library for accessing sonos devices
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/janbar/noson
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  zlib-devel

%description
C++ library for accessing sonos devices
The API supports basic features to browse music index and control playback
in any zones.

%package -n libnoson2
Summary:        C++ library for accessing sonos devices
Group:          System/Libraries

%description -n libnoson2
C++ library for accessing sonos devices
The API supports basic features to browse music index and control playback
in any zones.

%package devel
Summary:        Development files for noson library
Group:          Development/Libraries/C and C++
Requires:       libnoson2 = %{version}

%description devel
Development files for noson library. The noson library supports basic features
to browse music index and control playback in any zones.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake \
    -DCMAKE_INSTALL_FULL_LIBDIR=%{_libdir}
%make_build

%install
%make_install -C build

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n libnoson2
%license LICENSE
%doc README.md
%{_libdir}/libnoson.so.*

%files devel
%{_includedir}/noson
%{_libdir}/pkgconfig/noson.pc
%{_libdir}/cmake/noson/
%{_libdir}/libnoson.so

%changelog
