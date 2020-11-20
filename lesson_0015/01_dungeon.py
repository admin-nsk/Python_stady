# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход

import json
import re
from collections import defaultdict
import time

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


class UndergroundGame:

    def __init__(self, _remaining_time, _json_file):
        self.remaining_time = float(_remaining_time)
        self.json_file = _json_file
        self.json_data = {}
        self.field_names = defaultdict(int, {'current_location': '', 'current_experience': 0, 'current_date': 0})
        self.start = False


    def read_json_file(self):
        with open(self.json_file, 'r', encoding='utf8') as read_json_file:
            self.json_data = json.load(read_json_file)

    def walk_on_dict(self, dict_to_walk):
        for _key, _location_list in dict_to_walk.items():
            self.field_names['current_location'] = _key
            return _key, _location_list

    def walk_on_list(self, list_for_walk):
        for item in list_for_walk:
            if type(item) == str:
                yield True, item
            if type(item) == dict:
                for _key, _value in item.items():
                    yield False, _key

    def user_menu(self, current_location, room):
        print(f'\n', '>>'*20)
        print(f'Вы в локации:{current_location}')
        print(f'Опыт:{self.field_names["current_experience"]}')
        print(f'Осталос время:{self.remaining_time}')

        print('Внутри вы видите:')
        for monster, item in self.walk_on_list(room):
            if monster:
                print(f'-- Монстра {item}')
            else:
                print(f'-- Вход в локацию: {item}')
        print('\nВыберите действие:')
        for i in range(len(room)):
            if type(room[i]) == str:
                print(f'{i}. Атаковать монстра {room[i]}')
            if type(room[i]) == dict:
                for _next_location, _value in room[i].items():
                    print(f'{i}.Перейти в локацию: {_next_location}')
        print(f'{len(room)}. Выход')
        user_choice = input('->')
        return user_choice

    def parse_string(self, string_for_parse):
        if string_for_parse.find('Mob') != -1:
            _exp = re.search(r'exp(\d+)', string_for_parse)
            _tm = re.search(r'tm(\d+)', string_for_parse)
            return int(_exp.group(1)), int(_tm.group(1))
        elif string_for_parse.find('Boss') != -1:
            _exp = re.search(r'exp(\d+)', string_for_parse)
            _tm = re.search(r'tm(\d+)', string_for_parse)
            return int(_exp.group(1)), int(_tm.group(1))
        elif string_for_parse.find('Location') != -1:
            _tm = re.search(r'tm(\d+.\d+)', string_for_parse)
            return float(_tm.group(1) if _tm else 0)

    def calc_time(self, time):
        pass

    def attack_monster(self, monster):
        print(f'Бой с монстром {monster}')
        _exp, _tm = self.parse_string(monster)
        self.field_names['current_experience'] += _exp
        self.remaining_time -= _tm

    def engine(self, current_dict):
        while self.remaining_time > 0:
            _current_location, _location_list = self.walk_on_dict(current_dict)
            _choice = int(self.user_menu(_current_location, _location_list))
            _tm = self.parse_string(_current_location)
            self.remaining_time -= _tm
            if _choice == len(_location_list):
                return
            elif _choice > len(_location_list):
                print('Не корректный выбор')
            elif type(_location_list[_choice]) == str:
                self.attack_monster(_location_list[_choice])
                _location_list.pop(_choice)
            elif type(_location_list[_choice]) == dict:
                self.engine(_location_list[_choice])
        print('Закончилось время!!!!')

    def run(self):
        if not self.start:
            print('-'*10, 'Игра Подземелье', '-'*10)
            print('1. Начать игру')
            print('2. Выход')
            status = input('->')
            if status == '1':
                self.start = True
            else:
                exit()
        self.read_json_file()
        self.engine(self.json_data)

# Учитывая время и опыт, не забывайте о точности вычислений!


if __name__ == '__main__':
    json_file = 'D:\\Project\\Python\\lesson\\lesson_015\\rpg.json'
    start_game = UndergroundGame(_remaining_time=remaining_time, _json_file=json_file)
    start_game.run()

