%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	FileDrop
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Make Gtk widgets accept file drops
Summary(pl.UTF-8):	%{_pearname} - obsługa upuszczania plików w widżetach Gtk
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b33fa57dfcb730d66ce374852cb6a367
URL:		http://pear.php.net/package/Gtk_FileDrop/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-MIME_Type >= 1.0.0-0.beta3
Requires:	php-pear-PEAR-core >= 1:1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(FileDrop_testcase.php)'

%description
A class which makes it easy to make a GtkWidget accept the dropping of
files or folders.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa ułatwia obsługiwanie upuszczania plików lub folderów w
widżetach GtkWidget.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
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
