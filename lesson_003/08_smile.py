# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
sd.resolution = (1200, 600)
def smile(x,y):
    radius = 20
    radius_eyes = 2
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, color=sd.COLOR_YELLOW)
    y_eyes = y + 6
    x_r_eye = x + 5
    x_l_eye = x - 5
    point_r_eye = sd.get_point(x_r_eye, y_eyes)
    point_l_eye = sd.get_point(x_l_eye, y_eyes)
    sd.circle(center_position=point_r_eye, radius=radius_eyes, color=sd.COLOR_YELLOW)
    sd.circle(center_position=point_l_eye, radius=radius_eyes, color=sd.COLOR_YELLOW)
    x1_mouth = x - 6
    y1_mouth = y - 3
    x2_mouth = x
    y2_mouth = y - 7
    x3_mouth = x + 6
    y3_mouth = y - 3
    point_mouth = [sd.get_point(x1_mouth, y1_mouth), sd.get_point(x2_mouth, y2_mouth), sd.get_point(x3_mouth, y3_mouth)]
    sd.lines(point_mouth, color=sd.COLOR_YELLOW)

smile(100, 100)
sd.pause()
