from turtle import *
from math import sqrt

screensize(2000,2000)
speed(0)


def ice_fractal_1(order: int, size: float) -> None:
    if order == 0:
        fd(size)
        return
    ice_fractal_1(order - 1, size / 2)
    lt(90)
    ice_fractal_1(order - 1, size / 4)
    rt(180)
    ice_fractal_1(order - 1, size / 4)
    lt(90)
    ice_fractal_1(order - 1, size / 2)


def ice_fractal_2(order: int, size: float) -> None:
    if order == 0:
        fd(size)
        return
    ice_fractal_2(order - 1, size)
    lt(120)
    ice_fractal_2(order - 1, size / 2)
    rt(180)
    ice_fractal_2(order - 1, size / 2)
    lt(120)
    ice_fractal_2(order - 1, size / 2)
    rt(180)
    ice_fractal_2(order - 1, size / 2)
    lt(120)
    ice_fractal_2(order - 1, size)


def levy(order: int, size: float) -> None:
    if order == 0:
        fd(size)
        return
    lt(45)
    levy(order - 1, size / sqrt(2))
    rt(90)
    levy(order - 1, size / sqrt(2))
    lt(45)


def dragon(order: int, size: float, direction: int = 1) -> None:
    if order == 0:
        fd(size)
        return
    lt(45)
    dragon(order - 1, size / sqrt(2), 1)
    rt(90 * direction)
    dragon(order - 1, size / sqrt(2), -1)
    rt(45)


hideturtle()
done()