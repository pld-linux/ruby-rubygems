Summary:	Ruby package manager
Summary(pl.UTF-8):	Zarządca pakietów dla języka Ruby
Name:		ruby-RubyGems
Version:	0.8.11
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/5207/rubygems-%{version}.tgz
# Source0-md5:	aa363b428c4c1fc2e076a4ff77b957d7
URL:		http://borges.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
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

%prep
%setup -q -n rubygems-%{version}

sed -i -e "s,Gem\\.dir,'$RPM_BUILD_ROOT'+Gem.dir," post-install.rb

%build
ruby setup.rb config \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--rbdir=$RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ruby/gems/1.8

ruby setup.rb install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/rubygems
%dir %{_libdir}/ruby/gems
%dir %{_gemdir}
%dir %{_gemdir}/cache
%{_gemdir}/cache/sources-0.0.1.gem
%dir %{_gemdir}/specifications
%{_gemdir}/specifications/sources-0.0.1.gemspec
%dir %{_gemdir}/gems
%{_gemdir}/gems/sources-0.0.1/lib/sources.rb
%dir %{_gemdir}/doc
