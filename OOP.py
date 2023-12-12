## класс создается с помощью конструкции class:
class dog:
    ##переменные внутри класса называются полями
    name = None
    age = None
    isHappy = None

    ## ниже будет продемонстрирован конструктор __init__ который позволяет принимать значения при
    # обращении объекта к классу
    ## если установить значение по умолчанию то в случе когда не хватает данных значений в объекте
    ## будут показыватьзя изначально заданные
    def __init__(self, name = None, age = "пустое поле", isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        ## ниже мы показываем что мы обращаемся к функции внутри класса за счет метода self.
        # self.set_data(name, age, isHappy)
        self.get_data()
## создаем функцию self означает что обращение идет к классу и его полям
    def set_data(self,  name = "пустое поле", age = "пустое поле", isHappy = "пустое поле"):
        ## показываем что обращаемся к полям класса по средствам метода self.
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print("Имя пса :", self.name, "\nвозраст пса:",self.age, "\nи он счаслив ", self.isHappy, "\n")


dog3 = dog("tuzik",2,)

## ниже dog1 = dog() мы показываем что мы создаем объект на основе класса dog
# dog1 = dog()
## обращаемся к свойствам класса по средствам указания поля .name , .age и т д

# dog1.input_pass(name="tuzik",age=2,isHappy=True)
# dog1.set_data("tuzik",2,True)
# dog1.get_data()
#
# dog2 = dog()
# dog2.name = "sharik"
# dog2.age = 3
# dog2.isHappy = False
# print(dog2.name, dog2.age, dog2.isHappy)

## наследование или подкласс создается следующим методом
## подкласс позволяет разгрузить награможденность основного (супер-класса) но при этом позволяет пользоваться его
# функциями и полями
class paroda(dog):
    calor = None
    hair = None
    paroda = None

    def __init__(self, calor="пустое поле", hair="пустое поле"):
        super().__init__()
        self.calor = calor
        self.hair = hair

    def opred_paroda(self, calor = "пустое поле", hair= "пустое поле"):

        if calor == "black":
            self.paroda = "buldog"
            print("buldog")
            print("с шерстью длинной: ", hair)

        if calor == "bown":
            self.paroda = "ovcharka"
            print("ovcharka")
            print("с шерстью длинной: ", hair)

class spashl(paroda):
    def question(self):
        if self.paroda == "ovcharka":
            print("\nверный друг и помошник")
        if self.paroda == "buldog":
            print("\nпожилой пердун")

        question = input("Задайте свой вопрос касаемо: ухода или лечения")
        if question == "уход" and self.paroda == "ovcharka":
            print("гладить каждый день")
        if question =="уход" and self.paroda == "buldog":
            print("чесать за ушком")


dog4 = spashl()
dog4.set_data("tuzik",2,True)
dog4.opred_paroda("black","short")
dog4.question()
pop = "fflfflfl"

