Summary:	an ext2 filesystem resizer
Summary(pl):	narzêdzie do zmiany wielko¶ci systemu plików ext2
Name:		ext2resize
Version:	1.0.3
Release:	1
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Copyright:	GPL
Source: 	http://www.dsv.nl/~buytenh/ext2resize/%{name}-%{version}.tar.bz2
URL:		http://www.dsv.nl/~buytenh/ext2resize/
Vendor:		Lennert Buytenhek <buytenh@dsv.nl>
BuildRoot:	/tmp/%{name}-%{version}-root

%description
an ext2 filesystem resizer

%description -l pl
narzêdzie do zmiany wielko¶ci systemu plików ext2

%prep
%setup -q -n %{name}-1.0

%build
%configure
make CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d			$RPM_BUILD_ROOT%{_sbindir}
install -s src/ext2resize	$RPM_BUILD_ROOT%{_sbindir}
gzip -9nf THANKS doc/HOWTO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {THANKS,doc/HOWTO}.gz
%attr(755, root,     root)	%{_sbindir}/*
