# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass

class ParseFile:

    def __init__(self, file):
        self.file = file
        self.file_normal = "registrations_good.log"
        self.file_err = "registrations_bad.log"

    def write_to_file(self, status_parse, line, err=None):
        if status_parse:
            file = open(self.file_normal, 'a', encoding='utf8')
            file.write(line)
            file.close()
        else:
            file = open(self.file_err, 'a', encoding='utf8')
            file.write(line)
            file.write(err)
            file.write('\n')
            file.write('\n')
            file.close()

    def parse_line(self, line):
        list_line = line[:-1].split(" ")
        print(list_line)
        if len(list_line) != 3:
            raise ValueError("НЕ присутсвуют все три поля")
        if not list_line[0].isalpha:
            print(list_line[0])
            raise NotNameError("Поле имени содержит НЕ только буквы")
        if list_line[1].find("@") == -1 and list_line[1].find(".") == -1:
            print(list_line[1])
            raise NotEmailError("поле емейл НЕ содержит @ и .(точку)")
        if 10 > int(list_line[2]) > 99:
            print(list_line[2])
            raise ValueError("поле возраст НЕ является числом от 10 до 99")
        return True

    def parse(self):
        with open(self.file, 'r', encoding='utf8') as parse_file:
            for line in parse_file:
                try:
                    status = self.parse_line(line)
                    self.write_to_file(status, line)
                except NotNameError as exc:
                    print(exc)
                    self.write_to_file(False, line, str(exc))
                except NotEmailError as exc:
                    print(exc)
                    self.write_to_file(False, line, str(exc))
                except ValueError as exc:
                    print(exc)
                    self.write_to_file(False, line, str(exc))


path_file = "registrations.txt"
parse_file = ParseFile(path_file)
parse_file.parse()
