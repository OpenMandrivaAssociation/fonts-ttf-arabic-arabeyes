%define name fonts-ttf-arabic-arabeyes
%define name_orig	ae_fonts
%define version 1.1
%define release %mkrel 3
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
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
Buildrequires: 	freetype-tools
Requires(post):		chkfontpath
Requires(postun):	chkfontpath
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

%post
if [ -x %_sbindir/chkfontpath ]; then
   %_sbindir/chkfontpath -q -a %_datadir/%fontdir
fi
touch %_datadir/fonts/TTF
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_sbindir/chkfontpath ] && \
   %_sbindir/chkfontpath -q -r %_datadir/%fontdir
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



