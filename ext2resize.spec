Summary:	An ext2 filesystem resizer
Summary(pl):	Narzêdzie do zmiany wielko¶ci systemu plików ext2
Name:		ext2resize
Version:	1.1.14
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Vendor:		Lennert Buytenhek <buytenh@gnu.org>
Source0:	ftp://download.sourceforge.net/pub/sourceforge/ext2resize/%{name}-%{version}.tar.gz
Patch0:		ext2resize-automake.patch
URL:		http://ext2resize.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An ext2 filesystem resizer.

%description -l pl
Narzêdzie do zmiany wielko¶ci systemu plików ext2.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf THANKS doc/HOWTO README \
	$RPM_BUILD_ROOT%{_mandir}/man?/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {*,doc/*}.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
