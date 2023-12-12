## этот знак нужен для комментария
# print("результат ", 5, 6, ".", sep="", end="\n")
# print("\" 2 \nстрока")
# print("\t символ табуляции")
## print("в print можно производить математические действия пример :", 5 + 10)
## print("функция min выдает минимальное значение", min(3, 2, 4, 5, 6, 1, -2), "
# \nТак же есть противоположная функция max",
#       max(1, 2, 100, 15, 1.5, 100.5))
# a = random.randint(1, 9)
# print(a, "введите это число в строке ниже")
#
# b = input("введите число ")
#
# if not b:
#     print("строчка пустая")
# if not b.isdigit:
#     print("введите цифру")
# else:
#     b = int(b)
#     if b == 1:
#         print("вы угадали ", int("1"))
#     elif b > 9:
#         print("выше 9 низя")
#     elif b > 1:
#         print("попробуй снова")
# text = list(input())
# # # print(text)
# result = list()
# for char in text:
#     result += char
#     print(result)
import math


# # это список или массив он в питоне может принимать различные типы данных
# nums = [1, 2, 3, 4, 5]
# print(nums)
# # для пресвоение нового значения к элементу используется след конструкция
# nums[2] = 10
# print(nums)
# # можно использовать [-1] для обращения к последнему элементу массива
# print(nums[-1])
# # массив или список так же может быть и вложенным в другой массив список
# nums = [1, 2, 3, 4, 5, [106, 200, 203]]
# print(nums)
# # обращатся к списку или массиву в списке или массиве след образом
# print(nums[-1][0])
# nums = [1, 2, 3, 4, 5]
# print(nums)
# # для добавления элемента нужно использовать метод append тк питон не строго типизированный язык
# # мы можем добавлять разные типы данных в 1 массив или список
# # метод .insert позволяет нам задать индекс элемента в списке и добавить его оо смещением
# # предыдущего элемента дальше по списку или массиву
# nums.append(1234)
# nums.insert(0, True)
# print(nums)
# # метод extend позволяет добавить нам список из нескольких элемментов в конец списка или массива
# new_list = [1, False]
# nums.extend(new_list)
# print(nums)
# # для сортирофки списка можно использовать метод sort но данный метод не сможет
# # от сортировать список если в нем есть еще 1 вложенный список
# nums.sort()
# print(nums)
# nums.reverse()
# # print(nums)
# # переменная .pop удаляет последний элемент или ессли задан индекс то удалять по индексу
# # nums.pop()
# # print(nums)
# nums.pop(1)
# print(nums)
# # а метод .remove удалить элемент определенного значения
# nums.remove(1)
# print(nums)
# nums.remove(1234)
# print(nums)
# # для удаления всего используется метод .clear
# nums.clear()
# print("дальше идет метод clear")
# print(nums)
#
# # метод .count позволяет подсчитать элементы с заданным значением
# print(nums.count(1))
# True принимается как 1
# # для подсчета размера массива или списка используется метод len
# print((len(nums)))

# range = int(input("введите размер списка :"))
# element = []
# i = 0
# while i < range:
#     user_element = input("введите элемент #" + str(i) + ":")
#     element.append(user_element)
#     i += 1
# print(element)
# # print(len(element))
# print(element.count("1"))

# список можно разделить при помощи метода .split(по заданному элементу)
# primer = "футбол Баскетбол бейсбол"
# primer_split = primer.split(" ")
# print(primer.split(" "))
# print(primer_split[0])
#
# for i in range(len(primer_split)):
#     primer_split[i] = primer_split[i].capitalize()
#
# print(primer_split)
# # для объединения списка используется метод .join
# result = " ".join(primer_split)
# print(result)
## ниже указан пример среза [:] он делается через двоеточие
# fart = "1 2 3 4 5 6 7 8 9 10 11 12"
# fart_splite = fart.split(" ")
# print(fart_splite[::-1])
# ## если поставить еще : то мы настроем шаг с которой мы идем по срезу
# print(fart_splite[0: :2])


# text = input("введите текст: ")
# text_split = text.split(" ")
# rev = str()

# for i in text_split:
#     rev += i[::-1]
#     ran = text_split.index(i)
#     print(len(text_split)-1)
#     if ran < len(text_split)-1:
#         rev = rev.capitalize() + " "
# print(rev)

## кортежи тоже самое что и спмски но не изменяемые и показываются они в круглых скобках
# kort = ("привет", "мир", "это", "я", "да")
# ## пример попытки изменить кортеж который вызовет ошибку
# # kort[0] = 1
# ## ниже приведены методы для обращения к кортежам
# print(kort.count(1))
# print(len(kort))
# print(kort[0:2])
# for el in kort:
#     print(kort.index(el))
#     # index = kort.index(el)
#     # print("индэкс: ",index,"элемента: ",el)
# ## преобразование списка в кортеж делается с помощью функции tuple()
# list_data = [1,2,3,5]
# new_data = tuple(list_data)
# print(new_data)
##  для создания словаря используется либо {} либо функция dict() словарь заменяет индекс на ключи по
## которым мы обращаемся к элементам
# slovar = {
#     "name": "Timur",
#     "surname": "Gorinskiy",
#     "patronymic": "Eduardovich"
# }
#
# slovar_v2 = dict(
#     code="Ru",
#     country="Russia",
#     population="144 milions"
# )
#
# print(slovar["name"])
# print(slovar_v2["country"])
# ## для вывода словаря в ввиде кортежа используется метод items.
# print(slovar.items())
# for key, value in slovar.items():
#     print(key + " - " + value)
## метод .get аналогчен [] скобкам пример снизу
# print(slovar.get("name"))
## для очистки словоря используется метод .clear
# print(slovar.clear())
## для удаления элемента можно использовать метод .pop обращаясь по ключу
# slovar.pop("name")
# print(slovar)
# ## метод .popitem всегда удаляет последний элемент словоря
# slovar.popitem()
# print(slovar)
# ## для обращения к ключам и значениям в словре используются методы .keys и .values
# print(slovar_v2.keys())
# print(slovar_v2.values())
## для изменения значения нужно обратится по коду и потом уже заменять
# slovar_v2["code"] = "none"
# print(slovar_v2)
# словари моргут быть любой вложенности пример ниже
users = {
    "user_1":{
        "Profile":{"name":"Eduard", "sername":"Gaiak", "age":"24"},
        "pasport":(1234, 3354667464),
        "hobbies":["Dnd","Dota 2","code"]
    },
    "user_2":{

    },
    "user_3":{

    },
}
users["user_1"]["hobbies"][0]= "none"
print(users["user_1"]["Profile"]["name"])
print(users["user_1"]["pasport"][0])
print(users["user_1"][ "hobbies"])

## функцияset() отвечает за создание множеств (в множествах удаляются все
# повторяющиеся элементы и перемешиваются в случайном порядке)
# mnojestvo = set("hello")
# print(mnojestvo)
# ## множество можно выразить в фигурных скобках просто не указывая ключ
# mnojestvo_v2 = {2, 2, 1, 3, 5}
# print(mnojestvo_v2)
## ниже будут представленны методы .add добавить 1 элемент
# // .uppdat добавить несколько элементов
# // .remove убрать конкретный элемент
# // .pop удалить первый элемент
# // .clear удалить все элементы
# mnojestvo_v2.add(32)
# print(mnojestvo_v2)
# mnojestvo_v2.update([32, 33, 31])
# print(mnojestvo_v2)
# mnojestvo_v2.pop()
# print(mnojestvo_v2)
# mnojestvo_v2.clear()
# print(mnojestvo_v2)

## можно создать множество которое нельзя будет изменять (сделать из множество что-то похожеее на кортеж)
## для этого используем функцию .frozenset

# static_mnojestv = frozenset(mnojestvo_v2)
# print(static_mnojestv)
## пример того что его нельзя изменить
# static_mnojestv.add(3)
# static_mnojestv[0] = [1]
# print(static_mnojestv)

## функция создается с помощью оператора def
def revers_text(word):
    # word = input("введите текст: ")
    word_split = word.split(" ")
    rev = str()
    for i in word_split:
        rev += i[::-1]
        ran = word_split.index(i)
        if ran < len(word_split)-1:
            rev = rev.capitalize() + " "
    print(rev)

word = input("введите текст: ")
revers_text(word)

def input_mass():
    massiv = []
    it = 0

    dano = [[], [], []]
    pus_mass = []
    count = 0
    sircle = 0
    pus_znach = 0

    while it < 9:
        a = int(input("введите число :"))
        massiv.append(a)
        it += 1
    it = 0

    for i in massiv:
        count += 1
        pus_mass.append(i)
        if count % 3 == 0:
            dano[sircle] = pus_mass
            sircle += 1
            pus_mass = []
        if i == 0:
            pus_znach += 1
    sircle = 0

    if pus_znach != 3:

        dano_rev = [[], [], []]
        for i in dano:
            pus_mass = i[::-1]
            dano_rev[sircle] = pus_mass
            sircle += 1

        sum_1 = ()
        sum_2 = ()
        while it <= 1:
            sum_2 = (dano[0][0] * dano[1][1] * dano[2][2]
                     + dano[0][1] * dano[1][2] * dano[2][0]
                     + dano[0][2] * dano[1][0] * dano[2][1])
            dano = dano_rev
            if it == 0:
                sum_1 = sum_2
            it += 1
        sum_opred = sum_1 - sum_2

        print(sum_opred)
    else:
        print("есть нулевая строка ответ 0")



def metod_triug(dano):
        sircle = 0
        pus_mass_rev = []
        dano_rev = [[], [], []]
        for i in dano:
            pus_mass_rev = i[::-1]
            dano_rev[sircle] = pus_mass_rev
            sircle += 1
        it = 0
        sum_1 = ()
        sum_2 = ()
        while it <= 1:
            sum_2 = (dano[0][0] * dano[1][1] * dano[2][2]
                     + dano[0][1] * dano[1][2] * dano[2][0]
                     + dano[0][2] * dano[1][0] * dano[2][1])
            dano = dano_rev
            if it == 0:
                sum_1 = sum_2
            it += 1
        sum_opred = sum_1 - sum_2
        print(sum_opred)

# def triugol ():

    # sircle = 0
    # pus_mass_rev = []
    # dano_rev = [[],[],[]]
    # for i in dano:
    #     pus_mass_rev = i[::-1]
    #     dano_rev[sircle] = pus_mass_rev
    #     sircle += 1
    # it = 0
    # while it < 0:
    #     a = dano
    #     if it < 0:
    #         sum_tringl = (a[0][0]*a[1][1]*a[2][2]
    #                      +a[0][1]*a[1][2]*a[2][0]
    #                      +a[0][2]*a[1][0]*a[2][1])
    #         it += 1
    #     else:
    #         a = dano_rev
    #         sum_tringl_rev = sum_tringl

    # print(sum_tringl_rev)


#     # sum_tringl_revers = (dano[0][2]*dano[1][1]*dano[2][0]
#     #                     +dano[0][0]*dano[1][2]*dano[2][1]
    #                     +dano[0][1]*dano[1][0]*dano[2][2])
    # opredel = sum_tringl - sum_tringl_revers
    # print("определитель равен :", opredel)


# for i, e, c in dano:
#     ras1 = i,e,c
#     # if count == 1:
#     #     ras2 = i, e, c
#     #     count += 1
#     #     print(ras2)
#     # if count == 2:
#     #     ras3 = i, e, c
#     #     count += 1
#     #     print(ras3)
#     print(ras1)


## решение нормального человека
# mass = [1,2,3,4,5,6,7,8,9]
# matrix = [[],[],[]]
# count = 0
# circle = 0
#
# for i in mass:
#     if count == 3:
#         circle += 1
#         count = 0
#     matrix[circle].append(i)
#     count += 1
#
# print(matrix)

## для создания файла используется функция open() для записи используется формат
# 'w' а для добавления 'a' существуют и другие форматы


# sozdan_file = open('data/text.txt','w')
# ## для закрытия файла необходимо использовать метод (функцию) .close
# ## для записи в файл используется метод .write
# data = input("say to me: ")
# sozdan_file.write("hello world\n")
# sozdan_file.write("its me")
# sozdan_file.write(" Timur\n")
# sozdan_file.write(data + "\n")
# sozdan_file.close()

# ## для чтения файла используется формат 'r'
# read_file = open('data/text.txt', 'r')
# ## число в скобках указывает число символов для вывода
# # print(read_file.read())
# for line in read_file:
#     print(line, end="")
# read_file.close()
#
# ## конструкиця блок try: позволяет отследить заданную ошибку и если она срабатывает то начинается
# ## чтения кода except: пример ниже

def proverka_mass():
    tot = True
    while tot is True:
        try:
            input_mass()
            tot = False
        except ValueError:
            print("введите числа")
        ## блок else: срабатывает только если сработал try:
        else:
            print("ответ")
        ## после блок finally прописывается что выводится при любом результате
        finally:
            print("в любом случае")

def massiv_search():

    try:

        dano = input("введите цифры")
        finde = int(input("найти число :"))
        id_el = ()
        sicrle = 0
        el_summ = 0
        first_id = 0
        otvet =[[],[]]

        for el in dano:
            el = int(el)
            sicrle += 1

            if finde == el:
                id_el = sicrle - 1
                el_summ += 1
                otvet[1] = el_summ

            if el_summ == 1:
                first_id = id_el
                otvet[0] = first_id
        print(otvet)

    except ValueError:
        print("лучше ввести цифру")

## менеджер (конструкция, блок) with и as ( в скобках указываем путь и параметр действий с файлом (чтение запись
# и т д) а 3 encoding+  пункт это кодировка которой мы будем читать файл utf-8 базовая кодировка для чтения латыницы
# и кирилицы после as указываем имя. При открытие данного блока прописывать close() не нужно тк он закроется сам в
# блоке weith

# import time
#
# try:
#     with open('data/text.txt', 'r', encoding='utf-8') as datas:
#         time_plus = 0
#         for lane in datas:
#             time.sleep(time_plus)
#             print(lane, end="")
#             time_plus += 1
# except FileNotFoundError:
#     print("файл не найден")

## Импорт модулей (библиотек) осуществляется благодаря менеджеру или блоку import пример ниже импорт библиотеки time



## для обращения к функциям библиотеки необходимо сначало прописать ее название time.
## sleep() позволяет заморозить программу на определенное количество сек

import time
## название импортированной библиотеки можно сокрощать по средствам

import datetime as D

try:
    with open('data/text.txt', 'r', encoding='utf-8') as datas:
        time_plus = 0
        for lane in datas:
            time.sleep(time_plus)
            if time_plus == 0:
                print(lane, D.datetime.now().date(), end="\n")
            else:
                print(lane, end="")
            time_plus += 1
except FileNotFoundError:
    print("файл не найден")

## для импорта сразу нескольких библиотек просто ставим после библиотеки , и пишем след

import sys, os, platform
print(platform.system())
print(sys.platform)
# print(os.path)

## Импротировать можно конкретный элемент библиотеки
from math import sqrt, ceil
print(sqrt(25))
print(ceil(math.sqrt(30)))

## импортирую свою библиотеку
import Sozdanie_biblioteki as Sb

print(Sb.proverka_mass())

