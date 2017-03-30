%define kmod_name aic94xx

%if %{undefined version}
%error "Missing required macro: 'version'"
%endif

%if %{undefined release}
%error "Missing required macro: 'release'"
%endif

Name:           %{kmod_name}-kmod
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        aic94xx kernel driver module
Group:          System Environment/Kernel
License:        GPL
URL:            http://github.com/pruiz/centos7-aic94xx
Source0:        aic94xx-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %kernel_module_package_buildreqs

%description
This package contains the missing aic94xx kernel module for el7+

#kernel_module_package -n %{name} default debug
%kernel_module_package -n %{kmod_name} default

%prep
%setup -c -T -a 0
mkdir builds

%build
for flavor in %flavors_to_build; do
	rm -rf builds/$flavor
	cp -r %{kmod_name} builds/$flavor
	make -C %{kernel_source $flavor} M=$PWD/builds/$flavor
done

%install
%{__rm} -rf $RPM_BUILD_ROOT

export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=extra/%{name}
for flavor in %flavors_to_build ; do
	make -C %{kernel_source $flavor} modules_install M=$PWD/builds/$flavor
done

#install -m 644 -D %{SOURCE2} $RPM_BUILD_ROOT/etc/depmod.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
