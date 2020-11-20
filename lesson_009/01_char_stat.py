# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile


class GetStat:
    analize_count = 1

    def __init__(self, file):
        self.file_name = file
        self.stat ={}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def _counter(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def get_stat(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        # self.sequence = ' ' * self.analize_count
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._counter(line=line[:-1])

    def print_stat(self):
        self.total = 0
        print('+' + '-' * 9 + '+' + '-' * 9 + '+')
        print('|' + f'{"буква":^9}' + '|' + f'{"частота":^9}' + '|')
        print('+' + '-' * 9 + '+' + '-' * 9 + '+')
        list_keys = list(self.stat.keys())
        list_keys.sort(reverse=True)
        list_items = list(self.stat.items())
        list_items.sort(key=lambda i: i[1])
        # for items in list_items:
        #     print('|' + f'{items[0]:^9}' + '|' + f'{items[1]:^9}' + '|')
        #     self.total += self.stat[items[0]]
        for char in list_keys:
            print('|' + f'{char:^9}' + '|' + f'{self.stat[char]:^9}' + '|')
            self.total += self.stat[char]
        print('+' + '-' * 9 + '+' + '-' * 9 + '+')
        print('|' + f'{"Итого":^9}' + '|' + f'{self.total:^9}' + '|')
        print('+' + '-' * 9 + '+' + '-' * 9 + '+')

Stat_Voyna = GetStat(file='voyna-i-mir.txt')
Stat_Voyna.get_stat()
Stat_Voyna.print_stat()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
