Summary:	Ruby package manager
Summary(pl.UTF-8):	Zarządca pakietów dla języka Ruby
Name:		ruby-RubyGems
Version:	1.0.1
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	http://files.rubyforge.mmmultiworks.com/rubygems/rubygems-%{version}.tgz
# Source0-md5:	0d5851084955c327ee1dc9cbd631aa5f
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

%prep
%setup -q -n rubygems-%{version}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gemdir}

ruby setup.rb \
	--root="$RPM_BUILD_ROOT"

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
%dir %{ruby_vendorlibdir}/rubygems/indexer
%{ruby_vendorlibdir}/rubygems/*/*.rb
%dir %{ruby_vendorlibdir}/rbconfig
%{ruby_vendorlibdir}/rbconfig/datadir.rb
%dir %{_libdir}/ruby/gems
%dir %{_gemdir}
