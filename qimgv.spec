Name:           qimgv
Version:	0.9.1
Release:	1
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
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(exiv2)
# As of Qimgv 0.9 OpenCV is used. We provide OpenCV 3.4.5 but for compile needed is 4.2. 
# So disable it for now, until update OpenCV to 4.X series.
#BuildRequires:  pkgconfig(opencv)
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

%cmake -G Ninja -DVIDEO_SUPPORT=ON -DKDE_SUPPORT=ON -DOPENCV_SUPPORT=OFF
%ninja_build

%install
%ninja_install -C build

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/libqimgv_player_mpv.so*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
