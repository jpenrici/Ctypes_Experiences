# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_char_p, c_double
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./libsmath/lib/libsmath.so')
except OSError:
    print("File 'libsmath.so' not found!")
    sys.exit(0)


def add(first, second):
    lib.add.restype = c_double
    lib.add.argtypes = [c_double, c_double]
    result = lib.add(first, second)
    lib.add.restype = None
    return result


def subtract(first, second):
    lib.subtract.restype = c_double
    lib.subtract.argtypes = [c_double, c_double]
    result = lib.subtract(first, second)
    lib.subtract.restype = None
    return result


def multiply(first, second):
    lib.multiply.restype = c_double
    lib.multiply.argtypes = [c_double, c_double]
    result = lib.multiply(first, second)
    lib.multiply.restype = None
    return result


def divide(first, second):
    lib.divide.restype = c_double
    lib.divide.argtypes = [c_double, c_double]
    result = lib.divide(first, second)
    lib.divide.restype = None
    return result


def info():
    lib.info.restype = c_char_p
    result = lib.info()
    lib.info = None
    return result.decode('utf-8')


def test():

    text = info()
    print("This is a shared library C++ test ...", text)

    first = 10
    second = 20

    sum = add(first, second)
    sub = subtract(first, second)
    mult = multiply(first, second)
    div = divide(first, second)

    # Result: 30.0 -10.0 200.0 0.5
    print("{} {} {} {}\n".format(sum, sub, mult, div))


if __name__ == '__main__':
    test()
