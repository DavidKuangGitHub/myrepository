################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/CPPhowtoprogram8th_TheCppProgramming2ndedtion_HelloWCppP_MacOSX_GCC.cpp \
../src/GradeBook.cpp \
../src/Leetcode_num75.cpp 

OBJS += \
./src/CPPhowtoprogram8th_TheCppProgramming2ndedtion_HelloWCppP_MacOSX_GCC.o \
./src/GradeBook.o \
./src/Leetcode_num75.o 

CPP_DEPS += \
./src/CPPhowtoprogram8th_TheCppProgramming2ndedtion_HelloWCppP_MacOSX_GCC.d \
./src/GradeBook.d \
./src/Leetcode_num75.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


