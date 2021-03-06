### CMake Configuration ########################################################
# Set minimum required CMake version.
cmake_minimum_required (VERSION 2.8)

# Add to the cmake modules path.
set (CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} 
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules)

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

                
# Platform specific link libraries.
if(WIN32)
  set (LIB "ws2_32")
  add_definitions(-D_WIN32_WINNT=0x0501)
  add_definitions(-D_SCL_SECURE_NO_WARNINGS)
endif()

### Add Sources ################################################################
# Add the base project directory.
FILE(GLOB JetduinoHeaders *.h)

install(FILES ${JetduinoHeaders} DESTINATION include/Jetduino)

### Project Settings ###########################################################
project (jetduino)

add_executable (jetduino_analog_read
                jetduino_analog_read.c
				jetduino.c)
target_link_libraries(jetduino_analog_read m)

add_executable (jetduino_analog_write
                jetduino_analog_write.c
				jetduino.c)
target_link_libraries(jetduino_analog_write m)

add_executable (jetduino_digital_read
                jetduino_digital_read.c
				jetduino.c)
target_link_libraries(jetduino_digital_read m)

add_executable (jetduino_digital_write
                jetduino_digital_write.c
				jetduino.c)
target_link_libraries(jetduino_digital_write m)

add_executable (jetduino_standard_servo
                jetduino_standard_servo.c
				jetduino.c)
target_link_libraries(jetduino_standard_servo m)
                
add_executable (jetduino_temp_read
                jetduino_temp_read.c
				jetduino.c)
target_link_libraries(jetduino_temp_read m)
                
add_executable (jetduino_ultrasonic_read
                jetduino_ultrasonic_read.c
				jetduino.c)
target_link_libraries(jetduino_ultrasonic_read m)
                
add_executable (jetduino_button
                jetduino_button.c
				jetduino.c)
target_link_libraries(jetduino_button m)
                
add_executable (jetduino_led_fade
                jetduino_led_fade.c
				jetduino.c)
target_link_libraries(jetduino_led_fade m)
                
add_executable (jetduino_dynamixel_move
                jetduino_dynamixel_move.c
				jetduino.c)
target_link_libraries(jetduino_dynamixel_move m)
                
add_executable (jetduino_dynamixel_synch_move
                jetduino_dynamixel_synch_move.c
				jetduino.c)
target_link_libraries(jetduino_dynamixel_synch_move m)
                
add_executable (jetduino_dynamixel_set_register
                jetduino_dynamixel_set_register.c
				jetduino.c)
target_link_libraries(jetduino_dynamixel_set_register m)
                

