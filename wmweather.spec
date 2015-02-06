%define name	wmweather
%define version	2.4.4
%define release 9

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
BuildRequires:  xmessage
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

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/*
%config(noreplace) %_sysconfdir/wmweather.conf
%{_mandir}/man1/*



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.4-8mdv2011.0
+ Revision: 615457
- the mass rebuild of 2010.1 packages

* Fri Nov 13 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.4.4-7mdv2010.1
+ Revision: 465847
- Don't require X11R6-contrib. Replace for xmessage.

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 2.4.4-6mdv2010.0
+ Revision: 434938
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 2.4.4-5mdv2009.0
+ Revision: 262096
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.4.4-4mdv2009.0
+ Revision: 256272
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.4.4-2mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 07 2007 Austin Acton <austin@mandriva.org> 2.4.4-2mdv2008.0
+ Revision: 49554
- rebuild for new libcurl
- drop menu entry

  + Jérôme Soyer <saispo@mandriva.org>
    - New release 2.4.4


* Mon Apr 10 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.4.3-2mdk
- Add BuildRequires
- use mkrel

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 2.4.3-1mdk
- decapitalize name
- 2.4.3
- new URL
- fix buildrequires

* Mon Jun 07 2004 Austin Acton <austin@mandrake.org> 1.31-1mdk
- initial package

