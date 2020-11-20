# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = 300
        self.y = 1200
        self.length = 25
        # self.color = []

    def clear_previous_picture(self):
        sd.start_drawing()
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)
        sd.finish_drawing()

    def move(self):
        if self.y > 30:
            self.y -= 30
            self.x += sd.random_number(-15, 15)

    def draw(self):
        sd.start_drawing()
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length)
        sd.finish_drawing()

    def can_fall(self):
        if self.y < 30:
            return False
        return True


# flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

color_list_dist = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE,
                   sd.COLOR_PURPLE]


def get_flakes(count):
    flakes_list = []
    for i in range(count):
        flakes_list.append(Snowflake())
        flakes_list[i].x = sd.random_number(30, 600)
        flakes_list[i].y = sd.random_number(550, 1500)
        flakes_list[i].length = sd.random_number(5, 20)
        # flakes_list[i].color = color_list_dist[sd.random_number(0, 6)]
    return flakes_list


def get_fallen_flakes():
    _fallen_flakes = 0
    for _flake in flakes:
        if _flake.y <= 30:
            _fallen_flakes += 1
    return _fallen_flakes


def append_flakes(count):
    for i in range(count):
        flakes.append(Snowflake())
        flakes[i].x = sd.random_number(30, 600)
        flakes[i].y = sd.random_number(550, 1500)
        flakes[i].length = sd.random_number(5, 20)
        # flakes[i].color = color_list_dist[sd.random_number(0, 6)]

flakes = get_flakes(count=100)  # создать список снежинок
print(flakes[1])

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
