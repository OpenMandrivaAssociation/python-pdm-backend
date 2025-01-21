Name:		python-pdm-backend
Version:	2.4.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pdm-backend/pdm_backend-%{version}.tar.gz
Summary:	The build backend used by PDM that supports latest packaging standards
URL:		https://pypi.org/project/pdm-backend/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
The build backend used by PDM that supports latest packaging standards

%prep
%autosetup -p1 -n pdm_backend-%{version}

%files
%{py_sitedir}/pdm
%{py_sitedir}/pdm_backend-*.*-info
