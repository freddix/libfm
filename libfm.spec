Summary:	libfm library
Name:		libfm
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/pcmanfm/%{name}-%{version}.tar.xz
# Source0-md5:	07d1361bc008db46b0fd4c775f5696de
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
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
%attr(755,root,root) %ghost %{_libdir}/libfm-extra.so.?
%attr(755,root,root) %ghost %{_libdir}/libfm-gtk.so.?
%attr(755,root,root) %ghost %{_libdir}/libfm.so.?
%attr(755,root,root) %{_libdir}/libfm-extra.so.*.*.*
%attr(755,root,root) %{_libdir}/libfm-gtk.so.*.*.*
%attr(755,root,root) %{_libdir}/libfm.so.*.*.*

%files runtime -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libfm-pref-apps
%attr(755,root,root) %{_bindir}/lxshortcut
%dir %{_libdir}/libfm
%dir %{_libdir}/libfm/modules
%attr(755,root,root) %{_libdir}/libfm/modules/gtk-fileprop-x-desktop.so
%attr(755,root,root) %{_libdir}/libfm/modules/gtk-fileprop-x-shortcut.so
%attr(755,root,root) %{_libdir}/libfm/modules/gtk-menu-actions.so
%attr(755,root,root) %{_libdir}/libfm/modules/gtk-menu-trash.so
%attr(755,root,root) %{_libdir}/libfm/modules/vfs-menu.so
%attr(755,root,root) %{_libdir}/libfm/modules/vfs-search.so
%{_datadir}/libfm
%{_datadir}/mime/packages/libfm.xml
%{_desktopdir}/libfm-pref-apps.desktop
%{_desktopdir}/lxshortcut.desktop
%{_sysconfdir}/xdg/libfm
%{_mandir}/man1/libfm-pref-apps.1*
%{_mandir}/man1/lxshortcut.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfm-extra.so
%attr(755,root,root) %{_libdir}/libfm-gtk.so
%attr(755,root,root) %{_libdir}/libfm.so
%{_includedir}/libfm
%{_includedir}/libfm-1.0
%{_pkgconfigdir}/libfm-gtk.pc
#%{_pkgconfigdir}/libfm-gtk3.pc
%{_pkgconfigdir}/libfm.pc

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

