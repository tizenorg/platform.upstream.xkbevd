%bcond_with x

Name:           xkbevd
Version:        1.1.3
Release:        1
License:        MIT
Summary:        XKB event daemon
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xkbevd.manifest
BuildRequires:  bison
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%if !%{with x}
ExclusiveArch:
%endif

%description
The xkbevd event daemon listens for specified XKB events and executes
requested commands if they occur. The configuration file consists of
a list of event specification/action pairs and/or variable definitions.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc COPYING
%{_bindir}/xkbevd
%{_mandir}/man1/xkbevd.1%{?ext_man}

%changelog
