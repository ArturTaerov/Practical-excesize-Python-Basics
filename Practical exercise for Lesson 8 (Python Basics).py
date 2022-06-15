
#1. Реализовать класс «Дата», функция-конструктор которого должна принимать
#дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
#метода. Первый, с декоратором @classmethod.
#Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
#и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
#на реальных данных.


class Date:
    dat = "12-17-1967"   
    def __init__(self, sp_diap):
        self.sp_diap = sp_diap
       
    @classmethod               
    def met(self, sp_diap):
        sp = self.dat.split("-")
        print(".".join(sp))
        for i in range(len(sp)):
            sp[i]=int(sp[i])
        Date.valid(sp, sp_diap)
        return sp
    
    @staticmethod
    def valid(sp, sp_diap):
        for j in range(len(sp)):
            if sp[j] < sp_diap[j][0] or sp[j] > sp_diap[j][1]:
                print("Вы ввели неверное значение даты!")
                break
        pass

sp_diap = [[1, 31], [1, 12], [0, 2022]]
mc = Date(sp_diap)
mc.met(sp_diap)




# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
# ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class Except:
    @staticmethod        
    def zerodiverror(divisible, divider):
        # метод возвращает None в случае деления на ноль и True, если деления на ноль нет
        x = None
        try:
            divisible/divider
        except ZeroDivisionError:
            print("Нельзя делить на ноль!")
        else:
            x = True
        finally:
            if divider == 0:
                print("Нет результата деления!")
        return x
divis = int(input("Введите делимое: "))
divid = int(input("Введите делитель: "))
Except.zerodiverror(divis, divid)




# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном
# примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов
# списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду
# «stop». При этом скрипт завершается, сформированный список с числами
# выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только
# числа и строки. Во время ввода пользователем очередного элемента необходимо
# реализовать проверку типа элемента. Вносить его в список, только если введено
# число. Класс-исключение должен не позволить пользователю ввести текст
# (не число) и отобразить соответствующее сообщение. При этом работа скрипта не
# должна завершаться.


class Exeption:
    @staticmethod
    def exept(sp0):
        try:
            float(sp0) or int(sp0)    
        except: 
            result = False 
            print("Неверно введенное значение!")
        else:
            result = True
        return result
sp = []
sp0 = input("Введите число либо команду 'stop' для окончания ввода: ")

while sp0 != "stop":
    if Exeption.exept(sp0) == True:
        sp.append(sp0)
    sp0 = input("Введите число либо команду 'stop' для окончания ввода: ")
print(sp)



# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа
# оргтехники.

class Warehouse:
    def __init__(self):
        pass

class Office_equipment:
    def __init__(self, velocity, color):
        self.velocity = velocity
        self.color = color
           
class Printer(Office_equipment):
    def __init__(self, setev):
        self.setev = setev
    
class Scaner(Office_equipment):
    def __init__(self, permission):    
        self.permission = permission

class Хerox(Office_equipment):
    def __init__(self, formate):    
        self.formate = formate



# 5. Продолжить работу над первым заданием. Разработайте методы, которые
# отвечают за приём оргтехники на склад и передачу в определённое подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру
# (например, словарь).

class Warehouse:
    def __init__(self):
        pass

class Office_equipment:
    def __init__(self, quantity, velocity):
        self.quantity = quantity
        self.velocity = velocity
    
class Printer(Office_equipment):
    def __init__(self, setev):
        self.setev = setev
        self.typ = typ
    
class Scaner(Office_equipment):
    def __init__(self, permission):    
        self.permission = permission
        self.typ = typ

class Хerox(Office_equipment):
    def __init__(self, formate):    
        self.formate = formate
   
    


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.

# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум 
# возможностей, изученных на уроках по ООП.


class Warehouse:
    
    def __init__(self):
        pass
 

class Office_equip:
    
    def __init__(self):
        self.sp_inpt = None
        self.sp = []
        self.sp0 = []
        self.sp1 = []
        self.dict_tov = {}
        self.dict_podr = {}
        self.dict_vr = {}
        self.name = None
        self.quantity = 0
        self.velocity = "high"

    def inpt():
    # выводит на печать инструкцию для ввода данных, принимает и возхвращает
    # введенные значения
        x = "Введите через 2 пробела, подразделение, наименование, количество,"
        y = " , тип оргтехники ('принтер', 'сканер' или 'ксерокс'), скорость р"
        z = "аботы (high, medium или low), а также индивидуальные характеристи"
        v = "ки каждого типа оргтехники для принтера: ['сетевой' или 'не сете"
        w = "вой'], для сканера (разрешение): ['600' или '1200'], для ксерокса"
        q = " (формат): ['А4', 'А5'] либо команду 'stop' для окончания ввода: "
        return input(x+y+z+v+w+q)
    
    def izm_dict_tov(self):
    # прибавляем поступление (вычитаем отгрузку) товаров в словарь, в котором
    # ведется общий учет товаров, поступивших во все подразделения
        if (int(self.quantity) < 0) and (abs(int(self.quantity)) == \
                            self.dict_podr.get(self.sp[1]).get(self.name)[0]):
            self.dict_tov.pop(self.name)
        elif (int(self.quantity) < 0) and (abs(int(self.quantity)) > \
                                        int(self.dict_tov.get(self.name)[0])):
            print(f"Количества заданного товара '{self.name}' не хват", end="")
            print("ает! Задайте количество не более ", end="")
            print(f"{self.dict_tov.get(self.name)[0]}", end="")
        else:
            el = int(self.dict_tov.get(self.name)[0]) + int(self.quantity)
            sp1_vr = self.sp1.copy()
            sp1_vr.pop(0)
            sp1_vr.insert(0, el)
            self.dict_tov.update({self.name: sp1_vr})
        if self.dict_tov.get(self.name)[0] == 0:
            self.dict_tov.pop(self.name)
        return self.dict_tov
    
    def izm_dict_podr(self):
    # прибавляем поступление (вычитаем отгрузку) товаров в словарь, в котором
    # ведется общий учет товаров, поступивших в конкретное подразделение
        if (int(self.quantity) < 0) and (abs(int(self.quantity)) == \
                        int(self.dict_podr.get(self.sp[1]).get(self.name)[0])):   
            self.dict_podr.get(self.sp[1]).pop(self.name)
            if len(self.dict_podr.get(self.sp[1])) == 0:
                self.dict_podr.pop(self.sp[1])
        else:
            if (int(self.quantity) < 0) and (self.dict_podr.get(self.sp[1]).\
                                                     get(self.name) == None):
                print(f"Товара '{self.name}' в подразделении", end="")
                print(f" '{self.sp[1]}' в наличии нет!")
            else:
                v = self.dict_podr.get(self.sp[1]).get(self.name)          
                if v == None:
                    v = [0]
                    self.dict_podr.update({self.name: self.sp1.copy()})
                else:
                    self.sp1[0] = str(int(self.sp1[0])+ int(v[0]))
                    dh2 = self.dict_podr.get(self.sp[1])
                    dh2.update({self.name: self.sp1.copy()})
                    self.dict_podr.update({self.sp[1]: dh2})
        return self.dict_podr
        
    
    def plus_minus(self):
        # проводятся подолнительные проверки условий перед вызовом функций
        # по приему и отгрузке товаров в подразделениях
        print("сейчас будем складывать или вычитать")
        if self.sp[1] in self.dict_podr.keys():
            # проверка: есть ли такое подразделение уже есть в словаре
            # подразделений
            if int(self.quantity) > 0:
                Office_equip.izm_dict_tov(self)
                Office_equip.izm_dict_podr(self)  
            elif (self.sp[0] in self.dict_podr.get(self.sp[1]).keys()) and \
                (abs(int(self.quantity)) <= int(self.dict_podr.get(self.sp[1])\
                                                          .get(self.name)[0])):
                Office_equip.izm_dict_tov(self)
                Office_equip.izm_dict_podr(self)  
            else:
                print(f"Товара '{self.name}' в количестве ", end="")
                print(f"{abs(int(self.quantity))} в подразделении", end="")
                print(f" '{self.sp[1]}' в наличии нет!") 
        else:
            if (int(self.quantity) > 0):
                Office_equip.izm_dict_tov(self)
                self.dict_podr.update({self.sp[1]:self.dict_vr.copy()})
            else:
                print(f"Товар '{self.name}' в подразделении в количес", end="")
                print(f"тве {abs(int(self.quantity))} отсутствует!")
            return self.dict_tov, self.dict_podr            

    def delet(self):  
        # обнуляет значения перед очередной итерацией цикла
        self.sp.clear()
        self.sp1.clear()
        self.dict_vr.clear()        
        return self.sp, self.sp1, self.dict_vr
        
    def initzial(self):
        # инициализирует значения перед очередной итерацией цикла
        self.sp1=[self.sp[i+1] for i in range(1,len(self.sp)-1)]
        self.name = self.sp[0]
        self.quantity = self.sp[2]
        self.velocity = self.sp[4]
        self.dict_vr={self.name: self.sp1.copy()}
        return self.sp, self.sp1, self.name, self.velocity, self.dict_vr 

    def start(self):
        def proverka(self):
        # проверяет впервые ли поступил товар, есть ли в словаре подразделение,
        # куда должен поступить товар и записывает в этом случае данные в
        # словарь
            if self.name not in self.dict_tov.keys():
                self.dict_tov.update({self.sp[0]:self.sp1.copy()})
                if len(self.dict_podr) == 0:
                    self.dict_podr.update({self.sp[1]:self.dict_vr.copy()})
                else:
                    if self.dict_podr.get(self.sp[1]) == None:
                        self.dict_podr.update({self.sp[1]:self.dict_vr.copy()})  
                    else:
                        dh = self.dict_podr.get(self.sp[1])
                        dh.update(self.dict_vr.copy())
                        self.dict_podr.update({self.sp[1]: dh})       
            else:
                Office_equip.plus_minus(self)
            return self.dict_tov, self.dict_podr
        prnt = Printer()
        prnt.setev = ("сетевой", "не сетевой")
        scnr = Scaner()
        scnr.permission = ("600dpi", "1200dpi")
        xrx = Хerox()
        xrx.formate = ("А4", "А5")
        sp_equipment={"принтер": prnt.setev, "сканер": scnr.permission, \
                      "ксерокс": xrx.formate}
        velocities=("high", "medium", "low")
        self.sp=Office_equip.inpt().split("  ")
        while (self.sp[0] != "stop"):
            if self.sp[0] == "stop":
                break
            if ((len(self.sp) != 6) or Exeption.exept_numb(self.sp[2]) or \
            (self.sp[3] not in sp_equipment.keys()) or (self.sp[4] not in \
            velocities) or (self.sp[5] not in sp_equipment.get(self.sp[3]))):
                print("Нарушен формат ввода данных!")
                Office_equip.delet(self)
                self.sp=Office_equip.inpt().split("  ")
                continue               
            if (abs(int(self.sp[2])) == 0):
                print("Количество поступившего товара не должно быть", end="")
                print(" нулевым! Введите значение количества товара", end="")
                print(" отличное от нуля!")
                Office_equip.delet(self)
                self.sp=Office_equip.inpt().split("  ")
                continue
            Office_equip.initzial(self)
            
            if ((int(self.quantity) < 0) and (self.dict_podr.get(self.sp[1])\
            != None) and (int(self.dict_tov.get(self.name)[0]) < abs(int(self.\
            quantity)))) or (int(self.quantity) < 0 and (len(self.dict_podr) \
            == 0)) or ((len(self.dict_podr) != 0) and Exeption.exept_dict(self\
            .dict_podr, self.sp[0])) or Exeption.exept_dict(self.dict_podr, \
            self.sp[1]) or (Exeption.exept_dict(self.dict_podr, self.sp[1]) \
            and Exeption.exept_dict(self.dict_podr.get(self.sp[1]),self.name))\
            or ((int(self.quantity) < 0) and Exeption.exept_dict2\
            (self.dict_podr, self.sp, self.name)):              
                print(f"Такого количества товара '{self.name}' в подр", end="")
                print(f"азделении '{self.sp[1]}' в наличии нет!")
                continue
            else:
                if (self.sp[3] == "принтер") and (self.sp[5] in sp_equipment.\
                                                              get(self.sp[3])):
                    proverka(self)
                elif (self.sp[3] == "сканер") and (self.sp[5] in sp_equipment.\
                                                              get(self.sp[3])):
                    proverka(self)
                elif (self.sp[3] == "ксерокс") and (self.sp[5] in \
                                                 sp_equipment.get(self.sp[3])):
                    proverka(self)
                else:
                    print("Нарушен формат ввода данных!")
            Office_equip.delet(self)
            self.sp=Office_equip.inpt().split("  ")                        
        return self.dict_tov, self.dict_podr

class Printer(Office_equip):
    def __init__(self):
        self.setev = ()
    
class Scaner(Office_equip):
    def __init__(self):
        self.permission = ()
    
class Хerox(Office_equip):
    def __init__(self):
        self.formate = ()

class Exeption:
    @staticmethod
    def exept_numb(number):
    # проверяет является ли символ числом
        try:
            float(number) or int(number)
        except:
            result = True
        else:
            result = False
        return result
    
    @staticmethod
    def exept_dict(dic, sp):
    # проверяет существует ли элемент словаря по заданному товару    
        try:
            dic.get(sp)
        except:
            result = True
        else:
            result = False
        return result    

    @staticmethod
    def exept_dict2(dic, sp, name):
    # проверяет существует ли элемент вложенного словаря по заданному товару
        try:
            dic.get(sp[0]).get(name)[0]
        except:
            result = False
        else:
            result = True
        return result        

of_eq = Office_equip()    
of_eq.start()  

# Вывод на печать

dict_print = of_eq.dict_tov.copy()
if len(dict_print) == 0:
    print("Словари пустые!")
else:
    print("Выводим на печать словарь, в котором ведется общий учет то", end="")
    print("варов:\n{")
    for i in range(len(of_eq.dict_tov)):
        print(f"{dict_print.popitem()}")
    print("}\n")   
    print("Выводим на печать словарь, в котором ведется учет товаров ", end="")
    print("в разрезе подразделений:\n{")
    dict_print = of_eq.dict_podr.copy()
    for i in dict_print:
        t = dict_print.get(i)
        print(i, ":")
        print(t)
    print("}")


# ОБРАЗЕЦ ввода данных:    HP LaserJet  склад  100  принтер  high  сетевой
# ОБРАЗЕЦ ввода данных:    Xerox WorkCentre  склад  200  ксерокс  medium  А4

# ОБРАЗЕЦ ввода данных:    Xerox WorkCentre  адм  300  ксерокс  medium  А4
# ОБРАЗЕЦ ввода данных:    HP ScanJet  адм  400  сканер  medium  600

# ОБРАЗЕЦ ввода данных:    HP LaserJet  отдел  500  принтер  high  сетевой
# ОБРАЗЕЦ ввода данных:    Xerox WorkCentre  отдел  600  ксерокс  medium  А4
# ОБРАЗЕЦ ввода данных:    HP ScanJet  отдел  900  сканер  medium  600



# РЕЗУЛЬТАТ (ожидаемый):    HP LaserJet  склад  600  принтер  high  сетевой
# РЕЗУЛЬТАТ (ожидаемый):    Xerox WorkCentre  склад  1100  ксерокс  medium  А4
# РЕЗУЛЬТАТ (ожидаемый):    HP ScanJet  склад  1300  сканер  medium  600




# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число». Реализуйте перегрузку методов сложения и умножения
# комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
# класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class Complex:
    
    def __init__(self, st):
        self.st = st
        self.st0 = ""
        self.st1 = ""
        self.set_result = ("", 0, "0")
        self.real = ""
        self.image = ""
        self.other_real = ""
        self.other_image = ""
        self.real_itog = ""
        self.image_itog = ""
        
    @staticmethod
    def exept_numb(number):
    # проверяет является ли символ числом
        try:
            int(number)
        except:
            result = True
        else:
            result = False
        return result    
  
    def one(number):
    # меняет значение реальной и мнимой части для выполнения над ними
    # арифметических операций 
        set = ("+", "-")
        if number in set:
            number += "1"
        return number
    
    def ne_nul_add(param1, param2, real_itog = ""):
    # убирает значение "0" в реальной и мнимой части комплексного числа перед
    # выводом на печать
        if abs(int(param1) + int(param2)) == 0:
            result = ""
        else:
            result = real_itog
        return result    

    def __mul__(self, other):
    # перегружает операцию умножения
        if (compl_1.initial() != False) and ((compl_2.initial() != False)):
            self.real = Complex.one(self.real)
            self.image = Complex.one(self.image)
            self.other_real = Complex.one(other.real)
            self.other_image = Complex.one(other.image)
            a1a2 = int(self.real) * int(self.other_real)
            b1b2 = int(self.image) * int(self.other_image)
            self.real_itog = a1a2 - b1b2
            self.real_itog = self.real_itog #Complex.print_pl_min_real(abs(self.real_itog)) + f"{self.real_itog}"
            a1b2 = int(self.real) * int(self.other_image)
            b1a2 = int(self.image) * int(self.other_real)
            self.image_itog = a1b2 + b1a2
            self.image_itog = Complex.print_pl_min_image(self.image_itog) + f"{Complex.calc_image(abs(self.image_itog))}"
            if (Complex.ne_nul_add(a1b2, b1a2, self.image_itog) in self.set_result):
                if (Complex.ne_nul_add(a1a2, -b1b2, self.real_itog) in self.set_result):
                    result = 0
                else:
                    result = self.real_itog
            else:    
                result = str(Complex.ne_nul_add(a1a2, -b1b2, self.real_itog)) + str(Complex.ne_nul_add(a1b2, b1a2, self.image_itog)) + "i"
        else:
            result = "Нет результата!"           
        return result
        
    def __add__(self, other):
        # перегружает операцию сложения
        if (compl_1.initial() != False) and ((compl_2.initial() != False)):
            self.image = Complex.one(self.image)
            self.other_real = other.real
            self.other_image = Complex.one(other.image)
            self.real_itog = int(self.real) + int(self.other_real)
            self.image_itog = Complex.print_pl_min_image(int(self.image) + int(self.other_image)) + f"{Complex.calc_image(abs(int(self.image) + int(self.other_image)))}"
            if (Complex.ne_nul_add(self.image, self.other_image, self.image_itog) in self.set_result):
                if (Complex.ne_nul_add(self.real, self.other_real, self.real_itog) in self.set_result):
                    result = 0
                else:
                    result = Complex.ne_nul_add(self.real, self.other_real, self.real_itog)
            else:    
                result = str(Complex.ne_nul_add(self.real, self.other_real, self.real_itog)) + str(Complex.ne_nul_add(self.image, self.other_image, self.image_itog)) + "i"
        else:
            result = "Нет результата!"           
        return result
    
    def print_pl_min_image(number):
    # формирует знак мнимой части комплексного числа
        print("number = ", number)
        if number < 0:
            result = "-"
        elif number == 0:
            result = ""
        else:
            result = "+"
        return result
    
    def calc_image(number):
    # формирует абсолютную часть мнимой части комплексного числа
        if number == 1:
            result = ""
        else:
            result = number
        return result
    
    def initial(self):
        # проверяет порядок ввода и записывает в переменные self.real и 
        # self.image значение реальной и мнимой части введенного комплексного
        # числа для дальнейших операций с ними
        result = True
        index = None
        if self.st.startswith("+") or self.st.startswith("-"):
            self.st1 = self.st[1:]
            self.st0 = self.st[:1]
            print("def initial: self.st.startswith('+') or self.st.startswith('-') = ", self.st.startswith("+") or self.st.startswith("-"))
            print("def initial: self.st1 = ", self.st1)
            print("def initial: self.st0 = ", self.st0)
        else:
            self.st1 = self.st
        print("(self.st1.find('+') == -1) and (self.st1.find('-') == -1) = ", (self.st1.find('+') == -1) and (self.st1.find('-') == -1))
        if (self.st1.find("+") == -1) and (self.st1.find("-") == -1):
            self.real = 0
            self.image = self.st0 + self.st1.split("i")[0]
            print("def initial: self.image = ", self.image)
        elif self.st1.find("+") != -1:
            index = self.st1.find("+")
        elif self.st1.find("-") != -1:
            index = self.st1.find("-")
        else:
            result = False
            print("0 - Нарушен формат ввода комплексного числа!")
        print(f"index({self.st}) = ", index)
        print("self.st.split('i') = ", self.st.split("i"))
        print("len(self.st.split('i')) = ", len(self.st.split('i')))
        print("self.st = ", self.st)
        print("len(self.st) = ", len(self.st))
        print("self.image == '-' = ", self.image == "-")
        
        if (result == True) and (index != None):
            if (self.st.endswith("i") != True) or (self.st1[index:].split("i")[0] == ""):
                print("1 - Нарушен формат ввода комплексного числа!")
                result = False
            elif self.st1[:index] == "":
                self.real = 0
                self.image = self.st1[index:].split("i")[0]
            else:
                self.real = self.st0 + self.st1[:index]
                self.image = self.st1[index:].split("i")[0]
            if Complex.exept_numb(self.st1[:index]) or ((self.image[1:] != "") and Complex.exept_numb(self.image[1:])):
                print("2 - Нарушен формат ввода комплексного числа!")
                result = False
            else:
                result = True
        
        elif (result == True) and (index == None):
            if ((self.image == "") or (self.image == "+")) and (self.st.endswith("i") == True) and (len(self.st.split("i")[0])<2):
                self.image = "1"
                print("присвоили 1!")
            elif (self.image == "-") and (self.st.endswith("i") == True) and (len(self.st.split("i")[0])<2):
                self.image = "-1"
                print("присвоили -1!")
            else:
                result = False
                print("3 - Нарушен формат ввода комплексного числа!")
            
        return result
    
st1 = input("Введите 1-ое комплексное число: ")
compl_1 = Complex(st1)
st2 = input("Введите 2-ое комплексное число: ")
compl_2 = Complex(st2)

print(f"{st1} прибавить {st2} равно", compl_1 + compl_2)
#print(f"{st1} умножить {st2} равно", compl_1 * compl_2)