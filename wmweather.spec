%define name	wmweather
%define version	2.4.4
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Weather docklet for WindowMaker
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.godisch.de/debian/wmweather/
License:	GPL
Group:		Graphical desktop/WindowMaker
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel curl-devel
BuildRequires:  X11R6-contrib
Provides:	wmWeather
Obsoletes:	wmWeather

%description
A Window Maker docklet to show local weather conditions.

%prep
%setup -q

%build
cd src
%configure2_5x
%make
										
%install
cd src
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/*
%config(noreplace) %_sysconfdir/wmweather.conf
%{_mandir}/man1/*

