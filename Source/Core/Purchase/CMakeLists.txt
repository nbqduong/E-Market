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

#------------------- Helper Function ----------------#
function(create_library target_name type)
    add_library(${target_name} ${type} ${LIBRARY_SOURCES} ${LIBRARY_HEADERS})
    target_include_directories(${target_name} PUBLIC ${LIBRARY_INCLUDES})
    target_link_libraries(${target_name} PUBLIC ${LIBRARIES_TO_LINK})
    set_target_properties(${target_name} PROPERTIES PREFIX "")

    # Set suffix based on platform
    if(WIN32)
        set_target_properties(${target_name} PROPERTIES SUFFIX ".pyd")
    elseif(UNIX)
        set_target_properties(${target_name} PROPERTIES SUFFIX ".so")
    endif()
endfunction()

#------------------- Generate Libraries ----------------#
create_library(${LIBRARY_NAME} MODULE)
create_library(${LIBRARY_NAME}_include STATIC)
