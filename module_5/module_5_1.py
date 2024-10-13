# Домашняя работа по уроку "Атрибуты и методы объекта."

# Задача "Developer - не только разработчик":

class House:

    name = ''
    number_of_floors = 0

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (self.number_of_floors < new_floor):
            print ("Такого этажа не существует")
        else:
            for i in range(new_floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
