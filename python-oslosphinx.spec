# Created by pyp2rpm-3.1.2
%global pypi_name oslosphinx

Name:           python-%{pypi_name}
Version:        4.6.0
Release:        1%{?dist}
Summary:        OpenStack Sphinx Extensions and Theme

License:        UNKNOWN
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildConflicts: sphinx = 1.3b1
BuildRequires:  python-hacking < 0.11
BuildRequires:  python-hacking >= 0.10.0
BuildRequires:  python-pbr >= 1.8
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  sphinx < 1.3
BuildRequires:  sphinx >= 1.2.1
BuildRequires:  python-sphinx

%description
  OpenStack Sphinx Extensions .. image::
https://img.shields.io/pypi/v/oslosphinx.svg     :target:
https://pypi.python.org/pypi/oslosphinx/     :alt: Latest Version..
image::
https://img.shields.io/pypi/dm/oslosphinx.svg     :target:
https://pypi.python.org/pypi/oslosphinx/     :alt: DownloadsTheme and
extension
support for Sphinx documentation from the OpenStack
project.* Free software:
...

%package -n     python2-%{pypi_name}
Summary:        OpenStack Sphinx Extensions and Theme
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pbr >= 1.6
Requires:       python-requests >= 2.10.0
Requires:       python-six >= 1.9.0
%description -n python2-%{pypi_name}
  OpenStack Sphinx Extensions .. image::
https://img.shields.io/pypi/v/oslosphinx.svg     :target:
https://pypi.python.org/pypi/oslosphinx/     :alt: Latest Version..
image::
https://img.shields.io/pypi/dm/oslosphinx.svg     :target:
https://pypi.python.org/pypi/oslosphinx/     :alt: DownloadsTheme and
extension
support for Sphinx documentation from the OpenStack
project.* Free software:
...

%package -n python-%{pypi_name}-doc
Summary:        oslosphinx documentation
%description -n python-%{pypi_name}-doc
Documentation for oslosphinx

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install


%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/ 
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Mon Jul 25 2016 Mehdi Abaakouk <sileht@redhat.com> - 4.6.0-1
- Initial package.
