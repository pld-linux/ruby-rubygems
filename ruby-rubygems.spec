%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define ruby_gemdir	%{_libdir}/ruby/gems/%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')

Summary:	Ruby package manager
Name:	ruby-RubyGems
Version:	0.6.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/729/rubygems-%{version}.tgz
# Source0-md5:	c4a0faa9f876ad805ae80d1396a29d97
URL:		http://borges.rubyforge.org/
BuildArch:	noarch
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%prep
%setup -q -n rubygems-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_bindir}}
ruby -e "DESTDIR='$RPM_BUILD_ROOT'; require 'install.rb'"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%dir %{ruby_gemdir}
%attr(755,root,root) %{_bindir}/*
%dir %{ruby_gemdir}/cache
%{ruby_gemdir}/cache/sources-0.0.1.gem
%dir %{ruby_gemdir}/specifications
%{ruby_gemdir}/specifications/sources-0.0.1.gemspec
%dir %{ruby_gemdir}/gems
%{ruby_gemdir}/gems/sources-0.0.1/lib/sources.rb
%dir %{ruby_gemdir}/gems/cache
%dir %{ruby_gemdir}/gems/specifications
%dir %{ruby_gemdir}/gems/gems
%dir %{ruby_gemdir}/doc
