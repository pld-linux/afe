#
# TODO: add icon
#
Summary:	Another (PSF) Font Editor
Summary(pl.UTF-8):	afe (jeszcze jeden edytor fontów PSF)
Name:		afe
Version:	20080102
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://republika.pl/rkd/%{name}-%{version}.tar.bz2
# Source0-md5:	c518075962146907659afc833217b31c
Source1:	%{name}.desktop
URL:		http://rkd.republika.pl/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afe is a simple PSF font editor.

%description -l pl.UTF-8
Afe to prosty edytor fontów PSF. Pozwala na pracę z wieloma
fontami równocześnie.

%prep
%setup -q
qmake-qt4
%{__make}

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
