
Name:       lsb
Summary:    LSB support for SLP
Version:    3.2
Release:    2
Group:      System/Base
License:    GPLv2
Source0:    lsb-%{version}.tar.gz
Source1001: packaging/lsb.manifest 
Provides:   /lib/lsb/init-functions


%description
Linux Standard Base 3.2



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .



%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/lsb
cp -p init-functions %{buildroot}/lib/lsb







%files
%manifest lsb.manifest
%defattr(-,root,root,-)
/lib/lsb/init-functions


