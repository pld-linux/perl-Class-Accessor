%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Accessor
Summary:	%{pdir}::%{pnam} Perl module - Automated accessor generation
Summary(pl):	Modu³ Perla %{pdir}::%{pnam} - automatyczne generowanie sk³adowych accessor
Name:		perl-Class-Accessor
Version:	0.17
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-require.patch
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module automatically generates accessor/mutators for your class.

%description -l pl
Ten modu³ automatycznie generuje sk³adniki accessor/mutator dla klas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
