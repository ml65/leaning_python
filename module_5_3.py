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
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название {self.name}, кол-во этажей: {self.number_of_floors}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
