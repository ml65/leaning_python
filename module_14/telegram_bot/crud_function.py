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

