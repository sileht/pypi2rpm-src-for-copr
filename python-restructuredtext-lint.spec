# Created by pyp2rpm-3.1.2
%global pypi_name restructuredtext-lint

Name:           python-%{pypi_name}
Version:        0.14.3
Release:        1%{?dist}
Summary:        reStructuredText linter

License:        UNLICENSE
URL:            https://github.com/twolfson/restructuredtext-lint
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
restructuredtextlint .. image::
https://travisci.org/twolfson/restructuredtextlint.png?branchmaster
:target:
https://travisci.org/twolfson/restructuredtextlint    :alt:
Build
StatusreStructuredText_ linter_This was created out of
frustration with PyPI_;
it sucks finding out your reST_ is invalid
**after** uploading it. It is being
developed in junction with a
Sublime Text_ linter... ...

%package -n     python2-%{pypi_name}
Summary:        reStructuredText linter
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-docutils >= 0.11
Requires:       python-docutils < 1.0
Requires:       python-setuptools
%description -n python2-%{pypi_name}
restructuredtextlint .. image::
https://travisci.org/twolfson/restructuredtextlint.png?branchmaster
:target:
https://travisci.org/twolfson/restructuredtextlint    :alt:
Build
StatusreStructuredText_ linter_This was created out of
frustration with PyPI_;
it sucks finding out your reST_ is invalid
**after** uploading it. It is being
developed in junction with a
Sublime Text_ linter... ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name} 
%doc README.rst UNLICENSE
%{_bindir}/restructuredtext-lint
%{_bindir}/rst-lint
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Jul 26 2016 Mehdi Abaakouk <sileht@redhat.com> - 0.14.3-1
- Initial package.
