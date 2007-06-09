#
# TODO: add icon
#
Summary:	Another (PSF) Font Editor
Summary(pl.UTF-8):	afe (jeszcze jeden edytor fontów PSF)
Name:		afe
Version:	20070609
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://republika.pl/rkd/%{name}-%{version}.tar.bz2
# Source0-md5:	19486c937061858f270bc378e3f5994a
Source1:	%{name}.desktop
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afe is a simple PSF font editor.

%description -l pl.UTF-8
Afe to prosty edytor fontów PSF. Pozwala na pracę z wieloma
fontami równocześnie.

%prep
%setup -q
QTDIR=%{_prefix}
export QTDIR
qmake
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
