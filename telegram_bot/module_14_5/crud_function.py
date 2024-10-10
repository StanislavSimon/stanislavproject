import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
            )
        ''')
    connection.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    connection.commit()

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)",
                   (username, email, age))
    connection.commit()

def is_included(username):
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    return cursor.fetchone() is not None

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    return cursor.fetchall()

initiate_db()

cursor.execute("DELETE FROM Products")
for num in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f"Продукт {num}", f"Описание {num}", num * 100))
