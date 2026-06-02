'''
Jake David

This program refactors my Project 2 by breaking the draw_scene function into
smaller functions like draw_house, draw_tree, and draw_sun. This removes repeated
code and makes it easier to reuse shapes. After refactoring, I made the scene more
populated by adding multiple houses and trees in the second scene using the same
functions.
'''

import turtle
import math


def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


# ----- ORIGINAL SHAPE FUNCTIONS (UNCHANGED) -----
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


def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# ----- NEW SIMPLE HELPER FUNCTIONS -----
def draw_sun(t, x, y):
    jump_to(t, x, y)
    draw_circle(t, 40, "yellow")


def draw_ground(t):
    jump_to(t, -200, -50)
    draw_rectangle(t, 400, 100, "green")


def draw_house(t, x, y):
    jump_to(t, x, y)
    draw_square(t, 100, "brown")

    jump_to(t, x, y + 100)
    draw_triangle(t, 100, "red")


def draw_tree(t, x, y):
    jump_to(t, x, y)
    draw_rectangle(t, 20, 60, "brown")

    jump_to(t, x + 10, y + 70)
    draw_circle(t, 30, "green")


# ----- REQUIRED FUNCTION -----
def draw_scene(t):
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # --- FIRST SCENE (same as Project 2) ---
    draw_sun(t, 150, 150)
    draw_ground(t)
    draw_house(t, -50, -50)
    draw_tree(t, 80, -50)

    screen.update()
    turtle.time.sleep(2)

    # --- SECOND SCENE (more populated) ---
    t.clear()

    draw_ground(t)

    draw_sun(t, 150, 150)

    # just add a few more objects (simple but enough)
    draw_house(t, -150, -50)
    draw_house(t, 50, -50)

    draw_tree(t, -50, -50)
    draw_tree(t, 120, -50)


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()