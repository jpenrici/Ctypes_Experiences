# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_double, c_uint, Structure, POINTER
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./lib/libcvectors.so')
except OSError:
    print("File custom library not found!")
    sys.exit(0)


def test1():

    class MyStruct(Structure):
        _fields_ = [('values', POINTER(c_double)),
                    ('size', c_uint)]

    lib.myStruct.restype = MyStruct
    result = lib.myStruct()

    values = result.values
    size = result.size

    print("Size:", size)
    for i in range(size):
        print(values[i])


def test2():

    lib.sum.argtypes = [POINTER(c_double), c_uint]
    lib.sum.restype = c_double

    values = [1.1, 1.2, 1.3, 1.4, 2.2]
    values_c = (c_double * len(values))(*values)
    size = c_uint(len(values))

    print("Total: ", lib.sum(values_c, size))


if __name__ == '__main__':
    test1()
    test2()
