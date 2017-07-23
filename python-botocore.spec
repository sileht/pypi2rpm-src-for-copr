# Created by pyp2rpm-3.2.2
%global pypi_name botocore

Name:           python-%{pypi_name}
Version:        1.4.42
Release:        1%{?dist}
Summary:        Low-level, data-driven core of boto 3

License:        Apache License 2.0
URL:            https://github.com/boto/botocore
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
 A lowlevel interface to a growing number of Amazon Web Services. The botocore
package is the foundation for the AWS CLI < as well as boto3 < Documentation
Documentation for botocore can be found on Read the Docs < Getting Help We use
GitHub issues for tracking bugs and feature requests and have limited bandwidth
to address them. Please use these community resources for getting help. Please
...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-jmespath
Requires:       python-dateutil
Requires:       python-docutils
%description -n python2-%{pypi_name}
 A lowlevel interface to a growing number of Amazon Web Services. The botocore
package is the foundation for the AWS CLI < as well as boto3 < Documentation
Documentation for botocore can be found on Read the Docs < Getting Help We use
GitHub issues for tracking bugs and feature requests and have limited bandwidth
to address them. Please use these community resources for getting help. Please
...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst tests/unit/response_parsing/README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Jul 23 2017 Mehdi Abaakouk <sileht@redhat.com> 1.4.42-1%{?dist}
- Use older version

* Sun Jul 23 2017 Mehdi Abaakouk <sileht@redhat.com> 1.5.86-2
- Remove doc package

* Sun Jul 23 2017 Copr dist git <copr-devel@lists.fedorahosted.org> - 1.5.86-1
- Initial package.
