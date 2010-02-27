%define tarname rubygems
Summary:	Ruby package manager
Summary(pl.UTF-8):	Zarządca pakietów dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.3.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://files.rubyforge.vm.bytemark.co.uk/rubygems/%{pkgname}-%{version}.tgz
# Source0-md5:	a04ee6f6897077c5b75f5fd1e134c5a9
Patch0:		%{name}-setup.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-EACCES.patch
URL:		http://rubygems.org/
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-devel
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-RubyGems
Provides:	ruby-RubyGems
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

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
%setup -q -n rubygems-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

# external packages?
rm -rf ri/Config
rm -rf ri/Kernel
rm -rf ri/OpenSSL
rm -rf ri/TempIO

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}}
ruby setup.rb \
	--vendor \
	--no-rdoc \
	--no-ri \
	--destdir=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{ruby_vendorlibdir}/*.rb
%dir %{ruby_vendorlibdir}/rubygems
%{ruby_vendorlibdir}/rubygems/*.rb
%dir %{ruby_vendorlibdir}/rubygems/commands
%dir %{ruby_vendorlibdir}/rubygems/digest
%dir %{ruby_vendorlibdir}/rubygems/ext
%dir %{ruby_vendorlibdir}/rubygems/package
%dir %{ruby_vendorlibdir}/rubygems/package/tar_reader
%{ruby_vendorlibdir}/rubygems/package/tar_reader/*.rb
%{ruby_vendorlibdir}/rubygems/*/*.rb
%dir %{ruby_vendorlibdir}/rbconfig
%{ruby_vendorlibdir}/rbconfig/datadir.rb
#%%dir %{_libdir}/ruby/gems

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Gem

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
