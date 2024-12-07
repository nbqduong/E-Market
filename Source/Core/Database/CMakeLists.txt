#-------------------DEFINE ZONE----------------------#
#this library
set(LIBRARY_NAME "database")
set(LIBRARY_INCLUDES "./" "${CMAKE_BINARY_DIR}/configured_files/include")

set(LIBRARY_SOURCES
        
)
set(LIBRARY_HEADERS
        DBPlugin.h
)

#include more
set(LIBRARIES_TO_LINK pybind11::embed Python3::Python)
# Create the Python extension module
pybind11_add_module(example ${LIBRARY_SOURCES})



#----------------------------------------------------#
# add_executable(${LIBRARY_NAME} db_crud.cpp)
add_library(${LIBRARY_NAME} STATIC ${LIBRARY_SOURCES} ${LIBRARY_HEADERS})
target_include_directories(${LIBRARY_NAME} PUBLIC ${LIBRARY_INCLUDES})
target_link_libraries( ${LIBRARY_NAME} PUBLIC ${LIBRARIES_TO_LINK})
