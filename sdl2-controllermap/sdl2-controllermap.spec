Name:           sdl2-controllermap
Version:        2.0.9
Release:        1%{?dist}
Summary:        Official tool to create SDL2 Game Controller controller mappings

License:        zlib and MIT
URL:            http://www.libsdl.org
Source0:        %{url}/release/SDL2-%{version}.tar.gz

Patch0:         0001-controllermap-set-datadir-to-RPM-packaging.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(sdl2)
Requires:       SDL2%{_isa} >= %{version}


%description
%{name} is the official tool to create SDL2 Game Controller controller mappings.


%prep
%autosetup -n SDL2-%{version} -p1

sed -e 's|_RPM_DATADIR_|%{_datadir}/%{name}|g' -i test/controllermap.c


%build
gcc %{build_cflags} %{build_ldflags} $(pkg-config --cflags --libs sdl2) \
  test/controllermap.c -o %{name}


%install
mkdir -p %{buildroot}%{_bindir}
install -pm0755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}
install -pm0644 test/{axis,button,controllermap}.bmp \
  %{buildroot}%{_datadir}/%{name}/


%files
%license COPYING.txt
%doc README-SDL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Sat Mar  9 2019 Phantom X <megaphantomx at bol dot com dot br> - 2.0.9-1
- Initial spec
