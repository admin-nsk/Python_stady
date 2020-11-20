# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
sd.resolution = (1200, 600)

def draw_shapes(point, angle, lenght, delta_angle, num_angles):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()
    next_angle = angle + delta_angle
    next_point = v1.end_point
    if num_angles == 1:
        next_angle += 1
    if num_angles == 0:
        return
    num_angles -= 1
    draw_shapes(point=next_point, angle=next_angle, lenght=lenght, delta_angle=delta_angle, num_angles=num_angles)

    def triangle(point, angle, lenght):
        draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=120, num_angles=3)


    def square(point, angle, lenght):
        draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=90, num_angles=4)


    def fiveangle(point, angle, lenght):
        draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=72, num_angles=5)


    def sixangle(point, angle, lenght):
        draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=60, num_angles=6)


point_1 = sd.get_point(100, 100)
point_2 = sd.get_point(400, 100)
point_3 = sd.get_point(100, 400)
point_4 = sd.get_point(400, 400)
triangle(point_1, 25, 90)
square(point_2, 15, 50)
fiveangle(point_3, 30, 100)
sixangle(point_4, 45, 100)

sd.pause()


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!



sd.pause()
