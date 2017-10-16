from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("mergesortLL", ["mergesortLLmodule.cpp", "MergeSortLL.cpp"])

setup(name = "mergesortLL", ext_modules=[extension_mod])
