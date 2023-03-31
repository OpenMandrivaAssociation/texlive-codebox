Name:		texlive-codebox
Version:	61771
Release:	2
Summary:	Highlighted source code in a fancy box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/codebox
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codebox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/codebox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX3 package provides environments codebox and codeview
to typset with an environment body, and macros \codefile and
\cvfile to typeset programming source code from a file in a
fancy box. Starred versions of these environments and macros
are provided to add a comment at the bottom of the fancy box.
The package is based on tcolorbox, minted, and listings.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/codebox
%doc %{_texmfdistdir}/doc/latex/codebox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
