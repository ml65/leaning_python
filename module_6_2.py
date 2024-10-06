# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

# Задача "Изменять нельзя получать":

# в выводе ответов есть вывод красным и зеленым
from colorama import init, Fore
from colorama import Back
from colorama import Style


class Vehicle:

    owner:str
    _model:str
    _engine_power:int
    _color:str
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__ (self, owner, model, color, engine_power):
        self.owner = owner
        self._model = model
        self._color = color
        self._engine_power = engine_power
        self.__COLOR_VARIANTS = [x.lower() for x in self.__COLOR_VARIANTS]

    def get_model(self):
        return f" Модель: {self._model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self._engine_power}"

    def get_color(self):
        return "Цвет: " + Fore.GREEN + f"{self._color}" + Fore.RESET

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец: " + Fore.GREEN + f"{self.owner}" + Fore.RESET)

    def set_color(self, newcolor:str):
        if newcolor.lower() in self.__COLOR_VARIANTS:
            self._color = newcolor

        else:
            print(Fore.RED + f"Нельзя сменить цвет на {newcolor}" + Fore.RESET)

class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

