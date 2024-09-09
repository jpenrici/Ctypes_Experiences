# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_int, POINTER
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./lib/libSimpleSum.so')
except OSError:
    print("File custom library not found!")
    sys.exit(0)


def test():

    # Extern C : auto sum_c(int num_numbers, const int * numbers) -> int;
    lib.sum_c.argtypes = (c_int, POINTER(c_int))  # input
    lib.sum_c.restype = c_int                     # output

    numbers = [1, 2, 3, 4, 5]
    size = len(numbers)
    array_type = c_int * size
    result = lib.sum_c(c_int(size), array_type(*numbers))

    print(numbers)
    print("Sum:", result)


if __name__ == '__main__':
    test()
