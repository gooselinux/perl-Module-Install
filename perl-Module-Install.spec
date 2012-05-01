Name:           perl-Module-Install
Version:        0.91
Release:        4%{?dist}
Summary:        Standalone, extensible Perl module installer
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Install/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/Module-Install-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

# Note, Makefile.PL is going to complain about having lower versions of
# certain modules than is supported. (Especially under F-10.) However, 
# all tests pass and AFAICT everything works just fine in normal usage.

BuildRequires:  perl(Archive::Tar) 
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Devel::PPPort) 
BuildRequires:  perl(ExtUtils::Install) 
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::ScanDeps)
BuildRequires:  perl(PAR::Dist) >= 0.29
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.39
BuildRequires:  perl(Test::CPAN::Meta) >= 0.07
BuildRequires:  perl(Test::Harness) >= 3.13
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(YAML::Tiny) >= 1.38
Requires:       perl(Archive::Tar)
Requires:       perl(ExtUtils::ParseXS)
Requires:       perl(Module::Build)
Requires:       perl(Module::CoreList)
Requires:       perl(Module::ScanDeps)
Requires:       perl(PAR::Dist) >= 0.29
Requires:       perl(YAML::Tiny) 
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Module::Install is a package for writing installers for CPAN (or CPAN-like)
distributions that are clean, simple, minimalist, act in a strictly correct
manner with both the ExtUtils::MakeMaker and Module::Build build systems,
and will run on any Perl installation version 5.004 or newer.

%prep
%setup -q -n Module-Install-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
rm -rf $RPM_BUILD_ROOT/blib/lib/auto/share/dist/Module-Install/dist_file.txt
%{_fixperms} $RPM_BUILD_ROOT/*
find $RPM_BUILD_ROOT%{perl_vendorlib} -type f -perm +100 -exec chmod a-x {} \;

%check
make test AUTOMATED_TESTING=1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 25 2010 Marcela Mašláňová <mmaslano@redhat.com> - 0.91-4
- change to DESTDIR
- add README
- Resolves: rhbz#543948

* Wed Dec 23 2009 Marcela Mašláňová <mmaslano@redhat.com> - 0.91-3
- dist_file.txt wasn't packaged -> removed, it's needed only for test of build
- Resolves: rhbz#550011

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.91-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.91-1
- update to 0.91
- add br on Parse::CPAN::Meta: 1.39

* Sat May 23 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.90-1
- update to 0.90 
- add br on JSON, Test::Harness (3.13)
- update br on YAML::Tiny (1.38)

* Mon May 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.87-1
- update to 0.87

* Sun Apr 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.85-1
- update to 0.85
- add BR on File::Spec

* Thu Apr 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.82-1
- update to 0.82

* Sun Mar 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.80-1
- update to 0.80 
- remove 03_autoinstall.t swizzle (now self-skipped; see RT29448)

* Fri Mar 13 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.79-1
- update to 0.79

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.77-1
- update to 0.77

* Wed Jun 04 2008 Steven Pritchard <steve@kspei.com> 0.75-1
- Update to 0.75.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 0.74-1
- Update to 0.74.
- Update versioned dependencies for File::Remove, Module::ScanDeps,
  PAR::Dist, and YAML::Tiny.
- BR Test::CPAN::Meta.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.73-1
- Update to 0.73.
- BR File::Remove.
- Drop zero-length README.

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.68-3
- disable broken test (upstream bug present)
- add Test::MinimumVersion as BR

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.68-2
- rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 0.68-1
- Update to 0.68.
- Explicitly require Archive::Tar and ExtUtils::ParseXS.

* Sun Dec 30 2007 Ralf Corsépius <rc040203@freenet.de> - 0.67-2
- BR: perl(Test::More), perl(CPAN) (BZ 419631).
- Remove TEST_POD (Unused).
- Add AUTOMATED_TESTING.
- BR: perl(Test::Pod) for AUTOMATED_TESTING.
- Adjust License-tag.

* Fri May 18 2007 Steven Pritchard <steve@kspei.com> 0.67-1
- Update to 0.67.
- BR Archive::Tar, ExtUtils::ParseXS, and YAML::Tiny.
- Add a couple more docs.

* Tue Mar 13 2007 Steven Pritchard <steve@kspei.com> 0.65-1
- Update to 0.65.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sun Sep 17 2006 Steven Pritchard <steve@kspei.com> 0.64-2
- Rebuild.

* Fri Aug 25 2006 Steven Pritchard <steve@kspei.com> 0.64-1
- Update to 0.64.
- Fix find option order.

* Thu Jun 08 2006 Steven Pritchard <steve@kspei.com> 0.63-1
- Update to 0.63.

* Mon May 08 2006 Steven Pritchard <steve@kspei.com> 0.62-2
- Fix Source0 URL.

* Sat May 06 2006 Steven Pritchard <steve@kspei.com> 0.62-1
- Update to 0.62.
- Drop executable bit from everything in vendor_perl to make rpmlint happy.

* Thu Mar 23 2006 Steven Pritchard <steve@kspei.com> 0.61-1
- Specfile autogenerated by cpanspec 1.63.
- Drop explicit BR: perl.
- Turn on TEST_POD.
