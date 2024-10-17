Name:		texlive-happy4th
Version:	25020
Release:	2
Summary:	A firework display in obfuscated TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/happy4th
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/happy4th.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/happy4th.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
