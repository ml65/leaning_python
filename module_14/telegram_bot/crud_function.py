#
import os
import sqlite3
from pathlib import Path


class Product:
    '''
    CRUD Product - модель продуктов
    '''

    def __init__(self):
        if not os.path.isfile("not_telegram.db"):
            Path("not_telegram.db").touch()
        self.connection = sqlite3.connect("not_telegram.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'Products\'')
        istable = self.cursor.fetchall()
        if (len(istable) == 0):
            self.initiate_db()
            self.seeder_db()

    def initiate_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        photo TEXT
        )     
        ''')

    def seeder_db(self):
        for i in range(1, 5):
            self.cursor.execute("INSERT INTO Products(id, title, description, price, photo) "
                                "VALUES (?, ?, ?, ?, ?)",
                                (i, f"Product{i}", f"Описание product{i}", i * 100, f"imgs/product_{i}.png"))
            self.connection.commit()

    def get_all_product(self):
        self.cursor.execute("SELECT * FROM Products")
        return self.cursor.fetchall()

class User:
    '''
    CRUD User - модель пользователей
    '''

    DEFAULT_BALANCE = 1000

    def __init__(self):
        if not os.path.isfile("not_telegram.db"):
            Path("not_telegram.db").touch()
        self.connection = sqlite3.connect("not_telegram.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'Users\'')
        istable = self.cursor.fetchall()
        if (len(istable) == 0):
            self.initiate_db()

    def initiate_db(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )     
        ''')

    def add_user(self,username, email, age):
        # TODO! валидация данных, защита от инъекций
        self.cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                            (username, email, age, self.DEFAULT_BALANCE))
        self.connection.commit()

    def is_included(self, username):
        # TODO! валидация данных - защита от инъекций
        self.cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        return self.cursor.fetchone()



