# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class CountEvents:

    def __init__(self, file):
        self.file_name = file
        self.stat = {}
        self.counter = 0
        self.date = ""
        self.time = ""

    def _write_file(self, out_file_name=None, out_string=' '):
        if out_file_name is not None:
            file = open(out_file_name, 'a', encoding='utf8')
        else:
            file = None
        if file:
            file.write(out_string)
        else:
            print(out_string, end='')
        if file:
            file.write('\n')
        else:
            print()
        if file:
            file.close()

    def processing_file(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._read_file(line=line[:-1])

    def _read_file(self, line):
        if line.find('NOK') != -1:
            if self.date == line[1:11]:
                if self.time == line[12:17]:
                    self.counter += 1
                else:
                    out_string = f'[{self.date} {self.time}] {self.counter}'
                    self._write_file(out_file_name="out-file.txt", out_string=out_string)
                    self.time = line[12:17]
                    self.counter = 1
            else:
                out_string = f'[{self.date} {self.time}] {self.counter}'
                self._write_file(out_file_name="out-file.txt", out_string=out_string)
                self.date = line[1:11]
                self.time = line[12:17]
                self.counter = 1


Events = CountEvents(file='events.txt')
Events.processing_file()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
