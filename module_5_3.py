# Домашняя работа по уроку "Атрибуты и методы объекта."

# Задача "Developer - не только разработчик":

class House:


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

    def __eq__(self, other):
        if (other.__class__.__name__ == "int"):
            return self.number_of_floors == other
        elif (other.__class__.__name__ == "House"):
            return self.number_of_floors == other.number_of_floors
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {other.__class__.__name__}" )
        return False

    def __lt__(self, other):
        if (other.__class__.__name__ == "int"):
            return self.number_of_floors < other
        elif (other.__class__.__name__ == "House"):
            return self.number_of_floors < other.number_of_floors
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {other.__class__.__name__}" )
        return False

    def __le__(self, other):
        if (other.__class__.__name__ == "int"):
            return self.number_of_floors <= other
        elif (other.__class__.__name__ == "House"):
            return self.number_of_floors <= other.number_of_floors
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {other.__class__.__name__}" )
        return False

    def __gt__(self, other):
        if (other.__class__.__name__ == "int"):
            return self.number_of_floors > other
        elif (other.__class__.__name__ == "House"):
            return self.number_of_floors > other.number_of_floors
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {other.__class__.__name__}" )
        return False

    def __ge__(self, other):
        if (other.__class__.__name__ == "int"):
            return self.number_of_floors >= other
        elif (other.__class__.__name__ == "House"):
            return self.number_of_floors >= other.number_of_floors
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {other.__class__.__name__}" )
        return False

    def __ne__(self, other):
        if (other.__class__.__name__ == "int"):
            return self.number_of_floors != other
        elif (other.__class__.__name__ == "House"):
            return self.number_of_floors != other.number_of_floors
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {other.__class__.__name__}" )
        return False

    def __add__(self, value):
        if (value.__class__.__name__ == "int"):
            self.number_of_floors += value
            return self
        # исключение - пока не изучали
        print(f"Недопустимый параметр класса {value.__class__.__name__}" )
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__