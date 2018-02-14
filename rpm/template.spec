Name:           ros-kinetic-app-manager
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS app_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/app_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-roslaunch
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rosunit
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-rosgraph
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rosunit

%description
app_manager

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Feb 14 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.0.5-0
- Autogenerated by Bloom

