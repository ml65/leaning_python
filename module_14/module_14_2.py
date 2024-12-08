# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
import os
# Задача "Средний баланс пользователя":
import sqlite3
from pathlib import Path

if os.path.isfile("not_telegram.db"):
    os.remove("not_telegram.db")
    Path("not_telegram.db").touch()

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
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",(500, id))
connection.commit()
# 3
for id in range(1,10,3):
    cursor.execute("DELETE FROM Users WHERE id = ?",(id,))

cursor.execute("DELETE FROM Users WHERE id = ?",(6,))
connection.commit()

# 4
print("#4")
cursor.execute("SELECT * FROM Users WHERE age != 60")
for row in cursor.fetchall():
    id, username, email, age, balance = row
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users")
average = cursor.fetchone()[0]

print(all_balance/total_users)

connection.close()
