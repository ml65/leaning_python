# Домашнее задание по теме "Режимы открытия файлов"

# Задача "Учёт товаров":

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:

    __file_name = "products.txt"

    def __init__(self):
        pass

    def get_products(self):
        file = open(self.__file_name,"r")
        str = file.read()
        file.close()
        return str

    def add(self, *products):
        shop = self.get_products()
        for product in products:
        # согласно условию задачи нужно просто делать поиск по подстроке
        # реализую так, как написано в ТЗ. В реальной жизни строки из файла
        # нужно преобразовать в объекты, поместить их в словарь (т.к. работаем в памяти)
        # и далее работать со словарем
            if (shop.find(product.name + ",") == -1):
                # Для большей корректности кода после названия продукта добавим разделитель
                self.save(product)
                shop += str(product)
            else:
                print(f'Продукт {product.name} уже есть в магазине')

    def save(self, product):
        file = open(self.__file_name,"a")
        file.write(product.__str__() + "\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



