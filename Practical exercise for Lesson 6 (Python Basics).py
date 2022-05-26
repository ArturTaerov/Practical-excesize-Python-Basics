# 1. Создать класс TrafficLight (светофор).

#    определить у него один атрибут color (цвет) и метод running (запуск);
#    атрибут реализовать как приватный;
#    в рамках метода реализовать переключение светофора в режимы: красный,
#    жёлтый, зелёный;
#    продолжительность первого состояния (красный) составляет 7 секунд, второго
#    (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#    переключение между режимами должно осуществляться только в указанном
#    порядке (красный, жёлтый, зелёный);
#    проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

class TrafficLight:
    __color = ["красный", "желтый", "зеленый"] 
    def __running(self, __color):
        def count(prodolz):
            cnt = []
            for i in range(len(prodolz)):
                cnt.append(prodolz[i])
                return int("".join(cnt))
        prodolz = [7, 2, int(input("Введите продолжительность зеленого \
сигнала светофора в секундах: "))]
        tek_rezh = input("Введите режим работы светофора в виде \
последовательности цветов через пробел: ").split()
        for j in range(len(tek_rezh)):
            if tek_rezh[j] != __color[j]:
                print("Задан неверный режим работы светофора!")
                break
        else:
            import time
            for i in range(len(tek_rezh)):
                print (__color[i])
                time.sleep(prodolz[i])
traf = TrafficLight()
traf._TrafficLight__running(traf._TrafficLight__color)            
print ("Переключение светофора завершено.")



# 2. Реализовать класс Road (дорога).

#    определить атрибуты: length (длина), width (ширина);
#    значения атрибутов должны передаваться при создании экземпляра класса;
#    атрибуты сделать защищёнными;
#    определить метод расчёта массы асфальта, необходимого для покрытия всей
#    дороги;
#    использовать формулу: длина*ширина*масса асфальта для покрытия одного кв.
#    метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#    проверить работу метода.

# Например: 20 м*5000 м*25 кг*5 см = 12500 т.



class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width       
    def calc_r (self, massa, thickness):
        ms_rd = self._length*self._width*massa*thickness/1000
        return ms_rd
length = int(input("Введите длинну дороги: "))
width = int(input("Введите ширину дороги: "))
rd = Road(length, width)
print(f"Маса дороги в тоннах: {rd.calc_r(25,5)}")




# 3. Реализовать базовый класс Worker (работник).

#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, 
#содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника
#(get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса
#Position, передать данные, проверить значения атрибутов, вызвать методы
#экземпляров.



class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income       
class Position(Worker):
    def get_full_name(self):
        print ("Имя: ", self.name)
        print ("Фамилия: ", self.surname)
        print ("Должность: ", self.position)
        print ("Доход: ", self._income)
        return self.name + " " + self.surname 
    def get_total_income(self, _income):
        return int(_income.setdefault("wage")) + int(_income.setdefault("bonus"))
k = input("Введите количество сотрудников, кому надо рассчитать зарплату: ")
for i in range(int(k)):
    name = input(f"Введите имя {i+1}-го сотрудника: ")
    surname = input(f"Введите фамилию {i+1}-го сотрудника: ")
    position = input(f"Введите должность {i+1}-го сотрудника: ")
    income = {"wage": input(f"Введите оклад {i+1}-го сотрудника: "), \
              "bonus": int(input(f"Введите премию {i+1}-го сотрудника: "))}
    pos = Position(name, surname, position, income)
    print (f"Полное имя {i+1}-го сотрудника: ", pos.get_full_name())
    print (f"Итоговый доход {i+1}-го сотрудника: ", pos.get_total_income(pos._income))



# 4. Реализуйте базовый класс Car.

# у класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    speed = float(input("Введите скорость автомобиля в км/ч: "))
    color = "yellow"
    name = "запорожец"
    is_police = False
    
    def __init__(self, sp_wc = None, sp_tc = None):
        self.sp_wc = sp_wc
        self.sp_tc = sp_tc
        
    
    def go(self):
       print(f"Машина {self.name} поехала.") 
        
    def stop(self):
        print(f"Машина {self.name} остановилась.")
        
    def turn(self):
        print(f"Машина {self.name} повернула направо.")
        
    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {int(self.speed)} км/ч.")
 
            

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print\
            (f"Машина {self.name} едет со скоростью {int(self.speed)} км/ч.")
    
class SportCar(Car):
    pass
    
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print\
            (f"Машина {self.name} едет со скоростью {int(self.speed)} км/ч.")

class PoliceCar(Car):
    pass


    
cr = Car()
cr.show_speed()

tc = TownCar()
tc.show_speed()

spc = SportCar()
spc.show_speed()  

wc = WorkCar()
wc.show_speed() 

spc = PoliceCar()
spc.show_speed() 

spc.go()
spc.stop()
spc.turn() 




# 5. Реализовать класс Stationery (канцелярская принадлежность).

# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.

class Stationery:
    def __init__(self, title):    
	    self.title = title
    def draw(self):
        print(self.title)
        
class Pen(Stationery):
    def draw(self):
        print(f"{self.title} {dct.setdefault(str(type(pn))[17:-2])}")

class Pensil(Stationery):
    def draw(self):
        print(f"{self.title} {dct.setdefault(str(type(pns))[17:-2])}")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title} {dct.setdefault(str(type(hnd))[17:-2])}")
        
dct = {"Pen":"ручкой", "Pensil":"карандашом", "Handle":"маркером"}
title = "Запуск отрисовки"
st = Stationery(title)
st.draw()

pn = Pen(title)
pn.draw()

pns = Pensil(title)
pns.draw()

hnd = Handle(title)
hnd.draw()