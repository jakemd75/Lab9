'''
Jake David
This program draws a simple outdoor scene with a house, sun, and tree using Turtle graphics.
'''

import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_square(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    segment_length = length / segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)

    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ✅ THIS is the only part you were supposed to write
def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    jump_to(t, 150, 150)
    draw_circle(t, 40, "yellow")

    jump_to(t, -200, -50)
    draw_rectangle(t, 400, 100, "green")

    jump_to(t, -50, -50)
    draw_square(t, 100, "brown")

    jump_to(t, -50, 50)
    draw_triangle(t, 100, "red")

    jump_to(t, 80, -50)
    draw_rectangle(t, 20, 60, "brown")

    jump_to(t, 90, 20)
    draw_circle(t, 30, "green")


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()