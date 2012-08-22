#sbs-git:slp/pkgs/l/lsb lsb 3.2 1eb8dfd6cc0768fd81b1d604eddd82287099af01

Name:       lsb
Summary:    LSB support for SLP
Version:    3.2
Release:    2
Group:      System/Base
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz
Provides:   /lib/lsb/init-functions

%description
Linux Standard Base 3.2

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/lsb
cp -p init-functions %{buildroot}/lib/lsb

%files
%defattr(-,root,root,-)
/lib/lsb/init-functions
