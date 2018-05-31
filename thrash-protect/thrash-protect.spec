Name:           thrash-protect
Version:        0.12
Release:        2%{?dist}
Summary:        Simple-Stupid user-space program protecting a linux host from thrashing

License:        GPLv3
URL:            https://github.com/tobixen/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Add some missing processes
Patch0:         %{name}-whitelist.patch

BuildArch:      noarch

BuildRequires:  python3-rpm-macros
BuildRequires:  systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
The program will on fixed intervals check if there has been a lot of
swapping since previous run, and if there are a lot of swapping, the
program with the most page faults will be temporary suspended.  This
way the host will never become so thrashed up that it won't be
possible for a system administrator to ssh into the box and fix the
problems, and in many cases the problems will resolve by themselves.


%prep
%autosetup -p1

sed -e '1s|^#!.*$|#!%{__python3}|' -i %{name}.py

sed -e 's|/usr/sbin/|%{_sbindir}/|g' -i systemd/%{name}.service

%build

%install

mkdir -p %{buildroot}%{_sbindir}
install -pm0755 %{name}.py %{buildroot}%{_sbindir}/%{name}

mkdir -p %{buildroot}%{_unitdir}
install -pm0644 systemd/%{name}.service %{buildroot}%{_unitdir}/


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service


%changelog
* Wed May 30 2018 Phantom X <megaphantomx at bol dot com dot br> - 0.12-2
- Patch to add more whitelisted processes

* Tue May 29 2018 Phantom X <megaphantomx at bol dot com dot br> - 0.12-1
- Initial spec
