# Домашняя работа по уроку "Пространство имён"

# Задача "Счётчик вызовов":
calls = 0
def count_calls():
    global calls

    calls += 1

def string_info(param):
    count_calls()
    return ( len(param), param.upper(), param.lower())

def is_contains(str, list):
    count_calls()
    res = False
    for item in list:
        if str == item:
            res = True
            break
    return res

tuple = string_info("О сколько нам открытий чудных")
print (tuple)
tuple = string_info("Готовит просвещенья дух")
print (tuple)
tuple = string_info("И опыт - сын ошибок трудных")
print (tuple)
tuple = string_info("И гений")
print (tuple)

list = ["О", "сколько", "нам", 3, 66, False]

param = "сколько"
if ( is_contains(param, list)):
    print (param, "содержится")
else:
    print (param, "не содержится")

param = 66
if ( is_contains(param, list)):
    print (param, "содержится")
else:
    print (param, "не содержится")

print ("Число вызовов методов:", calls)