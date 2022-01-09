Name:           qimgv
Version:	1.0.2
Release:	2
Summary:        Simple Qt5 image viewer
License:        GPL
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(exiv2)
# As of Qimgv 0.9 OpenCV is used. We provide OpenCV 3.4.5 but for compile needed is 4.2. 
# So disable it for now, until update OpenCV to 4.X series.
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  stdc++-static-devel
BuildRequires:  ninja
# Optional, mpv needed for video support and KF5WindowSystem for better KDE support.
BuildRequires:  pkgconfig(mpv)
BuildRequires:  cmake(KF5WindowSystem)

%description
Qt5 image viewer also with video support.

%prep
%setup -q
%autopatch -p0

%build
# Needed for i686 or error "has non-ABS relocation R_386_GOTOFF against symbol '.LC11'" appear.
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%global ldflags %{ldflags} -Wl,-z,notext
%global ldflags %{ldflags} -fuse-ld=gold
%endif

%cmake -G Ninja -DVIDEO_SUPPORT=ON -DKDE_SUPPORT=ON -DOPENCV_SUPPORT=ON
%ninja_build

%install
%ninja_install -C build

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/qimgv/player_mpv.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
