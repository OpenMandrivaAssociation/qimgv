Name:           qimgv
Version:        0.8.4
Release:        1
Summary:        Simple Qt5 image viewer
License:        GPL
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}/%{name}-%{version}.tar.gz
# Add patch to fix build issue https://github.com/easymodo/qimgv/issues/63
# https://github.com/easymodo/qimgv/commit/33cccbe76736bdb6245ba4eb6d7de50473d7b3d1
#Patch0:         qimgv0.7.1-fix-build-QImageReader-del-const.patch
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
BuildRequires:  stdc++-static-devel
BuildRequires:  ninja
# Optional, mpv needed for video support and KF5WindowSystem for better KDE support.
BuildRequires:  pkgconfig(mpv)
BuildRequires:  cmake(KF5WindowSystem)

%description
Qt5 image viewer also with video support.

%prep
%setup -q
#autopatch -p0

%build

%cmake -G Ninja -DVIDEO_SUPPORT=ON -DKDE_SUPPORT=ON
%ninja_build

%install
%ninja_install -C build

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

