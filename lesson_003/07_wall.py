# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

sd.resolution = (1200, 600)
x1 = 0
y1 = 0
x2 = 100
y2 = 50
kf = -50



for step_y in range(0, 805, 52):
    if kf < 0:
        kf = 0
    else:
        kf = -50
    y1 = step_y
    y2 = step_y + 50
    for step_x in range(0, 1602, 102):
        x1 = step_x + kf
        x2 = step_x + 100 + kf
        point_1 = sd.get_point(x1, y1)
        point_2 = sd.get_point(x2, y2)
        sd.rectangle(left_bottom=point_1, right_top=point_2, color=sd.COLOR_ORANGE)

sd.pause()
