%define		module	rich
Summary:	Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal
Summary(pl.UTF-8):	Renderowanie wzbogaconego tekstu, tabel, pasków postępu, podświetlania składni, znaczników itp. na terminalu
Name:		python3-%{module}
Version:	13.9.4
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	566d05ed481cd8add803fa9ca002720b
URL:		https://pypi.org/project/rich/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-poetry-core
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
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
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
