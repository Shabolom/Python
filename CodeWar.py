import random
import string, math


def square_digits(num):
    # Your code here
    num = str(num)
    sqr = ()
    mass = []
    string = str()

    for i in num:
        sqr = int(i)
        sqr *= sqr
        mass.append(sqr)

    for el in mass:
        string += str(el)

    return print(int(string))


# square_digits(223456)

def likes(names):

    el_text = ""
    id_el = 0
    first_name = str()
    second_name = str()
    therd_name = str()

    for el in names:
        id_el = names.index(el) + 1
        el_text = el
        if id_el == 1 and id_el < 2:
            first_name = el_text
        if id_el == 2 and id_el < 3:
            second_name = el_text
        if id_el == 3 and id_el < 4:
            therd_name = el_text

    if id_el == 1:
        return first_name + ' likes this'
    if id_el == 2:
        return first_name + ' and ' + second_name + ' like this'
    if id_el == 3:
        return first_name + ', ' + second_name + ' and ' + therd_name + ' like this'
    if id_el > 3:
        return first_name + ', ' + second_name + ' and ' + str(id_el - 2) + ' others like this'

    return 'no one likes this'

# print(likes([]))
# print(likes(['Jacob', 'Alex']))
# print(likes(['Max', 'John', 'Mark']))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'pall']))

## метод 1 перевод числа в строку
## метод 2 перевод стоки в число (Ascii)


# if 2175 == ord("р"):
#     print("hui")

def textToAscii():

    dano = input("Введите текст: ")
    el_ascii = []
    ascii_str = ""

    for el in dano:
        ascii_str = str(ord(el))
        # ascii_text += ascii_str
        el_ascii.append(str(ord(el)))
    ascii_text = " ".join(el_ascii)

    return str(ascii_text)


def asciiToText():

    ascii_dano = input("введите ascii код: ")
    ascii_split = ascii_dano.split(" ")
    ascii_word = ""
    for el in ascii_split:
        el = int(el)
        ascii_word += chr(el)

    return str(ascii_word)

# cards = {
#         "низкая цена": {
#             "радион": {
#                 "п600": "10000 r",
#                 "еп1030": "13000 r"
#             },
#             "палит":{
#                 'pal100': "20000 r",
#                 'gor320': "18000 r"
#             }
#         },
#         "средняя цена": {
#             'gygabite': {
#                 "rtx 3060 ti": '30000 r',
#                 "rtx 4060 ti": '60000r'
#             },
#             'asus': {
#                 'rtew10-0': '45000 r',
#                 'meteor1020': '50000 r'
#             }
#         },
#         "высокая цена": {
#             "Msi": {
#                 'Dragon perd': '1000000 r',
#                 'Govno iz jopi': '2000000 r'
#             }
#         }
#     }
# user = input("какого сегмента карта:")
# user_chois = ' '.join(cards[user].keys())

# print(user_chois)

def check_valid(value:str):
    """проверяет на закрытие скобки"""
    count = 0
    count_zero = 0
    # ror = len(value) % 2
    # print(ror)
    if value.index(value[-1]) == 0:
        return False
    for el in value:
        if count > count_zero:
            return False
        if value.index(el) == 0:
            count_zero += 1
        else:
            count += 1
    if count == count_zero:
        return True
    else:
        return False

# print(check_valid("()())))("))
# assert check_valid('()') == True
# assert check_valid("()(") == False
# assert  check_valid("()()") == True
# assert  check_valid("((()()") == False
# assert  check_valid("()()))") == False
# assert  check_valid("(()(()") == False


def serch_sum_9(mass:list)->str:
    """принимает массив интов возвращая 2 элемента сумма которых равна 9"""
    # circle = 1
    # it = 0
    # sums = 0
    # i = 1
    # first = []
    # case = []

    # while circle != len(mass):
    #     for el in mass:
    #         sums = mass[it] + el
    #         if sums == 9:
    #             first = [mass[it],el]
    #             case.append(first)
    #             i += 1
    #         if sums != 9:
    #             i += 1
    #         if i == len(mass) + 1:
    #             i = 1
    #             it += 1
    #             circle += 1
    #
    # circle = 0
    # key1 = 0
    # valu1 = 0
    # case2 = []
    # for key2, valu2 in case:
    #     circle += 1
    #     if key1 == key2 or key1 == valu2:
    #         first = key2,valu2
    #         case2.append(first)
    #     if circle > 1:
    #         key1 = key2
    #         valu1 = valu2
    #     circle += 1
    # print(case2)
    # return case

def edos(mass:list)->str:
    """мастер класс"""
    mass = list(set(mass))
    resul = []
    for i, el in enumerate(mass):
        count = i + 1
        while count < len(mass):
            if el + mass[count] == 9:
                resul.append(f"[{el}, {mass[count]}]")
            count += 1
    str_resul = ", ".join(resul)
    return str_resul

print(edos([1,8,3,4,5,6,7,-1,9,10,8]))

def binar_sum_one(num:int)->int:
    """перевод в бинарный и возвращение количества единиц"""
    return format(num, 'b').count("1")

def alf(text:str)->bool:
    """проверяет на нахождение в тексте всех букв алфовитов"""
    text = set(text.lower())
    count = 0
    for el in text:
        ask = ord(el)
        if 97 <= ask <= 122:
            count += 1
    return count == 26
# ниже приведен пример записи в одну строку при помощи метода a.issubset(b) мы проверяем находится ли значение
# переменно a внутри переменной b
# def is_pangram(s):
#     return set(string.ascii_lowercase).issubset(s.lower())

print(alf("The quick, brown fox jumps over the lazy dog!"))
# for el in num:
#     if int(el) > 0:
#         one += 1

# if el >= 97 and el <= 117 and el not in mass:

# ffk = [1,2,3,4,5,1,1,1,1]
# for el in ffk:
#     print(ffk[el])
#
# my_list = [3, 5, 4, 2, 2, 5, 5]
# print("Indices and values in my_list:")
# for index, value in enumerate(my_list):
#     print(list((index, value)))


def CaesarCipher(text:str)->str:
    """шифр цезаря: возвращает текст со смещением на 11 букв по алфовиту"""

    aski = 0
    aski_plus = 0
    text_cezar = []

    for el in text:

        aski = ord(el)

        if ord(el) <= 64 or 91 <= ord(el) <= 96 or ord(el) >= 123:
            text_cezar.append(f"{chr(aski)}")

        if 65 <= ord(el) <= 79 or 97 <= ord(el) <= 112:
            aski += 11
            text_cezar.append(f"{chr(aski)}")

        if 90 > ord(el) > 80 or 122 > ord(el) > 112:
            aski_plus = (aski + 11) - 90
            aski = 64 + aski_plus
            text_cezar.append(chr(aski))

    return "".join(text_cezar)



def cesar_Edos_ne_nrav(text:str, slice:int):
    """еще 1 вариация шифра цезаря через обращение по индексам"""

    non = string.ascii_letters
    result = ""
    for el in text:
        if el in non:
            if 0 <= non.index(el) <= 25 - slice or 26 <= non.index(el) <= 51 - slice:
                result += non[non.index(el) + slice]
            elif non.index(el) <= 25:
                result += non[slice - (26 - non.index(el))]
            else:
                result += non[slice - (52 - non.index(el)) + 26]
        else:
            result += el
    print(result)

cesar_Edos_ne_nrav(f"{string.ascii_letters}", 0)
print(string.ascii_letters)


def math_sqr_search(num: int) -> bool:
    """данная функция принимает в себя число и дает ответ являетсяли оно совершенным квадратом"""
    if num == -1:
        return False
    if num == 0:
        return True
    if num < 0:
        num = num * (-1)
        return num / round(math.sqrt(num)) == math.sqrt(num)
    return num / round(math.sqrt(num)) == math.sqrt(num)


print(math_sqr_search(-1))
# пример записи в 1 строку
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;


def persistence(num: int) -> int:
    """хз как описать """
    num = str(num)
    count = 0
    if len(num) == 1:
        return len(num) - 1
    while len(num) > 1:
        sum_num = 1
        for el in num:
            sum_num *= int(el)
        num = str(sum_num)
        count += 1
    return count


print(persistence(9999))


def revers_if_5words(text: str) -> str:
    """реверсируем слово если в нем есть 5 букв"""
    text = text.split(" ")
    count = 0
    for el in text:
        word = el
        if len(word) >= 5:
            word = word[::-1]
            text[count] = word
        count += 1
    return " ".join(text)

print(revers_if_5words("This,, sentence is a sentence"))


def two_sum(numbers: list, target: int) -> tuple:

    output = []
    first = ()

    for id, ele in enumerate(numbers):
        for i, el in enumerate(numbers):
            if id != i and ele + el == target:
                first = tuple([id,i])
                output.append(first)

    return tuple(output)


print(two_sum([1234,5678,9012],14690))


def duplicate_count(text: str) -> str:
    """считаем количество повторений букв в слове"""
    answer = []

    if len(text) == 0 or len(text) == len(set(text)):
        return "answer 0"
    for word in text:
        doopl = text.count(word)
        if doopl >= 2:
            answer.append(f'буква: {word}, повтаряется: {doopl}')

    return ' // '.join(reversed(sorted(set(answer)))) + f' // всего букв с повторением: {len(set(answer))}'


print(duplicate_count('aaaiiIIooOO'))

a = []
n = 10

for i in range(n):
    a.append(random.randint(1, 99))
print(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)


def sort_array(mass:list) -> list:
    """Вам нужно отсортировать нечетные числа в порядке возрастания, оставив четные числа на исходных позициях"""

    for i, el in enumerate(mass):
        count = i + 1
        while count < len(mass):
            if mass[i] % 2 == 1 and mass[count] % 2 == 1 and mass[i] > mass[count]:
                mass[i], mass[count] = mass[count], mass[i]
            count += 1

    return mass




