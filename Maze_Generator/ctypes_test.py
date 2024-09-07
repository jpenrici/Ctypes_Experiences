# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_int, POINTER, Structure
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./Ctypes_Maze_Generator/lib/libmazegenerator.so')
except OSError:
    print("File custom library not found!")
    sys.exit(0)

try:
    import numpy as np
except ModuleNotFoundError:
    print("Module 'Numpy' is not installed!")
    sys.exit(0)

from Py_Maze_Generator.mazeView import Display


def test():

    rows, columns = 80, 80

    class Matrix(Structure):
        _fields_ = [('values', POINTER(POINTER(c_int))),
                    ('rows', c_int),
                    ('cols', c_int)]

    lib.mazeGenerator.argtypes = [c_int, c_int]
    lib.mazeGenerator.restype = Matrix

    lib.destroy.argtypes = [Matrix]

    result = lib.mazeGenerator(c_int(rows), c_int(columns))

    # Convert 2D array of pointers to Numpy array.
    array2D = np.zeros((result.rows, result.cols), dtype=int)
    for r in range(result.rows):
        row_ptr = result.values[r]
        array2D[r, :] = [row_ptr[c] for c in range(result.cols)]
    print(array2D)

    # View
    display = Display()
    display.height, display.width = 500, 500
    display.show(array2D, rows, columns)

    # Free up memory.
    lib.destroy(result)


if __name__ == '__main__':
    test()
