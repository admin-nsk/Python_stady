# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
from functools import reduce


class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        for number in range(2, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)
                return number
        raise StopIteration()


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+  2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
#TODO простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

class CheckHappyNumber:

    def __init__(self, n, mode):
        self.n = n
        self.mode = mode

    def __iter__(self):
        self.gen_number = self.numbers_generator()
        return self

    def __next__(self):
        for number in self.gen_number:
            if self.mode == "ph":
                if self.happy_number(number):
                    return number
            elif self.mode == "pp":
                if self.check_polyandrom(number):
                    return number
            elif self.mode == "php":
                if self.happy_number(number):
                    if self.check_polyandrom(number):
                        return number
        else:
            raise StopIteration()

    def happy_number(self, number):
        num_str = str(number)
        half_len = int(len(num_str) // 2)
        sum_first = reduce(lambda x, y: int(x) + int(y), num_str[:half_len])
        sum_second = reduce(lambda x, y: int(x) + int(y), num_str[-half_len:])
        if sum_first == sum_second:
            return True
        else:
            return False

    def check_polyandrom(self, number):
        num_str = str(number)
        half_len = int(len(num_str) // 2)
        first = num_str[:half_len]
        second = num_str[:-half_len-1:-1]
        if first == second:
            return True
        else:
            return False

    def numbers_generator(self):
        prime_numbers = []
        for number in range(100, self.n + 1):
            for prime in prime_numbers:
                if number % prime == 0:
                    break
            else:
                prime_numbers.append(number)
                yield number


number_iterator = CheckHappyNumber(n=100000, mode="php")
for number in number_iterator:
    print(number)