# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
sd.resolution = (1200, 600)


def get_polygon(n):
    _angle = 360 / n

    def draw_shapes(point, angle, lenght, delta_angle=_angle, num_angles=n):
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

    return draw_shapes


draw_triangle = get_polygon(n=3)
draw_rectangle = get_polygon(n=4)
draw_fiveangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(100, 200), angle=13, lenght=100)
draw_rectangle(point=sd.get_point(400, 100), angle=0, lenght=100)
draw_fiveangle(point=sd.get_point(100, 400), angle=45, lenght=100)

sd.pause()
