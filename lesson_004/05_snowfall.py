# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

y = 550
x = 100
x_bias = 10
x_list = []
y_list = []
length_list = []
for i in range(N):
    x_list.append(sd.random_number(30, 600))
    y_list.append(sd.random_number(550, 1500))
    length_list.append(sd.random_number(5, 20))
print(x_list)


def snowflake(_x, _y, _length):
    # sd.clear_screen()
    sd.start_drawing()
    point = sd.get_point(_x, _y)
    sd.snowflake(center=point, length=_length)


def del_snowflake(_x, _y, _length):
    point = sd.get_point(_x, _y)
    sd.snowflake(center=point, length=_length, color=sd.background_color)


while True:
    y_for = y
    for _i in range(len(x_list)):
        sd.start_drawing()
        del_snowflake(x_list[_i], y_list[_i], length_list[_i])
        if 110 > y_list[_i] > 80:
            x_list.append(sd.random_number(30, 600))
            y_list.append(sd.random_number(550, 1500))
            length_list.append(sd.random_number(5, 20))
        if y_list[_i] > 70:
            y_list[_i] -= 30
            x_list[_i] += sd.random_number(-15, 15)
        snowflake(x_list[_i], y_list[_i], length_list[_i])
        sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


