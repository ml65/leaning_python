# Домашнее задание по теме "Обзор сторонних библиотек Python"

# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.

import pandas as pd

data = pd.read_csv('Mall_Customers.csv', delimiter=',')
print(data.head())
males = data[data.Genre == 'Male']
females = data[data.Genre == 'Female']

print('Мужчины: средний возраст:', round(males['Age'].mean(),2), ' средний чек:', round(males['Annual Income (k$)'].mean(),2))
print('Женщины: средний возраст:', round(females['Age'].mean(),2), ' средний чек:', round(females['Annual Income (k$)'].mean(),2))
