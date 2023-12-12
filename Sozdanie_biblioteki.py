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


class PublicClass:
    _name = "bob"
    __surname = "hui"

    def __init__(self, name: str):
        self.__name = name

    def get_attrs(self) -> str:
        return self.name


# publicInstance = PublicClass('Публичный класс')
# publicInstance2 = PublicClass('Новый публичный класс')
# print(publicInstance.name, '!=', publicInstance2.name)

# PublicClass.name - Error

# class PrivateClass:
#     name = 'Можно получить название без создания экземпляра'
#
# privateInstance = PrivateClass()
# print(privateInstance.name, '==', PrivateClass.name)
#
# class DecoratorClass:
#     class_value = 'Я значение именно класса'
#
#     def __init__(self, instance_value: str):
#         self.instance_value = instance_value
#
#     @staticmethod
#     def static_method():
#         """
#         Функция которая не зависит от контекста и может вызываться вне ее, в класс она добавлена чисто для логики
#         self - не работает
#         """
#         return 'Я вне этой системы'
#
#     @classmethod
#     def class_method(cls):
#         """
#         Функция которая вызывается только от класса, и имеет его контекст
#         self - не работает, но есть cls - текущий класс
#         """
#         return 'я знаю только что ' + cls.class_value
#
#     def method(self):
#         """
#         Обычная функция, содержит в себе и класс и инстанс
#         """
#         return 'Я знаю только что ' + self.class_value + ' + ' + self.instance_value
#
# instance = DecoratorClass('Я значение инстанса')
# print(instance.static_method())
# print(instance.class_method())
# print(instance.method())
#
# cls = DecoratorClass
# print(cls.static_method())
# print(cls.class_method())
# # print(cls.method()) - Ошибка так как нужен self - а это экземпляр
#
# human = PublicClass("timur")
# print(PublicClass._name)
# print(PublicClass.__surname)


