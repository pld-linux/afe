Summary:	Another (PSF) Font Editor
Summary(pl):	afe (jeszcze jeden edytor fontów PSF)
Name:		afe
Version:	20020901
Release:	1
License:	GPLv2
Group:		X11/Applications
Source0:	http://www.mat.uni.torun.pl/~witek/%{name}-%{version}.src.tar.bz2
Requires:	/usr/bin/wish
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afe is simple PSF font editor written in Tcl/Tk. Editing many fonts
with afe is very easy.

%description -l pl
Afe to prosty edytor fontów PSF napisany w Tcl/Tk.  Pozwala na pracê
z wieloma fontami równocze¶nie.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
