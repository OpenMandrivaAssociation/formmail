%define name	formmail
%define version	3.14m1
%define release	%mkrel 2

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


