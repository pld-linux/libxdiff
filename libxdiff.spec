Summary:	Create diffs/patches for text/binary files
Summary(pl):	Tworzenie diffów/³at dla plików tekstowych i binarnych
Name:		libxdiff
Version:	0.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.xmailserver.org/%{name}-%{version}.tar.gz
# Source0-md5:	df55fb2e5b6ab1478412dde02379221c
Patch0:		%{name}-shared.patch
URL:		http://www.xmailserver.org/xdiff-lib.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LibXDiff library implements basic and yet complete functionalities
to create file differences/patches to both binary and text files. It
uses memory files as file abstraction to achieve both performance and
portability. For binary files, it implements (with some modification)
the algorithm described in "File System Support for Delta Compression"
by Joshua P. MacDonald. For text files, it follows directives described
in "An O(ND) Difference Algorithm and Its Variations" by Eugene W.
Myers. Memory files used by the library are basically a collection of
buffers that store the file content.

%description -l pl
Biblioteka LibXDiff ma zaimplementowan± podstawow± i prawie kompletn±
funkcjonalno¶æ do tworzenia plików ró¿nicowych/³atek zarówno dla
plików binarnych jak i tekstowych. Wykorzystuje pliki pamiêciowe w
celu uzyskania zarówno wydajno¶ci, jak i przeno¶no¶ci. Dla plików
binarnych wykorzystuje (z drobnymi modyfikacjami) algorytm opisany w
ksi±¿ce "Wsparcie Systemu Plików dla Kompresji Delta" autorstwa Joshuy
P. Macdonalda. Dla plików tekstowych postêpuje zgodnie z zaleceniami
opisanymi w "Algorytm ró¿nicowy O(ND) i jego wariacje" autorstwa
Eugene W. Myers. Pliki pamiêciowe u¿yte w bibliotece s± w zasadzie
kolekcj± buforów przechowuj±cych zawarto¶æ pliku.

%package devel
Summary:	Header files for libxdiff library
Summary(pl):	Pliki nag³ówkowe biblioteki libxdiff
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libxdiff library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libxdiff.

%package static
Summary:	Static libxdiff library
Summary(pl):	Statyczna biblioteka libxdiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libxdiff library.

%description static -l pl
Statyczna biblioteka libxdiff.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/xdiff.h
%{_mandir}/man3/xdiff.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
