Summary:        Yerase's TNEF Stream Reader
Name:           ytnef
Epoch:          1
Version:        1.9.3
Release:        100%{?dist}
License:        GPLv2+
URL:            https://github.com/Yeraze/ytnef
Source0:        https://github.com/Yeraze/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         ytnef-pkgconfig.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  gcc
BuildRequires:  perl-generators
Requires:       libytnef%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Yerase's TNEF Stream Reader.  Can take a TNEF Stream (winmail.dat) sent from
Microsoft Outlook (or similar products) and extract the attachments, including
construction of Contact Cards & Calendar entries.

%package -n     libytnef
Summary:        TNEF Stream Reader Library

%description -n libytnef
TNEF Stream Parser Library, used by "ytnef" to decode TNEF (winmail.dat)
streams generated by Microsoft Outlook.

%package -n     libytnef-devel
Summary:        Development files for libytnef
Requires:       libytnef%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libytnef-devel
The libytnef-devel package contains libraries and header files for
developing applications that use libytnef.

%prep
%setup -q
./autogen.sh
%patch0 -p1

%build
%configure --disable-static
%make_build

%install
%make_install includedir=%{_includedir}/libytnef
find %{buildroot} -name '*.la' -delete


%files
%license COPYING
%doc README.md ChangeLog ytnef/README.ytnefprocess
%{_bindir}/*

%files -n libytnef
%doc lib/doc/recurrence.txt
%{_libdir}/*.so.*

%files -n libytnef-devel
%{_includedir}/libytnef/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libytnef.pc

%changelog
* Wed Aug 01 2018 Phantom X <megaphantomx at bol dot com dot br> - 1.9.3-100.chinfo
- 1.9.3

* Sat Apr 14 2018 Phantom X <megaphantomx at bol dot com dot br> - 1.9.2-101.chinfo
- ldconfig scriplets update

* Thu Jul 27 2017 Phantom X <megaphantomx at bol dot com dot br> - 1.9.2-100.chinfo
- Download URL
- Upstream patches
- Make rpmlint happy

* Tue Mar 28 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1:1.9.2-2
- include dir should be libytnef
- adjust pkgconfig

* Sat Mar 18 2017 Andreas Bierfert <andreas.bierfert@lowlatency.de>
- 1:1.9.2-1
- version upgrade
- fix cve rhbz#1431730
- merge ytnef/libytnef and add epoch

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.6-10
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 19 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-5
- fix location in ytnefprocess.pl

* Thu May 28 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-4
- fix perl requires

* Tue Mar 24 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-3
- Changed License to the same as libytnef-devel
- Macronify everything as possible.
- Included ChangeLog as part of the documentation.

* Fri Feb 13 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.6-2
- Rebuild for fedora 10

* Fri Mar 12 2004 Patrick <rpms@puzzled.xs4all.nl>
- Initial version

