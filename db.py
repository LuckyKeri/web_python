import sqlite3 as sql

def connection(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    return connect, cursor

def commit(connect):
    connect.commit()
    connect.close()

# создание БД
def create_db(path):
    connect, cursor = connection(path)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pwd TEXT,
            salt TEXT,
            num_char  INTEGER,
            result TEXT
        );
        """
    )
    commit(connect)

# запись в БД
def write_db(path, data):
    connect, cursor = connection(path)
    cursor.executemany(
        "INSERT INTO data (pwd, salt, num_char, result) VALUES (?,?,?,?);",
        data 
    )
    commit(connect)

# Чтение из БД
def read_db(path):
    connect, cursor = connection(path)
    cursor.execute(
        "SELECT * FROM data;"
    )
    result = cursor.fetchall()
    return result