Summary:	Ruby package manager
Summary(pl):	Zarz±dca pakietów dla jêzyka Ruby
Name:		ruby-RubyGems
Version:	0.6.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/729/rubygems-%{version}.tgz
# Source0-md5:	c4a0faa9f876ad805ae80d1396a29d97
URL:		http://borges.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%ruby_mod_ver_requires_eq
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gemdir		%{_libdir}/ruby/gems/%{ruby_version}

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%description -l pl
RubyGems to standard tworzenia i zarz±dzania zewnêtrznymi bibliotekami
dla jêzyka Ruby.

%prep
%setup -q -n rubygems-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_bindir}}

ruby -e "DESTDIR='$RPM_BUILD_ROOT'; require 'install.rb'"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ruby/gems
%dir %{_gemdir}
%dir %{_gemdir}/cache
%{_gemdir}/cache/sources-0.0.1.gem
%dir %{_gemdir}/specifications
%{_gemdir}/specifications/sources-0.0.1.gemspec
%dir %{_gemdir}/gems
%{_gemdir}/gems/sources-0.0.1/lib/sources.rb
%dir %{_gemdir}/gems/cache
%dir %{_gemdir}/gems/specifications
%dir %{_gemdir}/gems/gems
%dir %{_gemdir}/doc
