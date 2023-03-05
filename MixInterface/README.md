### Python C++胶水

------

这里主要介绍两种Python C++对应的接口

#### （1）Pybind 11

这里暂时省略如何去安装环境，这里直接上一个简单的例子，如定义一个

```
//example.cpp
#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
m.doc() = "pybind11 example plugin"; // optional module docstring

m.def("add", &add, "A function that adds two numbers");
}
```

然后需要在终端进行编译

```
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)
```

这样就会形成一个.so文件，然后就可以在对应的库文件里面去调用啦 ❀❀❀

后续一些语法对应可参考：[First steps - pybind11 documentation](https://pybind11.readthedocs.io/en/stable/basics.html)

#### （2）Cython

Cython可以完成一个非常优秀的过程，主要包括两个部分：

（1）`.pyx`文件由 Cython 编译为`.c`文件，它含有 Python 扩展模块的代码

（2）`.c`文件由 C 编译器编译为`.so`文件（或 Windows 上的`.pyd`），可直接被`import`引入到 一个Python会话中. Distutils 或 setuptools 负责这部分。虽然 Cython 可以在某些情况下为你调用它们，这样实现的函数就会更加快啦

比如现在有一个pyx文件

```py
#Hello.pyx
def say_hello_to(name):
    print("Hello %s!" % name)
```

然后有一个对应的setup.py脚本

```py
#setup.py
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello world app',
      ext_modules=cythonize("hello.pyx"))
```

```
#运行对应的脚本
python setup.py build_ext --inplace
```

这样就可以在python库里面去调用啦 ❀❀❀（注意这里很有可能只在build下生成对应的.so文件，需要去移动.so文件）

更多关于Cython的语法说明：[构建 Cython 代码 (apachecn.org)](https://cython.apachecn.org/#/docs/5)

