%define upstream_name    Attribute-Util
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Attribute interface to Memoize.pm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Attribute/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Attribute::Handlers)
BuildRequires: perl(Memoize)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
When used without argument, this module provides four universally
accessible attributes of general interest as follows:

* Abstract

  See the Attribute::Abstract manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


