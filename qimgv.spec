Name:           qimgv
Version:	1.0.2
Release:	6
Summary:        Simple Qt5 image viewer
License:        GPL
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		qimgv-1.0.2-exiv2-0.28.patch
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
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  stdc++-static-devel
BuildRequires:  ninja
# Optional, mpv needed for video support and KF5WindowSystem for better KDE support.
BuildRequires:  pkgconfig(mpv)
BuildRequires:  cmake(KF5WindowSystem)

%description
Qt5 image viewer also with video support.

%prep
%autosetup -p1
%cmake -G Ninja -DVIDEO_SUPPORT=ON -DKDE_SUPPORT=ON -DOPENCV_SUPPORT=ON

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/qimgv/player_mpv.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
