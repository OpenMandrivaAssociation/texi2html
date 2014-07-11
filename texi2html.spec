Name:           texi2html
Version:        1.82
Release:        13
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
%{configure2_5x} --build=%{_arch}-mandriva-linux-gnu
%{make}

%install
%{makeinstall}

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


%changelog
* Mon Apr 11 2011 Paulo Andrade <pcpa@mandriva.com.br> 0:1.82-4mdv2011.0
+ Revision: 652733
- Rebuild obsoleting provides of tetex-texi2html

* Tue Mar 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 0:1.82-3
+ Revision: 647549
- Obsolete tetex-texi2html

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0:1.82-2mdv2010.0
+ Revision: 445418
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0:1.82-1mdv2009.1
+ Revision: 332990
- New upstream release

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0:1.78-7mdv2009.0
+ Revision: 261510
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0:1.78-6mdv2009.0
+ Revision: 254401
- rebuild

* Sun Jan 20 2008 Anssi Hannula <anssi@mandriva.org> 0:1.78-4mdv2008.1
+ Revision: 155159
- match texlive changes

* Thu Jan 17 2008 Anssi Hannula <anssi@mandriva.org> 0:1.78-3mdv2008.1
+ Revision: 154162
- do not obsolete tetex as per texlive pkgs
- add obsolete_tetex switch to mimic texlive

* Fri Jan 11 2008 Anssi Hannula <anssi@mandriva.org> 0:1.78-2mdv2008.1
+ Revision: 147914
- versionize obsoletes

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jun 20 2007 David Walluck <walluck@mandriva.org> 0:1.78-1mdv2008.0
+ Revision: 41759
- Import texi2html



* Wed Jun 13 2007 David Walluck <walluck@mandriva.org> 0:1.78-1mdv2008.0
- release
