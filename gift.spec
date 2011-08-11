%define name    gift
%define lname	giFT
%define major	0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define version 0.11.8.1
%define rel	3

Summary:        Internet File Transfer
Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
License:        GPL
Group:          Networking/File transfer
URL:            http://gift.sf.net/
Source0:        %{name}-%{version}.tar.bz2
Patch0:		gift-0.11.8.1-gcc4.patch
Patch1:		gift-sformatfix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libltdl-devel
BuildRequires:	libmagick-devel
BuildRequires:	libmagic-devel
BuildRequires:	libvorbis-devel

%description
This packages containt the giFT daemon. giFT is the filesharing tool for
linux.

%package -n %{libname}
Summary:	Shared libraries for a %{name}
Group:          System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{devname}
Summary:	Header files and static library for development with %{name}
Requires: 	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel
Group: 		Development/C
Obsoletes:	%{_lib}gift0-devel < 0.11.8.1-2

%description -n %{devname}
Header files and static library for development with %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--enable-libmagic \
	--enable-perl \
	--with-Magick=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std
pushd %{buildroot}%{_bindir}
ln -sf giftd giFT
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README INSTALL NEWS TODO
%{_bindir}/*
%{_datadir}/%{lname}/*
%{_mandir}/*/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/*

