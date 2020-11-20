# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall_engine import create_snowflakes, delete_snowflakes, drawing_snowflake, displace_snowflakes, \
    check_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
create_snowflakes(50)
del_snowflakes = []
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    drawing_snowflake()
    #  сдвинуть_снежинки()
    displace_snowflakes()
    #  нарисовать_снежинки_цветом(color)

    #  если есть номера_достигших_низа_экрана() то
    del_snowflakes = check_snowflakes()
    if del_snowflakes:
        delete_snowflakes(del_snowflakes)
        create_snowflakes(len(del_snowflakes))
        del_snowflakes.clear
    drawing_snowflake(True)
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
