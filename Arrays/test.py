# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_int, POINTER
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./lib/libarrays.so')
except OSError:
    print("File 'libarrays.so' not found!")
    sys.exit(0)


def test():
    lib.myarray.restype = POINTER(c_int)
    array_ptr = lib.myarray()
    array_size = 10

    myarray = [array_ptr[i] for i in range(array_size)]
    print(myarray)

    lib.myarray.restype = None


if __name__ == '__main__':
    test()
