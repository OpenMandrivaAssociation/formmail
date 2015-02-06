%define name	formmail
%define version	3.14m1
%define release	7

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Converts an HTML form submission to an email message
License:	    Apache License
Group:		    Networking/WWW
URL:		    http://nms-cgi.sourceforge.net/scripts.shtml
Source:         http://nms-cgi.sourceforge.net/%{name}_modules-%{version}.tar.bz2
BuildRequires:	rpm-mandriva-setup >= 1.23
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
NMS FormMail is a drop-in replacement for Matt Wright's FormMail script. It
converts an HTML form submission to an email message.

%prep
%setup -q -n %{name}_modules-%{version}
chmod 644 ChangeLog EXAMPLES README
find lib -type d | xargs chmod 755
find lib -type f | xargs chmod 644

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_var}/www/cgi-bin
install -d -m 755 %{buildroot}%{perl_vendorlib}

install -m 755 FormMail.pl %{buildroot}%{_var}/www/cgi-bin
cp -pr lib/* %{buildroot}%{perl_vendorlib}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc ChangeLog EXAMPLES README
%{_var}/www/cgi-bin/*
%{perl_vendorlib}/CGI




%changelog
* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 3.14m1-6mdv2010.0
+ Revision: 428856
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.14m1-5mdv2009.0
+ Revision: 245303
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.14m1-3mdv2008.1
+ Revision: 136793
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.14m1-2mdv2007.0
+ Revision: 100238
- really fix all perms issues
- fix perl modules perms

* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.14m1-1mdv2007.1
+ Revision: 100214
- Import formmail

* Tue Dec 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.14m1-1mdv2007.1
- first mdv release

