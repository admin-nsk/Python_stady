# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
#  Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %#   Минимальная волатильность:

#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
from collections import OrderedDict
import os

class CalculationVolatility:

    def __init__(self, path):
        self.data_order = {}
        self.volatility_list = {}
        self.path = path

    def walk(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            print(dirpath, dirnames, filenames)
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                self.read_file(file_path)

    def read_file(self, file_name):
        with open(file_name, 'r', encoding='cp1251') as open_file:
            for line in open_file:
                if line.find('SECID') == -1:
                    self.processing_line(line[:-1])

    def processing_line(self, line):
        order_list = line.split(",")
        if order_list[0] in self.data_order:
            if self.data_order[order_list[0]]['max_price'] < order_list[2]:
                self.data_order[order_list[0]]['max_price'] = order_list[2]
            elif self.data_order[order_list[0]]['min_price'] > order_list[2]:
                self.data_order[order_list[0]]['min_price'] = order_list[2]
        else:
            self.data_order[order_list[0]] = {'max_price': order_list[2], 'min_price': order_list[2]}

    def calc_volatility(self):
        for tiker in self.data_order:
            max_price = float(self.data_order[tiker]['max_price'])
            min_price = float(self.data_order[tiker]['min_price'])
            average_price = (max_price + min_price) / 2
            self.volatility_list[tiker] = ((max_price - min_price) / average_price) * 100

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
        _check_min = lambda _item: self.volatility_list[_item[0]] == min(self.volatility_list.values())
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
        self.calc_volatility()
        self.print_data()


calculation = CalculationVolatility("/media/alex/Data/Project/Python/lesson/lesson_012/trades")
calculation.run()
