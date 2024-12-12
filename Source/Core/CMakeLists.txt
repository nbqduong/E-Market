cmake_minimum_required(VERSION 3.10)

#-------------------DEFINE ZONE----------------------#
##INFORMATION AND CONFIGURATION
project(
        "CLib"
        VERSION 1.0.0
        LANGUAGES C CXX)


# Set the C++ standard to C++11 or later
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)


# Find MySQL Connector/C++
find_package(pybind11 REQUIRED)
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
set(PYTHON_VERSION "${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}")
# Determine the platform suffix
if(WIN32)
    set(PLATFORM_SUFFIX "win_amd64")
elseif(UNIX)
    set(PLATFORM_SUFFIX "linux_x86_64")
endif()

add_subdirectory(General)
add_subdirectory(Purchase)
add_subdirectory(Login)
add_subdirectory(User)



add_executable(CLib test.cpp)
target_link_libraries(CLib PUBLIC user_include)



# Add the source code file (adjust path if needed)
# add_executable(mysql_crud_operations "Login/db_crud.cpp")

# Link MySQL Connector library to the executable
# target_link_libraries(mysql_crud_operations pybind11::embed Python3::Python)

# Specify additional linker flags (optional, based on your system)
# On Linux, you may need to link against MySQL client libraries
# target_link_libraries(mysql_crud_operations mysqlclient)
