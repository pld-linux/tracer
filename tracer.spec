Summary:	Finds outdated running applications in your system
Name:		tracer
Version:	0.7.5
Release:	3
License:	GPL v2+
Source0:	https://github.com/FrostyX/tracer/archive/%{name}-%{version}-1/tracer-%{version}.tar.gz
# Source0-md5:	6f3e8bba2a918f570ea6eb44db0aae09
URL:		http://tracer-package.com/
BuildRequires:	asciidoc
BuildRequires:	gettext
BuildRequires:	python3-dbus
BuildRequires:	python3-devel
BuildRequires:	python3-psutil
BuildRequires:	python3-pytest
BuildRequires:	python3-rpm
BuildRequires:	python3-six
BuildRequires:	sphinx-pdg
Requires:	python3-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tracer determines which applications use outdated files and prints
them. For special kind of applications such as services or daemons, it
suggests a standard command to restart it. Detecting whether file is
outdated or not is based on a simple idea. If application has loaded
in memory any version of a file which is provided by any package
updated since system was booted up, tracer consider this application
as outdated.

%package -n python3-%{name}
Summary:	Finds outdated running applications in your system
Requires:	python3-dbus
Requires:	python3-lxml
Requires:	python3-psutil
Requires:	python3-rpm
Requires:	python3-setuptools
Requires:	python3-six
Suggests:	python3-argcomplete

%description -n python3-%{name}
Tracer determines which applications use outdated files and prints
them. For special kind of applications such as services or daemons, it
suggests a standard command to restart it. Detecting whether file is
outdated or not is based on a simple idea. If application has loaded
in memory any version of a file which is provided by any package
updated since system was booted up, tracer consider this application
as outdated.

%prep
%setup -q -n %{name}-%{name}-%{version}-1

%build
%py3_build

%{__make} man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_datadir}/%{name}}

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/data
cp -a data/*.xml $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -p doc/build/man/%{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*
%{_datadir}/%{name}

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/tracer-*-py*.egg-info
