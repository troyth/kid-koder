"""
shapes.py - A super simple drawing library for learning to code!

Every shape works the same way:
    rectangle(x, y, width, height, color)
    circle(x, y, radius, color)
    triangle(x, y, size, color)
    square(x, y, size, color)

(x, y) is where the shape starts - measured from the CENTER of the screen.
Move right = bigger x. Move up = bigger y.
"""

import turtle

# Set up the drawing window
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Drawing")

artist = turtle.Turtle()
artist.speed(3)          # 1 = slow, 10 = fast, 0 = instant
artist.penup()


def rectangle(x, y, width, height, color):
    """Draw a rectangle starting at (x, y) with the given width, height, and color."""
    artist.color(color)
    artist.goto(x, y)
    artist.pendown()
    artist.begin_fill()
    for side_length in (width, height, width, height):
        artist.forward(side_length)
        artist.left(90)
    artist.end_fill()
    artist.penup()


def square(x, y, size, color):
    """Draw a square starting at (x, y) with the given size and color."""
    rectangle(x, y, size, size, color)


def circle(x, y, radius, color):
    """Draw a circle centered near (x, y) with the given radius and color."""
    artist.color(color)
    artist.goto(x, y - radius)   # move to bottom of circle first
    artist.pendown()
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()
    artist.penup()


def triangle(x, y, size, color):
    """Draw an equilateral triangle starting at (x, y) with the given size and color."""
    artist.color(color)
    artist.goto(x, y)
    artist.pendown()
    artist.begin_fill()
    for _ in range(3):
        artist.forward(size)
        artist.left(120)
    artist.end_fill()
    artist.penup()


def done():
    """Call this at the end so the window stays open."""
    artist.hideturtle()
    screen.exitonclick()
