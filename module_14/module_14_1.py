# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

# Задача "Первые пользователи":

import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL 
)     
''')

# 1
for i in range(1,11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i*10, 1000))
connection.commit()
# 2
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for u in users:
    id, name, email, age, balance = u
    if id % 2:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",(balance + 500, id))
connection.commit()
# 3
for id in range(1,10,3):
    cursor.execute("DELETE FROM Users WHERE id = ?",(id,))

connection.commit()
connection.close()
