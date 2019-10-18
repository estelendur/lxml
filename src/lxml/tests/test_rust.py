import unittest
from lxml.tests.common_imports import HelperTestCase
from cffi import FFI
import ctypes
from ctypes import c_void_p, c_uint8

lib = ctypes.cdll.LoadLibrary("../rxml/target/debug/librxml.so")
lib.say_hello.restype = c_void_p
lib.hello_free.argtypes = (c_void_p, )

class RustTestCase(HelperTestCase):
    def test_sayhello(self):
        def say_hello():
            ptr = lib.say_hello()
            try:
                str_thing = ctypes.cast(ptr, ctypes.c_char_p).value.decode('utf-8')
                return str_thing
            finally:
                lib.hello_free(ptr)

        self.assertEqual(say_hello(), "hello")

def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([unittest.makeSuite(RustTestCase)])
    return suite
