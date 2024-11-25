from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "matrix_ops", # Module Name
        ["bindings.cpp"],
    ),
]

setup(
    name="matrix_ops",
    version="1.0",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext}
)