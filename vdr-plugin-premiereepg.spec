
%define plugin	premiereepg
%define name	vdr-plugin-%plugin
%define version	0.2.0
%define rel	3

Summary:	VDR plugin: Parses extended Premiere EPG data
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		https://www.muempf.de/
Source:		http://www.muempf.de/down/vdr-%plugin-%version.tar.gz
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 396131
- new version

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.8-7mdv2009.1
+ Revision: 359354
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-6mdv2009.0
+ Revision: 197966
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-5mdv2009.0
+ Revision: 197711
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix License tag
- add HISTORY file

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.8-4mdv2008.1
+ Revision: 145190
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.8-3mdv2008.1
+ Revision: 103185
- rebuild for new vdr

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.8-2mdv2008.0
+ Revision: 90345
- rebuild

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.0.8-1mdv2008.0
+ Revision: 81886
- 0.0.8
- adapt license tag to the new policy

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.7-6mdv2008.0
+ Revision: 50034
- rebuild for new vdr

* Fri Jun 22 2007 Anssi Hannula <anssi@mandriva.org> 0.0.7-5mdv2008.0
+ Revision: 42749
- rebuild due to buildsystem failure

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.7-4mdv2008.0
+ Revision: 42121
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.7-3mdv2008.0
+ Revision: 22772
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.7-2mdv2007.0
+ Revision: 90963
- rebuild for new vdr

* Fri Nov 03 2006 Anssi Hannula <anssi@mandriva.org> 0.0.7-1mdv2007.1
+ Revision: 76360
- 0.0.7

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-6mdv2007.1
+ Revision: 74073
- rebuild for new vdr
- Import vdr-plugin-premiereepg

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-2mdv2007.0
- rebuild for new vdr

* Tue Jul 18 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2007.0
- initial Mandriva release

