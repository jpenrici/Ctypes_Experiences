# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    import tkinter as tk
except ModuleNotFoundError:
    print("Module 'Tkinter' is not installed!")
    sys.exit(0)


class Display:

    def __init__(self):
        self.title = "Maze Generator"
        self.height = 200
        self.width = 200
        self.bg = 'blue'  # screen background
        self.rect_fill_color = 'red'
        self.rect_line_color = 'black'
        self.rect_line_stroke = 5

    def show(self, matrix: list, rows: int, columns: int):

        # Matrix is a two-dimensional list where the binary flag represents:
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

        rectangle_size = min(self.height // rows, self.width // columns)

        display = tk.Tk()
        display.title(self.title)
        display.geometry(f'{max(50, self.height)}x{max(50, self.width)}')

        canvas = tk.Canvas(display, bg=self.bg, width=self.width, height=self.height)

        for row in range(rows):
            for col in range(columns):
                side = self._convert(matrix[row][col])
                print(side)
                w, h = rectangle_size, rectangle_size
                x, y = row * w, col * w
                canvas.create_line(
                    (x, y, x, y + h), fill=self.rect_line_color if side[0] else self.bg, width=self.rect_line_stroke)
                canvas.create_line((x, y + h, x + w, y + rectangle_size),
                                   fill=self.rect_line_color if side[1] else self.bg, width=self.rect_line_stroke)
                canvas.create_line((x + w, y, x + w, y + h),
                                   fill=self.rect_line_color if side[2] else self.bg, width=self.rect_line_stroke)
                canvas.create_line(
                    (x, y, x + w, y), fill=self.rect_line_color if side[3] else self.bg, width=self.rect_line_stroke)

        canvas.pack()
        display.mainloop()

    def _convert(self, value: int) -> list:
        print(value)
        return [value & 1, value & 2, value & 4,  value & 8]  # left, down, right, up


def main():
    matrix = [[2, 0], [4, 2]]

    app = Display()
    app.show(matrix, 2, 2)


if __name__ == '__main__':
    main()
