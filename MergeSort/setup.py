from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("mergesort", ["mergesortmodule.cpp", "MergeSort.cpp"])

setup(name = "mergesort", ext_modules=[extension_mod])