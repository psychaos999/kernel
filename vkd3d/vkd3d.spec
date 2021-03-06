%global commit 71034acc761d4095778d2734717957a54fcf82ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200514
%global with_snapshot 1

%if 0%{?with_snapshot}
%global gver .%{date}git%{shortcommit}
%endif

Name:           vkd3d
Version:        1.1
Release:        102%{?gver}%{?dist}
Summary:        Direct3D 12 to Vulkan translation library

Epoch:          1

License:        LGPLv2+
URL:            http://www.winehq.org/

%if 0%{?with_snapshot}
Source0:        https://github.com/HansKristian-Work/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://dl.winehq.org/%{name}/source/%{name}-%{version}.tar.xz
Source10:       https://dl.winehq.org/%{name}/source/%{name}-%{version}.tar.xz.sign
%endif

BuildRequires:  gcc
BuildRequires:  pkgconfig(vulkan) >= 1.2.140
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(SPIRV-Tools-shared)
BuildRequires:  spirv-headers-devel
BuildRequires:  pkgconfig(dxil-spirv-c-shared)
%if 0%{?with_snapshot}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  wine-devel
%endif

%description
The vkd3d project includes libraries, shaders, utilities, and demos for
translating D3D12 to Vulkan.


%package -n libvkd3d
Summary:        D3D12 to Vulkan translation library


%description -n libvkd3d
libvkd3d is the main component of the vkd3d project. It's a 3D graphics
library built on top of Vulkan with an API very similar to Direct3D 12.


%package -n libvkd3d-devel
Summary:        Development files for vkd3d
Requires:       libvkd3d%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}


%description -n libvkd3d-devel
Development files for vkd3d.


%package -n libvkd3d-utils
Summary:        Utility library for vkd3d


%description -n libvkd3d-utils
libvkd3d-utils contains simple implementations of various functions which
might be useful for source ports of Direct3D 12 applications.


%package -n libvkd3d-utils-devel
Summary:        Development files for libvkd3d-utils
Requires:       libvkd3d-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libvkd3d-utils%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}


%description -n libvkd3d-utils-devel
Development files for libvkd3d-utils.


%prep
%if 0%{?with_snapshot}
%autosetup -n %{name}-%{commit} -p1
autoreconf -ivf
%else
%autosetup -n %{name}-%{version} -p1
%endif


%build
%configure \
  --disable-static \
  --disable-silent-rules \
  --with-spirv-tools
%make_build


%install
%make_install

find %{buildroot} -name '*.la' -delete


%files -n libvkd3d
%license COPYING LICENSE
%doc AUTHORS README
%{_libdir}/libvkd3d.so.*
%{_libdir}/libvkd3d-shader.so.*


%files -n libvkd3d-devel
%dir %{_includedir}/vkd3d
%{_includedir}/vkd3d/vkd3d_d3d12.h
%{_includedir}/vkd3d/vkd3d_d3dcommon.h
%{_includedir}/vkd3d/vkd3d_d3d12sdklayers.h
%{_includedir}/vkd3d/vkd3d_dxgibase.h
%{_includedir}/vkd3d/vkd3d_dxgiformat.h
%{_includedir}/vkd3d/vkd3d.h
%{_includedir}/vkd3d/vkd3d_shader.h
%{_includedir}/vkd3d/vkd3d_types.h
%{_includedir}/vkd3d/vkd3d_windows.h
%{_libdir}/libvkd3d.so
%{_libdir}/libvkd3d-shader.so
%{_libdir}/pkgconfig/libvkd3d.pc
%{_libdir}/pkgconfig/libvkd3d-shader.pc


%files -n libvkd3d-utils
%{_libdir}/libvkd3d-utils.so.*


%files -n libvkd3d-utils-devel
%{_includedir}/vkd3d/vkd3d_utils.h
%{_libdir}/libvkd3d-utils.so
%{_libdir}/pkgconfig/libvkd3d-utils.pc


%changelog
* Tue May 19 2020 Phantom X <megaphantomx at bol dot com dot br> - 1:1.1-102.20200514git71034ac
- Bump

* Wed May 06 2020 Phantom X <megaphantomx at bol dot com dot br> - 1:1.1-101.20200506git0d74a13
- HansKristian snapshot
- dxil-spirv support

* Fri Jan 25 2019 Phantom X <megaphantomx at bol dot com dot br> - 1:1.1-100
- 1.1

* Sun Oct 07 2018 Phantom X <megaphantomx at bol dot com dot br> - 1.0-102.chinfo
- BR:gcc

* Fri Jun 01 2018 Phantom X <megaphantomx at bol dot com dot br> - 1.0-101.chinfo
- Sync with Fedora

* Sat May 26 2018 Phantom X <megaphantomx at bol dot com dot br> - 1.0-100.chinfo
- Initial spec
