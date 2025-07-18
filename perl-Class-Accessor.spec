#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Accessor
Summary:	Class::Accessor - automated accessor generation
Summary(pl.UTF-8):	Class::Accessor - automatyczne generowanie składowych accessor
Name:		perl-Class-Accessor
Version:	0.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1f1e5990f87cad7659b292fed7dc0407
Patch0:		%{name}-require.patch
URL:		http://search.cpan.org/dist/Class-Accessor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module automatically generates accessor/mutators for your class.

%description -l pl.UTF-8
Ten moduł automatycznie generuje składniki accessor/mutator dla klas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Accessor.pm
%{perl_vendorlib}/Class/Accessor
%{_mandir}/man3/Class::Accessor*.3pm*
