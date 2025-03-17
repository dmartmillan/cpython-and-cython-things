from setuptools import setup, Extension

setup(
    ext_modules=[Extension("mmap_io_extension_module", sources=["mmap_io_extension_module.c"])]
)
