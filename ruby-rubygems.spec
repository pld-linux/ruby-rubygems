#
# Conditional build:
%bcond_with	doc			# don't build ri/rdoc

%define pkgname rubygems
Summary:	Ruby package manager
Summary(pl.UTF-8):	Zarządca pakietów dla języka Ruby
Name:		ruby-%{pkgname}
Version:	2.6.13
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	https://rubygems.org/gems/rubygems-update-%{version}.gem
# Source0-md5:	cad98b534ae8e1d65f9a5cf00fdaa89f
Source1:	operating_system.rb
URL:		https://rubygems.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Provides:	rubygems = %{version}
Obsoletes:	ruby-RubyGems
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%description -l pl.UTF-8
RubyGems to standard tworzenia i zarządzania zewnętrznymi bibliotekami
dla języka Ruby.

%package ri
Summary:	Ruby Gem package manager ri documentation
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla menadżera pakietów Ruby
Group:		Documentation
Requires:	ruby

%description ri
Ruby Gem package manager ri documentation.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla menadżera pakietów Ruby.

%package rdoc
Summary:	Ruby Gem package manager HTML documentation
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla menadżera pakietów Ruby
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Ruby Gem package manager HTML documentation.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla menadżera pakietów Ruby.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with doc}
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

# external packages?
rm -rf ri/{*Config,Kernel,OpenSSL,TempIO}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-update-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

# Install custom operating_system.rb.
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}/rubygems/defaults
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{ruby_vendorlibdir}/rubygems/defaults

# please use system ca-certificagtes
%{__rm} -r $RPM_BUILD_ROOT%{ruby_vendorlibdir}/rubygems/ssl_certs

install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

%if %{with doc}
install -d $RPM_BUILD_ROOT{%{ruby_rdocdir}/%{name}-%{version},%{ruby_ridir}}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/gem
%attr(755,root,root) %{_bindir}/update_rubygems
#%%dir %{_libdir}/ruby/gems
%dir %{ruby_vendorlibdir}/rubygems
%{ruby_vendorlibdir}/*.rb
%{ruby_vendorlibdir}/rubygems/*.rb
%{ruby_vendorlibdir}/rubygems/commands
%{ruby_vendorlibdir}/rubygems/core_ext
%{ruby_vendorlibdir}/rubygems/defaults
%{ruby_vendorlibdir}/rubygems/ext
%{ruby_vendorlibdir}/rubygems/package
%{ruby_vendorlibdir}/rubygems/request
%{ruby_vendorlibdir}/rubygems/request_set
%{ruby_vendorlibdir}/rubygems/resolver
%{ruby_vendorlibdir}/rubygems/security
%{ruby_vendorlibdir}/rubygems/source
%{ruby_vendorlibdir}/rubygems/util
%{ruby_specdir}/rubygems-update-%{version}.gemspec

%if %{with doc}
%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Gem*

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%endif
