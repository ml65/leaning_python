# Домашнее задание по теме "Позиционирование в файле".

# Задача "Записать и запомнить":

def custom_write(file_name:str, strings:str):
    file = open(file_name, "w", )
    str_ptr = 1
    strings_positions = {}
    for str in strings:
        strings_positions[(str_ptr,file.tell())] = str
        file.write(str + "\n")
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
