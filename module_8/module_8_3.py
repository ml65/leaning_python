# Домашнее задание по теме "Создание исключений"

# Задача "Некорректность":

class Car:
    def __init__(self, model, vin, number):
        self.model = model
        if self._is_valid_vin(vin):
            self.vin = vin
        if self._is_valid_number(number):
            self.number = number

    def _is_valid_vin(self, vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return  True

    def _is_valid_number(self, number):
        if not isinstance(number, str):
            raise  IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(number) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')