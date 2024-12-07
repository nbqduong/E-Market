# #-------------------DEFINE ZONE----------------------#
# project(AddFunctionPythonBinding)
#this library
set(LIBRARY_NAME "login")
set(LIBRARY_INCLUDES "./" "${CMAKE_BINARY_DIR}/configured_files/include")

set(LIBRARY_SOURCES
        Login.cpp
        LoginBinding.cpp
)
set(LIBRARY_HEADERS
        Login.h
)

# #include more
set(LIBRARIES_TO_LINK pybind11::embed Python3::Python)

# #----------------------------------------------------#
add_library(${LIBRARY_NAME} MODULE  ${LIBRARY_SOURCES} ${LIBRARY_HEADERS})
target_include_directories(${LIBRARY_NAME} PUBLIC ${LIBRARY_INCLUDES})
target_link_libraries( ${LIBRARY_NAME} PUBLIC ${LIBRARIES_TO_LINK})
# # set_target_properties(${LIBRARY_NAME} PROPERTIES PREFIX "")

# Set the suffix based on the platform
if(WIN32)
    set_target_properties(${LIBRARY_NAME} PROPERTIES SUFFIX ".pyd")  # Windows uses .pyd
elseif(UNIX)
    set_target_properties(${LIBRARY_NAME} PROPERTIES SUFFIX ".so")  # Linux/macOS use .so
endif()



