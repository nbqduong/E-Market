#-------------------DEFINE ZONE----------------------#
#this library
set(LIBRARY_NAME "Puchase")
set(LIBRARY_INCLUDES "./" "${CMAKE_BINARY_DIR}/configured_files/include")

set(LIBRARY_SOURCES
        User.cpp
)
set(LIBRARY_HEADERS
        Admin.h
        Customer.h
        Seller.h
        User.h
)

# Include more libraries
set(LIBRARIES_TO_LINK pybind11::embed Python3::Python)

# Create the target
add_library(${LIBRARY_NAME} MODULE ${LIBRARY_SOURCES} ${LIBRARY_HEADERS})
target_include_directories(${LIBRARY_NAME} PUBLIC ${LIBRARY_INCLUDES})
target_link_libraries(${LIBRARY_NAME} PUBLIC ${LIBRARIES_TO_LINK})

# Set the target properties
set_target_properties(${LIBRARY_NAME} PROPERTIES PREFIX "")

# Set the suffix based on the platform
if(WIN32)
    set_target_properties(${LIBRARY_NAME} PROPERTIES SUFFIX ".pyd")  # Windows uses .pyd
elseif(UNIX)
    set_target_properties(${LIBRARY_NAME} PROPERTIES SUFFIX ".so")  # Linux/macOS use .so
endif()
