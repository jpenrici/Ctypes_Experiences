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


def test():

    class MyStruct(Structure):
        _fields_ = [('values', POINTER(c_double)),
                    ('size', c_uint)]

    lib.myStruct.restype = MyStruct
    result = lib.myStruct()  # libcvectors.so

    values = result.values
    size = result.size

    print("Size:", size)

    for i in range(size):
        print(values[i])


if __name__ == '__main__':
    test()
