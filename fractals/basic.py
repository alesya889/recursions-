import turtle

t = turtle.Turtle()
t.left(90)


def draw_binary_tree(depth: int, size: float, angle: float):
    if depth == 0:
        t.pendown()
        t.forward(size)
        t.penup()
        return
    t.pendown()
    t.forward(size)
    t.penup()
    t.right(angle)
    draw_binary_tree(depth - 1, size / 2, angle)
    t.backward(size / 2)
    t.left(angle * 2)
    draw_binary_tree(depth - 1, size / 2, angle)
    t.backward(size / 2)
    t.right(angle)
    return


turtle.done()
