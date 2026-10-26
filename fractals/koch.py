import turtle as t
import math

def koch(order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
    else:
        koch(order - 1, size / 3)
        t.left(60)
        koch(order - 1, size / 3)
        t.right(120)
        koch(order - 1, size / 3)
        t.left(60)
        koch(order - 1, size / 3)

def koch_snowflake(order: int, size: float) -> None:
    for _ in range(3):
        koch(order, size)
        t.right(120)


def minkowski(order: int, size: float) -> None:
    if order == 0:
        t.forward(size)
    else:
        minkowski(order - 1, size / 4)
        t.left(90)
        minkowski(order - 1, size / 4)
        t.right(90)
        minkowski(order - 1, size / 4)
        t.right(90)
        minkowski(order - 1, size / 4)
        t.right(0)
        minkowski(order - 1, size / 4)
        t.left(90)
        minkowski(order - 1, size / 4)
        t.left(90)
        minkowski(order - 1, size / 4)
        t.right(90)
        minkowski(order - 1, size / 4)


def draw_koch(order: int, size: float) -> None:
    t.penup()
    t.setheading(0)
    t.goto(-size / 2, 0)
    t.pendown()
    koch(order, size)


def draw_koch_snowflake(order: int, size: float) -> None:
    start_x = -size / 2
    start_y = size * math.sqrt(3) / 6
    t.penup()
    t.setheading(0)
    t.goto(start_x, start_y)
    t.pendown()
    koch_snowflake(order, size)


def draw_minkowski(order: int, size: float) -> None:
    t.penup()
    t.setheading(0)
    t.goto(-size / 2, 0)
    t.pendown()
    minkowski(order, size)