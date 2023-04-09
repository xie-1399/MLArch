cmake_minimum_required (VERSION 2.8)

# 项目信息
project (define)

#增加版本号的信息
set (Define_VERSION_MAJOR 1)
set (Define_VERSION_MINOR 0)


set(CMAKE_INCLUDE_CURRENT_DIR ON)
#
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
# 是否使用自己的 MathFunctions 库
option (USE_MYMATH
        "Use provided math implementation" ON)

# 加入一个配置头文件，用于处理 CMake 对源码的设置
configure_file (
        "${PROJECT_SOURCE_DIR}/config.h.in"
        "${PROJECT_BINARY_DIR}/config.h"
)

# 是否加入 MathFunctions 库
if (USE_MYMATH)
    include_directories ("${PROJECT_SOURCE_DIR}/math")
    add_subdirectory (math)
    set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 指定生成目标
add_executable (Define ${DIR_SRCS})
target_link_libraries (Define  ${EXTRA_LIBS})
install (TARGETS Define DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/config.h"
        DESTINATION include)

# 启用测试
enable_testing()

# 测试程序是否成功运行
add_test (test_run Define 5 2)

# 测试帮助信息是否可以正常提示
add_test (test_usage Define)
set_tests_properties (test_usage
        PROPERTIES PASS_REGULAR_EXPRESSION "Usage: .* base exponent")

# 测试 5 的平方
add_test (test_5_2 Define 5 2)
set_tests_properties (test_5_2
        PROPERTIES PASS_REGULAR_EXPRESSION "is 25")

# 测试 10 的 5 次方
add_test (test_10_5 Define 10 5)
set_tests_properties (test_10_5
        PROPERTIES PASS_REGULAR_EXPRESSION "is 100000")

# 测试 2 的 10 次方
add_test (test_2_10 Define 2 10)
set_tests_properties (test_2_10
        PROPERTIES PASS_REGULAR_EXPRESSION "is 1024")

#如果需要生成安装包,需要构建一个CPack安装包
include (InstallRequiredSystemLibraries)
set (CPACK_RESOURCE_FILE_LICENSE
        "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${Define_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${Define_VERSION_MINOR}")
include (CPack)