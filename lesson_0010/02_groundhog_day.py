# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

ENLIGHTENMENT_CARMA_LEVEL = 777


def one_day():
    karma = 0
    event_day = random.randint(1, 14)
    if event_day <= 7:
        karma = event_day
    elif event_day == 8:
        raise Exception("IamGodError")
    elif event_day == 9:
        raise NameError("DrunkError")
    elif event_day == 10:
        raise ValueError("CarCrashError")
    elif event_day == 11:
        raise TypeError("GluttonyError")
    elif event_day == 12:
        raise AttributeError("DepressionError")
    elif event_day == 13:
        raise Exception("SuicideError")

    return karma


user_karma = 0
day = 0
while ENLIGHTENMENT_CARMA_LEVEL > user_karma:
    day += 1
    try:
        user_karma += one_day()
        print(f'Карма {user_karma}')
    except BaseException as exc:
        print(f'Ошибка {exc}')
print(f"Карма достигла {user_karma} за {day} дней")

# https://goo.gl/JnsDqu
