# -*- coding: utf-8 -*-
import random

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dust = 0
        self.cat_food = 30
        self.cat = None

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, скопилось грязи {}'.format(
            self.food, self.money, self.dust)


class Husband:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.happy = 100
        self.house = house
        self.salary = 0
        self.live = True

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.satiety, self.happy)

    def act(self):
        if self.house.dust >= 90:
            self.happy -= 10
        if self.happy < 10:
            # cprint('{} умер от депрессии!'.format(self.name), color='red')
            self.live = False
        elif self.house.money == 0 and self.satiety > 0:
            self.work()
        elif self.satiety < 20:
            self.eat()
        elif self.house.cat_food < 10:
            self.bay_cat_food()
        elif self.happy < 20:
            self.gaming()
        elif random.choice([True, False]):
            self.pet_the_cat(self.house.cat)
        else:
            self.work()

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.satiety += 30
            # cprint('{} поел!'.format(self.name), color='green')
        elif 30 > self.house.food > 0:
            self.satiety += self.house.food
            self.house.food = 0
        elif self.satiety <= 0:
            # cprint('{} умер!'.format(self.name), color='red')
            self.live = False
        else:
            pass
            # cprint('{} голодает!'.format(self.name), color='yellow')

    def work(self):
        self.satiety -= 10
        self.house.money += self.salary
        # cprint('{} сходил на работу!'.format(self.name), color='green')

    def gaming(self):
        self.happy += 20
        self.satiety -= 10
        # cprint('{} играл весь день!'.format(self.name), color='blue')

    def bay_cat_food(self):
        if self.house.money <= 0:
            pass
            # cprint('{} Нет денег на еду котам!'.format(self.name), color='yellow')
        elif self.house.money < 20:
            self.house.cat_food += self.house.money
            self.house.money -= 0
            self.satiety -= 10
            # cprint('{} купил котам немного поесть!'.format(self.name), color='blue')
        else:
            self.house.cat_food += 20
            self.house.money -= 20
            self.satiety -= 10
            # cprint('{} купил котам поесть!'.format(self.name), color='blue')

    def pet_the_cat(self, cat):
        self.happy += 5
        # cprint('{} гладил кота!'.format(self.name), color='blue')


class Wife:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.happy = 100
        self.house = house
        self.live = True

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.satiety, self.happy)

    def act(self):
        if self.house.dust > 90:
            self.happy -= 10
        if self.satiety > 0 and self.house.food == 0:
            self.shopping()
        elif self.satiety <= 30:
            self.eat()
        elif self.happy < 30:
            self.buy_fur_coat()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.dust > 50:
            self.clean_house()
        else:
            self.pet_the_cat(self.house.cat)

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.satiety += 30
            # cprint('{} поела!'.format(self.name), color='green')
        elif 30 > self.house.food > 0:
            self.satiety += self.house.food
            self.house.food = 0
            # cprint('{} поела немного!'.format(self.name), color='yellow')
        elif self.satiety <= 0:
            # cprint('{} умерла!'.format(self.name), color='red')
            self.live = False
        else:
            pass
            # cprint('{} голодает!'.format(self.name), color='yellow')

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 50
            # cprint('{} купила еды!'.format(self.name), color='yellow')
        elif self.house.money <= 0:
            pass
            # cprint('{} Нет денег на еду!'.format(self.name), color='yellow')
        else:
            self.house.food += self.house.money
            self.house.money = 0
            # cprint('{} купила немного еды!'.format(self.name), color='yellow')
        self.satiety -= 10
        self.happy -= 10

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.satiety -= 10
            self.happy += 60
            # cprint('{} купила шубу!'.format(self.name), color='blue')
        elif self.happy < 10:
            # cprint('{} умерла от депрессии!'.format(self.name), color='red')
            self.live = False

    def clean_house(self):
        if self.house.dust >= 100:
            self.house.dust -= 100
        else:
            self.house.dust = 0
        self.satiety -= 10
        self.happy -= 10
        # cprint('{} убралась!'.format(self.name), color='yellow')

    def pet_the_cat(self, cat):
        self.happy += 5
        # cprint('{} гладила кота!'.format(self.name), color='blue')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.house = house
        self.live = True

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.satiety)

    def act(self):
        if self.satiety <= 0:
            # cprint('{} умер от голода!'.format(self.name), color='red')
            self.live = False
        elif self.satiety < 20:
            self.eat()
        elif random.choice([True, False]):
            self.sleep()
        else:
            self.tear()

    def eat(self):
        if self.house.cat_food < 10:
            pass
            # cprint('Еды нет, {} голодный!'.format(self.name), color='red')
        else:
            self.satiety += 20
            self.house.cat_food -= 10
            # cprint('{} поел!'.format(self.name), color='green')

    def sleep(self):
        self.satiety -= 10
        # cprint('{} спит!'.format(self.name), color='yellow')

    def tear(self):
        self.satiety -= 10
        self.house.dust += 5
        # cprint('{} Дерет обои!'.format(self.name), color='cyan')


# murzik = Cat(name='Мурзик')
# home = House(cat=murzik)
# murzik.house = home
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.dust += 5
#     serge.act()
#     masha.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(murzik, color='cyan')
#     cprint(home, color='cyan')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self, name, house):
        self.name = name
        self.happiness = 100
        self.satiety = 50
        self.house = house
        self.live = True

    def __str__(self):
        return 'Я - {}, сытость {}, счастье {}'.format(
            self.name, self.satiety, self.happiness)

    def act(self):
        if self.satiety <= 0:
            self.live = False
            # cprint('{} умер от голода!'.format(self.name), color='red')
        elif self.satiety < 50:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.satiety += 10
            self.house.food -= 10
            # cprint('{} поел!'.format(self.name), color='green')
        elif self.house.food <= 0:
            pass
            # cprint('{} глодает!'.format(self.name), color='red')
        else:
            self.satiety += self.house.food
            self.house.food = 0
            # cprint('{} поел!'.format(self.name), color='green')

    def sleep(self):
        self.satiety -= 5
        # cprint('{} спит!'.format(self.name), color='green')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


class Simulation:

    def __init__(self, _money_incidents, _food_incidents):
        self.money_incidents = _money_incidents
        self.food_incidents = _food_incidents
        self.home = House()
        self.serge = Husband(name='Сережа', house=self.home)
        self.masha = Wife(name='Маша', house=self.home)
        self.kolya = Child(name='Коля', house=self.home)

    def check_alive(self, cats):
        # cprint(self.serge.live, color='yellow')
        # cprint(self.masha.live, color='yellow')
        for cat in cats:
            if not cat.live:
                return False
        if not self.serge.live:
            return False
        elif not self.masha.live:
            return False
        elif not self.kolya.live:
            return False
        else:
            return True

    def experiment(self, _salary):
        self.home.food = 50
        self.home.money = 100
        self.home.cat_food = 30
        self.serge.live = True
        self.serge.satiety = 30
        self.serge.happy = 100
        self.serge.salary = _salary
        self.masha.live = True
        self.masha.happy = 100
        self.masha.satiety = 30
        if self.money_incidents:
            period_money_incidents = 365 / self.money_incidents
        else:
            period_money_incidents = 0
        if self.food_incidents:
            period_food_incidents = 365 / self.food_incidents
        else:
            period_food_incidents = 0

        _life = True
        cats = []
        while _life:
            cats.append(Cat(name='cat_name', house=self.home))
            for day in range(365):
                if period_food_incidents == day:
                    period_food_incidents += period_food_incidents
                    self.home.food = 0
                if period_money_incidents == day:
                    period_money_incidents += period_money_incidents
                    self.home.money = 0
                # cprint('================== День {} =================='.format(day), color='red')
                self.serge.act()
                self.masha.act()
                self.kolya.act()
                for cat in cats:
                    cat.act()
                if not self.check_alive(cats):
                    break
                # cprint(self.serge, color='cyan')
                # cprint(self.masha, color='cyan')
                # cprint(self.kolya, color='cyan')
                # cprint(self.home, color='cyan')
                # cprint("Котов {}".format(len(cats)), color='cyan')
            _life = self.check_alive(cats)
        return len(cats)


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
for food_incidents in range(6):
    cprint("food_incidents= {}".format(food_incidents), color='red')
    for money_incidents in range(6):
        cprint("money_incidents= {}".format(money_incidents), color='red')
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            cprint("salary= {}".format(salary), color='red')
            max_cats = life.experiment(salary)
            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
