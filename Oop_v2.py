# class Computer:
#     price = None
# class VideoCard (Computer):
#     cards = {
#         "низкая цена":{
#             "радион":{
#                 "п600":"10000 r",
#                 "еп1030":"13000 r"
#             },
#             "палит":{
#                 'pal100':"20000 r",
#                 'gor320':"18000 r"
#             }
#         },
#         "средняя цена":{
#             'gygabite':{
#                 "rtx 3060 ti":'30000 r',
#                 "rtx 4060 ti":'60000r'
#             },
#             'asus':{
#                 'rtew10-0':'45000 r',
#                 'meteor1020':'50000 r'
#             }
#         },
#         "высокая цена":{
#             "Msi":{
#                 'Dragon perd':'1000000 r',
#                 'Govno iz jopi':'2000000 r'
#             }
#         }
#     }
#     cards_prise = input(cards)
# class WaterCooling(VideoCard):
# class Motherboard (Computer):
# class HardDrive(Motherboard):
# class RMemory(Motherboard):
# class processor (Computer):
# class cooler (processor):
# class PowerUnit (Computer):
import random


class Char:

    def __init__(self, hp: int, mana: int, stamina: int, luck: int, lvl: int, clas: str):
        self._clas = clas
        self._lvl = lvl
        self._hp = hp * lvl
        self._mana = mana * lvl
        self._stamina = (stamina * lvl) / 2
        self._luck = luck


    def getter(self):
        print(self._hp, self._mana, self._stamina, self._luck)

    def check(self):

        if self._clas == "танк":
            self._hp = self._hp * 2
        if self._clas == "охотник":
            self._stamina = self._stamina * 2
        if self._clas == "прист":
            self._mana = self._mana * 2

        while True:
            circle = 0
            user = input("введите интересующий стат: ")

            try:

                stats = {
                    "lvl": str(self._lvl),
                    "hp": str(round(self._hp)),
                    "mana": str(round(self._mana)),
                    "stamina": str(round((self._stamina)))
                }
                print(stats[user])

                while circle == 0:

                    user_answer = input("это все (да/нет): ")
                    if user_answer == "да":
                        circle += 1
                        return False
                    if user_answer == "нет":
                        circle += 1
                        pass
                    elif user_answer != "да" or user_answer != "нет":
                        print("введите ответ да или/нет")

            except KeyError:
                print("введите 1 из следующих статов \"lvl\", \"hp\",\"mana\",\"stamina\".")


class UserChar(Char):

    def __init__(self, hp: int, mana: int, stamina: int, luck: int, lvl: int, clas: str,
                 armor: int):
        super().__init__(hp, mana, stamina, luck, lvl, clas)
        self._armor = armor
        self._damage = round((random.randint(1,self._luck) * self._lvl) / 2)

        self._fire_ball = self._mana * 1.3
        self._fire_arrow = (self._mana * 0.3) * 3
        self._heal = self._mana / 0.2
        self._ice_coulb = self._mana / 0.2

    def spels(self):

        proc = (self._mana / 100) * self._lvl
        spel_list = {
            "Школа огня":{
                "Огненный шар": f"Снаряд с мгновенным уроном: {round(self._fire_ball)}",
                "Огненные стрелы": f" Три стрелы с уроном: {round(self._fire_arrow)}"
        },
            "Школа воды":{
                "Лечение ран": f"Лечит в течении 2 сек на: {str(self.heal)}",
                "Ледяная колба": f"Наносит урон: {self._ice_coulb} и заморозит на {self._mana / 100}сек"
            },
            "Школа воздуха":{
                "Увороты" : f"Дает уворот в течении {round((self._mana * self._stamina) / proc)}"
            }
        }

        while True:
            user = input("Введите одну из школ \n" + str('\n'.join(spel_list.keys()) + "\nВыбор: "))
            circle = 0
            uns = 0
            if user == "выход":
                return False

            if user == "Школа огня":
                print(f'Огненный шар: {spel_list["Школа огня"]["Огненный шар"]}\n'
                      f'Огненные стрелы: {spel_list["Школа огня"]["Огненные стрелы"]}')
                uns += 1

            if user == "Школа воды":
                print(f'Лечение ран: {spel_list["Школа воды"]["Лечение ран"]}\n'
                      f'"Ледяная колба" {spel_list["Школа воды"]["Ледяная колба"]}')
                uns += 1

            if user == "Школа воздуха":
                print(f'Увороты: {spel_list["Школа воздуха"]["Увороты"]}')
                uns += 1

            if uns > 0:
                while  circle == 0:
                    user_unswer = input("Dы узнали все что хотели (да/нет) :")

                    if user_unswer == "да":
                        circle += 1
                        return False
                    elif user_unswer == "нет":
                        circle += 1
                    else:
                        print("пожалуйста напишите да / нет\n")
            else:
                print("Выберите одну из школ или напишите выход.\n")

class Mob(UserChar):
    def __init__(self, hp: int, mana: int, stamina: int, luck: int, lvl: int, armor: int,
                 clas: str):
        super().__init__(hp, mana, stamina, luck, lvl, clas, armor)




# class User_Char(Char):
#     def __int__(self, hp: int, mana: int, stamina: int, luck: int, lvl: int, clas: str,
#                 armor: int, damage: int):
#         super().__int__(hp, mana, stamina, luck, lvl, clas)
#         armor = lvl
#         damage = lvl * luck
#         print(f"ваша защита : {armor} "
#               f"ваща атака : {damage}")



timur = UserChar(10,10,10,10,10,"танк", 10)
skel = Mob(10,10,10,10,10,12,12,"охотник")
print(skel._armor)
print(timur._damage)


class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Марка: {self.make}"
        f"\nМодель: {self.model}"
        f"\nГод выпуска: {self.year}"
        f"\nСтоимость: {self.price} руб")

class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors, body_style):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors
        self.body_style = body_style

class Truck(Vehicle):
    def __init__(self, make, model, year, price, bed_length, towing_capacity):
        super().__init__(make, model, year, price)
        self.bed_length = bed_length
        self.towing_capacity = towing_capacity
