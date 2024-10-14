# Домашнее задание по теме "Зачем нужно наследование"

# Задача "Съедобное, несъедобное":
class Animal:
    """
    Базовый класс Animal
    """
    alive:bool = True
    fed:bool   = False
    def __init__(self, name: str):
        self.name = name
        print(self.name)

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False



class Plant:
    """
    Базовый класс Plant
    """
    edible:bool = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    """
    Дочерний класс Mammal
    """
class Predator(Animal):
    """
    Дочерний класс Predator
    """
class  Fruit(Plant):
    """
    Дочерний класс Plant
    """
    edible:bool = True

class Flower(Plant):
    edible:bool = False

if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)