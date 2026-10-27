import turtle as t
from math import sqrt


def ice_fractal_1(order: int, size: float) -> None:
    if order == 0:
        t.fd(size)
        return
    ice_fractal_1(order - 1, size / 2)
    t.lt(90)
    ice_fractal_1(order - 1, size / 4)
    t.rt(180)
    ice_fractal_1(order - 1, size / 4)
    t.lt(90)
    ice_fractal_1(order - 1, size / 2)


def ice_fractal_2(order: int, size: float) -> None:
    if order == 0:
        t.fd(size)
        return
    ice_fractal_2(order - 1, size)
    t.lt(120)
    ice_fractal_2(order - 1, size / 2)
    t.rt(180)
    ice_fractal_2(order - 1, size / 2)
    t.lt(120)
    ice_fractal_2(order - 1, size / 2)
    t.rt(180)
    ice_fractal_2(order - 1, size / 2)
    t.lt(120)
    ice_fractal_2(order - 1, size)


def levy(order: int, size: float) -> None:
    if order == 0:
        t.fd(size)
        return
    t.lt(45)
    levy(order - 1, size / sqrt(2))
    t.rt(90)
    levy(order - 1, size / sqrt(2))
    t.lt(45)


def dragon(order: int, size: float, direction: int = 1) -> None:
    if order == 0:
        t.fd(size)
        return
    t.lt(45)
    dragon(order - 1, size / sqrt(2), 1)
    t.rt(90 * direction)
    dragon(order - 1, size / sqrt(2), -1)
    t.rt(45)


def draw_ice_fractal_1(order: int, size: float) -> None:
    t.pu()
    t.setheading(0)
    t.goto(-size / 2, 0)
    t.pd()
    ice_fractal_1(order, size)


def draw_ice_fractal_2(order: int, size: float) -> None:
    t.pu()
    t.setheading(0)
    t.goto(-size / 2, 0)
    t.pd()
    ice_fractal_2(order, size)


def draw_levy(order: int, size: float) -> None:
    t.pu()
    t.setheading(0)
    t.goto(-size / 2, 0)
    t.pd()
    levy(order, size)


def draw_dragon(order: int, size: float) -> None:
    t.pu()
    t.setheading(0)
    t.goto(-size / 2, 0)
    t.pd()
    dragon(order, size)