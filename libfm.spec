Summary:	libfm library
Name:		libfm
Version:	1.1.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.gz
# Source0-md5:	a5bc8b8291cf810c659bfb3af378b5de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-gio-devel
BuildRequires:	libexif-devel
BuildRequires:	libtool
BuildRequires:	menu-cache-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfm library.

%package runtime
Summary:	libfm runtime
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,postun):	shared-mime-info

%description runtime
Runtime part of libfm library.

%package devel
Summary:	Header files for libfm library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libfm
library.

%package apidocs
Summary:	libfm API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libfm API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--enable-udisks		\
	--with-gtk=2		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{tt_RU,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post runtime
%update_mime_database

%postun runtime
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libfm-gtk.so.?
%attr(755,root,root) %ghost %{_libdir}/libfm.so.?
%attr(755,root,root) %{_libdir}/libfm-gtk.so.*.*.*
%attr(755,root,root) %{_libdir}/libfm.so.*.*.*

%files runtime -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libfm-pref-apps
%{_datadir}/libfm
%{_datadir}/mime/packages/libfm.xml
%{_desktopdir}/libfm-pref-apps.desktop
%{_sysconfdir}/xdg/libfm
%{_mandir}/man1/libfm-pref-apps.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfm-gtk.so
%attr(755,root,root) %{_libdir}/libfm.so
%{_libdir}/libfm-gtk.la
%{_libdir}/libfm.la
%{_includedir}/libfm
%{_includedir}/libfm-1.0
%{_pkgconfigdir}/libfm-gtk.pc
%{_pkgconfigdir}/libfm-gtk3.pc
%{_pkgconfigdir}/libfm.pc

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

