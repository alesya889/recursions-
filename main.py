
import turtle
from fractals.basic import draw_binary_tree, draw_branch
from fractals.koch import draw_koch, draw_koch_snowflake, draw_minkowski
from fractals.complex import draw_ice_fractal_1, draw_ice_fractal_2, draw_levy, draw_dragon
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.setworldcoordinates(-500, -400, 500, 400)


def show_menu() -> None:
    print("=== ФРАКТАЛЬНАЯ МАСТЕРСКАЯ ===")
    print("1. Двоичное дерево")
    print("2. Фрактал 'Ветка'")
    print("3. Кривая Коха")
    print("4. Снежинка Коха")
    print("5. Кривая Минковского")
    print("6. Ледяной фрактал #1")
    print("7. Ледяной фрактал #2")
    print("8. Кривая Леви")
    print("9. Дракон Хартера-Хейтуэя")
    print("10. Выход")


def get_int_input(txt: str, minval: int = None, maxval: int = None) -> int:
    while True:
        try:
            val = int(input(txt))

            if minval is not None and val < minval:
                print(f"Ошибка: число меньше минимального значения {minval}")
                continue

            if maxval is not None and val > maxval:
                print(f"Ошибка: число больше максимального значения {maxval}")
                continue

            return val
        except ValueError:
            print("Ошибка. Введите целое число")


def get_float_input(txt: str, minval: float = None, maxval: float = None) -> float:
    while True:
        try:
            val = float(input(txt))

            if minval is not None and val < minval:
                print(f"Ошибка: число меньше минимального значения {minval}")
                continue

            if maxval is not None and val > maxval:
                print(f"Ошибка: число больше максимального значения {maxval}")
                continue

            return val
        except ValueError:
            print("Ошибка. Введите целое число")


def draw_centered(draw_func, *args) -> None:
    screen = turtle.Screen()
    original_fd = turtle.fd
    original_forward = turtle.forward
    original_goto = turtle.goto
    original_setposition = turtle.setposition
    original_pendown = turtle.pendown

    points = [] #список кортежей: координаты, через которые проходит черепаха

    def measured_fd(distance):
        points.append(turtle.position())
        original_fd(distance)
        points.append(turtle.position())

    def measured_forward(distance):
        measured_fd(distance)

    def measured_goto(x, y=None):
        original_goto(x, y)
        points.append(turtle.position())

    def measured_setposition(x, y=None):
        measured_goto(x, y)

    try: #код, который нужно выполнить
        turtle.penup()
        turtle.fd = measured_fd
        turtle.goto = measured_goto
        turtle.forward = measured_forward
        turtle.setposition = measured_setposition
        turtle.pendown = lambda: None

        draw_func(*args)
        points.append(turtle.position())

    finally: #код, который выполнится в любом случае
        turtle.fd = original_fd
        turtle.goto = original_goto
        turtle.pendown = original_pendown
        turtle.forward = original_forward
        turtle.setposition = original_setposition

    if not points:
        return

    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    margin = 40
    width = max(max_x - min_x, 1)
    height = max(max_y - min_y, 1)

    canvas = screen.getcanvas() #холст Tkinter в пикселях
    canvas_width = canvas.winfo_width() #размер холста в пикселях
    canvas_height = canvas.winfo_height()

    scale = min(
        (canvas_width - margin * 2) / width, #пиксели на координаты. связь
        (canvas_height - margin * 2) / height
    ) #сколько пикселей на 1 единицу координат

    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    half_width = canvas_width / (2 * scale) #Координаты Turtle
    half_height = canvas_height / (2 * scale)

    screen.clear()
    screen.setworldcoordinates( #гранифцы координат в Turtle, которые будут видны на экране
        center_x - half_width, #левая граница
        center_y - half_height, #нижняя граница
        center_x + half_width,
        center_y + half_height
    )

    turtle.speed(0)
    turtle.hideturtle()
    screen.tracer(0)

    draw_func(*args)
    screen.update()


def main() -> None:
    turtle.speed(0)
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.tracer(0)
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "10":
            print("Выход из программы.")
            break

        elif choice == "1":
            depth = get_int_input("Глубина рекурсии (целое > 0): ")
            angle = get_float_input("Угол (от 0 до 90): ", minval = 0, maxval = 90)
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_binary_tree, depth, size, angle)

        elif choice == "2":
            size = get_float_input("Pазмер: ")
            n = get_int_input("Порядок n (целое > 0): ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_branch, size, n)

        elif choice == "3":
            order = get_int_input("Порядок (итерации): ")
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_koch, order, size)

        elif choice == "4":
            order = get_int_input("Порядок (итерации): ")
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_koch_snowflake, order, size)

        elif choice == "5":
            order = get_int_input("Порядок (итерации): ")
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_minkowski, order, size)

        elif choice == "6":
            order = get_int_input("Порядок (итерации): ")
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_ice_fractal_1, order, size)



        elif choice == "7":
            order = get_int_input("Порядок (итерации): ", minval=0, maxval=4)
            size = get_float_input("Размер: ", minval=1, maxval=250)
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_ice_fractal_2, order, size)


        elif choice == "8":
            order = get_int_input("Порядок (итерации): ")
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_levy, order, size)

        elif choice == "9":
            order = get_int_input("Порядок (итерации): ")
            size = get_float_input("Pазмер: ")
            turtle.reset()
            turtle.hideturtle()
            draw_centered(draw_dragon, order, size)

        else:
            print("Неверный пункт меню. Попробуйте снова.")

        #turtle.done()


if __name__ == "__main__":
    main()
