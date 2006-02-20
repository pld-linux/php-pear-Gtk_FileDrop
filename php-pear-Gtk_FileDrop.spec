%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	FileDrop
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Make Gtk widgets accept file drops
Summary(pl):	%{_pearname} - obs³uga upuszczania plików w wid¿etach Gtk
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8c2d69f40ce3408f46cbd5dd86aad1f1
URL:		http://pear.php.net/package/Gtk_FileDrop/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear-MIME_Type >= 1.0.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(FileDrop_testcase.php)'

%description
A class which makes it easy to make a GtkWidget accept the dropping of
files or folders.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa u³atwia obs³ugiwanie upuszczania plików lub folderów w
wid¿etach GtkWidget.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
