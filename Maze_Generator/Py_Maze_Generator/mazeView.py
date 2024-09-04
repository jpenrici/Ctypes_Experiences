# -*- Mode: Python3; coding: utf-8; indent-tabs-mpythoode: nil; tab-width: 4 -*-

import sys

try:
    import tkinter as tk
except ModuleNotFoundError:
    print("Module 'Tkinter' is not installed!")
    sys.exit(1)


class Display:

    def __init__(self):
        # Display
        self.title = "Maze Generator"
        self.height = 300
        self.width = 300
        self.bg = 'white'
        # Grid
        self.line_color = 'blue'
        self.line_thickness = 2

    def show(self, maze: list, rows: int, columns: int):

        display = tk.Tk()
        display.title(self.title)
        display.geometry(f'{max(50, self.height)}x{max(50, self.width)}')
        # display.resizable(height=False, width=False)

        frame_padding = 5
        frame = tk.Frame(display, bg="lightgrey")
        frame.pack(fill=tk.BOTH, expand=True, padx=frame_padding, pady=frame_padding)

        canvas_width = self.width - 2 * frame_padding
        canvas_height = self.height - 2 * frame_padding

        canvas = tk.Canvas(frame, bg=self.bg, width=canvas_width, height=canvas_height)
        canvas.pack(fill=tk.BOTH, expand=True)

        rect_size = min((canvas_height - 2 * self.line_thickness) // rows,
                        (canvas_width - 2 * self.line_thickness) // columns)

        for row in range(rows):
            for col in range(columns):
                side = self._convert(maze[row][col])
                x, y = self.line_thickness + col * rect_size, self.line_thickness + row * rect_size
                left = (x, y, x, y + rect_size)
                right = (x + rect_size, y, x + rect_size, y + rect_size)
                top = (x, y, x + rect_size, y)
                bottom = (x, y + rect_size, x + rect_size, y + rect_size)
                canvas.create_line(top, fill=self.line_color if side[0] else self.bg, width=self.line_thickness)
                canvas.create_line(right, fill=self.line_color if side[1] else self.bg, width=self.line_thickness)
                canvas.create_line(bottom, fill=self.line_color if side[2] else self.bg, width=self.line_thickness)
                canvas.create_line(left, fill=self.line_color if side[3] else self.bg, width=self.line_thickness)

        display.mainloop()

    def _convert(self, value: int) -> list:

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

        # [ top, right, botton, left ]
        result = [(value & 8) != 0, (value & 4) != 0, (value & 2) != 0, (value & 1) != 0]

        return result


def main():
    matrix = [[9, 14], [10, 6]]

    app = Display()
    app.show(matrix, 2, 2)


if __name__ == '__main__':
    main()
