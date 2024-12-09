#-------------------DEFINE ZONE----------------------#
#this library
set(LIBRARY_NAME "purchase")
set(LIBRARY_INCLUDES "./" "${CMAKE_BINARY_DIR}/configured_files/include")

set(LIBRARY_SOURCES
        Cart.cpp
        Inventory.cpp
        Product.cpp
        Shop.cpp  
)
set(LIBRARY_HEADERS
        Cart.h
        Inventory.h
        Product.h
        Shop.h
)

# Include more libraries
set(LIBRARIES_TO_LINK pybind11::embed Python3::Python common)

# Create the target
add_library(${LIBRARY_NAME} MODULE STATIC ${LIBRARY_SOURCES} ${LIBRARY_HEADERS})
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
