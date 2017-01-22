%global debug_package %{nil}
%global __strip /bin/true

%global pkgname Oracle_VM_VirtualBox_Extension_Pack

Name:           VirtualBox-extpack-oracle
Version:        5.1.14
Release:        1%{?dist}
Summary:        PUEL extensions for VirtualBox)

License:        PUEL
URL:            http://www.virtualbox.org/wiki/VirtualBox
Source0:        http://download.virtualbox.org/virtualbox/%{version}/%{pkgname}-%{version}.vbox-extpack

BuildRequires:  tar
Requires:       VirtualBox-server >= %{version}

%description
Support for USB 2.0 devices, VirtualBox RDP and PXE boot for Intel cards for
VirtualBox.

%prep
%autosetup -c T
tar -xzvf %{SOURCE0}


%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/virtualbox/ExtensionPacks/%{pkgname}
cp -rp * \
  %{buildroot}%{_libdir}/virtualbox/ExtensionPacks/%{pkgname}

%files
%license ExtPack-license.txt
%{_libdir}/virtualbox/ExtensionPacks/%{pkgname}


%changelog
* Wed Jan 18 2017 Phantom X <megaphantomx at bol dot com dot br> - 5.1.14-1
- new version

* Sat Jan  7 2017 Phantom X <megaphantomx at bol dot com dot br> - 5.1.12-1
- Initial spec.