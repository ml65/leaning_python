# Домашнее задание по теме "Обзор сторонних библиотек Python"

# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# https://habr.com/ru/articles/469355/

import cv2
from matplotlib import pyplot as plt

I = cv2.imread('sarajevo.jpg')[:, :, ::-1]  #OpenCV работает с изображениями в формате BGR, а нам привычен RGB.
                                            # Мы меняем порядок байтов вдоль оси цвета без обращения к функциям OpenCV, используя конструкцию
                                            #"[:, :, ::-1]".
#plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
#plt.imshow(I)
#plt.show()

# Уменьшим изображение в 2 раза по каждой оси. Наше изображение имеет четные размеры по осям,
# соответственно, может быть уменьшено без интерполяции:
I_ = I.reshape(I.shape[0] // 2, 2, I.shape[1] // 2, 2, -1)
print(I_.shape)

plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I_[:, 0, :, 0])
plt.show()

