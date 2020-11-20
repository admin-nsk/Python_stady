# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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

from multiprocessing import Process, Pipe, Queue
from queue import Empty
import os
from collections import defaultdict


class ProcessingFile(Process):

    def __init__(self, file, volatil_receiver, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name_tiker = ""
        self.max_price = 0.0
        self.min_price = 999999.0
        self.volatility = 0.0
        self.file = file
        self.volatil_receiver = volatil_receiver

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
        self.volatil_receiver.put([self.name_tiker, self.volatility])


class CalculationVolatility(Process):

    def __init__(self, path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.volatility_list = {}
        self.path = path
        self.volatil_receiver = Queue(maxsize=2)

    def walk(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                yield file_path

    def run_process(self):
        process_list = [ProcessingFile(file=file, volatil_receiver=self.volatil_receiver) for file in self.walk()]
        for process in process_list:
            process.start()
        while True:
            try:
                # Этот метод у очереди - атомарный и блокирующий,
                # Поток приостанавливается, пока нет элементов в очереди
                key, value= self.volatil_receiver.get(timeout=5)
                self.volatility_list[key] = value
            except Empty:
                if not any(process.is_alive() for process in process_list):
                    break
        for process in process_list:
            process.join()
        for process in process_list:
            self.volatility_list[process.name_tiker] = process.volatility

    def print_data(self):
        print('Максимальная волатильность:')
        i = 0
        while i != 3:
            key, value = self.max_volatility()
            print(f'{key} - {value:.2f} %')
            self.volatility_list.pop(key)
            i += 1
        print('\nМинимальная волатильность:')
        i = 0
        while i != 3:
            key, value = self.min_volatility()
            print(f'{key} - {value:.2f} %')
            self.volatility_list.pop(key)
            i += 1
        print('\nНулевая волатильность:')
        key_list = self.zero_volatility()
        print(', '.join(key_list))

    def max_volatility(self):
        _check_max = lambda _item: self.volatility_list[_item[0]] == max(self.volatility_list.values())
        for item in self.volatility_list.items():
            if _check_max(item):
                return item

    def min_volatility(self):
        _check_min = lambda _item: self.volatility_list[_item[0]] == min(i for i in self.volatility_list.values() if i > 0)
        for item in self.volatility_list.items():
            if _check_min(item):
                return item

    def zero_volatility(self):
        key_list = []
        _check_zero = lambda _item: self.volatility_list[_item[0]] == 0
        for item in self.volatility_list.items():
            if _check_zero(item):
                key_list.append(item[0])
        key_list.sort()
        return key_list

    def run(self):
        self.walk()
        self.run_process()
        self.print_data()


def main():
    path = "D:\\Project\\Python\\lesson\\lesson_012\\trades"
    calculation = CalculationVolatility(path=path)
    calculation.run()


if __name__ == '__main__':
    main()

