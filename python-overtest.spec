# Created by pyp2rpm-3.1.2
%global pypi_name overtest

Name:           python-%{pypi_name}
Version:        0.14.0
Release:        1%{?dist}
Summary:        Suite of tools to manage daemons for testing

License:        UNKNOWN
URL:            UNKNOWN
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
  Overtest Overtest is a suite of tools that allows to start and stop
daemons
for a quick throwaway usage. This is typically useful when
needing these
daemons to run integration testing_.Supported daemons
Overtest currently
supports:* PostgreSQL_ * MySQL_ * Memcached_ *
InfluxDB_ * Etcd_ * Redis_ (with
sentinel mode) * Elasticsearch_ *
ZooKeeper_ * Gnocchi_.. _PostgreSQL:
http://postgresql.org ...

%package -n     python2-%{pypi_name}
Summary:        Suite of tools to manage daemons for testing
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
  Overtest Overtest is a suite of tools that allows to start and stop
daemons
for a quick throwaway usage. This is typically useful when
needing these
daemons to run integration testing_.Supported daemons
Overtest currently
supports:* PostgreSQL_ * MySQL_ * Memcached_ *
InfluxDB_ * Etcd_ * Redis_ (with
sentinel mode) * Elasticsearch_ *
ZooKeeper_ * Gnocchi_.. _PostgreSQL:
http://postgresql.org ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{_bindir}/overtest
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{_datarootdir}/%{pypi_name}/lib

%changelog
* Mon Jul 25 2016 copr-service - 0.14.0-1
- Initial package.
