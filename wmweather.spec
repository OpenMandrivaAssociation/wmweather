%define name	wmweather
%define version	2.4.3
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
BuildRequires:	X11-devel ImageMagick curl-devel
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

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="WMWeather" longtitle="Weather docklet" section="System/Monitoring"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 wmweather-master.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 wmweather-master.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 wmweather-master.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

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
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

