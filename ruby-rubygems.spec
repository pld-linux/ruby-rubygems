%define		_name	%(echo %{name} | tr '[:upper:]' '[:lower:]')
Summary:	Ruby package manager
Summary(pl.UTF-8):	Zarządca pakietów dla języka Ruby
Name:		ruby-RubyGems
Version:	1.2.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://files.rubyforge.vm.bytemark.co.uk/rubygems/rubygems-%{version}.tgz
# Source0-md5:	b77a4234360735174d1692e6fc598402
Patch0:		%{name}-setup.patch
URL:		http://rubygems.org/
#BuildRequires:	rpmbuild(macros) >= 1.410
BuildRequires:	ruby-devel
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gemdir		%{_libdir}/ruby/gems/%{ruby_version}

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%description -l pl.UTF-8
RubyGems to standard tworzenia i zarządzania zewnętrznymi bibliotekami
dla języka Ruby.

%package ri
Summary:	Ruby Gem package manager ri documentation
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla menadżera pakietów Ruby
Group:	Documentation

%description ri
Ruby Gem package manager ri documentation.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla menadżera pakietów Ruby. 

%package rdoc
Summary:	Ruby Gem package manager HTML documentation
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla menadżera pakietów Ruby
Group:	Documentation

%description rdoc
Ruby Gem package manager HTML documentation.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla menadżera pakietów Ruby. 

%prep
%setup -q -n rubygems-%{version}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb \
	--vendor \
	--rdocdir=./rdoc \
	--destdir="$RPM_BUILD_ROOT"

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
%dir %{_libdir}/ruby/gems
%dir %{_gemdir}
%dir %{_gemdir}/doc
%dir %{_gemdir}/doc/rubygems-%{version}

%files ri
%defattr(644,root,root,755)
%dir %{_gemdir}/doc/rubygems-%{version}/ri
%{_gemdir}/doc/rubygems-%{version}/ri/*

%files rdoc
%defattr(644,root,root,755)
%doc rdoc/*
