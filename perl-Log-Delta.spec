#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Delta
Summary:	Log::Delta - Logging object with timing and caller information
Summary(pl):	Log::Delta - obiekt loguj±cy z informacjami o czasie i wywo³uj±cym
Name:		perl-Log-Delta
Version:	0.03
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9c422a4e9b7c6e8c7fe801b5e8649c6f
URL:		http://search.cpan.org/dist/Log-Delta/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Log::Delta is a simple Log utility with hi-resolution timing. It is
suitable for basic performance analysis.

%description -l pl
Log::Delta to proste narzêdzie do logowania z informacjami o czasie
du¿ej rozdzielczo¶ci. Nadaje siê do podstawowej analizy wydajno¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# in perl-debug package
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/debug.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/*.pm
%{_mandir}/man3/*
