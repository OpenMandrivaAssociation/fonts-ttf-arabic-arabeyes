%define oname	ae_fonts
%define fontdir	fonts/TTF/arabic/arabeyes

Name:		fonts-ttf-arabic-arabeyes
Summary:	Arabic TrueType fonts
Version:	2.0
Release:	21
License:	GPLv2+
Group:		System/Fonts/True type
Url:		https://www.arabeyes.org/project.php?proj=Khotot
Source0:	http://prdownloads.sourceforge.net/arabeyes/%{oname}_%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
Buildrequires: 	mkfontscale
Provides:	fonts-ttf-arabic

%description
This Package provides Free Arabic TrueType fonts donated under the GPL license
by arabeyes.org.

%prep
%setup -qn %{oname}_%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%fontdir
cp */*.ttf %{buildroot}/%{_datadir}/%fontdir

pushd %{buildroot}/%{_datadir}/%fontdir
mkfontscale
cp fonts.scale fonts.dir
popd

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/%fontdir \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-arabic-arabeyes:pri=50

%post
touch %{_datadir}/fonts/TTF

%files
%doc README ChangeLog
%dir %{_datadir}/%fontdir
%{_datadir}/%fontdir/*
%{_sysconfdir}/X11/fontpath.d/ttf-arabic-arabeyes:pri=50

