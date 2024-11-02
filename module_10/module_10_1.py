#Домашнее задание по теме "Введение в потоки".

# Задача "Потоковая запись в файлы":

import time
import threading

def write_kwords(word_count, file_name):
    file = open(file_name,"w");
    for i in range(1, word_count):
        file.write(f"Какое-то слово № {i}")
        time.sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")

start_time = time.time()
write_kwords(10, "example1.txt")
write_kwords(30, "example2.txt")
write_kwords(200, "example3.txt")
write_kwords(100, "example4.txt")
end_time = time.time()
elased_time = end_time - start_time
print (f"Работа потоков {elased_time}")

start_time = time.time()
thread1 = threading.Thread(target=write_kwords, args=(10, "example5.txt"))
thread1.start()
thread2 = threading.Thread(target=write_kwords, args=(30, "example5.txt"))
thread2.start()
thread3 = threading.Thread(target=write_kwords, args=(200, "example6.txt"))
thread3.start()
thread4 = threading.Thread(target=write_kwords, args=(100, "example7.txt"))
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

end_time = time.time()
elased_time = end_time - start_time
print (f"Работа потоков {elased_time}")
