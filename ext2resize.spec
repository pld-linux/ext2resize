Summary:	An ext2 filesystem resizer
Summary(pl):	Narz�dzie do zmiany wielko�ci systemu plik�w ext2
Name:		ext2resize
Version:	1.1.14
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Vendor:		Lennert Buytenhek <buytenh@gnu.org>
Source0:	ftp://download.sourceforge.net/pub/sourceforge/ext2resize/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake.patch
URL:		http://ext2resize.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An ext2 filesystem resizer.

%description -l pl
Narz�dzie do zmiany wielko�ci systemu plik�w ext2.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf THANKS doc/HOWTO README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {*,doc/*}.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
