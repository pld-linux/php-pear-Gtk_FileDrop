%include	/usr/lib/rpm/macros.php
%define		_class		Gtk
%define		_subclass	FileDrop
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Make Gtk widgets accept file drops
Summary(pl):	%{_pearname} - obs³uga upuszczania plików w wid¿etach Gtk
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9b17671c000669556aeef50e4ce9e3b1
URL:		http://pear.php.net/package/Gtk_FileDrop/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class which makes it easy to make a GtkWidget accept the dropping of
files or folders.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa u³atwia obs³ugiwanie upuszczania plików lub folderów w
wid¿etach GtkWidget.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,examples}
%{php_pear_dir}/%{_class}/*.php
