from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "sudoku_solver",
        ["sudoku_solver.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name="sudoku_solver",
    ext_modules=ext_modules,
    python_requires=">=3.6",
)