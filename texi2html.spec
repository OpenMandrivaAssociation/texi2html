%bcond_without	external_libintl_perl
# unpackaged yet
%bcond_with		external_Unicode_EastAsianWidth	

Summary:        Highly customizable texinfo to HTML and other formats translator
Name:           texi2html
Version:        5.0
Release:        2
# GPLv2+ is for the code
# OFSFDL (Old FSF Documentation License) for the documentation
# CC-BY-SA or GPLv2 for the images
License:	GPL-2.0-or-later AND LicenseRef-OFSFDL AND (CC-BY-SA-3.0 OR GPL-2.0-only)
Group:          Publishing
URL:            https://www.nongnu.org/texi2html/
Source0:        https://download.savannah.nongnu.org/releases/texi2html/texi2html-%{version}.tar.bz2
# (upstream) <https://savannah.nongnu.org/bugs/?43456>
Patch0:		texi2html-5.0-Do-not-install-Unicode-EastAsianWidth-if-external-is-used.patch
# (upstream) <https://savannah.nongnu.org/bugs/?43457>
Patch1:		texi2html-5.0-Do-not-install-libintl-perl-if-external-is-used.patch
Patch2:		texi2html-5.0-gettext.patch
BuildRequires:	gettext-devel
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Locale::Messages)
BuildRequires:	perl(Text::Unidecode)
BuildRequires:	perl(Unicode::EastAsianWidth)

Requires:	perl(Locale::Messages)
Requires:	perl(Text::Unidecode)
Requires:	perl(Unicode::EastAsianWidth)

BuildArch:      noarch

%description
The basic purpose of texi2html is to convert Texinfo documents into HTML,
and other formats. Configuration files written in perl provide fine degree
of control over the final output, allowing most every aspect of the final
output not specified in the Texinfo input file to be specified.

%prep
%autosetup -p1

# Remove bundled modules
#rm -r lib

%build
autoreconf -fiv
%configure \
	--with-external-libintl-perl=%{?with_external_libintl_perl:yes}%{!?with_external_libintl_perl:no} \
	--with-external-Unicode-EastAsianWidth=%{?with_external_Unicode_EastAsianWidth	:yes}%{!?with_external_Unicode_EastAsianWidth:no}
%make_build

%install
%make_install

# locales 
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO %{name}.init
%{_bindir}/%{name}
%{_datadir}/texinfo/html/%{name}.html
%{_mandir}/man*/%{name}*
%{_infodir}/%{name}.info*
%{_datadir}/texinfo/init/*.init
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/i18n/
%{_datadir}/%{name}/i18n/*	
%dir %{_datadir}/%{name}/images/
%{_datadir}/%{name}/images/*
%dir %{_datadir}/%{name}/lib/
%{_datadir}/%{name}/lib/*

