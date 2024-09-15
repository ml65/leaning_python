# Дополнительное практическое задание по модулю*
from attr.validators import instance_of


# Задание "Раз, два, три, четыре, пять .... Это не всё?":

def calculate_structure_sum(obj):
    '''
    Функция подсчета числе и строк в сложной структуреm
    :param obj:
    :return: int:
    '''
    sum = 0
    if (isinstance(obj, int)):
        sum = obj
    if (isinstance(obj, float)):    #
            sum = int(obj)
    elif (isinstance(obj, str)):
        sum = len(obj)
    elif (isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set)):
        for item in obj:
            sum += calculate_structure_sum(item)
    elif (isinstance(obj, dict)):
        for k,v in obj.items():
            sum += calculate_structure_sum(k)
            sum += calculate_structure_sum(v)

    return int(sum)


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print (calculate_structure_sum(data_structure))

