Name:           texi2html
Version:        1.82
Release:        5
Epoch:          0
License:        GPL
Group:          Publishing
Summary:        Highly customizable texinfo to HTML and other formats translator
URL:            http://www.nongnu.org/texi2html/
Source0:        http://download.savannah.nongnu.org/releases/texi2html/texi2html-%{version}.tar.bz2
%if %mdkversion >= 201100
Obsoletes:	tetex-texi2html <= 1.78
%endif
BuildArch:      noarch

%description
The basic purpose of texi2html is to convert Texinfo documents into HTML,
and other formats. Configuration files written in perl provide fine degree
of control over the final output, allowing most every aspect of the final
output not specified in the Texinfo input file to be specified.

%prep
%setup -q

%build
%configure2_5x --build=%{_arch}-mandriva-linux-gnu
%make

%install
%makeinstall

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO texi2html.init
%attr(0755,root,root) %{_bindir}/texi2html
%{_datadir}/texinfo/html/texi2html.html
%{_mandir}/man*/texi2html*
%{_infodir}/texi2html.info*
%dir %{_datadir}/texi2html
%{_datadir}/texi2html/*.init
%{_datadir}/texi2html/*.texi
%dir %{_datadir}/texi2html/i18n/
%{_datadir}/texi2html/i18n/*
%dir %{_datadir}/texi2html/images/
%{_datadir}/texi2html/images/*
