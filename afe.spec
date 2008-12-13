#
# TODO: add icon
#
Summary:	Another (PSF) Font Editor
Summary(pl.UTF-8):	afe (jeszcze jeden edytor fontów PSF)
Name:		afe
Version:	20081211
Release:	1
License:	Public Domain
Group:		X11/Applications
Source0:	http://rkd.republika.pl/AFE/%{name}
# Source0-md5:	151af89fb919da9d3487c1c95c26c8c1
Source1:	%{name}.desktop
URL:		http://rkd.republika.pl/AFE/afe.html
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afe is a simple PSF font editor.

%description -l pl.UTF-8
Afe to prosty edytor fontów PSF. Pozwala na pracę z wieloma fontami
równocześnie.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
