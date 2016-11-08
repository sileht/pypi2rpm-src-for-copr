%global pypi_name gabbi

Name:           python-%{pypi_name}
Version:        1.13.1
Release:        3%{?dist}
Summary:        Declarative HTTP testing library

License:        Apache-2.0
URL:            https://github.com/cdent/gabbi
Source0:        https://pypi.python.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  PyYAML
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools

Requires:       python-setuptools
Requires:       python-six
Requires:       python-pbr
Requires:       python-httplib2
Requires:       python-wsgi_intercept
Requires:       python-colorama
Requires:       python-jsonpath-rw
Requires:       python-jsonpath-rw-ext

%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{_bindir}/gabbi-run
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jul 27 2016 Mehdi Abaakouk <sileht@redhat.com> 1.13.1-3
-  Add jsonpath_rw_ext dep

* Wed Jul 27 2016 Mehdi Abaakouk <sileht@redhat.com> 1.13.1-2
-  Add jsonpath_rw dep

* Tue Jul 26 2016 Mehdi Abaakouk <sileht@redhat.com> 1.13.1-1
-  Upgrade to 1.13.1

* Thu Jul  14 2016 mpryc@redhat.com
- initial version 1.13.0
