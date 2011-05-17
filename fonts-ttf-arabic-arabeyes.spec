%define name fonts-ttf-arabic-arabeyes
%define name_orig	ae_fonts
%define version 2.0
%define release %mkrel 8
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

