%define version 3.0.7
%define release 9

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global srcname distribute

Name:		luma
Version:	%{version}
Release:	%{release}%{?dist}
Summary:	LDAP Browser and administration utility
Group:		Applications/System
License:	GNU General Public License (GPL) version 2
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Vendor:		Luma devel team <luma-devel@luma.sf.net>
Packager:	Einar Uvsløkk <einar.uvslokk@linux.com>
Url:		http://luma.sf.net

BuildRequires:	python2-devel

Requires:	python >= 2.6
Requires:	python-ldap >= 2.3
Requires:	PyQt4
Requires:	python-smbpasswd
Requires:	hicolor-icon-theme

%description
Luma is an cross-platform and open soruce graphical utility for accessing and
managing data stored on LDAP enabled servers. It is written in Python, using 
PyQt4 and python-ldap. Luma supports plugins through its own plugin system. A
selection of plugins, providing useful LDAP-functionality, is includeed in the
base application.

%prep
%setup -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT

# Add plugins/browser/templates
install -d $RPM_BUILD_ROOT%{python_sitelib}/luma/plugins/browser/templates
cp -R luma/plugins/browser/templates/* \
   $RPM_BUILD_ROOT%{python_sitelib}/luma/plugins/browser/templates

# Desktop entry for luma-settings
desktop-file-validate \
	$RPM_BUILD_ROOT%{_datadir}/applications/luma.desktop  


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/luma

%{_datadir}/icons/
%{_datadir}/pixmaps/

%{_datadir}/applications/luma.desktop

%{_mandir}/man1/luma.1.gz

%{python_sitelib}/

%doc AUTHORS ChangeLog COPYING README TODO

%changelog
* Thu Jan 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 3.0.7-2
- Add ../plugins/browser/templates (#906498)
* Wed May 26 2011 Einar Uvsløkk <einar.uvslokk@linux.com> 3.0.7-1
- Updated unconsistent license statements in the sourcecode.
- Added some missing patches from the Luma 2.4 svn trunk
* Mon May 16 2011 Einar Uvsløkk <einar.uvslokk@linux.com> 3.0.6-1
- Bugfix in LumaConnectionWrapper, export fixed in Browser plugin
* Mon May 10 2011 Einar Uvsløkk <einar.uvslokk@linux.com> 3.0.6b-4
- Updated to new and improved Connection wrapper for various ldap opreations.
* Sun May 8 2011 Einar Uvsløkk <einar.uvslokk@linux.com> 3.0.6b-3
- Fixed an issue where some required html templates not was installed.
* Sun May 7 2011 Einar Uvsløkk <einar.uvslokk@linux.com> 3.0.6b-2
- Updated the i18n system.
* Fri May 6 2011 Einar Uvsløkk <einar.uvslokk@linux.com> 3.0.6b-1
- Initial rpm build for the new Luma (version 3.*) - Beta 1 Release
