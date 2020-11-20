 # -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageFont, ImageDraw, ImageColor

user_data = {}
file_path = "D:\\Project\\Python\\lesson\\lesson_013\\images\\ticket_template.png"
font_path = "D:\\Project\\Python\\lesson\\lesson_013\\Bloknot.ttf"


def get_data():
    user_data['FIO'] = "Петров А.В."
    user_data['from'] = "Новосибирск"
    user_data['to'] = "Бали"
    user_data['date'] = "20.11.2020"
    user_data['save_to'] = "Ticket.png"


def make_ticket(fio, from_, to, date):
    try:
        im = Image.open(file_path)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(font_path, size=21)
        draw.text((50, 120), fio, font=font, fill=ImageColor.colormap['black'])
        draw.text((50, 185), from_, font=font, fill=ImageColor.colormap['black'])
        draw.text((50, 255), to, font=font, fill=ImageColor.colormap['black'])
        draw.text((240, 255), date, font=font, fill=ImageColor.colormap['black'])
        if user_data['save_to']:
            im.save(user_data['save_to'])
        else:
            im.show()
    except FileNotFoundError:
        print('Файл изображения не найден')


get_data()
make_ticket(fio=user_data['FIO'], from_=user_data['from'], to=user_data['to'], date=user_data['date'])

 # Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
