# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_double, c_void_p
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./lib/libMyClass.so')
except OSError:
    print("File custom library not found!")
    sys.exit(0)


def test():

    Point = c_void_p

    Point_new = lib.create
    Point_new.argtypes = [c_double, c_double]
    Point_new.restype = Point

    Point_getX = lib.getX
    Point_getX.argtypes = [Point]
    Point_getX.restype = c_double

    Point_setX = lib.setX
    Point_setX.argtypes = [Point, c_double]

    Point_getY = lib.getY
    Point_getY.argtypes = [Point]
    Point_getY.restype = c_double

    Point_setY = lib.setY
    Point_setY.argtypes = [Point, c_double]

    Point_delete = lib.destroy
    Point_delete.argtypes = [Point]

    obj = Point_new(10, 10)
    Point_setX(obj, Point_getX(obj) + 20.1)
    Point_setY(obj, Point_getY(obj) + 20.5)
    x, y = (Point_getX(obj), Point_getY(obj))

    Point_delete(obj)

    print(x, y)


if __name__ == '__main__':
    test()
