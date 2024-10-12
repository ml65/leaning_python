# Дополнительное практическое задание по модулю*
import math


# Задание "Они все так похожи":

class Figure:
    sides_count = 0

    def __init__(self, *param):
        pparam = self.parse_params(*param)
        if pparam[0]:
            self.set_color(*pparam[0])
        if pparam[1]:
            if (len(pparam[1]) != self.sides_count):
                pparam[1]= ()
                for i in range(0, self.sides_count):
                    pparam[1] += (1,)
            self.set_sides(*pparam[1])

    def set_sides_count(self, count):
        self.sides_count = count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *color):
        if (len(color) != 3):
            return False
        for color_item in color:
            if color_item < 0 or color_item > 255:
                return False
        return True

    def set_color(self, *param):
        if (self.__is_valid_color(*param)):
            self.__color = list(param)

    def is_valid_sides(self, *param):
        if (len(param) == self.sides_count):
            return True
        return False

    def set_sides(self, *new_sides):
        if self.is_valid_sides(*new_sides):
            self.sides = list(new_sides)

    def get_sides(self):
        return self.sides

    def __len__(self):
        len = 0
        for side in self.sides:
            len += side
        return len

    def parse_params(self, *param):
        color = ()
        sides = ()
        for par in param:
            if isinstance(par, tuple):
                color = par
            else:
                sides += (par,)
        return [color, sides]


class Circle(Figure):
    def __init__(self, *param):
        super().set_sides_count(1)
        super().__init__(*param)
        self.radius = self.sides[0]/(2 * math.pi)

    def get_square(self):
        return self.radius * math.pi

class Cube(Figure):
    def __init__(self, *param):
        super().set_sides_count(12)
        pparam = self.parse_params(*param)
        if (len(pparam[1]) == 1):
            for i in range(1, self.sides_count):
                param += (pparam[1][0],)
        super().__init__(*param)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0]**3


class Triangle(Figure):

    def __init__(self, *param):
        super().set_sides_count(3)
        super().__init__(*param)

    def get_square(self):
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

test = Triangle((1,1,1),100,200) # проверка ввода неправильных длинн сторон
print(test.get_sides())