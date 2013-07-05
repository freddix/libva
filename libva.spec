Summary:	Video Acceleration API
Name:		libva
Version:	1.2.1
Release:        1
Source0:	http://cgit.freedesktop.org/libva/snapshot/%{name}-%{version}.tar.bz2
# Source0-md5:	b7655f9c85b4e0e0d88b12c373f456ed
License:	BSD
Group:		Libraries
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXfixes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main motivation for VAAPI (Video Acceleration API) is to enable
hardware accelerated video decode/encode at various entry-points (VLD,
IDCT, Motion Compensation etc.) for the prevailing coding standards
today (MPEG-2, MPEG-4 ASP/H.263, MPEG-4 AVC/H.264, and VC-1/VMW3).

%package devel
Summary:	Header files for libva libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libva libraries.

%package driver-dummy
Summary:	Dummy VA driver
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-dummy
Dummy VA driver.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-drivers-path=%{_libdir}/%{name}/dri
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_bindir}/avcenc
%attr(755,root,root) %{_bindir}/h264encode
%attr(755,root,root) %{_bindir}/loadjpeg
%attr(755,root,root) %{_bindir}/mpeg2vaenc
%attr(755,root,root) %{_bindir}/mpeg2vldemo
%attr(755,root,root) %{_bindir}/putsurface
%attr(755,root,root) %{_bindir}/vainfo
%attr(755,root,root) %ghost %{_libdir}/libva-drm.so.1
%attr(755,root,root) %ghost %{_libdir}/libva-glx.so.1
%attr(755,root,root) %ghost %{_libdir}/libva-tpi.so.1
%attr(755,root,root) %ghost %{_libdir}/libva-x11.so.1
%attr(755,root,root) %ghost %{_libdir}/libva.so.1
%attr(755,root,root) %{_libdir}/libva-drm.so.*.*.*
%attr(755,root,root) %{_libdir}/libva-glx.so.*.*.*
%attr(755,root,root) %{_libdir}/libva-tpi.so.*.*.*
%attr(755,root,root) %{_libdir}/libva-x11.so.*.*.*
%attr(755,root,root) %{_libdir}/libva.so.*.*.*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/dri

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libva-drm.so
%attr(755,root,root) %{_libdir}/libva-glx.so
%attr(755,root,root) %{_libdir}/libva-tpi.so
%attr(755,root,root) %{_libdir}/libva-x11.so
%attr(755,root,root) %{_libdir}/libva.so
%{_includedir}/va
%{_pkgconfigdir}/libva-drm.pc
%{_pkgconfigdir}/libva-glx.pc
%{_pkgconfigdir}/libva-tpi.pc
%{_pkgconfigdir}/libva-x11.pc
%{_pkgconfigdir}/libva.pc

%files driver-dummy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/dri/dummy_drv_video.so

