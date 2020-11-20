# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
color_list = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
              sd.COLOR_PURPLE]

sd.resolution = (1200, 600)


def draw_shapes(point, angle, lenght, delta_angle, num_angles, color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw(color=color)
    next_angle = angle + delta_angle
    next_point = v1.end_point
    if num_angles == 1:
        next_angle += 1
    if num_angles == 0:
        return
    num_angles -= 1
    draw_shapes(point=next_point, angle=next_angle, lenght=lenght, delta_angle=delta_angle, num_angles=num_angles,
                color=color)


def triangle(point, angle, lenght, color):
    draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=120, num_angles=3, color=color)


def square(point, angle, lenght, color):
    draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=90, num_angles=4, color=color)


def fiveangle(point, angle, lenght, color):
    draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=72, num_angles=5, color=color)


def sixangle(point, angle, lenght, color):
    draw_shapes(point=point, angle=angle, lenght=lenght, delta_angle=60, num_angles=6, color=color)


print("Выберите фигуру: \n", "\t1. Треугольник\n\t2. Квадрат\n\t3. Пятиугольник\n\t4. Шестиуголник\n")
num_shape = int(input("Введите номер фигуры: "))
while not (0 < int(num_shape) < 5):
    print("Вы ввели не верный номер фигуры ", num_shape)
    num_shape = int(input("Повторите выбор: "))

print("Возможные цвета: \n", "\t1. Красный\n\t2. Оранжевый\n\t3. Желтый\n\t4. Зеленый\n\t"
                             "5. Фиолетовый\n\t6. Голубой\n\t7. Пурпурный")
num = int(input("Введите номер желаемого цвета: "))-1
while not (-1 < int(num) < 7):
    print("Вы ввели не верный номер цвета ", num)
    num = int(input("Повторите выбор желаемого цвета: "))-1

point_1 = sd.get_point(300, 300)
if num_shape == 1:
    triangle(point_1, 25, 90, color_list[num])
elif num_shape == 2:
    square(point_1, 15, 50, color_list[num])
elif num_shape == 3:
    fiveangle(point_1, 30, 100, color_list[num])
elif num_shape == 4:
    sixangle(point_1, 45, 100, color_list[num])

sd.pause()
