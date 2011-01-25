Summary:	GstRTCP - an RTSP server built on top of GStreamer
Summary(pl.UTF-8):	GstRTSP - serwer RTSP zbudowany w oparciu o GStreamera
Name:		gstreamer-rtsp
Version:	0.10.8
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-rtsp/gst-rtsp-%{version}.tar.bz2
# Source0-md5:	b511af07000595f63c3a705946221643
URL:		http://gstreamer.net/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gstreamer-devel >= 0.10.29
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.29
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
BuildRequires:	python-gstreamer-devel >= 0.10
BuildRequires:	python-pygobject-devel >= 2.11.2
Requires:	glib2 >= 1:2.10.0
Requires:	gstreamer >= 0.10.29
Requires:	gstreamer-plugins-base >= 0.10.29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GstRTSP is an RTSP server built on top of GStreamer.

%description -l pl.UTF-8
GstRTSP to serwer RTSP zbudowany w oparciu o GStreamera.

%package devel
Summary:	Header files for GstRTSPserver library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GstRTSPserver
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.10.0
Requires:	gstreamer-devel >= 0.10.29
Requires:	gstreamer-plugins-base-devel >= 0.10.29

%description devel
Header files for GstRTSPserver library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GstRTSPserver.

%package -n python-gstreamer-rtsp
Summary:	Python binding for GstRTSPserver library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki GstRTSPserver
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-gstreamer >= 0.10
Requires:	python-pygobject >= 2.11.2

%description -n python-gstreamer-rtsp
Python binding for GstRTSPserver library.

%description -n python-gstreamer-rtsp -l pl.UTF-8
Pythonowy interfejs do biblioteki GstRTSPserver.

%package -n vala-gstreamer-rtsp
Summary:	Vala binding for GstRTSPserver library API
Summary(pl.UTF-8):	Wiązanie API biblioteki GstRTSPserver dla języka Vala.
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 0.10

%description -n vala-gstreamer-rtsp
Vala binding for GstRTSPserver library API.

%description -n vala-gstreamer-rtsp -l pl.UTF-8
Wiązanie API biblioteki GstRTSPserver dla języka Vala.

%prep
%setup -q -n gst-rtsp-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
# workaround for configure bug
export PYGOBJECT_REQ=2.11.2
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gst-0.10/gst/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO docs/design/gst-rtp-server-design
%attr(755,root,root) %{_libdir}/libgstrtspserver-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstrtspserver-0.10.so.0
%{_libdir}/girepository-1.0/GstRtspServer-0.10.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstrtspserver-0.10.so
%{_libdir}/libgstrtspserver-0.10.la
%{_includedir}/gstreamer-0.10/gst/rtsp-server
%{_pkgconfigdir}/gst-rtsp-server-0.10.pc
%{_datadir}/gir-1.0/GstRtspServer-0.10.gir
# defs for python binding - move to python-gstreamer-rtsp-devel sometime?
%{_datadir}/gst-rtsp

%files -n python-gstreamer-rtsp
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/gst-0.10/gst/rtspserver.so

%files -n vala-gstreamer-rtsp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gst-rtsp-server-0.10.deps
%{_datadir}/vala/vapi/gst-rtsp-server-0.10.vapi
