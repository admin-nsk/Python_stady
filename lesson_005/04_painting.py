# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код
import simple_draw as sd
from paint.wall import paint_wall
from paint.snowfall import paint_snow
from paint.rainbow import paint_rainbow
from paint.tree import draw_branches


sd.resolution = (1200, 600)

paint_wall(400, 800, 0, 150)
paint_wall(400, 550, 152, 302)
paint_wall(650, 800, 152, 302)
paint_wall(400, 800, 304, 454)

paint_snow(0, 395)
point = sd.get_point(950, 0)
point_2 = sd.get_point(1050, 0)
draw_branches(point, 90, 100)
draw_branches(point_2, 90, 100)
paint_rainbow(600, -500, 1100)

sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
