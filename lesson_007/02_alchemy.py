# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Земля':
            return Dust()
        elif other.name == 'Огонь':
            return Lightning()
        else:
            return None

class Water:
    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Земля':
            return Dirt()
        elif other.name == 'Огонь':
            return Vapor()
        else:
            return None


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Земля':
            return Lava()
        elif other.name == 'Вода':
            return Vapor()
        elif other.name == 'Воздух':
            return Dust()
        else:
            return None

class Ground:
    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        # print(self.name)
        return self.name

    def __add__(self, other):
        if other.name == 'Огонь':
            return Lava()
        elif other.name == 'Вода':
            return Dirt()
        elif other.name == 'Воздух':
            return Lightning()
        else:
            return None


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name

    def __add__(self, other):
        return None


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        print(self.name)

    def __add__(self, other):
        return None


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name

    def __add__(self, other):
        return None


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name

    def __add__(self, other):
        return None


class Vapor:
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name

    def __add__(self, other):
        return None


class Dirt:
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        return None

print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Fire(), '+', Ground(), '=', Fire() + Ground())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
