import turtle as t

def binary_tree(depth: int, size: float, angle: float):
    if depth == 0:
        t.pendown()
        t.forward(size)
        t.penup()
        return
    t.pendown()
    t.forward(size)
    t.penup()
    t.right(angle)
    binary_tree(depth - 1, size / 2, angle)
    t.backward(size / 2)
    t.left(angle * 2)
    binary_tree(depth - 1, size / 2, angle)
    t.backward(size / 2)
    t.right(angle)
    return


def branch(size, n):
    if n == 0:
        t.left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(0.5 * x * (n - i - 1), n - i - 1)
        t.left(90)
        branch(0.5 * x * (n - i - 1), n - i - 1)
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)


def draw_binary_tree(depth: int, size: float, angle: float):
    t.speed(0)
    t.penup()
    t.setheading(90)
    t.pendown()
    binary_tree(depth, size, angle)
    t.setheading(0)
    return


def draw_branch(size, n):
    t.speed(0)
    t.penup()
    t.setheading(90)
    t.pendown()
    branch(size, n)
    return
