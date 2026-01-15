%define		module	rich
Summary:	Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
Summary(pl.UTF-8):	Renderowanie wzbogaconego tekstu, tabel, pasków postępu, podświetlania składni, znaczników itp. na terminalu
Name:		python3-%{module}
Version:	14.2.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rich/
Source0:	https://files.pythonhosted.org/packages/source/r/rich/%{module}-%{version}.tar.gz
# Source0-md5:	82b63b3508472d9e8393e571d74ab1a1
URL:		https://pypi.org/project/rich/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-poetry-core >= 1.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rich is a Python library for rich text and beautiful formatting in the
terminal.

%description -l pl.UTF-8
Rich to biblioteka Pythona do wzbogaconego tekstu i ładnego
formatowania na terminalu.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
