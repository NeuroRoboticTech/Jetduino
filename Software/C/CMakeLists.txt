### CMake Configuration ########################################################
# Set minimum required CMake version.
cmake_minimum_required (VERSION 2.8)

# Add to the cmake modules path.
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} 
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules)

### Project Settings ###########################################################
# Set the project name.
project (Jetduino)

### Platform Settings ##########################################################
message(STATUS ${CMAKE_GENERATOR})

# GNU Compiler Settings
if (CMAKE_COMPILER_IS_GNUCXX)
  message(STATUS "Set GNU compiler project build settings.")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
endif()

# Visual Studio Specific Settings
if(MSVC)
  message(STATUS "Set MSVC compiler project build settings.")
  add_definitions(-DBOOST_ALL_NO_LIB)
  add_definitions(-D_UNICODE)
  add_definitions(-DUNICODE)
  add_definitions(-D_SCL_SECURE_NO_WARNINGS)
  STRING(REPLACE "/O2" "/Od" CMAKE_CXX_FLAGS_RELWITHDEBINFO ${CMAKE_CXX_FLAGS_RELWITHDEBINFO})   
endif()

# Windows Settings
if(WIN32)
  add_definitions(-D_WIN32_WINNT=0x0501)
endif()

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

### Build Options ##############################################################
# Setup any build options.
option (BUILD_TEST "Build the unit test for this project." ON)

### Testing Settings ###########################################################
# Enable CTest.
enable_testing ()

# Add directories for unit testing.
if (BUILD_TEST)
  # Add the local project dependency include directories.
  #include_directories (dep/FakeIt/include)
  #include_directories (dep/FakeIt/config/tpunit)
  #include_directories (dep/tpunitpp)
endif()

### Add Sources ################################################################
# Add the base project directory.
FILE(GLOB JetduinoHeaders *.h)
FILE(GLOB JetduinoSource *.cpp)

install(FILES ${JetduinoHeaders} DESTINATION include/Jetduino)

add_executable (Jeduino
                ${JetduinoSource})
                    