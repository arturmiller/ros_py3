cmake_minimum_required(VERSION 3.0.0)
project(ros_py3)

find_package(catkin REQUIRED COMPONENTS)

catkin_package(
    LIBRARIES
    CATKIN_DEPENDS
)

catkin_install_python(PROGRAMS
    src/__init__.py
    src/run.py
DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/ros_py3)
