# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile


class FotoCatalog:

    def __init__(self, path, dest_dir):
        self.path = path
        self.dest_dir = dest_dir

    def _make_dir(self, dirs_name):
        if not os.path.exists(dirs_name):
            os.makedirs(dirs_name)

    def move_file(self, source, dest):
        raise NotImplementedError()

    def walk(self):
        raise NotImplementedError()

    def walk_zip(self):
        raise NotImplementedError()

    def sort(self):
        if zipfile.is_zipfile(self.path):
            self.walk_zip()
        else:
            self.walk()


class SortFoto(FotoCatalog):
    def walk(self):
        for dirpath, dirnames, filenames in os.walk(self.path):
            print(dirpath, dirnames, filenames)
            for file in filenames:
                old_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(old_file_path)
                file_time = time.gmtime(secs)
                new_dir_path = os.path.join(self.dest_dir, str(file_time.tm_year), str(file_time.tm_mon))
                new_file_path = os.path.join(new_dir_path, file)
                self._make_dir(new_dir_path)
                self.move_file(old_file_path, new_file_path)

    def move_file(self, source, dest):
        shutil.copy2(source, dest)
        os.remove(source)

    def walk_zip(self):
        with zipfile.ZipFile(self.path) as openzip:
            info = openzip.infolist()
            print(f'Namelist {openzip.namelist()}')
            for file in openzip.namelist():
                if '.' in file:
                    info = openzip.getinfo(file)
                    new_dir_path = os.path.join(self.dest_dir, str(info.date_time[0]), str(info.date_time[1]))
                    self._make_dir(dirs_name=new_dir_path)
                    filename = os.path.basename(file)
                    data = openzip.read(file)
                    myfile_path = os.path.join(new_dir_path, filename)
                    myfile = open(myfile_path, "wb")
                    myfile.write(data)
                    myfile.close()
                else:
                    print(f'Папка {file}')



path_to_catalog = 'D:\\Project\\Python\\lesson\\lesson_009\\icons.zip'
destination = 'D:\\Project\\Python\\lesson\\lesson_009\\iconszip'
Sort_Icons = SortFoto(path=path_to_catalog, dest_dir=destination)
Sort_Icons.sort()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
