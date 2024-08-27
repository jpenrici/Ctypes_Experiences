# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    from ctypes import cdll, c_char_p
except ModuleNotFoundError:
    print("Module 'cytpes' is not installed!")
    sys.exit(0)

try:
    lib = cdll.LoadLibrary('./lib/libhelloworld.so')
except OSError:
    print("File 'libhelloworld.so' not found!")
    sys.exit(0)


def test():
    text = "Hello World!"

    # Specify that the argument type for the message function is c_char_p (a char pointer).
    lib.message.argtypes = [c_char_p]

    # Call the message function, encoding the text as UTF-8 bytes.
    lib.message(text.encode('utf-8'))

    # Specify that the message function does not return any value.
    lib.message.restype = None


if __name__ == '__main__':
    test()
