from setuptools import setup, Extension

setup(
    ext_modules=[Extension("count_module", ["count_module.c"])]
)
