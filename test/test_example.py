#!/usr/bin/env python
from rostest_py_coverage_bug import mymodule
import unittest
PKG = "rostest_py_coverage_bug"


class TestPythonExample(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(mymodule.foo(3, 4), 7)


if __name__ == "__main__":
    import rostest
    rostest.rosrun(PKG, 'test_foo', TestPythonExample, sysargs=["--cov"])
