Summary:	An ext2 filesystem resizer
Summary(pl):	Narzêdzie do zmiany wielko¶ci systemu plików ext2
Name:		ext2resize
Version:	1.1.17
Release:	1
License:	GPL
Group:		Applications/System
Vendor:		Lennert Buytenhek <buytenh@gnu.org>
Source0:	http://dl.sourceforge.net/ext2resize/%{name}-%{version}.tar.bz2
# Source0-md5:	439bf19d6520194ca42b942f5b7a0703
Patch0:		%{name}-automake.patch
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
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc THANKS doc/HOWTO README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
