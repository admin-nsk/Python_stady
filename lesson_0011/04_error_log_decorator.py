# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def log_errors(out_file):
    def log_errors_internal(func):
        def surrogate(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except ValueError as exc:
                file = open(out_file, 'a', encoding='utf8')
                file.write(f'<{func.__name__}> <{args}> <ValueError> <{exc}>')
                file.write("\n")
                file.close()
                print(f'Ошибка в функции {func.__name__} - {exc}')
                raise ValueError(exc)
            except ZeroDivisionError as exc2:
                file = open(out_file, 'a', encoding='utf8')
                file.write(f'<{func.__name__}> <{args}> <ZeroDivisionError> <{exc2}>')
                file.write("\n")
                file.close()
                # raise ValueError(exc2)
        return surrogate
    return log_errors_internal

# Проверить работу на следующих функциях
@log_errors("function_errors.log")
def perky(param):
    return param / 0


@log_errors("function_errors.log")
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')
    return "Успех"


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass

