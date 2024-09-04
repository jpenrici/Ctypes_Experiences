# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

from Py_Maze_Generator.mazeGenerator import MazeGenerator
from Py_Maze_Generator.mazeView import Display


def test():
    rows, columns = 30, 30
    maze = MazeGenerator(rows, columns).generate()

    display = Display()
    display.height, display.width = 500, 500
    display.show(maze, rows, columns)


if __name__ == '__main__':
    test()
