# Created by pyp2rpm-3.1.2
%global pypi_name pifpaf

Name:           python-%{pypi_name}
Version:        0.6.0
epoch:          1
Release:        1%{?dist}
Summary:        Suite of tools and fixtures to manage daemons for testing

License:        UNKNOWN
URL:            https://github.com/jd/pifpaf
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
.. image:: https://travisci.org/jd/pifpaf.png?branchmaster
:target:
https://travisci.org/jd/pifpaf     :alt: Build Status..
image::
https://badge.fury.io/py/pifpaf.svg     :target:
https://badge.fury.io/py/pifpafPifpaf is a suite of fixtures_ and a
commandline
tool that allows to start and stop daemons for a quick
throwaway usage. This is
typically useful when needing these daemons
to run ...

%package -n     python2-%{pypi_name}
Summary:        Suite of tools and fixtures to manage daemons for testing
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-cliff
Requires:       python-stevedore
Requires:       python-pbr
Requires:       python-six
Requires:       python-fixtures
Requires:       pyxattr
Requires:       python-setuptools
%description -n python2-%{pypi_name}
.. image:: https://travisci.org/jd/pifpaf.png?branchmaster
:target:
https://travisci.org/jd/pifpaf     :alt: Build Status..
image::
https://badge.fury.io/py/pifpaf.svg     :target:
https://badge.fury.io/py/pifpafPifpaf is a suite of fixtures_ and a
commandline
tool that allows to start and stop daemons for a quick
throwaway usage. This is
typically useful when needing these daemons
to run ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install
cp %{buildroot}/%{_bindir}/pifpaf %{buildroot}/%{_bindir}/pifpaf-2
ln -sf %{_bindir}/pifpaf-2 %{buildroot}/%{_bindir}/pifpaf-%{python2_version}


%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{_bindir}/pifpaf
%{_bindir}/pifpaf-2
%{_bindir}/pifpaf-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Jul 25 2016 copr-service - 0.10.3-1
- Initial package.
