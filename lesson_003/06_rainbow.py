# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

sd.resolution = (1200, 600)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
i = 0
y1 = 50
y2 = 450
# while i < 7:
#     point_1 = sd.get_point(50, y1,)
#     point_2 = sd.get_point(650, y2,)
#     sd.line(start_point=point_1, end_point=point_2, color=rainbow_colors[i], width=4)
#     y1 += 5
#     y2 += 5
#     i += 1


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

def bubble(point, step, color):
    radius = 1000
    radius += step
    sd.circle(center_position=point, radius=radius, width=8, color=color)

point = sd.get_point(1000, -500)
step = 0
while i < 7:
    step += 5
    bubble(point=point, step=step, color=rainbow_colors[i])
    i += 1

kf = 0
if 1 < 2:
    kf == -51
else:
    kf == 0
sd.pause()
