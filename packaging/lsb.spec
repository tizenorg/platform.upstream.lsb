
Name:       lsb
Summary:    LSB support for SLP
Version:    3.2
Release:    2
Group:      System/Base
License:    GPLv2
Source0:    lsb_%{version}-23.1.tar.gz
Provides:   /lib/lsb/init-functions


%description
Linux Standard Base 3.2



%prep
%setup -q -n %{name}-%{version}


%build



%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/lsb
cp -p init-functions %{buildroot}/lib/lsb







%files
%defattr(-,root,root,-)
/lib/lsb/init-functions


