import sqlite3

CREATE_USER_TABLE = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, age INTEGER, t_1 INTEGER, t_2 INTEGER, t_3 INTEGER, t_all INTEGER, condition INTEGER);"

INSERT_USER = "INSERT INTO users (username, password, age, t_1, t_2, t_3, t_all, condition) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"
GET_USER_BY_NAME = "SELECT * FROM users WHERE username = ? AND WHERE password = ?;"
UPDATE_USER_TIMES = "UPDATE users SET t_1 = ?, t_2 = ?, t_3 = ?, t_all = ? WHERE username = ? AND password = ?;"

def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_USER_TABLE)
        
def add_user(connection, username, password, age, t_1, t_2, t_3, t_all, condition):
    with connection:
        connection.execute(INSERT_USER, (username, password, age, t_1, t_2, t_3, t_all, condition))

def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_user(connection, username, password):
    with connection:
        return connection.execute(GET_USER_BY_NAME, (username, password)).fetchall()

def get_times_from_user(connection, username, password, t_1, t_2, t_3, t_all):
    with connection:
        return connection.execute(UPDATE_USER_TIMES, (username, password, t_1, t_2, t_3, t_all))

#class SQL:
    def connect(self):
        return sqlite3.connect("data.db") #stupid nerd :p

    def create_tables(self, connection):
        with connection:
            connection.execute(CREATE_USER_TABLE)

    def add_user(connection, username, password, age, t_1, t_2, t_3, t_all, condition):
        with connection:
            connection.execute(INSERT_USER, (username, password, age, t_1, t_2, t_3, t_all, condition))

    def get_all_users(connection):
        with connection:
            return connection.execute(GET_ALL_USERS).fetchall()

    def get_user(connection, username, password):
        with connection:
            return connection.execute(GET_USER_BY_NAME, (username, password)).fetchall()

    def get_times_from_user(connection, username, password, t_1, t_2, t_3, t_all):
        with connection:
            return connection.execute(UPDATE_USER_TIMES, (username, password, t_1, t_2, t_3, t_all))
