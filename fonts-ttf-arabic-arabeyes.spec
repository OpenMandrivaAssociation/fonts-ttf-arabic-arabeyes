%define name fonts-ttf-arabic-arabeyes
%define name_orig	ae_fonts
%define version 1.1
%define release %mkrel 4
%define fontdir	fonts/TTF/arabic/arabeyes

Name:		%{name}
Summary:	Free Arabic TrueType fonts
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/True type
Source:		http://prdownloads.sourceforge.net/arabeyes/%{name_orig}-%{version}.tar.bz2
URL:		http://www.arabeyes.org/project.php?proj=Khotot
BuildArch:	noarch
Buildrequires: 	freetype-tools
Requires(post):		fontconfig
Requires(postun):	fontconfig
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by arabeyes.org.

%prep
%setup -n %name_orig-%version -q

%build

%install
rm -rf %buildroot

mkdir -p %buildroot/%_datadir/%fontdir
cp *.ttf %buildroot/%_datadir/%fontdir

pushd %buildroot/%_datadir/%fontdir
%_sbindir/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
%if %mdkversion < 20070
%_bindir/fc-cache . || touch fonts.cache-1
%endif
popd

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic-arabeyes:pri=50

%post
touch %_datadir/fonts/TTF
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc license.txt
%dir %_datadir/fonts/TTF/
%dir %_datadir/%fontdir
%_datadir/%fontdir/*
%_sysconfdir/X11/fontpath.d/ttf-arabic-arabeyes:pri=50

