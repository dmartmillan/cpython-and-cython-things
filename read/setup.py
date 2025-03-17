from setuptools import setup, Extension

setup(
    ext_modules=[Extension("mmap_module", sources=["mmap_module.c"])]
)
