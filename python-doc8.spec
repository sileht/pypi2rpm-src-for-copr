# Created by pyp2rpm-3.1.2
%global pypi_name doc8

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        2%{?dist}
Summary:        Style checker for Sphinx (or other) RST documentation

License:        UNKNOWN
URL:            https://launchpad.net/doc8
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

%description
Doc8 Doc8 is an *opinionated* style checker for rst_ (with basic
support for
plain text) styles of documentation.QuickStart ::    pip
install doc8To run
doc8 just invoke it against any doc directory::
$ doc8 coolproject/docsUsage
Command line usage ******************::
$ doc8  h    usage: doc8 [h] [config
path] [allowlongtitles] [ignore
code]                 [nosphinx] [ignorepath
path] ...

%package -n     python2-%{pypi_name}
Summary:        Style checker for Sphinx (or other) RST documentation
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-chardet
Requires:       python-docutils
Requires:       python-restructuredtext_lint >= 0.7
Requires:       python-six
Requires:       python-stevedore
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Doc8 Doc8 is an *opinionated* style checker for rst_ (with basic
support for
plain text) styles of documentation.QuickStart ::    pip
install doc8To run
doc8 just invoke it against any doc directory::
$ doc8 coolproject/docsUsage
Command line usage ******************::
$ doc8  h    usage: doc8 [h] [config
path] [allowlongtitles] [ignore
code]                 [nosphinx] [ignorepath
path] ...

%package -n python-%{pypi_name}-doc
Summary:        doc8 documentation
%description -n python-%{pypi_name}-doc
Documentation for doc8

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}
%doc doc/source/readme.rst README.rst LICENSE
%{_bindir}/doc8
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Jul 26 2017 Mehdi Abaakouk <sileht@redhat.com> 0.7.0-3
- Don't create doc package

* Tue Jul 26 2016 Mehdi Abaakouk <sileht@redhat.com> 0.7.0-2%{?dist}
- Fix python-restructuredtext_lint dep name

* Mon Jul 25 2016 Mehdi Abaakouk <sileht@redhat.com> - 0.7.0-1
- Initial package.
