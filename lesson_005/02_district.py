# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.central_street.house1 import room1 as cs_h1_room1, room2 as cs_h1_room2
from district.central_street.house2 import room1 as cs_h2_room1, room2 as cs_h2_room2
from district.soviet_street.house1 import room1 as ss_h1_room1, room2 as ss_h1_room2
from district.soviet_street.house2 import room1 as ss_h2_room1, room2 as ss_h2_room2

tenants = cs_h1_room1.folks + cs_h1_room2.folks + cs_h2_room1.folks + cs_h2_room2.folks + ss_h1_room1.folks + \
           ss_h1_room2.folks + ss_h2_room1.folks + ss_h2_room2.folks

string = ','.join(tenants)
print("На районе живут", string)


