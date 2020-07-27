# coding:utf-8
#
from tkinter import *
import math

a = int(input("Enter your value of X1: "))
b = int(input("Enter your value of Y1: "))

c = int(input("Enter your value of X2: "))
d = int(input("Enter your value of Y2: "))

g = int(input("Enter your value of X3: "))
h = int(input("Enter your value of Y3: "))

e = int(input("Enter your value of X4: "))
f = int(input("Enter your value of Y4: "))

my_window = Tk()
canvas = Canvas(my_window, width=400, height=400, background='white')
canvas.grid(row=0, column=0)
canvas.create_line(a, b, c, d, width=4)
canvas.create_line(c, d, e, f, width=4)
canvas.create_line(e, f, g, h, width=4)
canvas.create_line(g, h, a, b, width=4)
canvas.pack()


def find_gradient(x1, y1, x2, y2):
    if x1 == x2:
        return 'a'
    return (float(y1 - y2)) / (x1 - x2)


def find_intesection_point(a, b, c, d, e, f, g, h):
    # grad line 1
    m1 = find_gradient(c, d, g, h)
    # grad line 2
    m2 = find_gradient(a, b, e, f)
    x1 = (f - m2 * e + m1 * g - h) / (float(m1 - m2))
    y1 = m1 * (x1 - g) + h
    return x1, y1


def find_radius(x1, y1, x2, y2, center_x, center_y):
    m = find_gradient(x1, y1, x2, y2)
    if m == 'a': return abs(center_x - x2) / float(1)
    return abs(m * center_x - 1 * center_y - (m * x2 - y2)) / float(math.sqrt(m * m + 1))


center_x, center_y = find_intesection_point(a, b, c, d, e, f, g, h)

r1 = find_radius(g, h, e, f, center_x, center_y)
r2 = find_radius(e, f, c, d, center_x, center_y)
r3 = find_radius(c, d, a, b, center_x, center_y)
r4 = find_radius(a, b, g, h, center_x, center_y)

mini = r1

for x in [r1, r2, r3, r4]:
    if x < mini:
        mini = x

r = mini

points = [
    #
    center_x - int(r * math.sin(2 * math.pi / 5)),
    center_y - int(r * math.cos(2 * math.pi / 5)),

    #
    center_x + int(r * math.sin(2 * math.pi / 5)),
    center_y - int(r * math.cos(2 * math.pi / 5)),

    #
    center_x - int(r * math.sin(math.pi / 5)),
    center_y + int(r * math.cos(math.pi / 5)),

    # vertex
    center_x,
    center_y - r,

    #
    center_x + int(r * math.sin(math.pi / 5)),
    center_y + int(r * math.cos(math.pi / 5)),
]

print(points)
canvas.create_polygon(points, outline='black', fill='white')

my_window.mainloop()
