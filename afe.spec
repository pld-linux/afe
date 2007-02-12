#
# TODO: add icon
#
Summary:	Another (PSF) Font Editor
Summary(pl.UTF-8):	afe (jeszcze jeden edytor fontów PSF)
Name:		afe
Version:	20020901
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.mat.uni.torun.pl/~witek/%{name}-%{version}.src.tar.bz2
# Source0-md5:	fb82267c1f0fd347c189a40595f3b430
Source1:	%{name}.desktop
Requires:	/usr/bin/wish
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afe is simple PSF font editor written in Tcl/Tk. Editing many fonts
with afe is very easy.

%description -l pl.UTF-8
Afe to prosty edytor fontów PSF napisany w Tcl/Tk.  Pozwala na pracę
z wieloma fontami równocześnie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
