%define module pdm-backend
%define oname pdm_backend

Name:		python-pdm-backend
Version:	2.5.0
Release:	1
Summary:	The build backend used by PDM that supports latest packaging standards
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pdm-backend/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
The build backend used by PDM that supports latest packaging standards

%files
%{python_sitelib}/pdm
%{python_sitelib}/%{oname}-%{version}.dist-info
