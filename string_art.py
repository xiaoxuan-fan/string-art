# Author: Xiaoxuan
# Date: 4/29/2021
# Purpose: draw string art

from CS1.cs1lib import *

# x and y coordinates of the two ends of stick A
X1A = 25
Y1A = 50
X2A = 50
Y2A = 200

# x and y coordinates of the two ends of stick B
X1B = 350
Y1B = 180
X2B = 200
Y2B = 350

# number of strings
N = 25


# set background to black
def set_background_black():
    set_clear_color(0, 0, 0)  # black
    clear()


# set stroke color to magenta
def set_stroke_magenta():
    set_stroke_color(1, 0, 1)  # magenta


# set stroke color to cyan
def set_stroke_cyan():
    set_stroke_color(0, 1, 1)  # cyan


# draw the string art
def string_art(x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b, n):
    set_background_black()

    # draw the two sticks
    set_stroke_width(3)
    set_stroke_magenta()
    draw_line(x1a, y1a, x2a, y2a)
    draw_line(x1b, y1b, x2b, y2b)

    # draw the n strings
    set_stroke_width(1)
    set_stroke_cyan()
    i = 0
    while i < n:
        f = i / (n - 1)
        x1 = x1a + f * (x2a - x1a)
        y1 = y1a + f * (y2a - y1a)
        x2 = x1b + (1 - f) * (x2b - x1b)
        y2 = y1b + (1 - f) * (y2b - y1b)
        draw_line(x1, y1, x2, y2)
        i += 1


# the parameter-less function called by start_graphics
def main():
    string_art(X1A, Y1A, X2A, Y2A, X1B, Y1B, X2B, Y2B, N)


start_graphics(main)
