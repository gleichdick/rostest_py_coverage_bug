from distutils.core import setup

from catkin_pkg.python_setup import generate_distutils_setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

d = generate_distutils_setup()
d["package_dir"] = {"": "src"}
d["packages"] = ["rostest_py_coverage_bug"]

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension(
        "rostest_py_coverage_bug.python_example",
        ["src/main.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", d["version"])],
    ),
]
d["ext_modules"] = ext_modules
d["cmdclass"] = {"build_ext": build_ext}
# d["zip_safe"] = False

setup(**d)
