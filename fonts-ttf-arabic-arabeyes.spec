%define name fonts-ttf-arabic-arabeyes
%define name_orig	ae_fonts
%define version 2.0
%define release %mkrel 10
%define fontdir	fonts/TTF/arabic/arabeyes

Name:		%{name}
Summary:	Arabic TrueType fonts
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		System/Fonts/True type
Source:		http://prdownloads.sourceforge.net/arabeyes/%{name_orig}_%{version}.tar.bz2
URL:		http://www.arabeyes.org/project.php?proj=Khotot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
Buildrequires: 	mkfontscale
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by arabeyes.org.

%prep
%setup -n %{name_orig}_%version -q

%build

%install
rm -rf %buildroot

mkdir -p %buildroot/%_datadir/%fontdir
cp */*.ttf %buildroot/%_datadir/%fontdir

pushd %buildroot/%_datadir/%fontdir
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic-arabeyes:pri=50

%post
touch %_datadir/fonts/TTF

%clean
rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc README ChangeLog
%dir %_datadir/%fontdir
%_datadir/%fontdir/*
%_sysconfdir/X11/fontpath.d/ttf-arabic-arabeyes:pri=50



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-9mdv2011.0
+ Revision: 675406
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-8
+ Revision: 675170
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0-7
+ Revision: 664319
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 2.0-6mdv2011.0
+ Revision: 605824
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.0-5mdv2010.1
+ Revision: 494117
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.0-4mdv2009.1
+ Revision: 351035
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0-3mdv2009.0
+ Revision: 220855
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0-2mdv2008.1
+ Revision: 170831
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Funda Wang <fwang@mandriva.org> 2.0-1mdv2008.1
+ Revision: 139777
- New version 2.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1-4mdv2008.0
+ Revision: 48735
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:10:03 (52881)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 20:57:18 (52783)
- import fonts-ttf-arabic-arabeyes-1.1-2mdk

* Fri Feb 03 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1-2mdk
- Don't package fonts.cache-2 file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)
- Remove dependency on freetype, this is old stuff

* Thu Aug 05 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-1mdk
- fix rpmlint warnings
- do not use subsheels b/c they hide errors
- initial build (Munzir Taha <munzirtaha@newhorizons.com.sa>)

