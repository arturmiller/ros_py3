cmake_minimum_required(VERSION 3.0.0)
project(ros_py3)

find_package(catkin REQUIRED COMPONENTS)

catkin_package(
    LIBRARIES
    CATKIN_DEPENDS
)

catkin_python_setup()

catkin_install_python(PROGRAMS
    src/ros_py3/__init__.py
    src/ros_py3/run.py
DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/ros_py3)

if (CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(test/test_max.py)
endif()