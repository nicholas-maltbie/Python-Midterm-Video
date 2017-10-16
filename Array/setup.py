from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("copylist", ["arraymodule.cpp", "Array.cpp"])

setup(name = "copylist", ext_modules=[extension_mod])
