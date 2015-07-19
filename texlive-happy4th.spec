# revision 25020
# category Package
# catalog-ctan /macros/plain/contrib/happy4th
# catalog-date 2012-01-03 17:38:40 +0100
# catalog-license pd
# catalog-version 20120102
Name:		texlive-happy4th
Version:	20120102
Release:	9
Summary:	A firework display in obfuscated TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/happy4th
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/happy4th.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/happy4th.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The output PDF file gives an amusing display, as the reader
pages through it.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/happy4th/happy4th.pdf
%doc %{_texmfdistdir}/doc/plain/happy4th/happy4th.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120102-1
+ Revision: 758888
- texlive-happy4th
- texlive-happy4th

