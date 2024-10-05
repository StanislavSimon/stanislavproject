import random
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



#for i in range(1, 11):
    #cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com",f"{i * 10}" ,"1000"))

#cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")

#cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# cursor.execute("SELECT username, email, age, balance  FROM Users WHERE age != ?", (60,))
cursor.execute("DELETE FROM Users WHERE id = 6")
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)
cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]
print(all_balance)
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)


# users = cursor.fetchall()
# for user in users:
#     print(user)

connection.commit()
connection.close()