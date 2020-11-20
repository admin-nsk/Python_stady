# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

class CountEvents:

    def __init__(self, file):
        self.file_name = file
        self.stat = {}
        self.counter = 0
        self.date = ""
        self.time = ""

    def __iter__(self):
        self.open_file = open(self.file_name, 'r', encoding='utf8')
        self.parse_file = self._read_file()
        return self

    def __next__(self):
        for date, count in self.parse_file:
            return date, count
        else:
            self.open_file.close()
            raise StopIteration()

    def _read_file(self):
        for line in self.open_file:
            if line.find('NOK') != -1:
                if self.date == line[1:11]:
                    if self.time == line[12:17]:
                        self.counter += 1
                    else:
                        out_date = f'{self.date} {self.time}'
                        yield out_date, self.counter
                        self.time = line[12:17]
                        self.counter = 1
                else:
                    out_date = f'{self.date} {self.time}'
                    yield out_date, self.counter
                    self.date = line[1:11]
                    self.time = line[12:17]
                    self.counter = 1


grouped_events = CountEvents(file='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
