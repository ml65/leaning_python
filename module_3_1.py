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
        if str.lower() == item.lower():
            res = True
            break
    return res

print (string_info("О сколько нам открытий чудных"))
print (string_info("Готовит просвещенья дух"))
print (string_info("И опыт - сын ошибок трудных"))
print ( is_contains("СКОЛЬКО", ["О","сколько","нам","открытий"]))
print ( is_contains("открытых", ["О","сколько","нам","открытий"]))
print (calls)