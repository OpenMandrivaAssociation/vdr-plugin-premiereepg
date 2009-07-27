
%define plugin	premiereepg
%define name	vdr-plugin-%plugin
%define version	0.2.0
%define rel	2

Summary:	VDR plugin: Parses extended Premiere EPG data
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.muempf.de/
Source:		http://www.muempf.de/down/vdr-%plugin-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin parses the extended EPG data which is send by Premiere on their
portal channels (e.g. SPORT PORTAL). This EPG data is transmitted in a
non-standard format on a non-standard PID.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
