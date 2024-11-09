# Домашнее задание по теме "Многопроцессное программирование"
import time
import multiprocessing

# Задача "Многопроцессное считывание":

def read_info(name):
    all_data = []
    # вариант с использованием readline
    ''' 
    pri = True
    file = open(name,'r')
    while pri:
        str = file.readline()
        if len(str) > 0:
            all_data.append(str)
        else:
            pri = False

    print(all_data)
    '''
    # вариант с использованием readlines
    # Время выполнения 2.339155435562134
    with open(name,"r") as file:
        all_data = file.readlines()

filenames = [f'./file {number}.txt' for number in range(1, 5)]
start_time = time.time()
# Линейный вызов
# Время выполнения 4.865707159042358
'''
print("Линейный вызов!!!")
for name in filenames:
    print(f"Читаем файл {name}")
    read_info(name)
'''
# Многопроцессный
print("Многопроцессорный вызов")
i = 0
processes = []
for name in filenames:
    print(f"Читаем файл {name}")
    process = multiprocessing.Process(target=read_info, args=(name,))
    process.start()
    processes.append(process)

for process in processes:
    process.join()


end_time = time.time()
delta = end_time - start_time
print(f"Время выполнения {delta}")