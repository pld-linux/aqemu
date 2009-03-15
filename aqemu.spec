Summary:	A QEMU GUI with a user-friendly interface
Name:		aqemu
Version:	0.7
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/aqemu/%{name}-%{version}.tar.bz2
# Source0-md5:	a9e731e6202d72fff9aa77e9d9cadc87
Patch0:		%{name}-regex.patch
URL:		http://sourceforge.net/projects/aqemu/
BuildRequires:	QtGui-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtXml-devel
BuildRequires:	libvncserver-devel >= 0.8.2
BuildRequires:	qt4-build >= 4.4.2
BuildRequires:	qt4-qmake
Requires:	qemu >= 0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AQEMU is GUI to QEMU and KVM emulators, written in Qt4. The program
have user-friendly interface and allows to set up the majority of QEMU
and KVM options.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 AQEMU.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/aqemu
%dir %{_datadir}/aqemu
%{_datadir}/aqemu/os_icons
%{_datadir}/aqemu/os_templates
%lang(ru) %{_datadir}/aqemu/Russian.qm
%{_desktopdir}/aqemu.desktop
%{_pixmapsdir}/aqemu_*.png
