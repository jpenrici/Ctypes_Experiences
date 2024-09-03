# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

# Maze Generator
# Reference: Wilson's Loop Erased Random Walk Algorithm

import random


class MazeGenerator:

    def __init__(self, rows: int, columns: int):

        # Number of lines.
        self.rows = rows
        # Number of columns.
        self.columns = columns

        # Maze is a two-dimensional list where the binary flag represents:
        # 0: All walls closed.
        # 1: Left wall open.
        # 2: Bottom wall open.
        # 4: Right wall open.
        # 8: Top wall open.
        # 6 (2 + 4): Right wall and bottom wall open.
        # 9 (8 + 1): Top wall and left wall open.
        # 10 (8 + 2): Top wall and bottom wall open.
        # 12 (8 + 4): Top wall and right wall open.
        #
        # Detail:
        # 0000 : Zero (Closed), One (Open)
        # ||||__ Left Wall
        # |||___ Bottom Wall
        # ||____ Right Wall
        # |_____ Top Wall

        self.maze = [[0] * columns for _ in range(rows)]

    def generate(self) -> list:

        # Controllers.
        visited = set()
        unvisited = [(row, col) for col in range(self.columns) for row in range(self.rows)]

        # Initialize.
        current = unvisited.pop(random.randint(0, len(unvisited) - 1))
        visited.add(current)

        # Build.
        while unvisited:
            path = []
            start = unvisited[random.randint(0, len(unvisited) - 1)]

            # Walk.
            while start not in visited:
                path.append(start)
                direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  # right, down, left, up
                next_cell = (start[0] + direction[0], start[1] + direction[1])

                if 0 <= next_cell[0] < self.rows and 0 <= next_cell[1] < self.columns:
                    # Update cell.
                    start = next_cell
                else:
                    # Protect the boundaries.
                    start = path.pop()

                if start in path:
                    # Remove loop.
                    path = path[:path.index(start) + 1]

            # Update and clean.
            for cell in path:
                if cell in unvisited:
                    unvisited.remove(cell)
                    visited.add(cell)

            # Remove walls.
            for i in range(len(path) - 1):
                self._remove_wall(path[i], path[i + 1])

        return self.maze

    def _remove_wall(self, current: tuple, next_cell: tuple):
        row_diff = next_cell[0] - current[0]
        col_diff = next_cell[1] - current[1]

        if row_diff == 1:
            self.maze[current[0]][current[1]] |= 2  # 0010 : Remove bottom wall
            self.maze[next_cell[0]][next_cell[1]] |= 8  # 1000 : Remove top wall
        elif row_diff == -1:
            self.maze[current[0]][current[1]] |= 8  # 1000 : Remove top wall
            self.maze[next_cell[0]][next_cell[1]] |= 2  # 0010 : Remove bottom wall
        elif col_diff == 1:
            self.maze[current[0]][current[1]] |= 4  # 0100 : Remove right wall
            self.maze[next_cell[0]][next_cell[1]] |= 1  # 0001 : Remove left wall
        elif col_diff == -1:
            self.maze[current[0]][current[1]] |= 1   # 0001 : Remove left wall
            self.maze[next_cell[0]][next_cell[1]] |= 4  # 0100 : Remove right wall


def test():
    maze = MazeGenerator(10, 10)
    result = maze.generate()
    print(result)


if __name__ == '__main__':
    test()
