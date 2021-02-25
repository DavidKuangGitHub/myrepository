################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../src/Class7cpp.cpp \
../src/Solution_cppSourcefile.cpp \
../src/fig02_01.cpp \
../src/hw_cpp_project_MacOSX_GCC.cpp \
../src/lf_CPP_howtoprogram_cppsourcefilecanbefoundwithmain_method_Jul3rd_2019.cpp 

OBJS += \
./src/Class7cpp.o \
./src/Solution_cppSourcefile.o \
./src/fig02_01.o \
./src/hw_cpp_project_MacOSX_GCC.o \
./src/lf_CPP_howtoprogram_cppsourcefilecanbefoundwithmain_method_Jul3rd_2019.o 

CPP_DEPS += \
./src/Class7cpp.d \
./src/Solution_cppSourcefile.d \
./src/fig02_01.d \
./src/hw_cpp_project_MacOSX_GCC.d \
./src/lf_CPP_howtoprogram_cppsourcefilecanbefoundwithmain_method_Jul3rd_2019.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


