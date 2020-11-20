# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
from threading import Thread


class CalculationVolatility(Thread):

    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_tiker = ""
        self.max_price = 0.0
        self.min_price = 999999.0
        self.volatility = 0.0
        self.file = file

    def read_file(self):
        with open(self.file, 'r', encoding='cp1251') as open_file:
            for line in open_file:
                if line.find('SECID') == -1:
                    self.processing_line(line[:-1])

    def processing_line(self, line):
        order_list = line.split(",")
        self.name_tiker = order_list[0]
        self.max_price = float(order_list[2]) if self.max_price < float(order_list[2]) else self.max_price
        self.min_price = float(order_list[2]) if self.min_price > float(order_list[2]) else self.min_price


    def calc_volatility(self):
        average_price = (self.max_price + self.min_price) / 2
        self.volatility = ((self.max_price - self.min_price) / average_price) * 100


    def run(self):
        self.read_file()
        self.calc_volatility()


def walk(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath, dirnames, filenames)
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            yield file_path


def run_thread(thread_list):
    for process in thread_list:
        process.start()
    for process in thread_list:
        process.join()


def print_data(volatility_list):
    print('Максимальная волатильность:')
    i = 0
    while i != 3:
        key, value = max_volatility(volatility_list)
        print(f'{key} - {value:.2f} %')
        volatility_list.pop(key)
        i += 1
    print('\nМинимальная волатильность:')
    i = 0
    while i != 3:
        key, value = min_volatility(volatility_list)
        print(f'{key} - {value:.2f} %')
        volatility_list.pop(key)
        i += 1
    print('\nНулевая волатильность:')
    key_list = zero_volatility(volatility_list)
    print(', '.join(key_list))


def max_volatility(volatility_list):
    _check_max = lambda _item: volatility_list[_item[0]] == max(volatility_list.values())
    for item in volatility_list.items():
        if _check_max(item):
            return item


def min_volatility(volatility_list):
    _check_min = lambda _item: volatility_list[_item[0]] == min(i for i in volatility_list.values() if i > 0)
    for item in volatility_list.items():
        if _check_min(item):
            return item


def zero_volatility(volatility_list):
    key_list = []
    _check_zero = lambda _item: volatility_list[_item[0]] == 0
    for item in volatility_list.items():
        if _check_zero(item):
            key_list.append(item[0])
    key_list.sort()
    return key_list


def main():
    path = "D:\\Project\\Python\\lesson\\lesson_012\\trades"
    thread_list = [CalculationVolatility(file=file) for file in walk(path=path)]
    volatility_list = {}
    run_thread(thread_list)
    for process in thread_list:
        volatility_list[process.name_tiker] = process.volatility
    print_data(volatility_list)


if __name__ == '__main__':
    main()




