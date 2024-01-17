# Система управление базами данных(СУБД) SQLite

import sqlite3 as sql 

# Соединение с БД
conn = sql.connect("examples/test.db")

# курсор - понель управление базой данных
cursor = conn.cursor()

# создание таблицы
cmd = """CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    f_name TEXT,
    l-name TEXT,
    age REAL,
    gender TEXT
);
"""
cursor.execute(cmd)
conn.commit()

# запись данных
cmd ="INSERT INTO users VALUES (?,?,?,?,?)"

# одна строка
# first_user = (0, "John", "Sherman", 24.5, "m")
# cursor.execute(cmd, first_user)

# много строк
# user_data = [
#     (1, "Peter", "Penn", 32.3, "m"),
#     (2, "Katrin", "Simpson", 25.0, "f"),
#     (3, "Lena", "Chan", 26.5, "f")
# ]
# cursor.executemany(cmd, user_data)
# conn.commit()

# # чтение данных
# # все столбцы
# # cmd = "SELECT * FROM users;"
# # определение столбцы
# # cmd = "SELECT user_id, f_name, age FROM user;"
# # определеные столбцв с уловием 
# cmd = "SELECT user_id, f_name, age FROM user WHERE age < 30 AND gender='f';"
# cursor.execute(cmd)
# # первая строка 
# # result = cursor.fetchone()
# # все строки
# result = cursor.fetchall()
# # несколько строк начиная с первого
# result = cursor.fetchmany(3)
# print(result)

# удаление данных
# cmd = "DELETE FROM users WHERE l_name='Sherman';"
# cursor.execute(cmd)
# conn.commit()


# создание 2 таблицы
cmd = """CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER primary key,
    date TEXT,
    user_id INTEGER,
    total REAL
);
"""
cursor.execute(cmd)
conn.commit()

# запись данных
# cmd ="INSERT INTO orders VALUES (?,?,?,?)"
# order_data = [
#     (0, "15-01-2024", 2, 100.23),
#     (1, "15-01-2024", 1, 30.2),
#     (2, "16-01-2024", 2, 45.9),
#     (3, "17-01-2024", 3, 70.23),
#     (4, "17-01-2024", 4, 110.0)
# ]
# cursor.executemany(cmd, order_data)
# conn.commit()

# Чтение данных
# cmd = "SELECT * FROM orders;"
# Чтение данных из двух таблиц
cmd = "SELECT * FROM orders LEFT JOIN users ON orders.user_id;"
cursor.execute(cmd)
result = cursor.fetchall()
print(result)

conn.close()