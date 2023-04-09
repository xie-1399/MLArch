# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)

# 项目信息
project (CmakeTest)

# 单个文件的时候这样比较好用
#add_executable(Single TestSingle.cpp MathFunction.cpp)

# 将对应的源文件都存到某个变量名中去
#aux_source_directory(. DIR_SRCS)
#add_executable(Multi ${DIR_SRCS})

#如果出现多个目录以及多个源文件的时候
#aux_source_directory(. DIR_SRCS)
## 添加 math 子目录
#add_subdirectory(math)
#add_executable(MMulti Mulmain.cpp)
## 添加链接库
#target_link_libraries(MMulti MathFunctions)

#还可以自定义一些编译的选项,注意config.h是由.in进行生成的