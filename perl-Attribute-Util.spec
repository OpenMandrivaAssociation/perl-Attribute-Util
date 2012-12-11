%define upstream_name    Attribute-Util
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Attribute interface to Memoize.pm
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Attribute/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(Memoize)
BuildArch:	noarch

%description
When used without argument, this module provides four universally
accessible attributes of general interest as follows:

* Abstract

  See the Attribute::Abstract manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.60.0-2mdv2011.0
+ Revision: 658517
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2011.0
+ Revision: 552256
- update to 1.06

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 444061
- import perl-Attribute-Util


* Thu Sep 17 2009 cpan2dist 1.05-1mdv
- initial mdv release, generated with cpan2dist
